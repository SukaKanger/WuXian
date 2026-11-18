# ============================================================
#  VN2 · 菜单外壳（覆盖 screens.rpy 的 game_menu）
#  ------------------------------------------------------------
#  screens.rpy 原版用 add gui.game_menu_background（1280×720 纯色板）
#  贴在左上角，屏幕右下会漏出剧情场景里的立绘。这里改成整屏底板
#  images/ui/menu_shell.png（1920×1080，带暗角 + 内嵌金框），
#  并把 Return 改成「返回」。
# ============================================================

init offset = 1

# 菜单底图：不再用纯黑 shell 直接盖满整屏，下面垫一层共同线雨林，
# 再把 shell 压到低透明度，让设置/存档/画廊保留场景质感而不是一块黑板。
image vn2_ui_common_bg = Transform(
    "images/bg/jungle.png",
    xysize=(1920, 1080), fit="cover",
    matrixcolor=SaturationMatrix(0.55) * BrightnessMatrix(-0.30),
)

style game_menu_outer_frame:
    background None

style game_menu_navigation_frame:
    background None

style game_menu_label_text is gui_label_text:
    color VN2_GOLD
    size 42
    kerning 2.0
    outlines []

style return_button_text is navigation_button_text:
    color "#cfc7ae"
    hover_color VN2_GOLD_SOFT
    size 30
    xalign 0.5

# 原版是 yalign 1.0 + yoffset -30，按钮底边正好压在 menu_shell.png 的内金框上；
# 实测设置页内容更长时「返回」会被压到窗口底边外。这里上提 120px，
# 右移 60px 与左侧导航文字对齐，并补 hover 音。
style return_button:
    xpos 88
    xsize 220
    ysize 76
    xpadding 16
    ypadding 10
    yoffset -110
    activate_sound "audio/ui/back.wav"
    hover_sound "audio/ui/hover.wav"


screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    # 进菜单时『啪』地一下翻页声，给界面切换一个听觉上的落点
    on "show" action Play("sound", "audio/ui/page.wav")

    add "vn2_ui_common_bg"
    add Transform("images/ui/shell.png", alpha=0.84)

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 左侧导航条
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
