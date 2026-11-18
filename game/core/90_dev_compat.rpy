# ============================================================
#  VN2 • 开发脚本兼容（只补声明，不改 autoshot.rpy 本体）
#  ------------------------------------------------------------
#  autoshot.rpy 是交接书里标注「发布前删除」的开发期文件，
#  它引用的 bg yard / bg room / stand wolf / stand_pos 原本不存在，
#  会让 lint 报 4 条错误。这里补上同名声明，保证 lint 干净，
#  同时不触碰该文件的任何一行。
# ============================================================

image bg yard = vn2_bg("images/bg/jungle.png")
image bg room = vn2_bg("images/bg/hall.png")

image stand wolf = "images/chars/wolf_grey.png"

transform stand_pos:
    xalign 0.5
    yalign 1.0
    zoom 0.66
