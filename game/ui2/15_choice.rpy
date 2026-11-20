# ============================================================
#  VN2 • 选项层（覆盖 screens.rpy 的原生 choice）
#  ------------------------------------------------------------
#  原生 choice 用 640×86 的旧皮肤条，Frame 拉伸后边缘虚线会跟着变形，
#  放在画面中央像一条条“警告条”。这里统一改成：
#  • 820 宽墨板，左对齐正文，行距 12
#  • 悬停只亮金线与文字，不做整条高亮
#  • 整体挂在 56% 高度，避开底部对话框
# ============================================================

init offset = 1


style vn2_choice_button is vn2_btn:
    xsize 820
    left_padding 40
    right_padding 36
    ypadding 14


style vn2_choice_button_text is vn2_btn_text:
    size 25
    kerning 1.0
    text_align 0.0
    xalign 0.0
    xmaximum 740


screen choice(items):
    style_prefix "vn2_choice"

    vbox:
        xalign 0.5
        yalign 0.56
        spacing 12
        at vn2_fade(0.04)

        for i in items:
            textbutton i.caption action i.action


# ---------- 锁线选择屏（ch14） ----------
# 未达好感门槛的路线项置灰不可点，灰态下给出「需要多少 / 当前多少 / 还差多少」；
# solo（独自进入）永远可选。门槛口径仍由 core/20_router.rpy 的
# vn2_lock_options() / vn2_lock_pick() 决定，本屏只做展示与敏感态。
style vn2_lock_choice_button is vn2_choice_button:
    insensitive_background Frame("images/ui/plate_idle.png", 22, 6, 22, 6)

style vn2_lock_choice_sub is vn2_card_sub:
    size 15
    color VN2_FAINT
    text_align 0.0
    xalign 0.0


screen vn2_lock_choice(items, opts):

    style_prefix "vn2_choice"

    vbox:
        xalign 0.5
        yalign 0.56
        spacing 12
        at vn2_fade(0.04)

        for i, opt in zip(items, opts):
            button:
                action i.action
                sensitive opt["eligible"]
                style "vn2_lock_choice_button"

                vbox:
                    spacing 2
                    yalign 0.5

                    text i.caption:
                        style "vn2_choice_button_text"

                    if not opt["eligible"]:
                        text "需要好感 %d / 当前 %d（还差 %d）" % (
                            VN2_LOCK_THRESHOLD, opt["aff"], opt["need"]):
                            style "vn2_lock_choice_sub"

                    text "承诺：%s" % opt.get("bond_text", ""):
                        style "vn2_lock_choice_sub"
                        color (VN2_GOLD_DIM if opt.get("bond") else VN2_FAINT)

                    if opt.get("bond_hint"):
                        text opt["bond_hint"]:
                            style "vn2_lock_choice_sub"

    text "同行：本线好感至少 40 + 本线承诺。  独行：进了这条线，但没把最后一句话交出去。\n第七天：十七信任 + 带出证据 + 本线好感至少 60 + 本线承诺。":
        style "vn2_lock_choice_sub"
        xalign 0.5
        yalign 0.86
        text_align 0.5
        color "#b8b09a"

