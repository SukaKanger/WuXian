# ============================================================
#  VN2 • CG 画廊 + 结局收集
#  ------------------------------------------------------------
#  画廊格子用皮肤 gui/gallery/frame.png（已解锁）
#  与 locked.png（未解锁灰板）+ icons/lock.png
#  结局页列出 4 线 × 2 类，共 8 个
# ============================================================

init offset = 1

define VN2_CG_W = 476
define VN2_CG_H = 322


screen vn2_cg_view(item):

    modal True
    zorder 310

    add Solid("#050805ee")

    add Transform(item["img"], xysize=(1440, 810), fit="contain"):
        xalign 0.5
        yalign 0.42
        at vn2_cg_enter_at(item["id"])

    frame:
        background None
        xalign 0.5
        yalign 0.94

        vbox:
            spacing 4
            xalign 0.5

            text "CG %s　｜　%s" % (vn2_cg_num(item["id"])[2:], item["title"]):
                style "vn2_text"
                size 30
                color VN2_GOLD
                xalign 0.5

            text item["sub"]:
                style "vn2_small"
                xsize 700
                text_align 0.5
                xalign 0.5

    textbutton _("关闭"):
        style "vn2_btn"
        text_style "vn2_btn_text"
        xalign 0.96
        yalign 0.06
        action Hide("vn2_cg_view")

    key "game_menu" action Hide("vn2_cg_view")


screen vn2_cg_card(item, delay=0.0):

    $ unlocked = vn2_cg_unlocked(item["id"])

    button:
        background None
        xysize (462, 380)
        action (Show("vn2_cg_view", item=item) if unlocked else NullAction())

        fixed:
            xysize (462, 380)

            add ("images/ui/gcard.png" if unlocked else "images/ui/gcard_locked.png")

            if unlocked:

                # 单张满幅 cover 缩略图（426×272，离线烘焙，8px 圆角蒙版），
                # 背板纯色只垫在圆角透明缝下面；运行时零裁切、零 im.Crop/Scale。
                add Solid("#090e09") xysize (426, 272) xalign 0.5 ypos 15
                add ("images/ui/gthumb_cover_%s.png" % item["id"]) xalign 0.5 ypos 15

                text ("CG " + vn2_cg_num(item["id"])[2:]):
                    style "vn2_card_sub"
                    size 17
                    color VN2_GOLD_SOFT
                    xalign 1.0
                    xoffset -14
                    ypos 24

            else:

                add Solid("#0a0f0a") xysize (426, 272) xalign 0.5 ypos 15
                add "images/ui/gthumb_empty.png" xalign 0.5 ypos 15
                add "gui/icons/lock.png" xalign 0.5 ypos 104 zoom 1.6 alpha 0.6

            text (item["title"] if unlocked else "未解锁"):
                style "vn2_text"
                size 20
                color (VN2_GOLD_SOFT if unlocked else VN2_FAINT)
                xpos 32
                ypos 296

            if unlocked:
                text item["sub"]:
                    style "vn2_card_sub"
                    xalign 1.0
                    xoffset -32
                    ypos 300


screen vn2_cg_slot_empty(delay=0.0):
    # 3×2 网格的留白位（图集只有 4 张，补两个「未公开」占位，不算进收集数）
    fixed:
        xysize (462, 380)
        at vn2_slide_left(delay)

        add "images/ui/gcard_locked.png"
        add Solid("#0a0f0a") xysize (426, 272) xalign 0.5 ypos 15
        add "images/ui/gthumb_empty.png" xalign 0.5 ypos 15

        text "—":
            style "vn2_text"
            size 26
            color "#31362b"
            xalign 0.5
            ypos 138

        text "未公开":
            style "vn2_card_sub"
            xpos 32
            ypos 296
            color "#5c6152"

        text "敬请期待":
            style "vn2_card_sub"
            xalign 1.0
            xoffset -32
            ypos 300
            color "#4a4f43"



screen gallery():

    tag menu

    default view = "cg"
    default page = 0

    $ n_cg = vn2_cg_count()
    $ n_total = vn2_cg_total()
    $ n_end = vn2_endings_count()
    $ per_page = VN2_GALLERY_PER_PAGE
    $ page_count = max(1, (n_total + per_page - 1) // per_page)
    $ page = min(page, page_count - 1)
    $ page_items = VN2_GALLERY[page * per_page:(page + 1) * per_page]
    $ counter = ("%d / %d" % (n_cg, n_total)) if view == "cg" else ("%d / %d" % (n_end, len(vn2_endings_matrix())))

    use game_menu(_("画廊")):

        fixed:
            xsize 1470

            # ---------- 页签 ----------
            hbox:
                xpos 0
                ypos -18
                spacing 10

                textbutton _("CG 画廊"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    selected (view == "cg")
                    action SetScreenVariable("view", "cg")

                textbutton _("结局收集"):
                    style "vn2_btn"
                    text_style "vn2_btn_text"
                    selected (view == "end")
                    action SetScreenVariable("view", "end")

            text counter:
                style "vn2_card_sub"
                xalign 1.0
                ypos -4

            if view == "cg":

                grid 3 2:
                    xalign 0.5
                    ypos 46
                    xspacing 42
                    yspacing 28

                    for idx, item in enumerate(page_items):
                        use vn2_cg_card(item, 0.0)

                hbox:
                    xalign 0.5
                    ypos 856
                    spacing 24

                    textbutton _("上一页"):
                        style "vn2_btn"
                        text_style "vn2_btn_text"
                        sensitive (page > 0)
                        action SetScreenVariable("page", page - 1)

                    text "第 %d / %d 页" % (page + 1, page_count):
                        style "vn2_card_sub"
                        yalign 0.5
                        color VN2_DIM

                    textbutton _("下一页"):
                        style "vn2_btn"
                        text_style "vn2_btn_text"
                        sensitive (page < page_count - 1)
                        action SetScreenVariable("page", page + 1)

            else:

                vbox:
                    xalign 0.5
                    ypos 56
                    spacing 8

                    for e in vn2_ending_list():

                        $ got = e["key"] in (persistent.vn2_endings or set())

                        frame:
                            background Frame("gui/menu/row_idle.png", 48, 16, 48, 16)
                            xsize 1180
                            padding (30, 10, 30, 10)

                            hbox:
                                spacing 16
                                xfill True

                                add ("gui/icons/star_hover.png" if got else "gui/icons/lock.png") yalign 0.5 zoom 0.85

                                text (e["title"] if got else "？？？"):
                                    style "vn2_text"
                                    size 22
                                    color (VN2_GOLD_SOFT if got else VN2_FAINT)
                                    xsize 320

                                if got:
                                    text e["route"]:
                                        style "vn2_text"
                                        size 20
                                        color VN2_INK
                                        xsize 240

                                text ("已达成" if got else "未解锁"):
                                    style "vn2_card_sub"
                                    xalign 1.0
                                    yalign 0.5
                                    color (VN2_GOLD if got else VN2_FAINT)

