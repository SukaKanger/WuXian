# ============================================================
#  VN2 • 开发脚本兼容（只补声明，不改 autoshot.rpy 本体）
#  ------------------------------------------------------------
#  autoshot.rpy 是交接书里标注「发布前删除」的开发期文件，
#  它引用的 bg yard / bg room / stand_pos 原本不存在，
#  会让 lint 报错。这里补上同名声明，保证 lint 干净。
#  旧 stand wolf 已改指 V2 老周，不再依赖已清理的粗立绘。
# ============================================================

image bg yard = vn2_bg("images/bg/jungle.png")
image bg room = vn2_bg("images/bg/hall.png")

image stand wolf = "images/chars/v2/zhou_neutral.png"

transform stand_pos:
    xalign 0.5
    yalign 1.0
    zoom 0.66
