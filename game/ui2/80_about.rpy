# ============================================================
#  VN2 • 关于（游戏名 / 免责声明 / 作者说 / 发行与社交 / 操作提示）
# ============================================================

init offset = 1

define VN2_ANNOUNCE = [
    ("虚构", "《雾线》是虚构作品，人物、地名与事件均为原创或虚构；如有雷同，纯属巧合。"),
    ("内容", "含兽人角色、恋爱分支、轻度暴力，以及死亡、失踪相关描写；请按自身接受度游玩。"),
    ("AI", "当前版本的立绘、背景与 CG 使用 AI 生成，经过人工筛选、裁切与调色；AI 输出可能存在细节偏差。"),
    ("开源与二创", "代码以 MIT 协议开源，可直接复用、修改与再分发，保留版权与许可声明即可。"
                  "本作的原创剧情、角色设定与文本也欢迎直接拿去改、扩写、做二创；"
                  "不必先问授权，别把改后的版本冒充官方原版就行。"),
    ("发行", "itch.io 是本作的发行与更新页：https://sukakanger.itch.io；"
             "下载与版本说明以该页为准。"),
]

define VN2_AUTHOR_NOTE = (
    "《雾线》是我 SukaKanger 的第一部作品。\n"
    "它的问题我自己最清楚：立绘、CG 和配音都借助了 AI，有些段落还生涩，叙事节奏也仍在摸索。\n"
    "但我没有设付费墙，也没打算向任何人收费——代码以 MIT 开源，剧情与设定同样欢迎拿去改、拿去扩写。\n"
    "你愿意留下来，看我把这些不足一点点修好，就是对我最大的支持。\n"
    "我会继续做下去。下一部，会更好。"
)

define VN2_SOCIAL_LINKS = [
    ("B站", "https://b23.tv/3dPhiDD"),
    ("爱发电", "https://afdian.com/a/RoryMarshall"),
    ("GitHub", "https://github.com/SukaKanger"),
    ("抖音", "https://v.douyin.com/orcT-gKY19w/"),
]

# 主菜单右下角保持四个社交入口；itch.io 发行页是单独的发行入口，不混进社交列表。
define VN2_SOCIAL_MAIN = [item for item in VN2_SOCIAL_LINKS if item[0] != "VLink 聚合"]

# 「关于」页把发行页与社交入口并作一排：VLink 聚合、itch.io 打头，其余依次跟进。
define VN2_ABOUT_LINKS = [
    ("VLink 聚合", "https://vlink.cc/sukakanger"),
    ("itch.io", VN2_RELEASE_URL),
] + VN2_SOCIAL_LINKS

style vn2_link_text is button_text:
    font gui.text_font
    size 19
    kerning 1.2
    color VN2_GOLD
    hover_color "#f3e6bd"

style vn2_about_heading is vn2_text:
    size 22
    color VN2_GOLD


screen about():

    tag menu

    use game_menu(_("关于"), scroll="viewport"):

        vbox:
            spacing 16
            xsize 1200

            # ---------- 游戏名 ----------
            hbox:
                spacing 16
                text "雾线":
                    style "vn2_text"
                    size 48
                    color VN2_GOLD
                text "WUXIAN":
                    style "vn2_card_sub"
                    size 14
                    color VN2_FAINT
                    yalign 0.5
                    kerning 4.0
                    yoffset 4

            text "一支四人小队，二十七天，穿过一张地图上没有的雨林，去找一座从地图上消失的旧站。":
                style "vn2_text"
                size 22
                xmaximum 1140
                text_align 0.0
                xalign 0.0

            text "共同线 + 3 条恋爱线 / 28 章 / 8 个结局":
                style "vn2_card_sub"
                color VN2_DIM

            null height 6

            # ---------- 免责声明 ----------
            frame:
                background Frame("images/ui/section.png", 18, 18, 18, 18)
                xsize 1200
                padding (34, 24, 34, 26)
                at vn2_fade(0.03)

                vbox:
                    spacing 10

                    hbox:
                        spacing 12
                        text "免责声明":
                            style "vn2_about_heading"
                        text "DISCLAIMER":
                            style "vn2_card_sub"
                            size 13
                            color VN2_FAINT
                            yalign 0.5
                            kerning 2.0

                    use vn2_line(1130, 2)

                    for date, body in VN2_ANNOUNCE:
                        hbox:
                            spacing 18
                            xsize 1130

                            text date:
                                style "vn2_card_sub"
                                size 15
                                color VN2_GOLD_DIM
                                min_width 92
                                xmaximum 92

                            text body:
                                style "vn2_text"
                                size 17
                                color VN2_INK
                                xmaximum 990

            # ---------- 作者说（压在免责声明下面） ----------
            frame:
                background Frame("images/ui/section.png", 18, 18, 18, 18)
                xsize 1200
                padding (34, 24, 34, 26)
                at vn2_fade(0.09)

                vbox:
                    spacing 12

                    hbox:
                        spacing 12
                        text "作者说":
                            style "vn2_about_heading"
                        text "FROM THE AUTHOR":
                            style "vn2_card_sub"
                            size 13
                            color VN2_FAINT
                            yalign 0.5
                            kerning 2.0

                    use vn2_line(1130, 2)

                    text VN2_AUTHOR_NOTE:
                        style "vn2_text"
                        size 18
                        color VN2_INK
                        xmaximum 1090
                        line_spacing 6
                        text_align 0.0
                        xalign 0.0

                    text "—— SukaKanger":
                        style "vn2_card_sub"
                        size 16
                        color VN2_GOLD_DIM
                        xalign 1.0

            # ---------- 发行与社交（合并为一栏） ----------
            frame:
                background Frame("images/ui/section.png", 18, 18, 18, 18)
                xsize 1200
                padding (34, 22, 34, 24)
                at vn2_fade(0.15)

                vbox:
                    spacing 12

                    hbox:
                        spacing 12
                        text "发行与社交":
                            style "vn2_about_heading"
                        text "RELEASE & SOCIAL":
                            style "vn2_card_sub"
                            size 13
                            color VN2_FAINT
                            yalign 0.5
                            kerning 2.0

                    use vn2_line(1130, 2)

                    text "下载与版本说明以 itch.io 发行页为准；其余入口是更新与二创的出口。":
                        style "vn2_text"
                        size 16
                        color VN2_DIM
                        xmaximum 1100
                        text_align 0.0
                        xalign 0.0

                    hbox:
                        spacing 10
                        for label, url in VN2_ABOUT_LINKS:
                            textbutton label:
                                style "vn2_btn"
                                text_style "vn2_link_text"
                                action Function(renpy.open_url, url)

                    hbox:
                        spacing 14
                        text "玩家交流群":
                            style "vn2_card_sub"
                            size 16
                            color VN2_GOLD_DIM
                            yalign 0.5
                        text "QQ 1134240122":
                            style "vn2_text"
                            size 21
                            color VN2_GOLD
                            yalign 0.5
                        text "报版本号，方便定位 bug":
                            style "vn2_card_sub"
                            color VN2_FAINT
                            yalign 0.5

            # ---------- 操作提示 ----------
            hbox:
                spacing 40

                vbox:
                    spacing 4
                    text "操作":
                        style "vn2_text"
                        size 18
                        color VN2_GOLD_DIM
                    text "右键 / Esc　呼出游戏菜单" style "vn2_card_sub"
                    text "Ctrl　快进已读　空格 / 左键　推进" style "vn2_card_sub"
                    text "F11 / Alt+Enter　全屏切换" style "vn2_card_sub"

                vbox:
                    spacing 4
                    text "版本":
                        style "vn2_text"
                        size 18
                        color VN2_GOLD_DIM
                    text "版本 [config.version]" style "vn2_card_sub"
