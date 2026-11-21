# ============================================================
#  VN2 • 章节选择
#  ------------------------------------------------------------
#  按契约 §3 分 6 段：共同线 / 锁线 / 蓝羽线 / 白砚线 / 青岩线 / 结局；
#  段内按 disp（本线序号）排序，显示「第 N 章」，不显示目录编号 no。
#  已解锁章可直接跳（回看 + 开发期调试共用）；
#  跳转按章节路线回填一套合理的初始数值（见 vn2_seed_for_chapter）。
# ============================================================

init offset = 1


init python:

    def vn2_prepare_jump(cid):
        persistent.vn2_jump_target = cid


    def vn2_chapter_unlocked(cid):
        # 第一章永远可进，不依赖 persistent 记录
        if cid == "ch01":
            return True
        return cid in (persistent.vn2_unlocked or [])


    def vn2_block_chapters(route_key):
        """返回 [{"cid":..., "ch":...}, ...]，段内按 disp 升序（锁线排最前）。"""
        items = [{"cid": cid, "ch": CHAPTERS[cid]} for cid in VN2_ROUTE_BLOCKS[route_key]]
        items.sort(key=lambda item: (item["ch"]["disp"] is None,
                                     item["ch"]["disp"] if item["ch"]["disp"] is not None else 0))
        return items


label vn2_jump_entry:
    $ vn2_seed_for_chapter(persistent.vn2_jump_target)
    $ vn2_repair_state()
    $ renpy.jump(persistent.vn2_jump_target)


screen vn2_jump_confirm(cid):

    $ ctitle = CHAPTERS[cid]["title"]
    $ clabel = vn2_chapter_label(cid)

    modal True
    zorder 210

    add "gui/overlay_dim.png"

    frame:
        background Frame("gui/confirm.png", 56, 56, 56, 56)
        xalign 0.5
        yalign 0.5
        xsize 820
        padding (60, 48, 60, 42)

        vbox:
            spacing 26
            xalign 0.5

            text "跳到「%s / %s」？" % (clabel, ctitle):
                style "vn2_text"
                size 25
                color VN2_INK
                text_align 0.5
                xalign 0.5

            text "当前未保存的进度会丢失。":
                style "vn2_small"
                xalign 0.5

            hbox:
                spacing 28
                xalign 0.5

                textbutton _("跳转"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    action [Function(vn2_prepare_jump, cid), Start("vn2_jump_entry")]

                textbutton _("取消"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    action Hide("vn2_jump_confirm")


screen chapter_select():

    tag menu

    $ n_unlocked, n_chapter_total = vn2_chapter_progress()
    $ n_end = len(vn2_endings_matrix())

    use game_menu(_("章节选择"), scroll="viewport"):

        fixed:
            xsize 1470

            $ max_rows = max(len(vn2_block_chapters(k)) for k in VN2_BLOCK_ORDER)
            $ footer_y = 40 + 62 * max_rows + 30

            text "已解锁 [n_unlocked] / [n_chapter_total]　·　点已解锁章节可直接进入":
                style "vn2_card_sub"
                xpos 0
                ypos 6

            hbox:
                xalign 0.5
                ypos 40
                spacing 12

                for ci, route_key in enumerate(VN2_BLOCK_ORDER):

                    vbox:
                        spacing 6
                        xsize 235

                        text VN2_ROUTE_NAMES[route_key]:
                            style "vn2_text"
                            size 23
                            color VN2_GOLD
                            xalign 0.5

                        use vn2_line(216, 2)

                        for ri, item in enumerate(vn2_block_chapters(route_key)):

                            $ cid = item["cid"]
                            $ ch = item["ch"]
                            $ unlocked = vn2_chapter_unlocked(cid)
                            $ num = ("—" if ch["disp"] is None else "%02d" % ch["disp"])
                            $ daytxt = ch.get("day_label") or ("第 %d 天" % ch["day"])
                            $ jumplist = [Function(vn2_prepare_jump, cid), Start("vn2_jump_entry")]

                            button:
                                background "images/ui/chap_row.png"
                                hover_background "images/ui/chap_row_hover.png"
                                insensitive_background "images/ui/chap_row.png"
                                xysize (235, 56)
                                padding (14, 8, 12, 8)
                                sensitive unlocked
                                at vn2_row_in(vn2_stagger(ci * 7 + ri, 0.03, 0.32))

                                action If(main_menu, jumplist, Show("vn2_jump_confirm", cid=cid))

                                hbox:
                                    spacing 10
                                    yalign 0.5

                                    text num:
                                        style "vn2_text"
                                        size 19
                                        color (VN2_GOLD_DIM if unlocked else "#6b6759")
                                        xsize 30

                                    vbox:
                                        spacing 0
                                        yalign 0.5

                                        text ch["title"]:
                                            style "vn2_text"
                                            size 20
                                            color (VN2_INK if unlocked else "#7d7867")

                                        text daytxt:
                                            style "vn2_card_sub"
                                            size 14
                                            color (VN2_DIM if unlocked else "#63604f")

                    null height 2

            # ---------- 底部总览（从下方托入） ----------
            frame:
                background None
                xalign 0.5
                ypos footer_y
                xsize 1240
                at vn2_rise_in(0.15)

                vbox:
                    spacing 18

                    add "images/ui/hairline.png" xysize (1240, 1) alpha 0.45

                    hbox:
                        spacing 0
                        xfill True

                        for label_txt, value_txt, unit in (
                            ("已解锁章节", "%d" % n_unlocked, "/ %d" % n_chapter_total),
                            ("CG", "%d" % vn2_cg_count(), "/ %d" % len(VN2_GALLERY)),
                            ("结局", "%d" % vn2_endings_count(), "/ %d" % n_end),
                        ):
                            vbox:
                                xsize 310
                                spacing 4

                                text label_txt:
                                    style "vn2_small"
                                    size 16
                                    color VN2_DIM
                                    kerning 2.0

                                hbox:
                                    spacing 4
                                    yalign 0.0

                                    text value_txt:
                                        style "vn2_text"
                                        size 38
                                        color VN2_GOLD_SOFT

                                    if unit:
                                        text unit:
                                            style "vn2_small"
                                            size 15
                                            color VN2_FAINT
                                            yalign 0.5
                                            yoffset 8

                text "没解锁的章节显示为暗色；解锁记录来自实际通关与存档":
                    style "vn2_card_sub"
                    xalign 0.5
                    yalign 0.97
                    color VN2_FAINT
