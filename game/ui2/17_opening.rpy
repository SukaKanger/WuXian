# ============================================================
#  VN2 • 开场插画卡
#  ------------------------------------------------------------
#  命名确认后、第 1 章之前先给一张全屏雨林定场图，压黑边 + 标题，
#  代替直接切进营火。点击 / 回车 / 3.4 秒后自动继续。
#  真正的开场 CG 等画廊批次生成后用 images/cg/ 替换这张底图。
# ============================================================

init offset = 1


screen vn2_opening_card():
    zorder 800

    add Transform("images/bg/jungle.png", xysize=(1920, 1080), fit="cover")
    add Solid("#04070a9c")
    add Solid("#000000") xysize (1920, 110) ypos 0
    add Solid("#000000") xysize (1920, 110) ypos 970

    vbox:
        xpos 150
        yalign 0.46
        spacing 16
        at vn2_fade(0.0, 0.6)

        text "序　章":
            style "vn2_text"
            size 22
            color VN2_GOLD
            kerning 6.0

        text "雨林边缘":
            style "vn2_text"
            size 72
            color VN2_INK
            kerning 4.0

        add "images/ui/hairline.png" xysize (420, 2) alpha 0.85

        text "第 1 天 / 天亮之前　/　雾线":
            style "vn2_text"
            size 20
            color VN2_DIM
            kerning 2.0

    text "点击任意处继续":
        style "vn2_card_sub"
        size 15
        color VN2_FAINT
        xalign 0.5
        yalign 1.0
        yoffset -138

    timer 3.4 action Return()
    key "dismiss" action Return()
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
