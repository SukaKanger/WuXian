# ============================================================
#  VN2 • 载入界面（splashscreen）
#  ------------------------------------------------------------
#  结构：底图缓慢推进 → 两层雾横向漂移 → 暗角 + 胶片颗粒 + 浮尘
#        左下：标题落位 + hairline 展开 + 2.4s 进度细线 + 状态/百分比
#  进度是「表演性」的（真实资源加载由 Ren'Py 自己按需完成），
#  但走的是真实时间轴，点击任意处可直接跳过。
#
#  素材：_tools/make_loading_assets.py（fog_*/vignette/grain/dust）
# ============================================================

init offset = 1

init python:
    def vn2_now():
        # 只在函数内导入 time，避免模块对象进入 store 后被存档 pickle。
        import time
        return time.time()

define VN2_LOAD_TIPS = [
    "对话框右上角：回想 / 回退 / 快进 / 自动 / 存档 / 设置",
    "未到达的章节在章节选择里显示为暗色",
    "CG 解锁会存进 persistent，换存档也在",
    "按住 Ctrl 可以快进已读文本",
]

default vn2_load_progress = 0.0

# 截图/调试 harness 接管入口用；正常游玩为 None。
define VN2_SPLASH_HOOK = None


image vn2_grain_tile = Tile("images/ui/grain.png")


transform vn2_load_kenburns():
    zoom 1.0
    align (0.5, 0.5)
    linear 9.0 zoom 1.055


transform vn2_fog_drift(x0, period, w=2100, y=0, a=1.0):
    xpos x0
    ypos y
    alpha a
    linear period xpos (x0 - w)
    repeat



transform vn2_load_line_grow(delay=0.4, w=360):
    xsize 0
    pause delay
    easeout 0.55 xsize w


style vn2_load_bar is bar:
    ysize 2
    left_bar Solid("#d8b263")
    right_bar Solid("#232b22")


screen vn2_loading():

    zorder 950

    $ p = vn2_load_progress
    $ pct = int(round(p * 100))
    $ stage = 0 if p < 0.26 else (1 if p < 0.52 else (2 if p < 0.74 else (3 if p < 0.93 else 4)))
    $ stage_text = [ "正在校准雾线", "正在装载底片", "正在接入无线电信标", "正在对齐二十七日", "即将抵达" ][stage]
    $ tip = VN2_LOAD_TIPS[stage % len(VN2_LOAD_TIPS)]

    # ---------- 底图 ----------
    add Transform("images/bg/gate.png", xysize=(1920, 1080), fit="cover") at vn2_load_kenburns()
    add Solid("#050906") alpha 0.52

    # ---------- 雾 ----------
    add "images/ui/fog_b.png" at vn2_fog_drift(0, 66.0, 2100, 232, 0.62)
    add "images/ui/fog_b.png" at vn2_fog_drift(2100, 66.0, 2100, 232, 0.62)
    add "images/ui/fog_a.png" at vn2_fog_drift(0, 46.0, 2100, 512, 0.85)
    add "images/ui/fog_a.png" at vn2_fog_drift(2100, 46.0, 2100, 512, 0.85)

    # ---------- 质感层 ----------
    add "images/ui/vignette.png"
    add "vn2_grain_tile"

    # 浮尘
    for i, (dx, dy, dd, du) in enumerate([
            (312, 760, 0.6, 7.4), (498, 690, 1.9, 8.8), (742, 812, 3.1, 6.9),
            (980, 728, 0.9, 9.2), (1188, 786, 2.4, 7.8), (1396, 700, 4.2, 8.4),
            (1602, 828, 1.4, 7.1), (1726, 742, 3.6, 9.6), (628, 640, 5.0, 8.1),
            (1242, 652, 5.6, 7.7)]):
        add "images/ui/dust.png" at vn2_dust(dx, dy, dd, du)

    # ---------- 标题 ----------
    vbox:
        xpos 128
        ypos 300
        spacing 16

        text "雾　线":
            size 86
            color VN2_GOLD_SOFT
            kerning 5.0
            at vn2_rise(0.05, 28)

        fixed:
            xysize (360, 2)
            add Transform("images/ui/hairline.png", xysize=(360, 2)) alpha 0.55 at vn2_load_line_grow(0.42, 360)

        text "二十七日 / 雨林":
            size 20
            color VN2_DIM
            kerning 1.5
            at vn2_rise(0.72, 16)

    # ---------- 进度 ----------
    vbox:
        xpos 128
        ypos 826
        spacing 14
        xsize 560

        hbox:
            xsize 560
            text stage_text:
                size 15
                color "#9c9684"
                kerning 1.0
            text "[pct]%":
                size 15
                color VN2_GOLD
                xalign 1.0

        bar value p range 1.0 style "vn2_load_bar" xsize 560

        text tip:
            size 14
            color "#6b6759"
            xmaximum 560

    # 右下版本
    text "[config.version]":
        size 14
        color "#54514a"
        xalign 0.96
        yalign 0.94


# ---------- 出品方 logo 开场 ----------
#  近白底 #f4f2ec + 深色字标（logo_suka_dark.png，原图 859×560，显示 460×300 保持比例）。
#  logo_suka_light.png 是米白字透明底版本，留作未来深色底开场备用，本轮不接入。
#  时序：黑场 0.30s → 淡入 0.80s → 停留 2.00s → 淡出 0.80s（合计约 3.9s）；
#  淡出落到黑底再接下方载入页，接缝不闪白。本阶段不碰 music 通道，不抢主菜单音乐。
image vn2_black = Solid("#000000")
# 原图 859×560，显示 460×300 保持比例；anchor 0.5 + 中点定位保证真正居中
image vn2_logo_img = Transform("images/ui/logo_suka_dark.png", xysize=(460, 300),
                               anchor=(0.5, 0.5), xpos=0.5, ypos=0.5)

screen vn2_logo_splash():
    zorder 1000
    add Solid("#f4f2ec")
    add "vn2_logo_img"

label vn2_logo_splash:
    scene vn2_black with None
    $ renpy.pause(0.30, hard=True)
    show screen vn2_logo_splash with Dissolve(0.80)
    $ renpy.pause(2.00, hard=True)
    hide screen vn2_logo_splash with Dissolve(0.80)
    scene vn2_black with Dissolve(0.80)
    $ renpy.pause(0.10, hard=True)
    return


label splashscreen:

    if VN2_SPLASH_HOOK:
        $ renpy.jump(VN2_SPLASH_HOOK)

    call vn2_logo_splash

    $ vn2_load_progress = 0.0
    # 开场与主菜单统一用平缓的旧站环境曲；章节内仍由 common 接管。
    $ vn2_bgm("station", fade=3.0)
    show screen vn2_loading

    python:
        _t0 = vn2_now()
        _dur = 2.4
        while vn2_load_progress < 1.0:
            _e = (vn2_now() - _t0) / _dur
            if _e >= 1.0:
                vn2_load_progress = 1.0
                break
            vn2_load_progress = 1.0 - (1.0 - _e) ** 2
            renpy.restart_interaction()
            if renpy.pause(0.04):
                vn2_load_progress = 1.0
                break

    $ renpy.pause(0.30, hard=True)
    hide screen vn2_loading
    with Dissolve(0.45)
    return
