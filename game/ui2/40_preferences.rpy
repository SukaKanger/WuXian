# ============================================================
#  VN2 • 设置面板
#  ------------------------------------------------------------
#  所有项都落到 persistent：
#    文字速度 / 自动播放 / 三条音量 / 全屏 / 跳过未读 / 字号
#  字号走 persistent.vn2_text_scale，say 界面实时读，不写死 init。
#
#  排版：两列自然堆叠 + 一条通栏底栏收口。
#  之前两版都在跟「固定高度」较劲：定高栅格会把内容挤出底板，
#  列内钉底（yalign 1.0）又会和上面的块重叠。现在谁都不设 ysize，
#  底板高度跟着内容走，最后用一条 1430 宽的通栏把两列的底边「框」齐。
# ============================================================

init offset = 1

# 滚动类面板放宽（默认 920 太窄，两栏塞不下）
style game_menu_viewport:
    xsize 1500

define VN2_SET_COL_W = 700


screen vn2_section(title, delay=0.0, w=None, side="fade"):
    frame:
        # 自带 14px 内缩金线的底板（_tools/make_section_plate.py 生成）；
        # 不能用 gui/frame.png：它的金线在 45px 内缩，padding 小于 45 时内容会压在线上。
        background Frame("images/ui/section.png", 18, 18, 18, 18)
        xsize (w if w else VN2_SET_COL_W)
        padding (26, 14, 26, 16)
        if side == "left":
            at vn2_slide_left(delay)
        elif side == "right":
            at vn2_slide_right(delay)
        else:
            at vn2_fade(delay)

        vbox:
            spacing 10

            text title:
                style "vn2_text"
                size 22
                color VN2_GOLD

            use vn2_line((w - 60) if w else 640, 2)

            null height 2

            transclude


screen preferences():

    tag menu

    $ ts = persistent.vn2_text_scale
    $ cur_size = VN2_TEXT_SCALES[ts][1]
    $ n_cg_total = vn2_cg_total()
    $ n_chapter_total = VN2_CHAPTER_TOTAL
    $ n_end_total = len(vn2_endings_matrix())

    use game_menu(_("设置"), scroll="viewport"):

        vbox:
            spacing 12
            xsize 1470

            hbox:
                spacing 30

                # ---------- 左列：显示 / 文字 / 其他 ----------
                vbox:
                    spacing 12

                    use vn2_section("显示", 0.00, side="left"):
                        vbox:
                            spacing 8

                            text "窗口模式":
                                style "vn2_small"

                            hbox:
                                spacing 12

                                textbutton _("窗口"):
                                    style "vn2_btn"
                                    text_style "vn2_btn_text"
                                    action Preference("display", "window")

                                textbutton _("全屏"):
                                    style "vn2_btn"
                                    text_style "vn2_btn_text"
                                    action Preference("display", "fullscreen")

                            text "（F11 / Alt+Enter 也能切换全屏）":
                                style "vn2_card_sub"
                                color VN2_FAINT

                    use vn2_section("文字", 0.06, side="left"):
                        vbox:
                            spacing 4

                            text "文字速度":
                                style "vn2_text"
                                size 21

                            bar value Preference("text speed") style "vn2_bar" xsize 640

                            $ cps_on = (preferences.text_cps or 0) > 0

                            textbutton ("逐字显示：开（打字音会响）" if cps_on else "逐字显示：关（文字瞬间出现）"):
                                style "vn2_btn"
                                text_style "vn2_btn_text"
                                action Preference("text speed", 0 if cps_on else 28)

                            text "关掉后文字瞬间出完，也不会播打字音":
                                style "vn2_card_sub"
                                color VN2_FAINT

                            null height 4

                            text "自动播放等待":
                                style "vn2_text"
                                size 21

                            bar value Preference("auto-forward time") style "vn2_bar" xsize 640

                            null height 6

                            text "字号　当前 [cur_size] px":
                                style "vn2_text"
                                size 21

                            hbox:
                                spacing 12

                                for i, item in enumerate(VN2_TEXT_SCALES):
                                    textbutton item[0]:
                                        style "vn2_btn"
                                        text_style "vn2_btn_text"
                                        selected (ts == i)
                                        action Function(vn2_set_text_scale, i)

                    use vn2_section("其他", 0.12, side="left"):
                        vbox:
                            spacing 10

                            textbutton _("跳过转场动画"):
                                style "vn2_btn"
                                text_style "vn2_btn_text"
                                action InvertSelected(Preference("transitions", "toggle"))

                            text "全部设置即时写入 persistent，重启后保留":
                                style "vn2_card_sub"
                                color VN2_FAINT

                # ---------- 右列：音量 / 快进 / 界面反馈 ----------
                vbox:
                    spacing 12

                    use vn2_section("音量", 0.03, side="right"):
                        vbox:
                            spacing 4

                            text "音乐":
                                style "vn2_text"
                                size 21
                            bar value Preference("music volume") style "vn2_bar" xsize 640

                            null height 4

                            text "音效 / 环境音":
                                style "vn2_text"
                                size 21
                            bar value Preference("sound volume") style "vn2_bar" xsize 640

                            null height 4

                            text "语音（角色对白已接入）":
                                style "vn2_text"
                                size 21
                            bar value Preference("voice volume") style "vn2_bar" xsize 640

                            null height 4

                            textbutton _("角色说话时自动压低音乐"):
                                style "vn2_btn"
                                text_style "vn2_btn_text"
                                selected preferences.emphasize_audio
                                action Preference("emphasize audio", "toggle")

                            text ("开：音乐自动退到约 18%" if preferences.emphasize_audio else "关：音乐保持当前音量"):
                                style "vn2_card_sub"
                                color VN2_FAINT

                            null height 8

                            textbutton _("全部静音"):
                                style "vn2_btn"
                                text_style "vn2_btn_text"
                                action Preference("all mute", "toggle")

                    use vn2_section("快进", 0.09, side="right"):
                        vbox:
                            spacing 6

                            textbutton _("跳过未读文本"):
                                style "vn2_btn"
                                text_style "vn2_btn_text"
                                action Preference("skip", "toggle")

                            text ("开：连没读过的也跳过" if preferences.skip_unseen else "关：只跳已读（推荐）"):
                                style "vn2_card_sub"
                                color VN2_FAINT

                            null height 4

                            textbutton _("选项之后继续跳过"):
                                style "vn2_btn"
                                text_style "vn2_btn_text"
                                action Preference("after choices", "toggle")

                            text "（选项本身一定会打断跳过）":
                                style "vn2_card_sub"
                                color VN2_FAINT

                    use vn2_section("界面反馈", 0.12, side="right"):
                        vbox:
                            spacing 6

                            text "点击 / 悬停：轻量界面音":
                                style "vn2_card_sub"
                            text "返回 / 翻页 / 存档 / 确认：独立音色":
                                style "vn2_card_sub"
                            text "卡片从左划入 0.40s，悬停抬升 0.18s":
                                style "vn2_card_sub"

            # ---------- 通栏底栏：把两列的底边框齐 ----------
            frame:
                background Frame("images/ui/section.png", 18, 18, 18, 18)
                xsize 1430
                padding (32, 12, 32, 14)
                at vn2_rise_in(0.18)

                hbox:
                    spacing 0
                    xfill True

                    vbox:
                        xsize 460
                        spacing 4
                        text "存档与版本　章节 [n_chapter_total] / CG [n_cg_total] 张 / 结局 [n_end_total] 个":
                            style "vn2_text"
                            size 19
                            color VN2_GOLD_DIM
                        text "schema v[VN2_SAVE_SCHEMA]　自动 5 槽　手动 9 页 × 6 槽":
                            style "vn2_card_sub"

                    vbox:
                        xsize 460
                        spacing 4
                        text "快捷键":
                            style "vn2_text"
                            size 19
                            color VN2_GOLD_DIM
                        text "右键 / Esc 菜单　Ctrl 快进　F11 全屏　空格 推进":
                            style "vn2_card_sub"

                    vbox:
                        xsize 420
                        spacing 4
                        text "反馈":
                            style "vn2_text"
                            size 19
                            color VN2_GOLD_DIM
                        text "卡片划入 / 悬停抬升 / 按钮音效":
                            style "vn2_card_sub"
