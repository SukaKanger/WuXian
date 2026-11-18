# ============================================================
#  VN2 • HUD 层
#  ------------------------------------------------------------
#  覆盖：say（字号可调）、confirm（中文）、quick_menu（中文）
#  新增：vn2_chapter_card（章号标题卡）
# ============================================================

init offset = 1


## 对话界面 ##################################################
#  皮肤 textbox.png 实际是 1680×348（内框上沿 y≈35、下沿 y≈330），
#  但 gui.rpy 里 gui.textbox_height = gui.scale(185)，文字会挤在框底。
#  这里按图重设：窗口 348 高，名字 y=44，正文 y=108，左边距 246。

init python:
    gui.textbox_height = 300
    gui.textbox_yalign = 1.0
    gui.name_xpos = 236
    gui.name_ypos = -54
    gui.dialogue_xpos = 236
    gui.dialogue_ypos = 76
    gui.dialogue_width = 1348


style window:
    ysize 300
    yalign 1.0
    background None

style say_dialogue:
    xpos 236
    xsize 1348
    ypos 856
    line_spacing 10

style say_label:
    xalign 0.0
    yalign 0.5


screen say(who, what):

    window:
        id "window"

    # 对话框底板（1720×300，落在 y=780）—— 每次换场从下方托上来。
    # tb_vines.png 是以 tb.png 为底、右下角烘焙了丛林藤蔓的最终底板；
    # 矢量源文件在 images/ui/_source/dlg_vines.svg。
    add "images/ui/tb_vines.png" xpos 100 ypos 780

    # 名字牌压在对话框上沿，而不是浮在框外。
    # 名字和职位分开渲染：中间用小菱形分隔，不再用容易缺字的中点。
    if who is not None:
        $ _who_name, _who_role = vn2_name_role(who)
        frame:
            id "namebox"
            background Frame("images/ui/name.png", 18, 6, 18, 6)
            xpos 236
            ypos 744
            xminimum 210
            padding (30, 8, 28, 8)

            hbox:
                spacing 12
                yalign 0.5

                text _who_name id "who" size vn2_name_size() color VN2_GOLD_SOFT style "vn2_text" yalign 0.5

                if _who_role:
                    add "images/ui/bar_thumb.png" xysize (10, 10) yalign 0.5
                    text _who_role size 17 color VN2_DIM style "vn2_text" kerning 2.0 yalign 0.5 yoffset 1

    text what id "what" size vn2_dialogue_size() style "say_dialogue"

    # 对话框右上角的工具行（不再依赖 overlay 层的 quick_menu：
    # 在 call_in_new_context 里 overlay 会被抑制，截图和部分剧情上下文里看不见）
    if quick_menu:
        hbox:
            style_prefix "vn2_quick"
            xanchor 1.0
            xpos 1794
            ypos 802
            spacing 24

            textbutton _("回想") action ShowMenu('history')
            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("存档") action ShowMenu('save')
            textbutton _("设置") action ShowMenu('preferences')

            # 笔记本：实物封面小图标 + 文字，挂在对话工具行里（游戏内唯一入口）
            button:
                style "vn2_quick_button"
                action Show("vn2_notebook")
                hover_sound "audio/ui/hover.wav"
                activate_sound "audio/ui/back.wav"

                hbox:
                    spacing 8
                    yalign 0.5

                    add Transform("images/ui/notebook_cover.png", xysize=(44, 44)):
                        yalign 0.5
                        yoffset 2

                    text "笔记本":
                        style "vn2_quick_button_text"
                        size 19
                        yalign 0.5

        key "n" action Show("vn2_notebook")

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 章号标题卡 ################################################

screen vn2_chapter_card(no, title, sub=""):
    zorder 220
    modal False

    add Solid("#070b07")

    $ _card_route = getattr(store, "vn2_route_key", "common")
    $ _card_route_name = VN2_ROUTE_NAMES.get(_card_route, "")
    # 章节副题里的中点/圆点在思源黑体精简子集里可能缺字形，统一成斜杠。
    $ _card_sub = (sub or "").replace("•", "/").replace("·", "/")

    vbox:
        xalign 0.5
        yalign 0.46
        spacing 14
        at vn2_rise(0.0)

        if isinstance(no, int):
            text "CHAPTER  [no:02d]":
                style "vn2_text"
                size 19
                color VN2_GOLD_DIM
                xalign 0.5
                kerning 4.0

            if _card_route in ("lan", "bai", "qing"):
                text "%s / 第 [no] 章" % _card_route_name:
                    style "vn2_text"
                    size 34
                    color VN2_GOLD
                    xalign 0.5
            elif _card_route == "end":
                text "结局 / 第 [no] 章":
                    style "vn2_text"
                    size 34
                    color VN2_GOLD
                    xalign 0.5
            else:
                text "第 [no] 章":
                    style "vn2_text"
                    size 34
                    color VN2_GOLD
                    xalign 0.5
        else:
            text store.vn2_disp_label:
                style "vn2_text"
                size 34
                color VN2_GOLD
                xalign 0.5

        null height 4

        text title:
            style "vn2_text"
            size 62
            color VN2_INK
            xalign 0.5

        null height 12

        # 细金线用原始 PNG 指定 ysize，不再用 Frame 让它在 vbox 里被拉成巨块
        add "images/ui/hairline.png" xalign 0.5 xsize 620 ysize 2 alpha 0.8

        if _card_sub:
            null height 8
            text _card_sub:
                style "vn2_text"
                size 21
                color VN2_DIM
                xalign 0.5

    # 四角金托
    add "gui/decor/corner_tl.png" xpos 70 ypos 70 alpha 0.55
    add "gui/decor/corner_tr.png" xalign 1.0 xoffset -70 ypos 70 alpha 0.55
    add "gui/decor/corner_bl.png" xpos 70 yalign 1.0 yoffset -70 alpha 0.55
    add "gui/decor/corner_br.png" xalign 1.0 xoffset -70 yalign 1.0 yoffset -70 alpha 0.55


label vn2_title_card(no, title, sub=""):
    $ renpy.show_screen("vn2_chapter_card", no=no, title=title, sub=sub)
    with Dissolve(0.35)
    $ renpy.pause(0.5 if renpy.get_skipping() else 2.0, hard=True)
    hide screen vn2_chapter_card
    with Dissolve(0.4)

    # 等标题卡完全退场、场景帧稳定后再拍存档缩略图；否则会拍到启动页/转场纯色。
    $ renpy.pause(0.12, hard=True)
    $ vn2_autosave_entry()

    return


## 快捷菜单 ##################################################
#  实际按钮已经搬进 screen say（对话框右上角）。
#  这里保留一个空壳：config.overlay_screens 里仍列着 "quick_menu"，
#  删掉定义会报找不到 screen。

screen quick_menu():
    pass


style vn2_quick_button is default:
    background None
    hover_background None
    xpadding 2
    ypadding 2

style vn2_quick_button_text is button_text:
    font gui.text_font
    size 19
    kerning 1.6
    color "#c9c0a8"
    hover_color VN2_GOLD_SOFT
    selected_color VN2_GOLD
    insensitive_color "#4d4a40"


## 二次确认（中文） ##########################################

init python:

    VN2_CONFIRM_CN = {
        "Are you sure you want to delete this save?":
            "确定删除这个存档吗？",
        "Are you sure you want to overwrite your save?":
            "这个槽位已有存档，要覆盖吗？",
        "Loading will lose unsaved progress.\nAre you sure you want to do this?":
            "读档会丢掉当前未保存的进度。\n仍然要继续吗？",
        "Are you sure you want to quit?":
            "确定退出游戏吗？",
        "Are you sure you want to return to the main menu?\nThis will lose unsaved progress.":
            "返回主菜单会丢掉未保存的进度。\n仍然要返回吗？",
        "Are you sure?":
            "确定吗？",
        "Are you sure you want to begin skipping?":
            "确定开始跳过文本吗？",
        "Are you sure you want to skip to the next choice?":
            "确定跳过到下一个选项吗？",
        "Are you sure you want to skip unseen dialogue to the next choice?":
            "确定连未读文本一起跳过到下一个选项吗？",
        "Are you sure you want to continue where you left off?":
            "确定从上次离开处继续吗？",
        "Are you sure you want to end the replay?":
            "确定结束回放吗？",
    }

    def vn2_confirm_text(message):
        return VN2_CONFIRM_CN.get(message, message)


screen confirm(message, yes_action, no_action):

    modal True
    zorder 200

    add "gui/overlay_dim.png"

    frame:
        background Frame("gui/confirm.png", 56, 56, 56, 56)
        xalign 0.5
        yalign 0.5
        xsize 820
        padding (60, 48, 60, 42)

        vbox:
            spacing 30
            xalign 0.5

            text vn2_confirm_text(message):
                style "vn2_text"
                size 25
                color VN2_INK
                text_align 0.5
                xalign 0.5

            hbox:
                spacing 28
                xalign 0.5

                textbutton _("确定"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    action yes_action

                textbutton _("取消"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    action no_action

    key "game_menu" action no_action
