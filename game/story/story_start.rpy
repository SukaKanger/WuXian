# ============================================================
#  VN2 • 正式剧情入口
#  ------------------------------------------------------------
#  主菜单「开始新游戏」→ Start("story_start") → ch01
#  script.rpy 的 start 仍保留开发期 demo（末尾 renpy.quit()），
#  两者互不影响；发布前删 autostart.rpy 即可从主菜单进入正片。
# ============================================================

label story_start:

    $ vn2_reset_run()
    $ vn2_stage = {}
    $ quick_menu = True
    $ persistent.vn2_jump_target = "ch01"

    # 开局命名页：新游戏进第 1 章之前询问称呼（章节选择回跳不经过本 label）
    call vn2_name_picker

    # 开场定场插画卡：点击 / 回车 / 3.4 秒自动继续
    call screen vn2_opening_card

    scene bg firelight with slow_fade
    $ vn2_amb("fire")
    $ vn2_bgm("common")

    $ renpy.jump("ch01")
