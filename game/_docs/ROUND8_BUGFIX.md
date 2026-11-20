# VN2 实机 Bug 修复（2026-11-17）

## Bug 1：主菜单「继续游戏」点击无效

### 根因

`game/ui2/20_mainmenu.rpy` 的继续按钮调用 `FileLoad(cont_slot)`，没有传 `slot=True`。

`vn2_continue_slot()` 返回的已经是带页前缀的完整槽名（例如 `auto-1` 或 `1-5`），而 `FileLoad` 默认会把页前缀再加一次，拼成 `1-auto-1`，于是：

- `renpy.can_load("1-auto-1")` 为 `False`
- `FileLoad.get_sensitive()` 为 `False`
- 按钮看起来可点，实际 action 自身处于 insensitive，点击没有反应。

### 修复

`game/ui2/20_mainmenu.rpy`：

```renpy
(_("继续游戏"), If(cont_slot, FileLoad(cont_slot, slot=True), NullAction()), bool(cont_slot)),
```

### 实机证据

程序层对照（`renpy.newest_slot()` 返回 `auto-1`）：

```text
OLD FileLoad(name='auto-1', page=None, slot=False) -> fn='1-auto-1' can_load=False get_sensitive=False
NEW FileLoad(name='auto-1', page=None, slot=True)  -> fn='auto-1'   can_load=True  get_sensitive=True
```

实际调用修复后的 action：

```text
invoking real Continue action: <store.FileLoad object ...>
AFTER LOAD slot=auto-1
JSON  no=2 title='三里旧栈道' day=2
STATE no=2 title='三里旧栈道' day=2
```

截图：`artifacts/bugfix_round8/after/bug1_loaded.png`（读档后第 2 章）与 `after/bug1_mainmenu.png`。

---

## Bug 2：每推进一句对话，对话框闪一次“重新加载动画”

### 根因

`game/ui2/10_hud.rpy` 的 `screen say` 每次逐句更新时，会对静态控件重新应用 ATL：

- `tb_vines` 对话框底板：`at vn2_box_up(0.0, 28)`
- `namebox` 名字牌：`at vn2_box_up(0.05, 18)`
- 右上工具行 `quick_menu`：`at vn2_fade(0.05, 0.18)`

`vn2_box_up` / `vn2_fade` 都是带 `alpha` 和 `yoffset` 的 ATL。`screen say` 在每次对话更新时重建这些非 `id` 控件，ATL 随之重启，所以每句都从透明/下偏移重新入场，表现就是对话框闪一次。

### 修复

把这三处静态控件的入场 ATL 移除，让底板、名字牌、工具行常驻：

- `tb_vines`：去掉 `at vn2_box_up(0.0, 28)`
- `namebox`：去掉 `at vn2_box_up(0.05, 18)`
- `quick_menu`：去掉 `at vn2_fade(0.05, 0.18)`

`screen say` 内不再有逐句 ATL；章节卡的 `vn2_rise` 不属于对话循环，保留不动。

### 验证与限制

- 控件树内省显示：底板隐式 `Transform` 在每句 0.05s / 0.50s 均为 `alpha=1.0`、`yoffset=0.0`，不再从透明/下偏移启动。
- `renpy.screenshot` 在 0.05s 与 0.50s 抓到的两帧字节完全一致（MD5 相同、MAD=0），说明截图法无法作为可视帧差证据；本轮以源码 diff + 控件树状态作为主要证据，并在报告里如实标注这个限制。
- 快速工具行改静态后不再逐句淡入；视觉上比原来少一次淡入，但不会再闪。

---

## 同轮 UI 底板补齐（独立改动）

`game/ui2/05_menu_shell.rpy`：

- 新增 `vn2_ui_common_bg`，使用 `images/bg/jungle.png`，1920×1080 cover、降饱和压暗；
- `game_menu` 先铺共同线雨林，再把 `shell.png` 以 `alpha=0.84` 叠上去；
- 设置、存档、画廊、章节选择、历史、关于不再是一整块纯黑。

截图：`shots/ui_common_bg_settings.png`（设置页）。

---

## 最终状态

- `lint_final.txt`：**0 error / 0 warning**
- 统计：3,302 dialogue blocks / 107,021 characters / 87 menus / 63 images / 52 screens（63 images 含新增 UI 底板 1 张）
- 未改剧情场景图、`game/core/45_bg.rpy`、音频与文本正文
- 备份：
  - `_backup_ui_common_bg_20261117_2345/05_menu_shell.rpy`
  - `_backup_ui_bugfix_20261117_2357/20_mainmenu.rpy`、`10_hud.rpy`

## 涉及文件

- `game/ui2/20_mainmenu.rpy`
- `game/ui2/10_hud.rpy`
- `game/ui2/05_menu_shell.rpy`
- `game/_docs/ROUND8_UI_BG.md`
