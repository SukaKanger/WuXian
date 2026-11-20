define w  = Character("[player_name]", color="#e8b96a")
define b  = Character("蓝羽",  color="#7ab6e8")
define t  = Character("白砚",  color="#e8e0d0")
define d  = Character("青岩",  color="#7fd0a8")
define n  = Character(None)

image bg camp = Solid("#131a14")
image bg trail = Solid("#1a1c12")

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
    # 旧的开发期 demo 与 wolf_/tiger_/dragon_ 粗立绘已清理，
    # 剧情以 story/ch01.rpy 为准。
    jump story_start
