# ============================================================
#  VN2 • 回想 / Backlog
#  ------------------------------------------------------------
#  中文长句按 xmaximum 自动折行（Ren'Py 对 CJK 逐字断行）
#  每条右侧留语音重播位：条目里有 voice 字段才显示 ▶
#  语音字段由 config.history_callbacks 写入（见 50_audio.rpy）
# ============================================================

init offset = 1


screen history():

    tag menu
    predict False

    use game_menu(_("回想"), scroll="viewport", yinitial=1.0, spacing=16):

        vbox:
            spacing 18

            text "滚轮 / 拖动可翻查，最新一条在最下方":
                style "vn2_card_sub"
                color VN2_FAINT

            for h in _history_list:

                hbox:
                    spacing 20
                    xsize 1400

                    text (h.who or ""):
                        style "vn2_text"
                        size 21
                        color VN2_GOLD
                        xsize 170
                        text_align 1.0
                        xalign 1.0

                    vbox:
                        spacing 4
                        xsize 1120

                        if h.what:
                            text h.what:
                                style "vn2_text"
                                size 22
                                color VN2_INK
                                xmaximum 1100
                                substitute False

                        if getattr(h, "voice", None):
                            textbutton _("▶ 重播语音"):
                                style "vn2_btn"
                                text_style "vn2_btn_text"
                                action Play("voice", h.voice)

            if not _history_list:
                text "还没有可回想的对话。":
                    style "vn2_small"
                    xalign 0.5
                    ypos 200
