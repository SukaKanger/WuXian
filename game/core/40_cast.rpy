# ============================================================
#  VN2 • 角色与立绘管理器（V2 透明底立绘）
#  ------------------------------------------------------------
#  • 6 个角色各用独立 image tag（zhou / lan / bai / qing / arui / shiqi）
#  • V2 素材在 images/chars/v2/，1256×1616 RGBA 透明底、脚底居中，
#    直接引用 PNG，不再套 AlphaMask / sprite_feather 羽化遮罩
#  • 姿态缩放/定位走 vn2_pose（底部锚定，比例不变、不裁切）
#  • 阿瑞图片前缀 arui；旧台词/脚本里的 ari 走别名解析，旗标名 ari_helped 不变
#  • 清场走 VN2_SPRITE_TAGS（立绘 tag 表），不复用好感 key 表
# ============================================================

init -1 python:

    VN2_POS = {
        "far_left":  0.13,
        "left":      0.22,
        "mid_left":  0.34,
        "center":    0.50,
        "mid_right": 0.66,
        "right":     0.78,
        "far_right": 0.87,
    }

    VN2_CAST = {
        "zhou":  dict(name="玩家", role="队长", tag="zhou",  color="#e8b96a", pos="right",   prefix="zhou"),
        "lan":   dict(name="蓝羽", role="向导", tag="lan",   color="#7ab6e8", pos="left",    prefix="lan"),
        "bai":   dict(name="白砚", role="队医", tag="bai",   color="#e8e0d0", pos="left",    prefix="bai"),
        "qing":  dict(name="青岩", role="学者", tag="qing",  color="#7fd0a8", pos="right",   prefix="qing"),
        "arui":  dict(name="阿瑞", role="向导", tag="arui",  color="#e89a8a", pos="far_left", prefix="arui"),
        "shiqi": dict(name="十七", role="守门人", tag="shiqi", color="#9a94a8", pos="far_right", prefix="shiqi"),
    }

    # 旧名别名：脚本写 ari 时解析到 arui；旗标/好感键仍叫 ari，不在此表改
    VN2_CAST_ALIAS = {"ari": "arui"}

    # 清场用的立绘 tag 表（与好感 key 表解耦）
    VN2_SPRITE_TAGS = tuple(VN2_CAST.keys())


    def vn2_name_role(who):
        """把 Character 的 who 串拆成「名字 / 职位」两段。
        名字和职位不再用易缺字形的中点拼在一个字符串里，
        改为两个 Text，中间放一枚小菱形。"""
        if not who:
            return "", ""
        if who == getattr(store, "player_name", None):
            role = VN2_CAST["zhou"]["role"]
            return who, ("" if who == role else role)
        for info in VN2_CAST.values():
            if info.get("name") == who:
                return info.get("name", who), info.get("role", "")
        # 旧档/旧台词可能还带着「蓝羽 · 向导」这种整串；在这里兜底拆开。
        for sep in (" · ", "｜", " | "):
            if sep in who:
                name, role = who.split(sep, 1)
                return name, role
        return who, ""



    def _vn2_resolve(who):
        """把外部传入的角色 key 解析成 VN2_CAST 里的正式 key。"""
        key = VN2_CAST_ALIAS.get(who, who)
        return key, VN2_CAST[key]


    # ---------- 表情自动切换（不新增剧本变量） ----------
    VN2_EXPR_KEYS = ("neutral", "happy", "sad", "angry", "shy", "surprised")

    # 只抓明确情绪词，避免“死”“别碰”“忽然”这类剧情常用词误触发。
    # 命中优先级：怒 > 悲 > 惊 > 羞 > 喜。
    VN2_EXPR_HINTS = (
        ("angry", ("凭什么", "闭嘴", "住口", "吼", "咬牙", "混蛋", "质问")),
        ("sad", ("对不起", "抱歉", "别走", "哭", "墓", "埋", "失去", "没能")),
        ("surprised", ("愣", "没想到", "怎么会", "睁大", "一惊", "僵住", "吓")),
        ("shy", ("脸红", "耳根", "别过脸", "小声", "不好意思", "害羞", "耳尖")),
        ("happy", ("笑", "谢谢", "谢了", "高兴", "好耶")),
    )


    def vn2_expr_guess(what):
        """从当前台词里猜一个强情绪；猜不准就返回 None，保持当前表情。"""
        if not what:
            return None
        text = str(what)
        for expr, words in VN2_EXPR_HINTS:
            if any(w in text for w in words):
                return expr
        return None


    def vn2_set_expr(who, expr=None, what=None):
        """只给已经在舞台上的角色换表情；位置/压暗状态不变。"""
        key, info = _vn2_resolve(who)
        stage = dict(store.vn2_stage or {})
        item = dict(stage.get(key) or {})
        if not item:
            return False

        if not expr or expr == "auto":
            expr = vn2_expr_guess(what)

        if expr not in VN2_EXPR_KEYS:
            return False

        img = "%s %s" % (info["prefix"], expr)
        if not renpy.has_image(img):
            return False
        if item.get("img") == img:
            return False

        if getattr(store, "vn2_cg_scene", False):
            item["img"] = img
            stage[key] = item
            store.vn2_stage = stage
            return True

        try:
            renpy.show(
                img,
                tag=info["tag"],
                at_list=[vn2_pose(item.get("pos", "center"), item.get("lit", 1.0))],
                zorder=20,
            )
        except Exception:
            return False

        item["img"] = img
        stage[key] = item
        store.vn2_stage = stage
        return True


    def vn2_face(who, expr="neutral"):
        """逐句表情指令：台词前把表情显式钉死。

        - 角色已在台上：只换脸，位置/明暗/层级都不动（vn2_pose 是静态 ATL，
          不会有任何重播动画，所以不会出现「每句闪一下」）
        - 角色不在台上：什么也不做（不凭空把人拉上台，避免打乱调度）
        - 同时上锁：本句不会再被关键词自动猜表情覆盖
        """
        key, info = _vn2_resolve(who)
        if expr not in VN2_EXPR_KEYS:
            return False

        # 上锁：告诉 Character 回调「这句的表情是人写的，别猜」
        store.vn2_expr_lock = key

        stage = store.vn2_stage or {}
        if key not in stage:
            return False
        return vn2_set_expr(key, expr)


    def vn2_face_all(expr="neutral"):
        """把台上所有角色统一成同一个表情（清场/群戏用）。"""
        stage = dict(store.vn2_stage or {})
        for key in list(stage.keys()):
            vn2_set_expr(key, expr)


    def vn2_stage_add(who, pos, img, lit=1.0):
        d = dict(store.vn2_stage or {})
        d[who] = dict(pos=pos, img=img, lit=lit)
        store.vn2_stage = d


    def vn2_auto_pos():
        """按空位分配舞台位置：中间 → 左 → 右 → 远左 → 远右。"""
        used = set()
        for item in (store.vn2_stage or {}).values():
            used.add(item.get("pos"))

        for cand in ("center", "left", "right", "far_left", "far_right"):
            if cand not in used:
                return cand
        return "center"


    def vn2_show(who, expr=None, pos=None, trans=None, lit=1.0):
        """立绘入场/换位/换表情。pos=None 时自动找空位。"""
        key, info = _vn2_resolve(who)
        tag = info["tag"]
        prefix = info["prefix"]

        if pos is None or pos == "auto":
            pos = vn2_auto_pos()

        img = prefix
        if expr:
            img = "%s %s" % (prefix, expr)
            if not renpy.has_image(img):
                img = prefix
            else:
                # 显式给了表情：这句不让关键词再猜一遍
                store.vn2_expr_lock = key

        # CG 模式下只记录舞台状态，不渲染立绘；CG 收起后由 vn2_cg_hide 恢复。
        if getattr(store, "vn2_cg_scene", False):
            vn2_stage_add(key, pos, img, lit)
            return

        if trans is not None:
            renpy.show(img, tag=tag, at_list=[vn2_pose(pos, lit)], zorder=20)
            renpy.with_statement(trans)
        else:
            renpy.show(img, tag=tag, at_list=[vn2_pose(pos, lit)], zorder=20)

        vn2_stage_add(key, pos, img, lit)
        vn2_focus_quiet(key)


    def vn2_hide(who, trans=None):
        key, info = _vn2_resolve(who)
        renpy.hide(info["tag"])
        if trans is not None:
            renpy.with_statement(trans)

        d = dict(store.vn2_stage or {})
        d.pop(key, None)
        store.vn2_stage = d


    def vn2_hide_all(trans=None):
        for key in VN2_SPRITE_TAGS:
            try:
                renpy.hide(VN2_CAST[key]["tag"])
            except Exception:
                pass
        store.vn2_stage = {}
        if trans is not None:
            renpy.with_statement(trans)


    def vn2_focus(who, force=False):
        """说话人高亮：其他角色压到 0.35；只重绘真正变灯的角色。
        以前每次 say begin 都把整排立绘重新 show 一次，ATL 从头播放，
        看起来就是角色在轻微跳/漂。"""
        stage = dict(store.vn2_stage or {})

        if getattr(store, "vn2_cg_scene", False):
            for key, item in stage.items():
                item["lit"] = 1.0 if key == who else 0.35
            store.vn2_stage = stage
            return

        for key, item in stage.items():
            want = 1.0 if key == who else 0.35
            if not force and item.get("lit") == want:
                continue
            item["lit"] = want
            try:
                renpy.show(
                    item["img"],
                    tag=VN2_CAST[key]["tag"],
                    at_list=[vn2_pose(item["pos"], want)],
                    zorder=20,
                )
            except Exception:
                pass

        store.vn2_stage = stage


    def vn2_focus_quiet(who):
        """只在需要变灯时重排；阈值必须和 vn2_focus() 一致。
        旧版拿 0.5 去比 vn2_focus 写入的 0.35，导致每一句都判定“需要重排”，
        等于每句都把立绘重置一遍。"""
        stage = dict(store.vn2_stage or {})
        if getattr(store, "vn2_cg_scene", False):
            vn2_focus(who)
            return
        need = any(
            (1.0 if key == who else 0.35) != item.get("lit")
            for key, item in stage.items()
        )
        if need:
            vn2_focus(who)


    def vn2_char_cb(key):
        """给 Character 用的回调：说话时自动点亮该角色，并按台词切换表情。"""
        def _cb(event, interact=True, what=None, **kwargs):
            if event == "begin":
                resolved = VN2_CAST_ALIAS.get(key, key)
                try:
                    vn2_focus(resolved)
                except Exception:
                    pass
                # 人写的表情优先：这句被 vn2_face / vn2_show(expr=...) 钉过，就不再猜
                if getattr(store, "vn2_expr_lock", None) != resolved:
                    try:
                        vn2_set_expr(resolved, what=what)
                    except Exception:
                        pass
        return _cb


    def vn2_narrator_cb(event, interact=True, what=None, **kwargs):
        """旁白/独白没有 who，只在场上恰好一个角色时帮它接情绪。
        多角色场景不猜，避免把情绪切到错误的人。"""
        if event != "begin" or not what:
            return
        # 只要本段出现过人工表情指令，旁白就不再顺手改脸
        if getattr(store, "vn2_expr_lock", None):
            return
        stage = dict(store.vn2_stage or {})
        keys = [k for k in stage if k != "zhou"]
        if len(keys) != 1:
            return
        expr = vn2_expr_guess(what)
        if expr:
            try:
                vn2_set_expr(keys[0], expr)
            except Exception:
                pass


    if vn2_narrator_cb not in config.all_character_callbacks:
        config.all_character_callbacks.append(vn2_narrator_cb)


# ---------- V2 立绘（透明底，直连 PNG；neutral 同时作为裸 tag） ----------

# 玩家 zhou
image zhou            = "images/chars/v2/zhou_neutral.png"
image zhou neutral    = "images/chars/v2/zhou_neutral.png"
image zhou happy      = "images/chars/v2/zhou_happy.png"
image zhou sad        = "images/chars/v2/zhou_sad.png"
image zhou angry      = "images/chars/v2/zhou_angry.png"
image zhou shy        = "images/chars/v2/zhou_shy.png"
image zhou surprised  = "images/chars/v2/zhou_surprised.png"

# 蓝羽 lan
image lan            = "images/chars/v2/lan_neutral.png"
image lan neutral    = "images/chars/v2/lan_neutral.png"
image lan happy      = "images/chars/v2/lan_happy.png"
image lan sad        = "images/chars/v2/lan_sad.png"
image lan angry      = "images/chars/v2/lan_angry.png"
image lan shy        = "images/chars/v2/lan_shy.png"
image lan surprised  = "images/chars/v2/lan_surprised.png"

# 白砚 bai
image bai            = "images/chars/v2/bai_neutral.png"
image bai neutral    = "images/chars/v2/bai_neutral.png"
image bai happy      = "images/chars/v2/bai_happy.png"
image bai sad        = "images/chars/v2/bai_sad.png"
image bai angry      = "images/chars/v2/bai_angry.png"
image bai shy        = "images/chars/v2/bai_shy.png"
image bai surprised  = "images/chars/v2/bai_surprised.png"

# 青岩 qing
image qing            = "images/chars/v2/qing_neutral.png"
image qing neutral    = "images/chars/v2/qing_neutral.png"
image qing happy      = "images/chars/v2/qing_happy.png"
image qing sad        = "images/chars/v2/qing_sad.png"
image qing angry      = "images/chars/v2/qing_angry.png"
image qing shy        = "images/chars/v2/qing_shy.png"
image qing surprised  = "images/chars/v2/qing_surprised.png"

# 阿瑞 arui（旧台词别名 ari）
image arui            = "images/chars/v2/arui_neutral.png"
image arui neutral    = "images/chars/v2/arui_neutral.png"
image arui happy      = "images/chars/v2/arui_happy.png"
image arui sad        = "images/chars/v2/arui_sad.png"
image arui angry      = "images/chars/v2/arui_angry.png"
image arui shy        = "images/chars/v2/arui_shy.png"
image arui surprised  = "images/chars/v2/arui_surprised.png"

# 十七 shiqi
image shiqi            = "images/chars/v2/shiqi_neutral.png"
image shiqi neutral    = "images/chars/v2/shiqi_neutral.png"
image shiqi happy      = "images/chars/v2/shiqi_happy.png"
image shiqi sad        = "images/chars/v2/shiqi_sad.png"
image shiqi angry      = "images/chars/v2/shiqi_angry.png"
image shiqi shy        = "images/chars/v2/shiqi_shy.png"
image shiqi surprised  = "images/chars/v2/shiqi_surprised.png"


# ---------- 角色 ----------
# 名牌只放名字；职位由 vn2_name_role() 从 VN2_CAST 里单独取出，
# 用小型金色菱形分隔，避免「蓝羽 · 向导」里的中点在某些字体下缺字。
define zhou  = Character("[player_name]", color="#e8b96a", callback=vn2_char_cb("zhou"))
define lan   = Character("蓝羽", color="#7ab6e8", callback=vn2_char_cb("lan"))
define bai   = Character("白砚", color="#e8e0d0", callback=vn2_char_cb("bai"))
define qing  = Character("青岩", color="#7fd0a8", callback=vn2_char_cb("qing"))
define arui  = Character("阿瑞", color="#e89a8a", callback=vn2_char_cb("arui"))
define ari   = arui
define shiqi = Character("十七", color="#9a94a8", callback=vn2_char_cb("shiqi"))
define nar   = Character(None)
define think = Character(None, what_italic=True)


# ---------- 舞台状态（存档/回滚安全） ----------
default vn2_stage = {}

# 本句表情是否已被人工指令钉死（None = 没钉，允许关键词兜底）
default vn2_expr_lock = None
