define w  = Character("[player_name]", color="#e8b96a")
define b  = Character("蓝羽",  color="#7ab6e8")
define t  = Character("白砚",  color="#e8e0d0")
define d  = Character("青岩",  color="#7fd0a8")
define n  = Character(None)

image bg camp = Solid("#131a14")
image bg trail = Solid("#1a1c12")

image wolf grey   = "images/chars/wolf_grey.png"
image wolf blue   = "images/chars/wolf_blue.png"
image tiger white = "images/chars/tiger_white.png"
image dragon green = "images/chars/dragon_green.png"

transform stand_right:
    xalign 0.78
    yalign 1.0
    zoom 0.66

transform stand_left:
    xalign 0.22
    yalign 1.0
    zoom 0.66

label start:

    # 正式入口：命名页 → 开场定场插画 → ch01。
    # 旧的开发期 demo（wolf_/tiger_/dragon_ 立绘 + _shot 截图点）已移除：
    # 那段台词与 ch01 重复，且它把玩家写成第三人（"[player_name]把水壶递过来"）。
    # 需要旧立绘对照时看 game/images/chars/ 下的原文件，剧情以 story/ch01.rpy 为准。
    jump story_start
