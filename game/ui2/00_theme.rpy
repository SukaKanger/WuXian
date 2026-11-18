# ============================================================
#  VN2 • 主题层
#  ------------------------------------------------------------
#  配色沿用 076 抖线•缝线「橄榄」：墨绿底 + 金线 + 纸感
#  init offset = 1 → 本目录所有 screen/style 覆盖 screens.rpy(-1)
# ============================================================

init offset = 1

define VN2_GOLD      = "#d8b263"
define VN2_GOLD_SOFT = "#e9cd96"
define VN2_GOLD_DIM  = "#8d7540"
define VN2_INK       = "#e9e4d6"
define VN2_DIM       = "#9c9684"
define VN2_FAINT     = "#6b6759"
define VN2_PANEL     = "#0e140f"

init python:

    def vn2_dialogue_size():
        try:
            return VN2_TEXT_SCALES[persistent.vn2_text_scale][1]
        except Exception:
            return 30

    def vn2_name_size():
        return vn2_dialogue_size()

    def vn2_set_text_scale(index):
        persistent.vn2_text_scale = max(0, min(len(VN2_TEXT_SCALES) - 1, int(index)))
        renpy.restart_interaction()


# ---------- 立绘姿态（4 角色通用） ----------
# 注意：xalign 是按「父宽 − 子宽」算的，0.22 会把立绘挤到左边；
# 这里用 xanchor 0.5 + xpos 小数，0.22 才是真正的 22% 屏宽中心。
transform vn2_pose(pos="center", lit=1.0):
    subpixel True
    yalign 1.0
    zoom 0.58
    xanchor 0.5
    xpos VN2_POS.get(pos, 0.5)
    # 说话高亮：用「降饱和 + 压暗」而不是 alpha——立绘是矩形整图，
    # 半透明会把方框边缘和底下的背景一起透出来。
    matrixcolor SaturationMatrix(0.24 + 0.76 * lit) * BrightnessMatrix(-0.28 * (1.0 - lit))
    # 不再做无限 yoffset 呼吸。立绘必须像站在地面上，
    # 否则每 5.6 秒上下漂 5px，整套角色都会显得“飘”。
    yoffset 0


# ---------- 通用动画 ----------
transform vn2_rise(delay=0.0, dy=24):
    alpha 0.0
    yoffset dy
    pause delay
    parallel:
        ease 0.30 alpha 1.0
    parallel:
        easeout 0.36 yoffset 0

transform vn2_zoom_in(delay=0.0):
    alpha 0.0
    zoom 0.95
    pause delay
    parallel:
        ease 0.32 alpha 1.0
    parallel:
        easeout 0.36 zoom 1.0

transform vn2_btn_flex:
    on idle:
        easein 0.10 zoom 1.0
    on hover:
        easein 0.12 zoom 1.035
    on insensitive:
        easein 0.10 zoom 1.0

transform vn2_slide_in(delay=0.0, dx=48):
    alpha 0.0
    xoffset dx
    pause delay
    parallel:
        easein 0.28 alpha 1.0
    parallel:
        easeout 0.34 xoffset 0

transform vn2_slide_hover:
    on idle:
        easein 0.10 xoffset 0
    on hover:
        easein 0.14 xoffset -14


# ---------- 常用样式 ----------
style vn2_text is default:
    font gui.text_font
    color VN2_INK
    size 24

style vn2_small is vn2_text:
    size 18
    color VN2_DIM

style vn2_title is vn2_text:
    size 46
    color VN2_GOLD
    font gui.text_font

style vn2_h2 is vn2_text:
    size 26
    color VN2_GOLD_SOFT

style vn2_label is gui_label

style vn2_label_text is vn2_text:
    size 20
    color VN2_GOLD_DIM


# ---------- 界面音效 ----------
# 六件 UI 音均为本工程程序化合成（_tools/make_ui_sfx.py，numpy + wave），
# 同一套音色基底 / 包络 / 亮度。所有按钮共用轻点击，hover 用更轻的提示音；
# 返回键在自己的 style 里换成 back 声。
style button:
    activate_sound "audio/ui/click.wav"
    hover_sound "audio/ui/hover.wav"


# 主菜单竖排按钮：扁平墨板（mbtn_*.png 原生 360×84），hover 时左侧亮起金条
style vn2_menu_button is button:
    background "images/ui/mbtn_idle.png"
    hover_background "images/ui/mbtn_hover.png"
    xsize 360
    ysize 84
    left_padding 56
    right_padding 18
    ypadding 0

style vn2_menu_button_text is button_text:
    font gui.text_font
    size 25
    kerning 1.5
    color "#d5cfbc"
    hover_color VN2_GOLD_SOFT
    insensitive_color "#54514a"
    text_align 0.0
    xalign 0.0
    yalign 0.5
    yoffset -2


# 面板内的小按钮
style vn2_btn is button:
    background Frame("images/ui/plate_idle.png", 22, 6, 22, 6)
    hover_background Frame("images/ui/plate_hover.png", 22, 6, 22, 6)
    selected_background Frame("images/ui/plate_selected.png", 22, 6, 22, 6)
    xpadding 24
    ypadding 9

style vn2_btn_text is button_text:
    font gui.text_font
    size 20
    kerning 1.0
    color "#d5cfbc"
    hover_color VN2_GOLD_SOFT
    selected_color VN2_GOLD
    insensitive_color "#54514a"


# 分隔线：改用 400×14 的渐隐金线（hairline.png），
# 精确到 1~2 px，不再用 1185×52 的装饰块（那个给 xsize 会撑成巨块）
image vn2_divider = Frame("images/ui/hairline.png", 24, 6, 24, 6)


screen vn2_line(w=600, h=2, color=VN2_GOLD_DIM):
    add Transform("images/ui/hairline.png", xysize=(w, h), fit="fill") xalign 0.5


# 滑条：细线 + 菱形滑钮（原来的 22px 金色粗条太重）
style vn2_bar is bar:
    ysize 14
    left_bar Frame("images/ui/bar_fill.png", 4, 0)
    right_bar Frame("images/ui/bar_track.png", 4, 0)
    thumb "images/ui/bar_thumb.png"
    thumb_offset 7

# 滚动条（viewport: scrollbars "vertical" 生成 game_menu_vscrollbar）
style game_menu_vscrollbar:
    xsize 8
    base_bar Solid("#181c16")
    thumb Frame("images/ui/scroll_thumb.png", 3, 3)


# 加载/存档卡片的底部信息条
style vn2_card is button:
    background None
    hover_background None

style vn2_card_num is vn2_text:
    size 16
    color VN2_GOLD_DIM

style vn2_card_title is vn2_text:
    size 21
    color VN2_INK

style vn2_card_sub is vn2_text:
    size 15
    color VN2_DIM
