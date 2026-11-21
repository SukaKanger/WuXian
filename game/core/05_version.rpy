# ============================================================
#  VN2 • 版本号单一真值
#  ------------------------------------------------------------
#  规则详见 game/_docs/VERSIONING.md。本文件是 config.version 的
#  唯一赋值点；全仓界面一律用 [config.version] 插值引用，
#  不得再硬编码任何版本串。
#
#  内部版本：年份 + 四位代序号（无分隔符），形如 20260002
#  外部版本：V<大版本>.<章节数>.<补丁号> <阶段>，形如 V2.28.0 Beta
# ============================================================

init -6 python:

    # ---- 常量（改版本只动下面这几行）----
    VN2_VERSION_MAJOR    = 2      # 大版本号：2.x 系列
    VN2_VERSION_YEAR     = 2026   # 内部版本年份
    VN2_VERSION_GEN      = 4      # 第几代序号，内部号补零到四位（0004）
    VN2_VERSION_CHAPTERS = 28     # 已完成章节数（ch01–ch28）
    VN2_VERSION_PATCH    = 5      # 补丁号：2.28.5
    VN2_VERSION_STAGE    = "GA"   # 阶段："Demo" 早期测试 / "Beta" 公开测试 / "GA" 转正

    # ---- 拼合（一般不需要手改）----
    VN2_VERSION_INTERNAL = "%04d%04d" % (VN2_VERSION_YEAR, VN2_VERSION_GEN)
    config.version = "V%d.%d.%d %s" % (
        VN2_VERSION_MAJOR,
        VN2_VERSION_CHAPTERS,
        VN2_VERSION_PATCH,
        VN2_VERSION_STAGE,
    )


# 发行页：主菜单右下角与「关于」页共用同一个地址。
define VN2_RELEASE_URL = "https://sukakanger.itch.io"
define VN2_RELEASE_LABEL = "itch.io"
define VN2_VLINK_URL = "https://vlink.cc/sukakanger"


