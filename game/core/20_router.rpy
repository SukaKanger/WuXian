# ============================================================
#  VN2 • 章节路由表（schema 2 / ROUND4 冻结契约 §3）
#  ------------------------------------------------------------
#  新增一章只需要在 CHAPTERS 里加一项，再写对应 label。
#  不许在任何章节里写 if/else 链式跳转——统一走 vn2_leave_chapter()。
#  no  = 内容目录编号；disp = 界面显示号（本线内序号，不跳号）。
# ============================================================

init -1 python:

    CHAPTERS = {
        # ---------------- 共同线 • 第 1–13 章 ----------------
        "ch01": dict(no=1,  disp=1,  route="common", day=1,  title="雨停之后",   next="ch02"),
        "ch02": dict(no=2,  disp=2,  route="common", day=2,  title="三里旧栈道", next="ch03"),
        "ch03": dict(no=3,  disp=3,  route="common", day=3,  title="断崖",       next="ch04"),
        "ch04": dict(no=4,  disp=4,  route="common", day=4,  title="夜哨",       next="ch05"),
        "ch05": dict(no=5,  disp=5,  route="common", day=5,  title="绳结",       next="ch06"),
        "ch06": dict(no=6,  disp=6,  route="common", day=6,  title="雨幕",       next="ch07"),
        "ch07": dict(no=7,  disp=7,  route="common", day=7,  title="第一块站牌", next="ch08"),
        "ch08": dict(no=8,  disp=8,  route="common", day=8,  title="沼泽边",     next="ch09"),
        "ch09": dict(no=9,  disp=9,  route="common", day=9,  title="银纹",       next="ch10"),
        "ch10": dict(no=10, disp=10, route="common", day=10, title="改过的地图", next="ch11"),
        "ch11": dict(no=11, disp=11, route="common", day=11, title="第二座信标", next="ch12"),
        "ch12": dict(no=12, disp=12, route="common", day=12, title="旧营地",   next="ch13"),
        "ch13": dict(no=13, disp=13, route="common", day=13, title="分岔",     next="ch14"),

        # ---------------- 锁线 / 门口 ----------------
        "ch14": dict(no=14, disp=None, route="lock",   day=14, title="锁线", next="dynamic"),
        "ch15": dict(no=15, disp=15, route="common", day=15, title="门口", next="dynamic"),

        # ---------------- 蓝羽线 ----------------
        "ch16": dict(no=16, disp=1, route="lan", day=16, title="旧队徽",   next="ch17"),
        "ch17": dict(no=17, disp=2, route="lan", day=17, title="雾里的名字", next="ch18"),
        "ch18": dict(no=18, disp=3, route="lan", day=18, title="两条路",   next="ch25"),

        # ---------------- 白砚线 ----------------
        "ch19": dict(no=19, disp=1, route="bai", day=19, title="空药瓶", next="ch20"),
        "ch20": dict(no=20, disp=2, route="bai", day=20, title="手术",   next="ch21"),
        "ch21": dict(no=21, disp=3, route="bai", day=21, title="站门外", next="ch25"),

        # ---------------- 青岩线 ----------------
        "ch22": dict(no=22, disp=1, route="qing", day=22, title="门后",       next="ch23"),
        "ch23": dict(no=23, disp=2, route="qing", day=23, title="空的档案柜", next="ch24"),
        "ch24": dict(no=24, disp=3, route="qing", day=24, title="守站人",     next="ch25"),

        # ---------------- 结算 / 结局 ----------------
        "ch25": dict(no=25, disp=25, route="common", day=25, title="结算", next="ch26"),
        "ch26": dict(no=26, disp=26, route="end", day=26, title="结局",   next="ch27"),
        "ch27": dict(no=27, disp=27, route="end", day=27, title="清算",   next="ch28"),
        "ch28": dict(no=28, disp=28, route="end", day=27, day_label="后日谈", title="后日谈", next=None),
    }

    CHAPTER_ORDER = ["ch%02d" % i for i in range(1, 29)]

    VN2_ROUTE_BLOCKS = {
        "common": ["ch%02d" % i for i in range(1, 14)] + ["ch15", "ch25"],
        "lock":   ["ch14"],
        "lan":    ["ch16", "ch17", "ch18"],
        "bai":    ["ch19", "ch20", "ch21"],
        "qing":   ["ch22", "ch23", "ch24"],
        "end":    ["ch26", "ch27", "ch28"],
    }

    VN2_BLOCK_ORDER = ["common", "lock", "lan", "bai", "qing", "end"]


    def vn2_chapter(cid):
        return CHAPTERS.get(cid)


    def vn2_chapter_label(cid):
        """界面显示口径：disp，不显示 no。
        共同线 · 第 6 章 / 蓝羽线 · 第 3 章 / 锁线 / 结局 · 第 2 章。
        """
        ch = CHAPTERS.get(cid)
        if ch is None:
            return cid

        route = ch["route"]
        disp = ch["disp"]

        if route == "lock":
            return "锁线"
        if route == "common":
            return "共同线 / 第 %d 章" % disp
        if route == "end":
            return "结局 / 第 %d 章" % disp
        return "%s / 第 %d 章" % (VN2_ROUTE_NAMES[route], disp)


    def vn2_chapter_count():
        """只统计真正存在于 CHAPTERS 的已解锁章节，避免旧档残留 id 把进度算大。"""
        return len([cid for cid in (persistent.vn2_unlocked or [])
                    if cid in CHAPTERS])


    # 结局章（ch26/27/28）单独在「结局」栏统计，不进章节进度口径。
    VN2_END_CHAPTERS = set(VN2_ROUTE_BLOCKS["end"])

    # 章节进度分母 25 = 共同线 13（ch01–13）+ 锁线 ch14 + 三线各 3
    # （ch16–18 / ch19–21 / ch22–24）+ ch15 + ch25。
    VN2_CHAPTER_TOTAL = len([cid for cid in CHAPTERS
                             if cid not in VN2_END_CHAPTERS])


    def vn2_chapter_progress():
        """章节进度口径：返回 (已解锁数, 25)。

        分子只数正线章节（排除结局章 ch26/27/28，避免与「结局」栏重复计数），
        并过滤不在 CHAPTERS 里的旧档残留 id。
        """
        unlocked = [cid for cid in (persistent.vn2_unlocked or [])
                    if cid in CHAPTERS and cid not in VN2_END_CHAPTERS]
        return len(unlocked), VN2_CHAPTER_TOTAL


    def vn2_enter_chapter(cid):
        """进入章节：写上下文 → 解锁章节选择 → 切 BGM；自动存档由标题卡收尾负责。"""
        ch = CHAPTERS[cid]

        store.vn2_chapter_id = cid
        store.vn2_chapter_no = ch["no"]
        store.vn2_chapter_title = ch["title"]
        store.vn2_disp = ch["disp"]
        store.vn2_disp_label = vn2_chapter_label(cid)
        store.vn2_route_key = ch["route"]
        store.vn2_route_name = vn2_route_label(ch["route"])
        store.vn2_day = ch["day"]

        unlocked = list(persistent.vn2_unlocked or [])
        if cid not in unlocked:
            unlocked.append(cid)
            persistent.vn2_unlocked = unlocked

        # 自动存档不在这里拍：此处刚切场景，拿到的可能是上一帧启动页/纯色转场。
        # 改由章节标题卡收尾后调用 vn2_autosave_entry()，等画面稳定再截图。
        # 存档失败不能打断章节进入；失败时只记日志。
        vn2_bgm_for_route(ch["route"])

        return ch


    def vn2_autosave_entry():
        """章节标题卡收尾后自动存档，确保缩略图拍到当前场景。"""
        if renpy.game.after_rollback:
            return
        try:
            renpy.force_autosave(take_screenshot=True, block=True)
        except Exception as e:
            renpy.log("VN2 autosave skipped: " + repr(e))


    def vn2_leave_chapter():
        """章节结束：按路由表跳下一章；ch14/ch15 走动态分派。"""
        cid = store.vn2_chapter_id

        if cid == "ch14":
            renpy.jump("ch15")
            return

        if cid == "ch15":
            route = store.vn2_lock_route
            nxt = {"lan": "ch16", "bai": "ch19", "qing": "ch22"}.get(route, "ch25")
            renpy.jump(nxt)
            return

        nxt = CHAPTERS[cid]["next"]
        if nxt:
            renpy.jump(nxt)
            return

        # 最后一章（ch28）：回主菜单
        # 注意：工程没有名为 main_menu 的 label（主菜单是 _main_menu + screen），
        # 原先 renpy.jump("main_menu") 会抛 LabelNotFound；统一用 full_restart 回主菜单。
        renpy.full_restart()


    # ---------- 锁线（ch14） ----------

    def vn2_lock_options():
        """ch14 菜单四项：lan/bai/qing 需对应好感 >= VN2_LOCK_THRESHOLD，solo 永远可选。"""
        options = []
        for key in ("lan", "bai", "qing"):
            aff = vn2_aff_value(key)
            eligible = aff >= VN2_LOCK_THRESHOLD
            options.append(dict(
                key=key,
                name=VN2_CHAR_NAMES[key],
                aff=aff,
                eligible=eligible,
                need=max(0, VN2_LOCK_THRESHOLD - aff),
            ))
        options.append(dict(key="solo", name="独自进入", aff=0, eligible=True, need=0))
        return options


    def vn2_lock_pick(key):
        """菜单选项后果：达标则写 vn2_lock_route；未达标给「还差多少」提示，返回 False。"""
        if key == "solo":
            store.vn2_lock_route = "solo"
            return True

        aff = vn2_aff_value(key)
        if aff >= VN2_LOCK_THRESHOLD:
            store.vn2_lock_route = key
            return True

        need = VN2_LOCK_THRESHOLD - aff
        renpy.notify("%s 还差 %d 点好感（当前 %d / %d）" % (
            VN2_CHAR_NAMES[key], need, aff, VN2_LOCK_THRESHOLD))
        return False


    # ---------- 结局矩阵（契约 §4） ----------

    def vn2_endings_matrix():
        """8 个结局的静态定义：key / 路线 / 路线名 / 标题 / 条件文案 / 是否真结局。"""
        return [
            dict(key="lan_together", route="lan",  route_name="蓝羽线", title="蓝羽 · 同行",
                 cond_text="蓝羽线 · 好感 ≥ 40 · 蓝羽向你交过底", is_true=False),
            dict(key="lan_alone",    route="lan",  route_name="蓝羽线", title="蓝羽 · 独行",
                 cond_text="蓝羽线 · 好感 < 40 或未交底",  is_true=False),
            dict(key="bai_together", route="bai",  route_name="白砚线", title="白砚 · 同行",
                 cond_text="白砚线 · 好感 ≥ 40 · 你救过他的手", is_true=False),
            dict(key="bai_alone",    route="bai",  route_name="白砚线", title="白砚 · 独行",
                 cond_text="白砚线 · 好感 < 40 或未救过他的手",  is_true=False),
            dict(key="qing_together", route="qing", route_name="青岩线", title="青岩 · 同行",
                 cond_text="青岩线 · 好感 ≥ 40 · 他当面信过你", is_true=False),
            dict(key="qing_alone",    route="qing", route_name="青岩线", title="青岩 · 独行",
                 cond_text="青岩线 · 好感 < 40 或未当面信过你",  is_true=False),
            dict(key="sealed",   route="common", route_name="共同线", title="封口",
                 cond_text="选择封站，或独自进入且未达真结局", is_true=False),
            dict(key="seventh",  route="common", route_name="共同线", title="第七天",
                 cond_text="十七信任 · 带出证据 · 非独线 · 本线好感 ≥ 60 · 完成本线承诺", is_true=True),
        ]


    def vn2_ending_item(key):
        for item in vn2_endings_matrix():
            if item["key"] == key:
                return item
        return None


    def vn2_route_bond(route):
        """路线承诺：光靠好感不够，必须在本线关键选择里留下过动作。
        lan = 蓝羽交过底；bai = 你救过白砚的手；qing = 青岩当面信过你。
        """
        if route == "lan":
            return bool(getattr(store, "close_lan", False))
        if route == "bai":
            return bool(getattr(store, "saved_bai", False))
        if route == "qing":
            return bool(getattr(store, "qing_trusted", False))
        return False


    def vn2_decide_ending(force_sealed=False):
        """按优先级 封口 > 真结局 > 同行 > 独行 落结局 key，并写入收集。"""
        route = store.vn2_lock_route
        route_aff = vn2_aff_value(route) if route in VN2_ROMANCE_KEYS else 0
        route_bond = vn2_route_bond(route)

        if force_sealed or route == "solo":
            key = "sealed"
        elif (getattr(store, "trust_shiqi", False)
                and getattr(store, "evidence_kept", False)
                and route_aff >= 60
                and route_bond):
            key = "seventh"
        elif route in VN2_ROMANCE_KEYS and route_aff >= 40 and route_bond:
            key = "%s_together" % route
        elif route in VN2_ROMANCE_KEYS:
            key = "%s_alone" % route
        else:
            key = "sealed"

        store.vn2_ending_key = key
        done = set(persistent.vn2_endings or set())
        done.add(key)
        persistent.vn2_endings = done
        return key


    def vn2_ending_list():
        """结局收集列表：读 matrix，字段兼容旧页（key/title/route），缺字段兜底。"""
        items = []
        for item in vn2_endings_matrix():
            items.append(dict(
                key=item.get("key", ""),
                title=item.get("title", item.get("key", "")),
                route=item.get("route_name", item.get("route", "")),
                route_name=item.get("route_name", ""),
                cond_text=item.get("cond_text", ""),
                is_true=bool(item.get("is_true", False)),
            ))
        return items


    # ---------- 章节选择回填 ----------

    def vn2_seed_for_chapter(cid):
        """章节选择/调试用：按章节所在路线与进度回填一套合理的好感与旗标。"""
        ch = CHAPTERS[cid]
        route = ch["route"]
        no = ch["no"]

        # 好感：共同线按进度缓升；进入本线后把对应恋爱线抬到可读区间
        base = min(35, 10 + int(no * 1.2))
        for key in VN2_AFF_KEYS:
            vn2_set_aff(key, base)

        if route in VN2_ROMANCE_KEYS:
            vn2_set_aff(route, min(60, base + 25))

        # 旗标按章节位置回填，避免回看中途章节时剧情读不到变量
        if no >= 3:
            vn2_flag("trust_team", True)
        if no >= 8:
            vn2_flag("ari_helped", True)
        if no >= 10:
            vn2_flag("lan_map_fixed", True)
        if no >= 11:
            vn2_flag("close_lan", True)
        if no >= 12:
            vn2_flag("saved_bai", True)
        if no >= 13:
            vn2_flag("know_qing_secret", True)
        if route == "bai" or no >= 20:
            vn2_flag("bai_treated", True)
        if route == "qing" and no >= 23:
            vn2_flag("qing_trusted", True)
        if cid == "ch15" or route == "bai":
            vn2_flag("station_key", True)
        if no >= 15:
            vn2_flag("trust_shiqi", True)
        if no >= 23:
            vn2_flag("evidence_copied", True)
        if no >= 24:
            vn2_flag("evidence_kept", True)

        store.vn2_lock_route = route if route in VN2_ROMANCE_KEYS else "solo"

        store.vn2_chapter_id = cid
        store.vn2_chapter_no = ch["no"]
        store.vn2_chapter_title = ch["title"]
        store.vn2_disp = ch["disp"]
        store.vn2_disp_label = vn2_chapter_label(cid)
        store.vn2_route_key = ch["route"]
        store.vn2_route_name = vn2_route_label(ch["route"])
        store.vn2_day = ch["day"]
