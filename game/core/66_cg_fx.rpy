# ============================================================
#  VN2 • CG 编号 / 专属入画演出
#  ------------------------------------------------------------
#  24 张一代 CG 统一编号 cg01–cg24，剧情与画廊共用同一套文件。
#  每张 CG 有自己的入画参数：从哪一侧滑入、起始缩放、落位时长、
#  黑场长度、亮起速度、是否换 BGM。
#
#  参数含义（都是屏幕归一化单位，0.5 = 屏幕中心）：
#      sx, sy   起点偏移，-0.4 = 从左边外面进来
#      z0       起始缩放，1.0 = 原尺寸
#      dur      滑到位的时长
#      push     落位后继续缓慢推近到的缩放（1.0 = 不动）
#      push_t   推近时长
#      black    先压黑的时间（0 = 不压黑，直接淡入）
#      reveal   从黑里亮起来的时间
#      bgm      进这张 CG 时切换的曲目 key（None = 不动）
# ============================================================

init -1 python:

    # 编号 → 旧 id（剧情里仍按旧 id 调用，靠这张表反查）
    VN2_CG_ORDER = [
        ("cg01", "cg_camp_fire_v1"),
        ("cg02", "cg_key_rope_anchor_v2"),
        ("cg03", "cg_key_four_people_v0"),
        ("cg04", "cg_key_gate_v1"),
        ("cg05", "cg_key_badge_v2"),
        ("cg06", "cg_key_half_name_v0"),
        ("cg07", "cg_route_lan_ridge_v0"),
        ("cg08", "cg_key_half_map_v2"),
        ("cg09", "cg_key_half_pill_v2"),
        ("cg10", "cg_key_crush_v0"),
        ("cg11", "cg_key_surgery_v1"),
        ("cg12", "cg_route_bai_ward_v0"),
        ("cg13", "cg_key_archive_v1"),
        ("cg14", "cg_route_qing_ruins_v0"),
        ("cg15", "cg_key_settle_v2"),
        ("cg16", "cg_key_dawn_v2"),
        ("cg17", "cg_end_lan_together_v1"),
        ("cg18", "cg_end_lan_alone_v0"),
        ("cg19", "cg_end_bai_together_v1"),
        ("cg20", "cg_end_bai_alone_v0"),
        ("cg21", "cg_end_qing_together_v0"),
        ("cg22", "cg_end_qing_alone_v1"),
        ("cg23", "cg_end_sealed_v1"),
        ("cg24", "cg_end_seventh_v0"),
    ]

    VN2_CG_ID_BY_NUM = dict(VN2_CG_ORDER)                       # cg01 → cg_camp_fire_v1
    VN2_CG_NUM_BY_ID = dict((i, n) for n, i in VN2_CG_ORDER)    # cg_camp_fire_v1 → cg01

    # 剧情里可能还在用旧 id 的 4 张单角色图（不进画廊）
    VN2_CG_ID_BY_NUM.update({
        "cg_zhou": "cg_zhou",
        "cg_lan": "cg_lan",
        "cg_bai": "cg_bai",
        "cg_qing": "cg_qing",
    })

    VN2_CG_FX = {
        # ---- 共同线 ----
        "cg_camp_fire_v1": dict(  # 01 营火：从左边慢慢推进来，暖光慢起
            sx=-0.30, sy=0.02, z0=1.12, dur=1.25, push=1.04, push_t=1.6,
            black=0.45, reveal=0.22, bgm=None, bgm_fade=1.8),
        "cg_key_rope_anchor_v2": dict(  # 02 断崖绳锚：从上方砸下来，快落位
            sx=0.02, sy=-0.34, z0=1.28, dur=0.55, push=1.02, push_t=0.8,
            black=0.20, reveal=0.14, bgm=None, bgm_fade=1.6),
        "cg_key_four_people_v0": dict(  # 03 四个人的夜：从右边横着滑进来
            sx=0.36, sy=0.0, z0=1.10, dur=0.95, push=1.03, push_t=1.2,
            black=0.40, reveal=0.20, bgm=None, bgm_fade=1.8),
        "cg_key_gate_v1": dict(  # 04 门口：从地面升起来
            sx=0.0, sy=0.32, z0=1.14, dur=0.95, push=1.05, push_t=1.4,
            black=0.55, reveal=0.20, bgm=None, bgm_fade=1.8),
        "cg_key_badge_v2": dict(  # 05 旧队徽：由小顶到眼前，像递过来
            sx=0.0, sy=0.0, z0=0.84, dur=1.10, push=1.06, push_t=1.5,
            black=0.35, reveal=0.22, bgm=None, bgm_fade=1.8),
        "cg_key_half_name_v0": dict(  # 06 雾里的名字：左上方斜插
            sx=-0.24, sy=-0.20, z0=1.18, dur=1.15, push=1.05, push_t=1.5,
            black=0.60, reveal=0.25, bgm=None, bgm_fade=2.0),
        "cg_route_lan_ridge_v0": dict(  # 07 山脊：右边大幅横移，进蓝羽线
            sx=0.44, sy=-0.04, z0=1.22, dur=1.05, push=1.06, push_t=1.6,
            black=0.50, reveal=0.22, bgm="lan", bgm_fade=2.2),
        "cg_key_half_map_v2": dict(  # 08 半张地图：右下角斜铺开
            sx=0.30, sy=0.22, z0=1.06, dur=0.85, push=1.04, push_t=1.2,
            black=0.35, reveal=0.18, bgm=None, bgm_fade=1.8),
        "cg_key_half_pill_v2": dict(  # 09 半片药：左下角斜插
            sx=-0.28, sy=0.18, z0=1.12, dur=0.90, push=1.05, push_t=1.3,
            black=0.45, reveal=0.20, bgm=None, bgm_fade=1.8),
        "cg_key_crush_v0": dict(  # 10 药瓶：怼到眼前，最短最急
            sx=0.06, sy=0.04, z0=1.38, dur=0.42, push=1.08, push_t=0.9,
            black=0.14, reveal=0.12, bgm=None, bgm_fade=1.4),
        "cg_key_surgery_v1": dict(  # 11 灯下手术：长黑场，极慢推近
            sx=0.0, sy=0.0, z0=1.05, dur=1.60, push=1.07, push_t=2.0,
            black=0.85, reveal=0.35, bgm=None, bgm_fade=2.4),
        "cg_route_bai_ward_v0": dict(  # 12 站门外：从右边窄缝挤进来，进白砚线
            sx=0.26, sy=0.0, z0=1.02, dur=1.20, push=1.04, push_t=1.6,
            black=0.55, reveal=0.25, bgm="bai", bgm_fade=2.2),
        # ---- 后半程 ----
        "cg_key_archive_v1": dict(  # 13 档案室：从上方垂下来
            sx=0.0, sy=-0.28, z0=1.10, dur=1.00, push=1.04, push_t=1.4,
            black=0.50, reveal=0.20, bgm=None, bgm_fade=1.8),
        "cg_route_qing_ruins_v0": dict(  # 14 遗迹：从地下抬起来，进青岩线
            sx=-0.02, sy=0.36, z0=1.16, dur=1.10, push=1.06, push_t=1.6,
            black=0.55, reveal=0.22, bgm="qing", bgm_fade=2.2),
        "cg_key_settle_v2": dict(  # 15 结算：左边平推，收得干脆
            sx=-0.38, sy=0.0, z0=1.00, dur=0.80, push=1.02, push_t=1.0,
            black=0.26, reveal=0.15, bgm=None, bgm_fade=1.6),
        "cg_key_dawn_v2": dict(  # 16 出林：长黑里慢慢亮，画面往外退
            sx=0.0, sy=0.10, z0=1.16, dur=1.50, push=1.00, push_t=0.0,
            black=1.00, reveal=1.25, bgm="common", bgm_fade=2.6),
        # ---- 结局 ----
        "cg_end_lan_together_v1": dict(  # 17 蓝羽同行：中心推近，落结局曲
            sx=0.0, sy=0.0, z0=1.10, dur=1.30, push=1.06, push_t=1.8,
            black=1.10, reveal=0.45, bgm="ending", bgm_fade=2.8),
        "cg_end_lan_alone_v0": dict(  # 18 蓝羽独行：从左边极慢滑，留白
            sx=-0.30, sy=0.06, z0=1.04, dur=1.85, push=1.08, push_t=2.2,
            black=1.25, reveal=0.55, bgm="ending", bgm_fade=2.8),
        "cg_end_bai_together_v1": dict(  # 19 白砚同行：从右边贴着进来
            sx=0.32, sy=-0.04, z0=1.08, dur=1.30, push=1.05, push_t=1.8,
            black=1.05, reveal=0.45, bgm="ending", bgm_fade=2.8),
        "cg_end_bai_alone_v0": dict(  # 20 白砚独行：从地面升起，慢
            sx=0.0, sy=0.30, z0=1.06, dur=1.70, push=1.05, push_t=2.0,
            black=1.25, reveal=0.50, bgm="ending", bgm_fade=2.8),
        "cg_end_qing_together_v0": dict(  # 21 青岩同行：从上方压下来
            sx=0.04, sy=-0.30, z0=1.08, dur=1.30, push=1.06, push_t=1.8,
            black=1.05, reveal=0.45, bgm="ending", bgm_fade=2.8),
        "cg_end_qing_alone_v1": dict(  # 22 青岩独行：左上斜进来，最长的落位
            sx=-0.26, sy=-0.24, z0=1.12, dur=1.90, push=1.07, push_t=2.2,
            black=1.30, reveal=0.55, bgm="ending", bgm_fade=2.8),
        "cg_end_sealed_v1": dict(  # 23 封口：猛地缩回，重黑场压住
            sx=0.0, sy=0.0, z0=1.50, dur=0.50, push=1.00, push_t=0.0,
            black=1.40, reveal=0.60, bgm="common_tense", bgm_fade=2.0),
        "cg_end_seventh_v0": dict(  # 24 第七天：从黑里极缓浮出
            sx=0.0, sy=0.0, z0=1.04, dur=1.80, push=1.09, push_t=2.4,
            black=1.60, reveal=0.70, bgm="ending", bgm_fade=3.0),
    }

    # 没有登记的 CG（单角色旧图等）走这套中性参数
    VN2_CG_FX_DEFAULT = dict(
        sx=0.0, sy=0.0, z0=1.04, dur=0.9, push=1.02, push_t=1.0,
        black=0.35, reveal=0.55, bgm=None, bgm_fade=1.8)

    def vn2_cg_num(cid):
        """旧 id / 文件名 / cgNN 都换成 cgNN；认不出来就原样返回。"""
        if not cid:
            return None
        s = str(cid).replace("\\", "/")
        if "/" in s:
            s = s.rsplit("/", 1)[-1]
        if s.lower().endswith(".png"):
            s = s[:-4]
        if s in VN2_CG_ID_BY_NUM:
            return s
        return VN2_CG_NUM_BY_ID.get(s, s)

    def vn2_cg_resolve(x):
        """任意引用 → 旧 id（没有登记就返回 None）。"""
        if not x:
            return None
        s = str(x).replace("\\", "/")
        if "/" in s:
            s = s.rsplit("/", 1)[-1]
        if s.lower().endswith(".png"):
            s = s[:-4]
        if s in VN2_CG_FX:
            return s
        if s in VN2_CG_ID_BY_NUM:
            return VN2_CG_ID_BY_NUM[s]
        return None

    def vn2_cg_path(cid):
        """旧 id → 现在实际用的文件（cgNN.png 优先，其次保留旧文件名）。"""
        num = vn2_cg_num(cid)
        cand = "images/cg/%s.png" % num
        if vn2_playable(cand):
            return cand
        cand2 = "images/cg/%s.png" % cid
        if vn2_playable(cand2):
            return cand2
        return cand

    # 统一的“慢半拍”系数：原始参数是按短视频节奏写的，实际全屏观看时
    # 落位太快、黑场还没亮完画面就已经到位，看起来像硬切。
    # 这里统一把落位/推近/亮起拉长，再配合下方 transform 的 ease 缓动。
    VN2_CG_TIME_SCALE = 1.75
    VN2_CG_PUSH_SCALE = 1.55
    VN2_CG_REVEAL_SCALE = 1.35

    def vn2_cg_fx(cid):
        spec = dict(VN2_CG_FX.get(cid, VN2_CG_FX_DEFAULT))
        spec["dur"] = max(1.20, float(spec.get("dur", 0.9)) * VN2_CG_TIME_SCALE)
        spec["push_t"] = max(1.30, float(spec.get("push_t", 1.0)) * VN2_CG_PUSH_SCALE)
        spec["reveal"] = max(0.34, float(spec.get("reveal", 0.55)) * VN2_CG_REVEAL_SCALE)
        spec["black"] = max(0.30, float(spec.get("black", 0.35)) * 1.10)
        return spec

    def vn2_cg_enter_at(cid):
        """给画廊 / 预览用：只做运动，不带黑场。"""
        spec = vn2_cg_fx(cid)
        return vn2_cg_enter(spec["sx"] * 0.45, spec["sy"] * 0.45,
                           1.0 + (spec["z0"] - 1.0) * 0.6,
                           0.55, spec["push"], max(0.02, min(spec["push_t"], 1.4)))


transform vn2_cg_enter(sx=0.0, sy=0.0, z0=1.0, dur=0.9, push=1.0, push_t=1.2):
    xanchor 0.5
    yanchor 0.5
    xpos 0.5 + sx
    ypos 0.5 + sy
    zoom z0
    alpha 0.0

    # 黑场完全压住之后再起运动，避免观众看到的是“已经走了一半”
    pause 0.10

    parallel:
        ease dur alpha 1.0
    parallel:
        ease dur xpos 0.5
    parallel:
        ease dur ypos 0.5
    parallel:
        ease dur zoom 1.0

    ease push_t zoom push


# 剧情 CG 用的“落定”演出：不做横冲直撞的滑入，
# 只在黑场亮起后做很小的一段漂移 + 极缓推近，观感更像镜头自己站稳。
transform vn2_cg_settle(sx=0.0, sy=0.0, z0=1.0, dur=2.2, push=1.0, push_t=3.0, wait=0.8):
    xanchor 0.5
    yanchor 0.5
    xpos 0.5 + sx * 0.10
    ypos 0.5 + sy * 0.10
    zoom z0
    alpha 1.0

    pause wait

    parallel:
        ease dur xpos 0.5
    parallel:
        ease dur ypos 0.5
    parallel:
        ease dur zoom 1.0

    ease push_t zoom push

default vn2_cg_current = None
