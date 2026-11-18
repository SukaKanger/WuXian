# ============================================================
#  VN2 • 开局命名页（新游戏进入第 1 章之前）
#  雨林底图压暗 + 左侧对齐的标题与输入框（预填「队长」，限 2–10 字）。
#  回车或「确认」提交，校验不通过给明确提示，不静默截断。
#  结果写入全局 player_name（00_state.rpy 里 default 定义，默认「队长」）。
#  旁白统一用「你」；需要称呼玩家的对白用 [player_name] 插值。
# ============================================================

init offset = 1

default _vn2_name_text = "队长"
default _vn2_name_hint = ""

init python:

    def vn2_submit_name(text):
        name = (text or "").strip()
        if len(name) < 2 or len(name) > 10:
            store._vn2_name_hint = "称呼需要 2–10 个字（当前 %d 字）" % len(name)
            renpy.restart_interaction()
            return
        store.player_name = name
        store._vn2_name_hint = ""
        # call screen 的退出走 end_interaction，返回 True 后脚本继续；
        # 不能只 hide_screen：那样屏幕没了但 call screen 仍在等交互，玩家会卡住。
        renpy.end_interaction(True)


style vn2_name_input is input:
    xsize 560
    ypadding 10
    xpadding 0
    color VN2_GOLD_SOFT
    font gui.text_font
    size 44
    kerning 2


screen vn2_name_picker():

    # 不加 modal：实测 modal 屏挂在脚本 / pause 上下文里会让 renpy.pause 永久挂起
    # （与载入屏去掉 modal 同一坑）；全屏底图 + 压暗层本身已遮住下层。
    zorder 900

    add Transform("images/bg/jungle.png", xysize=(1920, 1080), fit="cover")
    add Solid("#04070ac4")
    add "images/ui/scrim_left.png"
    add "images/ui/vignette.png"
    add "images/ui/grain.png" xysize (1920, 1080) alpha 0.06

    # 右上角版本标记
    text "[config.version]":
        style "vn2_card_sub"
        size 15
        color VN2_FAINT
        xalign 0.975
        yalign 0.045

    # 右侧大号序号，压住画面右下角
    text "01":
        style "vn2_text"
        size 180
        color VN2_GOLD
        xalign 0.94
        yalign 0.86
        at Transform(alpha=0.12)

    vbox:
        xpos 160
        ypos 286
        xsize 820
        spacing 20

        text "序章 / 报名":
            style "vn2_card_sub"
            size 17
            color VN2_GOLD
            kerning 4.0

        text "他们需要一个称呼你的方式":
            style "vn2_text"
            size 48
            color VN2_INK
            kerning 1.5

        text "队里没人知道你的本名。写下它，往后每一句称呼都用这个。":
            style "vn2_card_sub"
            size 20
            color VN2_DIM
            line_spacing 6

        null height 16

        hbox:
            spacing 26

            fixed:
                xsize 560
                ysize 76

                input:
                    value VariableInputValue("_vn2_name_text")
                    length 10
                    style "vn2_name_input"
                    yalign 0.0

                add "images/ui/hairline.png" xysize (560, 2) yalign 1.0 alpha 0.85

            textbutton _("确认"):
                style "vn2_btn"
                text_style "vn2_btn_text"
                yalign 0.42
                action Function(vn2_submit_name, _vn2_name_text)

        text "2–10 个字，回车确认":
            style "vn2_card_sub"
            size 16
            color VN2_FAINT
            kerning 1.0

        text _vn2_name_hint:
            style "vn2_card_sub"
            size 18
            color VN2_GOLD
            kerning 1.0

    key "K_RETURN" action Function(vn2_submit_name, _vn2_name_text)
    key "K_KP_ENTER" action Function(vn2_submit_name, _vn2_name_text)


label vn2_name_picker:
    $ _vn2_name_text = player_name
    $ _vn2_name_hint = ""
    call screen vn2_name_picker
    return
