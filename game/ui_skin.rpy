# ============================================================
#  009 直线·纸感·橄榄  —— 丛林探险 UI 皮肤 + 丝滑动画层
#  皮肤（PNG）来自 L:\AI\RenPyUI_100_20261116\009_直线_纸感
#  动画全部为通用 ATL，不含任何第三方素材
# ============================================================

# ---------- 1. 皮肤尺寸与 Frame 边距（必须在 gui.rpy 之前） ----------
init -2 python:
    gui.textbox_height = 348
    gui.textbox_yalign = 1.0

    gui.namebox_width = 340
    gui.namebox_height = 78
    gui.namebox_borders = Borders(10, 0, 10, 0)
    gui.namebox_tile = False

    gui.name_xpos = 300
    gui.name_ypos = 42
    gui.name_xalign = 0.0

    gui.dialogue_xpos = 120
    gui.dialogue_ypos = 110
    gui.dialogue_width = 1680
    gui.dialogue_text_xalign = 0.0

    gui.choice_button_width = 640
    gui.choice_button_height = 86
    gui.choice_button_borders = Borders(44, 10, 44, 10)
    gui.choice_button_text_size = 30

    gui.button_borders = Borders(44, 10, 44, 10)
    gui.text_size = 30
    gui.name_text_size = 30


# ---------- 2. 补 style（用 Ren'Py 原生 style 语句，不用 python 赋值） ----------

style window:
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    background Frame("gui/namebox.png", gui.namebox_borders, tile=False)

style button:
    background Frame("gui/button/idle_background.png", 44, 10, 44, 10)
    hover_background Frame("gui/button/hover_background.png", 44, 10, 44, 10)
    insensitive_background Frame("gui/button/pressed_background.png", 44, 10, 44, 10)
    selected_background Frame("gui/button/selected_idle_background.png", 44, 10, 44, 10)
    selected_hover_background Frame("gui/button/hover_background.png", 44, 10, 44, 10)

style choice_button:
    background Frame("gui/choice_idle_background.png", 44, 10, 44, 10)
    hover_background Frame("gui/choice_hover_background.png", 44, 10, 44, 10)

style frame:
    background Frame("gui/frame.png", 64, 64, 64, 64)

style quick_button:
    background None
    hover_background Frame("gui/button/quick_hover_background.png", 20, 6, 20, 6)


# ---------- 3. 丝滑动画（ATL） ----------

# 3.1 通用按钮：hover 轻微放大
transform btn_flex:
    on idle:
        easein 0.10 zoom 1.0
    on hover:
        easein 0.12 zoom 1.025
    on insensitive:
        easein 0.10 zoom 1.0

# 3.2 主菜单项：从右侧滑入 + 淡入
transform menu_slide_in(delay=0.0, dx=60):
    alpha 0.0
    xoffset dx
    pause delay
    parallel:
        easein 0.32 alpha 1.0
    parallel:
        easeout 0.32 xoffset 0

# 3.3 主菜单项 hover：向左推 + 放大
transform menu_hover:
    on idle:
        easein 0.10 xoffset 0 zoom 1.0
    on hover:
        easein 0.14 xoffset -14 zoom 1.03

# 3.4 对话框：从下方滑入 + 淡入
transform textbox_slide:
    alpha 0.0
    yoffset 40
    parallel:
        easein 0.22 alpha 1.0
    parallel:
        easeout 0.26 yoffset 0

# 3.5 名字框：弹出回弹
transform namebox_pop:
    alpha 0.0
    zoom 0.88
    parallel:
        easeout 0.18 alpha 1.0
    parallel:
        easeout 0.18 zoom 1.0
    easein 0.06 zoom 1.015
    easeout 0.08 zoom 1.0

# 3.6 面板/弹窗：淡入 + 上移
transform panel_rise:
    alpha 0.0
    yoffset 26
    parallel:
        easein 0.20 alpha 1.0
    parallel:
        easeout 0.24 yoffset 0

# 3.7 选择项：依次入场
transform choice_in(idx=0):
    alpha 0.0
    xoffset -40
    pause (idx * 0.045)
    parallel:
        easein 0.20 alpha 1.0
    parallel:
        easeout 0.22 xoffset 0

# 3.8 背景：极慢推镜
transform bg_breath:
    subpixel True
    zoom 1.0
    linear 24.0 zoom 1.04
    linear 24.0 zoom 1.0
    repeat

# 3.9 立绘入场
transform char_in:
    alpha 0.0
    yoffset 24
    parallel:
        easein 0.24 alpha 1.0
    parallel:
        easeout 0.28 yoffset 0

# 3.10 立绘呼吸
transform char_breathe:
    subpixel True
    yoffset 0
    ease 2.6 yoffset -4
    ease 2.6 yoffset 0
    repeat

# 3.11 立绘说话轻推
transform char_speak:
    easein 0.12 zoom 1.012
    easeout 0.20 zoom 1.0


# ---------- 4. 全局转场与手感 ----------
define fade_soft = Fade(0.18, 0.0, 0.22, color="#000000")
define dissolve_soft = Dissolve(0.22)
define wipe_left = CropMove(0.22, "wipeleft")

init python:
    config.window_show_transition = Dissolve(0.16)
    config.window_hide_transition = Dissolve(0.16)
    preferences.text_cps = 28
    preferences.afm_time = 12
