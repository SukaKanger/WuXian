# ============================================================
#  VN2 · 主菜单 + 菜单导航
#  ------------------------------------------------------------
#  主菜单不复用 screens.rpy 的 navigation（那里是英文默认版），
#  但游戏内 game_menu 仍然 use navigation，所以两边都要给。
#  「开始新游戏」进 story_start（正式剧本），不是 script.rpy 的
#  开发期 demo（demo 末尾有 renpy.quit()，见交接书）。
#  背景用正片第一幕 images/bg/jungle.png（皮肤 main_menu.png 只是
#  1280×720 纯色板，铺满会变一片黑）。
# ============================================================

init offset = 1


style vn2_nav_button is vn2_menu_button:
    background "images/ui/nav_idle.png"
    hover_background "images/ui/nav_hover.png"
    xsize 240
    ysize 64
    left_padding 34
    right_padding 14

style vn2_nav_button_text is vn2_menu_button_text:
    size 22


screen main_menu():

    tag menu

    # 音乐不在这里放：screen 的 on "show" 在 call_in_new_context / 截图上下文里
    # 会把整屏刷黑（实测），改由 label before_main_menu 统一补


    $ cont_slot = vn2_continue_slot()
    $ n_chapter, n_chapter_total = vn2_chapter_progress()
    $ n_cg = vn2_cg_count()
    $ n_cg_total = vn2_cg_total()
    $ n_end = vn2_endings_count()
    $ n_end_total = len(vn2_endings_matrix())
    $ n_intel_unread = vn2_notebook_unread()

    # ---------- 背景 ----------
    add Transform("images/bg/jungle.png", xysize=(1920, 1080), fit="cover")
    add "images/ui/scrim_left.png"
    add "images/ui/veil_right.png" xpos 1300
    add Solid("#04070a0f")

    # ---------- 标题 ----------
    fixed:
        xpos 124
        ypos 104
        xsize 720
        ysize 250

        text "雾　线":
            style "vn2_text"
            size 96
            color VN2_GOLD_SOFT
            kerning 6.0

        text "二十七日 / 雨林":
            style "vn2_text"
            size 20
            color VN2_DIM
            kerning 3.0
            ypos 138

        add "images/ui/hairline.png" xysize (380, 2) ypos 188 alpha 0.8

    # ---------- 菜单 ----------
    vbox:
        xpos 140
        ypos 372
        spacing 6

        for i, (mtxt, mact, mok) in enumerate([
                (_("开始新游戏"), Start("story_start"), True),
                (_("继续游戏"), If(cont_slot, FileLoad(cont_slot, slot=True), NullAction()), bool(cont_slot)),
                (_("读取存档"), ShowMenu("load"), True),
                (_("章节选择"), ShowMenu("chapter_select"), True),
                (_("CG 画廊"), ShowMenu("gallery"), True),
                (_("设置"), ShowMenu("preferences"), True),
                ]):
            textbutton mtxt:
                style "vn2_menu_button"
                text_style "vn2_menu_button_text"
                sensitive mok
                action mact
                at vn2_slide_left(0.06 + 0.04 * i), vn2_nudge(12)

    # ---------- 左下：次级入口 ----------
    hbox:
        xpos 152
        ypos 962
        spacing 34

        textbutton _("关于"):
            style "vn2_quick_button"
            text_style "vn2_quick_button_text"
            action ShowMenu("about")

        textbutton _("退出"):
            style "vn2_quick_button"
            text_style "vn2_quick_button_text"
            action Quit(confirm=True)

    # 笔记本只在游戏内（对话框工具行 / 快捷键 N）出现，主菜单不再挂入口。

    # ---------- 右侧进度（无底板，只用细线分隔；从右外划入） ----------
    vbox:
        xpos 1508
        ypos 132
        xsize 330
        spacing 16
        at vn2_slide_right(0.18)

        text "进　度":
            style "vn2_text"
            size 16
            color VN2_GOLD
            kerning 6.0

        add "images/ui/hairline.png" xysize (330, 1) alpha 0.7

        null height 2

        hbox:
            xsize 330
            text "正文章节":
                style "vn2_small"
                size 18
                color "#cfc8b2"
                yalign 0.5
            hbox:
                xalign 1.0
                spacing 6
                yalign 0.5
                text "[n_chapter]":
                    style "vn2_text"
                    size 34
                    color VN2_GOLD_SOFT
                text "/ [n_chapter_total]":
                    style "vn2_small"
                    size 16
                    color "#8c8878"
                    yalign 0.5
                    yoffset 8

        add "images/ui/hairline.png" xysize (330, 1) alpha 0.35

        hbox:
            xsize 330
            text "CG":
                style "vn2_small"
                size 18
                color "#cfc8b2"
                yalign 0.5
            hbox:
                xalign 1.0
                spacing 6
                yalign 0.5
                text "[n_cg]":
                    style "vn2_text"
                    size 34
                    color VN2_GOLD_SOFT
                text "/ [n_cg_total]":
                    style "vn2_small"
                    size 16
                    color "#8c8878"
                    yalign 0.5
                    yoffset 8

        add "images/ui/hairline.png" xysize (330, 1) alpha 0.35

        hbox:
            xsize 330
            text "结局":
                style "vn2_small"
                size 18
                color "#cfc8b2"
                yalign 0.5
            hbox:
                xalign 1.0
                spacing 6
                yalign 0.5
                text "[n_end]":
                    style "vn2_text"
                    size 34
                    color VN2_GOLD_SOFT
                text "/ [n_end_total]":
                    style "vn2_small"
                    size 16
                    color "#8c8878"
                    yalign 0.5
                    yoffset 8

    # ---------- 右下：四个社交入口 ----------
    hbox:
        xalign 1.0
        yalign 1.0
        xoffset -60
        yoffset -92
        spacing 18

        for label, url in VN2_SOCIAL_MAIN:
            textbutton label:
                style "vn2_quick_button"
                text_style "vn2_quick_button_text"
                action Function(renpy.open_url, url)

    # ---------- 右下：发行入口（itch.io 与 VLink 聚合同行） ----------
    hbox:
        xalign 1.0
        yalign 1.0
        xoffset -60
        yoffset -132
        spacing 18

        textbutton "itch.io 发行页":
            style "vn2_quick_button"
            text_style "vn2_quick_button_text"
            text_color VN2_GOLD
            text_hover_color VN2_GOLD_SOFT
            action Function(renpy.open_url, VN2_RELEASE_URL)
            hover_sound "audio/ui/hover.wav"
            activate_sound "audio/ui/click.wav"

        textbutton "VLink 聚合":
            style "vn2_quick_button"
            text_style "vn2_quick_button_text"
            text_color VN2_GOLD
            text_hover_color VN2_GOLD_SOFT
            action Function(renpy.open_url, VN2_VLINK_URL)
            hover_sound "audio/ui/hover.wav"
            activate_sound "audio/ui/click.wav"

    text "[config.version]":
        style "vn2_text"
        size 15
        color VN2_FAINT
        xalign 1.0
        yalign 1.0
        xoffset -60
        yoffset -46


## 主菜单音乐 ################################################
#  before_main_menu 在「进入/退回主菜单」时都会跑，且不受 screen on-show 的限制。
label before_main_menu:
    $ vn2_menu_music()
    $ vn2_amb(None)
    return


## 游戏内菜单导航 ############################################

screen navigation():

    vbox:
        style_prefix "vn2_nav"
        xpos 52
        yalign 0.5
        spacing 5

        if main_menu:

            textbutton _("开始游戏") action Start("story_start")
            textbutton _("读取存档") action ShowMenu("load")

        else:

            textbutton _("回想") action ShowMenu("history")
            textbutton _("存档") action ShowMenu("save")
            textbutton _("读取") action ShowMenu("load")

        textbutton _("章节选择") action ShowMenu("chapter_select")
        textbutton _("CG 画廊") action ShowMenu("gallery")
        textbutton _("设置") action ShowMenu("preferences")

        if not main_menu:
            textbutton _("主菜单") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc"):
            textbutton _("退出") action Quit(confirm=not main_menu)
