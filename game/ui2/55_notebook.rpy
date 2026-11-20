# ============================================================
#  VN2 · 笔记本（情报）
#  ------------------------------------------------------------
#  只记录本局真正发生过的事：旗标为真才出现，不用“未解锁”
#  列表提前剧透。入口在对话右上工具行，快捷键 N 也可打开。
#  读取的都是 store 里已有的 default 变量，不新增存档字段。
# ============================================================

init offset = 1

style vn2_notebook_vscrollbar is vscrollbar:
    base_bar Solid("#1b2118")
    thumb Solid(VN2_GOLD_DIM)
    thumb_offset 0


init python:

    VN2_NOTEBOOK_INTEL = [
        dict(key="trust_team", title="队里把后背交给你", tag="共同线",
             body="守夜班次、清点人数、活锚换人。你先把队伍稳住，蓝羽才开始按你的节奏走。"),
        dict(key="ari_helped", title="阿瑞欠你一次", tag="共同线",
             body="沼泽边你没有绕开。阿瑞记住了这件事，后来在队伍里替你说话。"),
        dict(key="lan_map_fixed", title="地图上的断线补回去了", tag="蓝羽线",
             body="你把蓝羽那张旧图推到火光下，当众改掉错线。他没有谢你，但把图折好收进了内侧口袋。"),
        dict(key="close_lan", title="蓝羽把银纹给你看过", tag="蓝羽线",
             body="铁塔下那点气还没散，他把袖口卷起来。银纹不是装饰，是他不肯交给别人的那一部分。"),
        dict(key="saved_bai", title="你替白砚扛过那根杆", tag="白砚线",
             body="木头压上肩时你听见自己骨头响了一声。白砚没说什么，之后换药时手却稳了。"),
        dict(key="bai_treated", title="白砚的手在你手里稳过", tag="白砚线",
             body="你覆住他发抖的那只手，带着他一针一针走。灯下的影子靠得很近，谁都没有先松开。"),
        dict(key="bai_rationed", title="药箱余量的处置", tag="白砚线",
             body="你把针剂、药布、酒精摆成三份，谁也不多拿。",
             body_true="余量归白砚一个人管，你身边只留应急的一小份。",
             body_false="三份均分，摆在布面三格。谁也不多拿，谁也不少留。"),
        dict(key="know_qing_secret", title="青岩划掉过三个名字", tag="青岩线",
             body="他把折过的纸塞回箱底。你没问，他也没抬头，但你知道守站人为什么不肯离开。"),
        dict(key="qing_trusted", title="青岩当面信过你", tag="青岩线",
             body="你盯着他的眼睛问，他没有躲。尾巴慢慢垂下来，那是他不再把你当外人。"),
        dict(key="station_key", title="站门钥匙在你手里", tag="共同线 / 白砚线",
             body="铁钥匙齿口磨得发亮。它开的不是一扇门，是一条以后还能走的路。"),
        dict(key="trust_shiqi", title="十七记住你说的每一句", tag="共同线",
             body="你把路上的情报交给他，没有换条件。黑豹在暗处点了一下头，之后替你守住了走廊。"),
        dict(key="evidence_copied", title="名单的编号抄下来了", tag="青岩线",
             body="你趴在档案柜边，把槽边残留的名字和编号一笔一笔抄进本子。纸比记忆可靠。"),
        dict(key="evidence_kept", title="档案还在你身上", tag="结局线",
             body="防水袋按在胸口，纸隔着布，硬的。你带出去，放哪儿都记得。"),
    ]


    def vn2_notebook_known():
        """返回本局已经记下的情报；bai_rationed 的 False 也是有效选择。"""
        out = []
        chapter_no = int(getattr(store, "vn2_chapter_no", 1) or 1)
        route_key = getattr(store, "vn2_route_key", "common")

        for item in VN2_NOTEBOOK_INTEL:
            key = item["key"]

            if key == "bai_rationed":
                if getattr(store, key, False) or (chapter_no >= 21 and route_key == "bai"):
                    data = dict(item)
                    data["body"] = item["body_true"] if getattr(store, key, False) else item["body_false"]
                    out.append(data)
                continue

            if getattr(store, key, False):
                out.append(item)

        return out


    def vn2_notebook_mark_seen():
        seen = set(persistent.vn2_intel_seen or set())
        for item in vn2_notebook_known():
            seen.add(item["key"])
        persistent.vn2_intel_seen = seen


    def vn2_notebook_unread():
        seen = set(persistent.vn2_intel_seen or set())
        return len([item for item in vn2_notebook_known()
                    if item["key"] not in seen])


# 「关闭」按钮文字：垂直居中 + 水平居中，别再偏左
style vn2_nb_close_text is vn2_quick_button_text:
    xalign 0.5
    text_align 0.5


screen vn2_notebook():

    modal True
    zorder 160

    on "show" action Function(vn2_notebook_mark_seen)

    $ _items = vn2_notebook_known()
    $ _chapter_no = int(getattr(store, "vn2_chapter_no", 1) or 1)
    $ _chapter_title = getattr(store, "vn2_chapter_title", "") or "未命名章节"
    $ _day = int(getattr(store, "vn2_day", 1) or 1)

    add "vn2_ui_common_bg"
    add Transform("images/ui/shell.png", alpha=0.92)

    # 面板头部：左侧实物封面缩略图
    add Transform("images/ui/notebook_cover.png", xysize=(104, 104)):
        xpos 56
        ypos 46

    text _("笔记本"):
        style "vn2_text"
        size 48
        color VN2_GOLD
        xpos 186
        ypos 64

    textbutton _("关闭"):
        style "vn2_quick_button"
        text_style "vn2_nb_close_text"
        text_size 26
        text_color VN2_INK
        text_hover_color VN2_GOLD
        background Frame("gui/menu/row_idle.png", 48, 16, 48, 16)
        hover_background Frame("gui/menu/row_hover.png", 48, 16, 48, 16)
        xpos 1580
        ypos 44
        xsize 260
        ysize 76
        action Hide("vn2_notebook")
        hover_sound "audio/ui/hover.wav"
        activate_sound "audio/ui/back.wav"

    key "n" action Hide("vn2_notebook")
    key "game_menu" action Hide("vn2_notebook")

    viewport:
        xpos 170
        ypos 150
        xsize 1580
        ysize 790
        style_prefix "vn2_notebook"
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True

        vbox:
            xsize 1470
            spacing 14

            use vn2_section("当前任务", 0.0, w=1470):
                vbox:
                    spacing 8

                    text "穿过雨林，找到从地图上消失的旧站；在第 27 天前确认站内是否还有人，并带回记录。":
                        style "vn2_text"
                        size 20
                        color VN2_INK
                        xsize 1380

                    hbox:
                        spacing 28

                        text "第 %d 天 / 27 天" % _day:
                            style "vn2_card_num"
                            size 18
                            color VN2_GOLD

                        text "旧站最后一次报文：『别进来。』":
                            style "vn2_card_sub"
                            size 17
                            color VN2_DIM

            use vn2_section("这一路", 0.03, w=1470):
                vbox:
                    spacing 8

                    hbox:
                        spacing 32

                        vbox:
                            spacing 4
                            text "现在" style "vn2_card_num"
                            text "第 %d 章 / %s" % (_chapter_no, _chapter_title):
                                style "vn2_text"
                                size 22
                                color VN2_INK

                        vbox:
                            spacing 4
                            text "进山" style "vn2_card_num"
                            text "第 %d 天" % _day:
                                style "vn2_text"
                                size 22
                                color VN2_INK

            use vn2_section("已记下的情报", 0.06, w=1470):
                vbox:
                    spacing 8

                    if _items:
                        for _item in _items:
                            frame:
                                background Frame("gui/menu/row_idle.png", 48, 16, 48, 16)
                                xsize 1380
                                padding (24, 12, 24, 12)

                                vbox:
                                    spacing 4

                                    hbox:
                                        spacing 14
                                        xfill True

                                        text _item["title"]:
                                            style "vn2_text"
                                            size 21
                                            color VN2_INK

                                        text _item.get("tag", ""):
                                            style "vn2_card_num"
                                            xalign 1.0

                                    text _item["body"]:
                                        style "vn2_card_sub"
                                        size 17
                                        color VN2_DIM
                                        xsize 1320
                    else:
                        text "本局还没有记下的情报。多走一段路，笔记本会自己长出来的。":
                            style "vn2_card_sub"
                            size 18
                            color VN2_FAINT

            null height 2

            text "对话中按 N 也可以打开笔记本。" style "vn2_card_sub" color VN2_FAINT
