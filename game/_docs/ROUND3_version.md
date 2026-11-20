# ROUND3 · 版本号规则落地记录

> 范围：只处理版本号单一真值与四处界面显示。未跑 Ren'Py 实跑 / 截图（收尾环节统一做）。
> 未改动：`config.name`、`gui/` 资产、字体、story 正文 ch02–ch28、`CHANGELOG.md`；
> 未触碰其他 agent 正在改的文件（50_gallery.rpy / 30_saveload.rpy / 95_typing.rpy / 音效 / 背景图）。

## 1. 改动文件清单（文件 : 行）

### 1.1 新建单一真值文件

- **`L:\AI\FurryVN\20261117_uidemo\game\core\05_version.rpy`**（新建，1–30 行）
  - L15 `VN2_VERSION_MAJOR = 1`
  - L16 `VN2_VERSION_YEAR = 2026`
  - L17 `VN2_VERSION_GEN = 1`
  - L18 `VN2_VERSION_CHAPTERS = 28`
  - L19 `VN2_VERSION_PATCH = 0`
  - L20 `VN2_VERSION_STAGE = "Demo"`
  - L23 `VN2_VERSION_INTERNAL = "%04d%04d" % (VN2_VERSION_YEAR, VN2_VERSION_GEN)`
  - L24–29 `config.version = "V%d.%d.%d %s" % (...)`（全仓唯一赋值点）

### 1.2 options.rpy（去重赋值，改为指向注释）

- **`L:\AI\FurryVN\20261117_uidemo\game\options.rpy`**
  - 旧 L28 `define config.version = "1.0"` **已删除**；
  - 现 L26–28 为注释：版本号集中定义在 `game/core/05_version.rpy`，本文件不再重复赋值。

### 1.3 四处界面显示点

| 文件 : 行 | 改前 | 改后 |
| --------- | ---- | ---- |
| `game\ui2\20_mainmenu.rpy:185` | `text "v[config.version]　•　开发版":` | `text "[config.version]":` |
| `game\ui2\85_loading.rpy:137` | `text "v[config.version]　•　开发版":` | `text "[config.version]":` |
| `game\ui2\80_about.rpy:156` | `text "v[config.version]　存档 schema v[VN2_SAVE_SCHEMA]" style "vn2_card_sub"` | `text "[config.version]　存档 schema v[VN2_SAVE_SCHEMA]" style "vn2_card_sub"` |
| `game\ui2\25_name_picker.rpy:52` | `text "v1.0 • 开发版":` | `text "[config.version]":` |

## 2. 最终版本串与四处显示实际文本

- 内部版本：`20260001`（`VN2_VERSION_INTERNAL`）
- 外部版本（`config.version`）：**`V1.28.0 Demo`**

四处显示点运行时插值后的实际文本：

| 文件 : 行 | 实际显示文本 |
| --------- | ------------ |
| `game\ui2\20_mainmenu.rpy:185` | `V1.28.0 Demo` |
| `game\ui2\85_loading.rpy:137` | `V1.28.0 Demo` |
| `game\ui2\80_about.rpy:156` | `V1.28.0 Demo　存档 schema v1` |
| `game\ui2\25_name_picker.rpy:52` | `V1.28.0 Demo` |

> schema 位 `v[VN2_SAVE_SCHEMA]` 是存档兼容层版本（`VN2_SAVE_SCHEMA = 1`，见 `core/00_state.rpy:14`），
> 与游戏版本号无关，保留其前缀 `v`，未并入 `config.version`。

## 3. grep 证据

### 3.1 `config.version` 赋值唯一性

全仓 `*.rpy` 检索 `config.version`：

- 赋值点：仅 `game\core\05_version.rpy:24` 一处 `config.version = ...`。
- 只读插值引用（保留，非赋值）：
  - `game\screens.rpy:375` `text "[config.version]":`（默认主菜单版本文本，按规则保留不动）
  - `game\screens.rpy:562` `text _("Version [config.version!t]\n")`（默认关于屏，保留不动）
  - 四处界面见 §1.3。
- `game\options.rpy` 已无 `define config.version = ...`。

### 3.2 残留硬编码检查

- `v[config.version]`：**0 处**（改前 3 处：20_mainmenu / 85_loading / 80_about，均已清掉前缀 `v`）。
- `v1.0` / `"1.0"` / `'1.0'`（版本位置）：**0 处**（改前 25_name_picker.rpy:52 写死 `v1.0`，已改为插值）。
- 版本位置的「开发版」：四处版本串中 **0 处**残留。
- `.rpy.off` / `.txt` / 禁用脚本：无版本串匹配。
- `_tools/*.py`：仅 `patch_scrollbar.py:2` 文档字符串里有英文 "version"（“safe version”），非版本号，未动。

### 3.3 保留的描述性「开发版」（正文文案，非版本串，按规则保留并点名）

| 文件 : 行 | 内容 | 说明 |
| --------- | ---- | ---- |
| `game\ui2\80_about.rpy:20` | `("开发版", "章节选择、CG 画廊、存档兼容层均为可调试状态；正式版会收掉调试入口。")` | 公告条目文案，转正 GA 时再改写。 |
| `game\ui2\80_about.rpy:158` | `text "开发版：解锁与调试入口保持开放" style "vn2_card_sub"` | 关于页「版本」区块的状态说明文案，非版本串；转正 GA 时一并收掉。 |

### 3.4 范围外观察项（非版本串，本轮未改，仅记录）

- 正文/统计里写死的章节数 `28`（内容统计分母，不属版本号规则；后续若要随章节常量联动，可另开任务）：
  - `game\ui2\20_mainmenu.rpy:136` `text " / 28"`
  - `game\ui2\40_preferences.rpy:227` `章节 28 • CG ... 结局 8 个`
  - `game\ui2\60_chapters.rpy:86` `已解锁 [n_unlocked] / 28`
  - `game\ui2\60_chapters.rpy:177` `("/ 28")`
  - `game\ui2\80_about.rpy:46` `共 28 章 + 2 个结局章`
  - `game\ui2\80_about.rpy:157` `章节 28 + 结局 2`
- `game\_docs\CHANGELOG.md`：本轮未改（第三轮小节由收尾环节统一追加）。
- `交接给豆包.md:87` 提到的 `config.save_version = 1` 为存档 schema 说明，与本规则无关。

## 4. “只改哪一行”说明

| 场景 | 唯一要动的常量（`game/core/05_version.rpy`） | 结果 |
| ---- | ------------------------------------------ | ---- |
| 写完一章 | `VN2_VERSION_CHAPTERS` +1 | 外部号第二位同步 +1，内部号不变 |
| 修 bug / 小修 | `VN2_VERSION_PATCH` +1 | 外部号第三位 +1 |
| 转正 GA | `VN2_VERSION_STAGE` 改为 `"GA"`（另按 §3.3 清理两处描述文案） | 后缀 `Demo → GA` |
| 大改版 / 新一代 | `VN2_VERSION_MAJOR` +1、`VN2_VERSION_GEN` +1、`VN2_VERSION_PATCH` 归零 | 外部号第一位 +1；内部号代序号 +1 |

## 5. 静态自检结论

- 四个界面文件中不再出现 `v[config.version]`、`v1.0`、`"1.0"`，版本位置无「开发版」字样。
- `config.version` 全仓仅在 `core/05_version.rpy:24` 赋值一处；`options.rpy` 无第二处赋值。
- 界面插值均为方括号语法 `[config.version]`；未使用 `"v" + config.version` 这类拼接。
- 拼合公式已用 Python 静态核验：内部 `20260001`，外部 `V1.28.0 Demo`，与规则要求一致。
- 缩进、引号、字符串格式无明显语法问题；未跑 Ren'Py 实跑 / 截图。

## 6. 故事口径对齐（老周线 → 共同线）

> 依据 `game/_docs/STORY_CANON.md`（2026-11-17 定稿）：老周 = 玩家角色（灰狼队长，名字开局自填、默认「队长」），
> **不是第四条恋爱线**；三条恋爱线为蓝羽 / 白砚 / 青岩；ch01–14 为共同线。
> 本轮只换显示串：不动剧情逻辑、不动 ch08–ch28 正文、不重排；路由 key `zhou` 保留（存档 schema 依赖）。

### 6.1 改动文件 : 行（新旧文本）

| 文件 : 行 | 改前 | 改后 |
| --------- | ---- | ---- |
| `game\core\00_state.rpy:21` | `"zhou": "老周线",` | `"zhou": "共同线",`（key `zhou` 保留） |
| `game\core\60_gallery.rpy:13` | `sub="老周 • 第 3 章",` | `sub="共同线 • 第 3 章",` |
| `game\_dev_shots.rpy.off:98` | `$ store.vn2_route_name = "老周线"` | `$ store.vn2_route_name = "共同线"`（`vn2_route_key = "zhou"` 保留） |
| `game\story\ch02.rpy:7` | `call vn2_title_card(2, "三里旧栈道", "第 2 天 • 老周线")` | `call vn2_title_card(2, "三里旧栈道", "第 2 天 • 共同线")` |
| `game\story\ch03.rpy:7` | `call vn2_title_card(3, "断崖", "第 3 天 • 老周线")` | `call vn2_title_card(3, "断崖", "第 3 天 • 共同线")` |
| `game\story\ch04.rpy:7` | `call vn2_title_card(4, "夜哨", "第 4 天 • 老周线")` | `call vn2_title_card(4, "夜哨", "第 4 天 • 共同线")` |
| `game\story\ch05.rpy:7` | `call vn2_title_card(5, "绳结", "第 5 天 • 老周线")` | `call vn2_title_card(5, "绳结", "第 5 天 • 共同线")` |
| `game\story\ch06.rpy:7` | `call vn2_title_card(6, "雨幕", "第 6 天 • 老周线")` | `call vn2_title_card(6, "雨幕", "第 6 天 • 共同线")` |
| `game\story\ch07.rpy:7` | `call vn2_title_card(7, "第一块站牌", "第 7 天 • 老周线")` | `call vn2_title_card(7, "第一块站牌", "第 7 天 • 共同线")` |
| `game\story\ch01.rpy:1`（注释） | `# 第 1 章 • 雨停之后（第 1 天 / 老周线）` | `# 第 1 章 • 雨停之后（第 1 天 / 共同线）` |
| `game\core\20_router.rpy:11`（注释） | `# ---------------- 老周线 • 第 1–7 章 ----------------` | `# ---------------- 共同线 • 第 1–7 章 ----------------` |
| `game\story\ch02.rpy:1`–`ch07.rpy:1`（注释） | `# …（第 N 天 / 老周线）` | `# …（第 N 天 / 共同线）` |

> ch01 标题卡副题原本就是 `"第 1 天 • 天亮之前"`（无旧称），未改；ch02–ch07 仅动标题卡副题这一个字符串，
> 正文对白、选项、好感、立绘调度一律未碰。

### 6.2 四处运行时显示点最终文本（含数据链）

| 显示点 | 文件 : 行 | 数据链 | 最终文本 |
| ------ | --------- | ------ | -------- |
| 存档卡副题 | `game\ui2\30_saveload.rpy:102,106` | `FileJson("vn2_route")` ← `vn2_route_name` ← `vn2_route_label(route)` ← `VN2_ROUTE_NAMES[key]` | zhou 路线存档：`第 7 章 • 共同线` |
| 章节选择路线列头 | `game\ui2\60_chapters.rpy:102` | `text VN2_ROUTE_NAMES[route_key]` | 第一列列头：`共同线` |
| 画廊卡副题 | `game\ui2\50_gallery.rpy:41,92`（渲染）← `game\core\60_gallery.rpy:13`（数据） | `text item["sub"]` | `共同线 • 第 3 章` |
| 章节标题卡副题 | `game\ui2\10_hud.rpy:127`（渲染）← `game\story\ch02–ch07.rpy:7`（入参） | `vn2_title_card(no, title, sub)` → `text sub` | `第 2 天 • 共同线` … `第 7 天 • 共同线` |

附带：结局收集列表（`core\20_router.rpy:185`）路线标签同样走 `vn2_route_label(key)`，zhou 结局条目标签一并变为 `共同线`。

### 6.3 grep 证据

命令（工程根目录 `L:\AI\FurryVN\20261117_uidemo`）：

```
rg "老周线" game\ --glob '*.rpy*'      # 退出码 1，0 处匹配
rg "老周 •" game\ --glob '*.rpy*'      # 退出码 1，0 处匹配
rg "老周"  game\ui2\ -n                # 退出码 1，0 处匹配
```

- 运行时 `.rpy` / `.rpy.off` 内：旧路线名「老周线」、「老周 • 第 N 章」显示串 **0 处**；`ui2` 下无「老周」字样。
- 全仓残留（**均非运行时显示**，本轮未改，仅点名）：
  - 开发期脚本 `_tools/`：`gen_chapters.py:13`、`gen_docs.py:22,195`、`make_previews.py:107,161`、`story_data.py:13`（注释）——生成文档 / 离线预览图用，待路由重排轮一并更新。
  - 文档 `_docs/`：`STORY_CANON.md:28,32`（口径定稿本身引用旧称说明待改项）、`ROUTES_ENDINGS.md:5`、`CHAPTER_OUTLINE.md:7–13`（后者由 `gen_docs.py` 自动生成）。
- 保留未动的「老周」（角色名 / 待重排剧情文案，非路线名）：
  - `core\00_state.rpy:29` `VN2_CHAR_NAMES["zhou"] = "老周"`（角色名映射，本轮不在口径替换范围）；
  - `script.rpy` 开发期 demo、ch01–ch28 正文对白 / 选项 / 立绘调度里的「老周」称呼，属 STORY_CANON §四待重排内容，本轮按约束不动。
- 旧存档 JSON 中已写入的 `vn2_route` 旧串是运行时存档数据；代码改后新存档为新串，旧存档显示不在本轮处理范围。

### 6.4 边界与自检

- 路由 key `zhou`、`VN2_AFF_KEYS`、好感 / 旗标 / 存档 schema 一律未改名、未改逻辑。
- 未碰 ch08–ch28、未碰 `CHANGELOG.md`、未跑 Ren'Py 实跑 / 截图；改动均为字符串字面量与注释，缩进 / 引号未破坏。

