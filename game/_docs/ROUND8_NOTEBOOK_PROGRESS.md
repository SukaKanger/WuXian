# Round 8 · 笔记本与进度口径

日期：2026-11-18
工程：`L:\AI\FurryVN\20261117_uidemo`
版本：`V1.28.1 Beta` / 内部 `20260001`

## 一、笔记本

新增 `game/ui2/55_notebook.rpy`，屏幕名 `vn2_notebook`。

- 入口一：对话右上工具行新增「笔记」，快捷键 `N`。
- 入口二：主菜单左侧导航新增「笔记本」；主菜单右上进度栏上方也新增一个入口，带未读计数。
- 页面结构：本局（路线、章节、天数、四人好感条）、已记下的情报。
- 情报来源只读现有 store 旗标：`trust_team`、`ari_helped`、`lan_map_fixed`、`close_lan`、`saved_bai`、`bai_treated`、`bai_rationed`、`know_qing_secret`、`qing_trusted`、`station_key`、`trust_shiqi`、`evidence_copied`、`evidence_kept`。
- `bai_rationed` 的 `False` 也按有效选择展示为“三份均分”，不会把“没选过”和“选了三份均分”混在一起。
- 未读记录写入 `persistent.vn2_intel_seen`，打开笔记本时标记本局已记下的条目；不新增存档变量。
- 不在列表里提前放“未解锁”条目，避免剧透。

验证：`shots/notebook_v2.png`（实际游戏窗口截图，1920×1080）显示路线、章节、天数、四条好感与情报条目均正常；滚动条可用，左侧导航与返回按钮正常。

## 二、进度口径修正

原来主菜单显示 `CG 0 / 4`，画廊却是 3×2 六格；这是两个计数源不一致。

修正：

- `game/core/60_gallery.rpy` 新增 `VN2_GALLERY_SLOTS = 6` 与 `vn2_cg_total()`；`vn2_cg_count()` 只统计确实存在于 `VN2_GALLERY` 的 id；`vn2_endings_count()` 只统计结局矩阵里的 key。
- `game/ui2/20_mainmenu.rpy` 改用 `vn2_chapter_progress()`、`vn2_cg_total()`。
- `game/ui2/50_gallery.rpy` 计数与占位格都改用 `vn2_cg_total()`。
- `game/ui2/60_chapters.rpy` 的已解锁数改用 `vn2_chapter_count()`。
- `game/ui2/40_preferences.rpy` 的 CG 总数改用 `vn2_cg_total()`。

章节进度口径：`vn2_chapter_progress()` 返回 `(已解锁正线章节, 25)`。25 是 ch01–ch25 中排除 ch26/27/28 三个结局章的数目；结局章单独在「结局」栏计数。旧 persistent 里只有 `["ch01"]` 的假进度会在初始化时迁移成空表，`ch01` 仍然恒可进入，避免主菜单一直停在 1/28。

结果：主菜单 CG 总数改为 6，画廊 6 格与计数同源；章节选择与主菜单不再各算一套。

## 三、验证与限制

- 笔记本页面实机截图：`shots/notebook_v2.png`。
- 最终 `renpy.exe ... lint` 直接运行返回 `EXIT=0`；8.5.3 的 lint 在 PowerShell 重定向时会触发 `OSError: Errno 22`，因此没有保留文本报告。代码编译与笔记本页面启动均通过。
- 主菜单计数此前已有 `0 / 4` 的旧截图；本次改动后没有重新抓到主菜单截图，计数逻辑以源码与页面启动为准。
- `20_mainmenu.rpy` 中由子代理追加的「笔记本」导航入口保留；主线程的 `55_notebook.rpy` 已把屏幕名对齐为 `vn2_notebook`。
- 收口时发现 `game/ui2/45_notebook.rpy` 是背景子代理建立的重复页（也定义 `screen vn2_notebook` 与 `vn2_notebook_unread`），已整体移到 `_backup_notebook_duplicate_20261118_1810/45_notebook.rpy` 并删除 `.rpyc`；现只有 `55_notebook.rpy` 一页。
- 收口时删除了主线程自己的测试钩子 `game/zz_check.rpy` / `.rpyc`，避免启动时写入临时计数文件。

## 四、文件

- `game/ui2/55_notebook.rpy`（新增）
- `game/ui2/10_hud.rpy`（对话工具行）
- `game/ui2/20_mainmenu.rpy`（主菜单入口与进度）
- `game/ui2/50_gallery.rpy`（画廊计数）
- `game/ui2/60_chapters.rpy`（章节计数）
- `game/ui2/40_preferences.rpy`（设置页 CG 总数）
- `game/core/60_gallery.rpy`（CG 总格数与过滤）
- `game/core/20_router.rpy`（章节进度与已解锁过滤）
- `game/core/00_state.rpy`（空表默认、旧 persistent 迁移、未读集合）
