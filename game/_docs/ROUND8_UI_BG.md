# VN2 UI 共同线底板补齐（2026-11-17）

## 范围

菜单类界面此前用 `images/ui/shell.png` 直接铺满整屏。`shell.png` 本身几乎是一块纯黑底板，只有一圈金框，所以设置、存档、画廊、章节选择这些页面看起来都像“背景缺失”。

这次不生成新图，直接调用共同线的 `images/bg/jungle.png` 作为 UI 底板：

- 在 `game/ui2/05_menu_shell.rpy` 新增 `vn2_ui_common_bg`：1920×1080 cover、降饱和、压暗，保留雨林轮廓；
- `game_menu` 先铺 `vn2_ui_common_bg`，再把 `shell.png` 以 `alpha=0.84` 叠上去；
- 金框、左侧导航、内容区、返回按钮全部保持原样，不引入新字体或新控件。

这样设置、存档、画廊、章节选择、历史、关于共用同一层雨林底图，不再是一整块纯黑。

## 验证

- 设置页实机截图：`shots/ui_common_bg_settings.png`
- 文字、滑杆、按钮与金框对比度正常；背景只在边缘和暗部透出，不抢正文。
- 剧情场景图与 `core/45_bg.rpy` 未改动；本次只补菜单底板。

## 涉及文件

- `game/ui2/05_menu_shell.rpy`
- 备份：`_backup_ui_common_bg_20261117_2345/05_menu_shell.rpy`
