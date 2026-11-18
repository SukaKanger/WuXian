# ============================================================
#  VN2 • 场景图与背景滤镜层
#  ------------------------------------------------------------
#  6 张背景已统一过 LUT（降饱和 + 暗角，见 _tools/grade_bg.py）。
#  引擎内再叠一层 matrixcolor，保证以后替换实拍素材时调性一致。
#  vn2_bg_blur 用于回忆/失去意识等段落。
# ============================================================

init -1 python:

    def vn2_bg(path):
        """给背景图套统一 LUT：轻微降饱和 + 压暗。"""
        return Transform(
            path,
            matrixcolor=SaturationMatrix(0.92) * BrightnessMatrix(-0.015),
        )


image bg forest    = vn2_bg("images/bg/jungle.png")
image bg firelight = vn2_bg("images/bg/firelight.png")
image bg cliff     = vn2_bg("images/bg/cliff.png")
image bg marsh     = vn2_bg("images/bg/marsh.png")
image bg gate      = vn2_bg("images/bg/gate.png")
image bg hall      = vn2_bg("images/bg/hall.png")

# 雨林深处（同 forest，深一档）
image bg deep = Transform("images/bg/jungle.png", matrixcolor=SaturationMatrix(0.75) * BrightnessMatrix(-0.10))


# 背景虚化（回忆 / 昏睡）
transform vn2_bg_blur(amount=6.0):
    blur amount
    matrixcolor SaturationMatrix(0.6)
    alpha 1.0


# 通用转场
define slow_fade = Fade(0.6, 0.2, 0.8, color="#000000")
define blackout = Fade(0.35, 0.9, 0.35, color="#000000")
