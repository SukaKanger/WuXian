# ============================================================
#  VN2 • 存 / 读档界面（ROUND3：3 列 × 2 行 = 六槽）
#  ------------------------------------------------------------
#  卡片是「左图右字」：左侧 16:9 截图，右侧「第 N 章 • 谁线 / 章名」，
#  底边一条「好感 / 时间」。
#  版面（内容区 fixed xsize 1470，页码条 yalign 1.0 钉底）：
#    槽位 470×380；列间距 30；行间距 24；
#    3×470 + 2×30 = 1470，左右边距对称；
#    行1 顶 y=36，行2 顶 y=36+380+24=440，行2 底 820；
#    页码按钮高 42.6，顶 rel 875.5（真机截图实测），与行2 净空 55.5px（32–56），不出滚动条。
#  自动存档页仍 5 槽（第 6 格 null）。卡片皮肤由 _tools/make_save_cards.py
#  按 470×380 重烘，内嵌截图窗 / 分隔线全部按这个尺寸画，不拉伸旧图。
# ============================================================

init offset = 1

define VN2_SLOT_W = 470
define VN2_SLOT_H = 380
define VN2_SLOT_GAP_X = 30
define VN2_SLOT_GAP_Y = 24
define VN2_SLOT_THUMB = (300, 169)


screen save():
    tag menu
    use vn2_file_slots(_("存档"), False)


screen load():
    tag menu
    use vn2_file_slots(_("读取"), True)


screen vn2_file_slots(title, is_load):

    $ page = persistent._file_page
    $ is_auto = (page == "auto")
    $ count = 5 if is_auto else 6

    use game_menu(title):

        fixed:
            xsize 1470

            # 页说明
            text ("自动存档 / 最近 5 个" if is_auto else "点击槽位存档 / 读档"):
                style "vn2_small"
                xpos 0
                ypos -14

            grid 3 2:
                xalign 0.5
                ypos 36
                xspacing VN2_SLOT_GAP_X
                yspacing VN2_SLOT_GAP_Y

                for i in range(6):
                    $ slot = i + 1

                    if is_auto and i >= count:
                        null
                    else:
                        use vn2_slot_card(slot, page, is_load, vn2_stagger(i, 0.035))


            # 翻页：钉在内容区底部；从下方托入
            hbox:
                xalign 0.5
                yalign 1.0
                spacing 10
                at vn2_rise_in(0.12)

                textbutton _("<"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    action FilePagePrevious()

                textbutton _("自动"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    selected (page == "auto")
                    action FilePage("auto")

                for p in range(1, 10):
                    textbutton "[p]":
                        style "vn2_btn"
                        text_style "vn2_btn_text"
                        selected (str(page) == str(p))
                        action FilePage(p)

                textbutton _(">"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    action FilePageNext()


screen vn2_slot_card(slot, page, is_load, delay=0.0):

    $ loaded = FileLoadable(slot, page=page)
    $ cno = FileJson(slot, "vn2_chapter_no", missing=0, page=page)
    $ ctitle = FileJson(slot, "vn2_chapter", missing="", page=page)
    $ cro = FileJson(slot, "vn2_route", missing="", page=page)
    $ caff = FileJson(slot, "vn2_aff", missing="", page=page)
    $ cname = FileJson(slot, "vn2_player", missing="队长", page=page)
    $ cdisp = FileJson(slot, "vn2_disp_label", missing="", page=page)
    $ snum = "%02d" % slot
    # 标题行优先读章节动态标签（共同线 · 第 6 章 / 蓝羽线 · 第 3 章 / 锁线 / 结局 …）
    $ head = cdisp if cdisp else (("第 %d 章 / %s" % (cno, cro)) if cno else (cro or "—"))
    $ body = ctitle if ctitle else "—"
    $ can_save = (not is_load) and (page != "auto")
    $ empty_hint = ("读取后在此显示进度" if is_load else
                    "剧情推进时自动写入" if page == "auto" else
                    "点击后保存当前进度")
    # 翻页后让入场动画重播（delay 带上页号，transform 参数变化即重新开始）
    $ pg = 3 if page == "auto" else int(page or 1)

    button:
        style "vn2_card"
        xysize (VN2_SLOT_W, VN2_SLOT_H)
        # 皮肤板由 _tools/make_save_cards.py 按 470×380 重烘，内嵌截图窗与分隔线
        # 都是按这个尺寸画的，直接贴图不拉伸。
        background ("images/ui/card.png" if loaded else "images/ui/card_empty.png")
        hover_background "images/ui/card_hover.png"
        at vn2_slide_left(delay + 0.002 * pg), vn2_lift()

        if is_load:
            action (FileLoad(slot, page=page) if loaded else NullAction())
        elif can_save:
            action FileSave(slot, page=page)
        else:
            action NullAction()

        fixed:
            xysize (VN2_SLOT_W, VN2_SLOT_H)

            # 左：16:9 截图（contain，不变形；源图本身是 16:9 时正好铺满）
            fixed:
                xpos 16
                ypos 18
                xysize VN2_SLOT_THUMB

                add Solid("#070b08")

                if loaded:
                    add Transform(FileScreenshot(slot, page=page), xysize=VN2_SLOT_THUMB, fit="contain") align (0.5, 0.5)
                else:
                    # 空槽位：细金框 + 加号，比纯黑块有结构
                    text "+":
                        style "vn2_text"
                        size 40
                        color "#39402f"
                        xalign 0.5
                        yalign 0.5
                        yoffset -4

            # 槽号（右上）
            text snum:
                style "vn2_card_num"
                xpos 424
                ypos 16

            if loaded:

                text head:
                    style "vn2_card_num"
                    size 15
                    color VN2_GOLD
                    xpos 332
                    ypos 34
                    xmaximum 122

                text body:
                    style "vn2_card_title"
                    size 23
                    xpos 332
                    ypos 74
                    xmaximum 122

                text cname:
                    style "vn2_card_sub"
                    size 13
                    color VN2_DIM
                    xpos 332
                    ypos 116
                    xmaximum 122

                if caff:
                    text caff:
                        style "vn2_card_sub"
                        size 13
                        xpos 16
                        ypos 280
                        xmaximum 438

                text FileTime(slot, format="%Y-%m-%d  %H:%M", empty="", page=page):
                    style "vn2_card_sub"
                    size 13
                    xalign 1.0
                    xoffset -16
                    ypos 330

            else:

                text "空槽位":
                    style "vn2_card_title"
                    size 24
                    color VN2_FAINT
                    xpos 332
                    ypos 74

                if is_load:
                    text "没有可读取的存档":
                        style "vn2_card_sub"
                        xpos 332
                        ypos 116
                elif page == "auto":
                    text "自动存档槽":
                        style "vn2_card_sub"
                        xpos 332
                        ypos 116
                else:
                    text "点击存入进度":
                        style "vn2_card_sub"
                        xpos 332
                        ypos 116

                text empty_hint:
                    style "vn2_card_sub"
                    size 13
                    color VN2_FAINT
                    xpos 16
                    ypos 280

        if loaded:
            key "save_delete" action FileDelete(slot, page=page)
