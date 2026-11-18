# ============================================================
#  VN2 • 动效层（Motion）
#  ------------------------------------------------------------
#  统一时长/缓动，避免每个界面各写一套：
#    入场：淡入 + 位移/微缩放（错峰用 delay 累加）
#    交互：hover 抬升 + 微缩放、按下回弹、金线呼吸
#  约束：只动 alpha / offset / zoom，不动布局属性（xysize/xalign），
#  所以不会把面板挤歪——这是上一版「定高栅格」翻车后的教训。
#
#  §4.6 第二轮打磨：幅度与节奏整体上调一档（旧值见 CHANGELOG §4.6），
#  三档时长保持 快:中:慢 ≈ 1:2.25:3.4；位移仍控制在版面余量内，
#  不清零、不抖动、不遮挡文字、不引起滚动条。
# ============================================================

init offset = 1

define VN2_M_FAST = 0.16
define VN2_M_BASE = 0.36
define VN2_M_SLOW = 0.54


# ---------- 入场 ----------

# 卡片划入（旧版：右下浮起 + 微缩放）。第三轮起存档 / 画廊 / 主菜单卡片
# 统一改用 vn2_slide_left 从左外划入，本 transform 保留兼容，活动调用点已清零。
transform vn2_card_in(delay=0.0, dx=30, dy=16, z0=0.972):
    alpha 0.0
    xoffset dx
    yoffset dy
    zoom z0
    pause delay
    parallel:
        ease VN2_M_BASE alpha 1.0
    parallel:
        easeout VN2_M_SLOW xoffset 0
    parallel:
        easeout VN2_M_SLOW yoffset 0
    parallel:
        easeout VN2_M_SLOW zoom 1.0

# 纯淡入（面板、标题、状态文字）
transform vn2_fade(delay=0.0, dur=0.34):
    alpha 0.0
    pause delay
    linear dur alpha 1.0

# 从左侧滑入（章节行、列表项）
# 第三轮：起点推到屏幕左外 dx=-100，时长 0.40s，alpha 从 0 起（不在屏边露半张）
transform vn2_row_in(delay=0.0, dx=-100, dur=0.40):
    alpha 0.0
    xoffset dx
    pause delay
    parallel:
        ease dur alpha 1.0
    parallel:
        easeout dur xoffset 0


# ---------- 第三轮：分方向入场 ----------
# 左组 UI 从屏幕左外划入；右组统计区从右外划入；底部页码条从下方托入。
# 只动 xoffset / yoffset / alpha，不碰 xpos / xysize（不重排版面、不引滚动条）。
# 位移 ±100px，时长 0.35–0.45s（取 0.40），同组错峰 0.03–0.05s（各调用点 stagger）。
transform vn2_slide_left(delay=0.0, dx=-100, dur=0.40):
    alpha 0.0
    xoffset dx
    pause delay
    parallel:
        ease dur alpha 1.0
    parallel:
        easeout dur xoffset 0

transform vn2_slide_right(delay=0.0, dx=100, dur=0.40):
    alpha 0.0
    xoffset dx
    pause delay
    parallel:
        ease dur alpha 1.0
    parallel:
        easeout dur xoffset 0

transform vn2_rise_in(delay=0.0, dy=100, dur=0.40):
    alpha 0.0
    yoffset dy
    pause delay
    parallel:
        ease dur alpha 1.0
    parallel:
        easeout dur yoffset 0

# 对话框入场：整块从下方托上来
# 旧 dy=22；新 dy=30
transform vn2_box_up(delay=0.0, dy=30):
    alpha 0.0
    yoffset dy
    pause delay
    parallel:
        ease VN2_M_FAST alpha 1.0
    parallel:
        easeout VN2_M_BASE yoffset 0


# ---------- 交互 ----------

# hover 抬升 + 微缩放：卡片上浮并放大一点，移开落回
# 旧 dy=-6 dur=0.16 selected_idle=-2；新 dy=-12 dur=0.18 selected_idle=-5，
# hover 另加 zoom 1.02（抬升/发光之外的第二重反馈）
transform vn2_lift(dy=-12, dur=0.18):
    on idle:
        easeout dur yoffset 0
        easeout dur zoom 1.0
    on hover:
        easeout dur yoffset dy
        easeout dur zoom 1.02
    on selected_idle:
        easeout dur yoffset -5
        easeout dur zoom 1.0
    on selected_hover:
        easeout dur yoffset dy
        easeout dur zoom 1.02

# 按钮按下回弹（微缩）；旧 hover zoom 1.015，新 1.03
transform vn2_press:
    on idle:
        ease VN2_M_FAST zoom 1.0
    on hover:
        ease VN2_M_FAST zoom 1.03
    on selected_idle:
        ease VN2_M_FAST zoom 1.0
    on insensitive:
        ease VN2_M_FAST zoom 1.0

# 菜单按钮：hover 时向右轻推（配合左侧金条）
# 旧 dx=8 dur=0.15；新 dx=12 dur=0.18
transform vn2_nudge(dx=12):
    on idle:
        easeout 0.18 xoffset 0
    on hover:
        easeout 0.18 xoffset dx

# 进度条/标题线呼吸（载入界面用）
# 旧 lo=0.62 hi=0.95 dur=1.6；新 lo=0.55 hi=1.00 dur=1.8，起伏更明显
transform vn2_breathe(lo=0.55, hi=1.00, dur=1.8):
    alpha lo
    block:
        ease dur alpha hi
        ease dur alpha lo
        repeat

# 浮尘：上飘 + 淡出（载入界面用）
transform vn2_dust(x, y, delay, dur):
    xpos x
    ypos y
    alpha 0.0
    pause delay
    block:
        alpha 0.0
        yoffset 0
        parallel:
            linear (dur * 0.35) alpha 0.55
            linear (dur * 0.65) alpha 0.0
        parallel:
            linear dur yoffset -150
            linear 0.01 yoffset 0
        repeat


# ---------- 小工具 ----------

init python:
    def vn2_stagger(i, step=0.04, cap=0.40):
        """第 i 项的入场延迟，带封顶，避免长列表末尾等太久。"""
        return min(cap, max(0, i) * step)
