# CHANGELOG —《雾线》VN2 可玩化交付

> 工程：`L:\AI\FurryVN\20261117_uidemo`（Ren'Py 8.5.3.26051504）
> 交接原状：6 句 demo 的空壳（`script.rpy` 的 `label start` + 末尾 `renpy.quit()`）
> 本次目标：把它做成「能从主菜单一路玩到第 28 章 + 8 个结局」的工程。
> 最后更新：2026-11-21

---

## 0. 2.28.3 Beta 去 AI 味与结局脱钩（2026-11-21）

- 全量旁白/内心去 AI 味：30 个 story 文件 + `directors_cut.rpy`，只动 `nar` / `think`；角色台词 541 行、`voice` 引用 482 条逐一比对，0 改动，不触发重配。
- 原文 142 处“像……”降到 48 处；`一道一道 / 一点一点 / 一层压一层` 类排比从 67 处降到 1 处；清掉 `像在确认 / 像在等 / 像怕` 的猜心理句式，以及“同行结局 / 可攻略路线 / 好感够不够 / 选择里”这类元叙述。
- 合并重复复读、物件清单和章末格言收束；`ch26` 开场与随身清点从 7 段压到 3 段；`.rpy` 对话块 2037 → 2030，字符 108,608 → 105,822。
- ZCode 0.17.3 单代理执行：`--disallowed-tools "Agent Task"` + `--workflow-mode disabled`，ZCode 子代理全程禁用；其中 `directors_cut.rpy` 由 ZCode 直接改，98 个 `nar` 块、94 行 diff；审计报告在 `_qa_headless_20261121_ai/zcode_ai_audit.txt`。
- 结局判定与好感隐藏分脱钩：`vn2_decide_ending` 不再读 `aff_lan/aff_bai/aff_qing` 的 36/52 阈值。同行看“本线交底 + ch25 明确选一起离开（`route_commit`）”；第七天看“本线交底 + `trust_shiqi` + `evidence_kept`”；`ch27` 的后日谈分支也改用 `vn2_ending_key`，不再按 `aff >= 60` 分叉。
- 结局矩阵条件文案同步去掉好感阈值；`ch25` “和身边的人一起离开”写入 `route_commit`，`ch25` 进章时重置为 False。
- lint：0 error / 0 warning；100 菜单、8 结局、8 张结局 CG。
- 版本：内部 `20260004`（补丁不动内部号），外部 `V2.28.3 Beta`；`build.version = 2.28.3`，发行目录 `WuXian-2.28.3-beta`。

## 0. 2.28.2 Beta 全量旁白雕刻（2026-11-21）

- 30 个 story 文件全部过稿，旁白 / 内心逐块扫过；全量重排 71 处连续短句，把句号改成逗号或合流，保留原信息、原动作、原选择。
- `ch01` 冷开场无线电、晨起清点、折地图、青岩绕绳四段单独重写；`ch25` 封站玩家台词改为“封。连来路一起留在里面。”。
- 角色台词一行未改，`482` 个 voice 引用继续有效，不触发重配；`ch11` / `ch15` 的角色重复句保留为回环。
- lint：0 error / 0 warning；2037 对话块、108,608 字、100 菜单、286 选择。
- 版本：内部 `20260004`，外部 `V2.28.2 Beta`。
- Windows 安装包：`dist\WuXian-Setup-2.28.2.exe`（327,261,528 bytes，SHA256 `00013C0ECAC6EF584C20D7B72D0E57257DB49AF2E763DF19EE05CCA111D175E3`；已写入 Authenticode 自签名，证书 `CN=WuXianSukaKanger`，DigiCert 时间戳；自签名根不受公共信任，SmartScreen 仍可能提示）。
- Windows 免安装 zip：`build\WuXian-2.28.2-beta-win.zip`（344,142,782 bytes，SHA256 `E7216486B214EF62549D1ABC1796C665E35CF1FF9D68D71EEB03426EDF177B16`）。
- Android APK：`dist\WuXian-2.28.2-beta.apk`（370,322,648 bytes，SHA256 `23C646FE69BB4FA8B29847202DC064D1E9961578584071109A5CE9BF6ADE2A87`；`com.sukakanger.wuxian`、versionName 2.28.2、versionCode 1795195859）。
- 校验表：`dist\SHA256SUMS-2.28.2.csv`。
- 签名：使用 `CN=WuXianSukaKanger` 自签名代码签名证书（PFX 存于 `L:\AI\_codesign`，不入库），`signtool` SHA256 + DigiCert RFC3161 时间戳。签名只证明文件未被篡改，不能消除其他机器上的“未知发布者”；正式分发前应替换为 CA 签发的 OV/EV 代码签名证书。

## 0. 2.28.0 Beta 本轮交付（2026-11-21）

### 0.1 叙事翻页压缩

- 30 个 story 文件（`ch01`–`ch28`、`directors_cut.rpy`、`endings.rpy`）全部参与合并。
- 合并规则：连续同类型结构块（`nar` / `think`）合并；单块上限 180 字；超长按句号切分。
- 对话块 **3411 → 2030**，少 **1381 次翻页**，约 **-40.5%**。
- 旁白块 `nar+think` **2655 → 1489**，约 **-44%**；角色台词 **535 块**完全未动。
- 原文 **108,261 字**逐字比对 **0 差异**；合并不改文本，只改分页。
- 新增 ch18 / ch21 / ch25 菜单后，总字符 **108,576**、对话块 **2037**、菜单 **100**。
- 单块最大 **180 字**；159 块超过 160 字，0 块超过 180 字。
- 本轮未改任何角色台词，ending voice 原样保留，**不需要重配**。
- 原始 30 个文件备份：`_backup_narration_20261120`。

### 0.2 8 结局分配与路线调平

- 代码实际为 **8 个结局**：3 同行 + 3 独行 + `sealed` 封口 + `seventh` 第七天。
- 分配口径：3 条路线各 2 个，共同线封口 / 第七天 2 个。
- `VN2_LOCK_THRESHOLD` **25 → 22**。
- 同行门槛 **40 → 36** 好感 + 本线承诺；第七天门槛 **60 → 52** 好感 + 本线承诺 + 十七信任 + 带出证据。
- 判定优先级：**封口 / 独自进入 > 强制独行 > 第七天 > 同行 > 独行**。
- `vn2_route_bond`：lan = `close_lan or lan_map_fixed`；bai = `saved_bai or bai_treated`；qing = `know_qing_secret or qing_trusted`。
- ch18 新增 lan 晚期 `trust_shiqi` 补救；ch21 新增 bai 晚期 `trust_shiqi` 补救；qing 保留 ch23 / ch24 补救。
- ch25 新增“一个人走，不跟谁同路”，设置 `_vn2_force_alone`；`vn2_decide_ending` 支持 `force_alone`。
- 调平前 5 个文件备份：`_backup_route_balance_20261120`。

### 0.3 8 结局 QA

- QA runner：`_qa_headless_20261120_endings\run_endings.ps1`，SDK `D:\renpy-8.5.3-sdk`。
- 判定矩阵 10 例全部通过：3 条同行、3 条强制独行、封口、3 条第七天。
- 8 个 ending label 演出冒烟全部通过，均有 CG 截图（截图已按约定删除）。
- 验证了 `force_alone`、`sealed`、`seventh` 的优先级，以及三条路线共享第七天出口。
- 现有 `e_*` 用例直接 Jump 到 ending label，不经过真实判定路径；本轮另建决策矩阵覆盖。

### 0.4 构建

- Windows：`build\windows` 由 2.28.0 发行包重建；安装器 `dist\WuXian-Setup-2.28.0.exe`。
- Android：`dist\WuXian-2.28.0-beta.apk`；`versionName=2.28.0`，`versionCode=1795191015`，包名 `com.sukakanger.wuxian`。
- Windows zip：`build\WuXian-2.28.0-beta-win.zip`。
- 发行目录：`WuXian-2.28.0-beta`。

---

## 1. 交付清单（对应交接书 §8）

| # | 交付项 | 落点 | 状态 |
| - | ------ | ---- | ---- |
| ① | 能跑到第 28 章的剧本章节文件（按章拆分 `.rpy`） | `game/story/`：`story_start.rpy`、`ch01.rpy`…`ch28.rpy`、`end_e01.rpy`、`end_e02.rpy` | 完成，lint 0 error / 0 warning |
| ② | 存档 / 好感度 / 章节路由三套系统 + 存档兼容层 | `game/core/00_state.rpy`…`90_dev_compat.rpy` | 完成 |
| ③ | 变更记录 | `game/_docs/CHANGELOG.md`（本文） | 完成 |
| ④ | 5 张截图 | `shots/ui_01_main_menu.png`、`ui_02_dialogue.png`、`ui_03_save.png`、`ui_04_gallery.png`、`ui_05_preferences.png`（另有 `ui_06_chapters.png` 附赠） | 完成 |

故事层文档（另附，属 §8 之外的补充交付）：

- `game/_docs/CHAPTER_OUTLINE.md` — 28 章分章大纲，一章一行（章名 / 天 / 线 / 发生什么 / 好感 / 伏笔）
- `game/_docs/ROUTES_ENDINGS.md` — 4 条个人线的冲突点与结局分支
- `game/_docs/CHOICES.md` — 每个选项的数值影响表（好感 + 旗标），含好感总账与旗标索引

---

## 2. 剧本层

### 2.1 结构

- **28 章线性推进**，路由表在 `core/20_router.rpy` 的 `CHAPTERS`：`ch01` → … → `ch28`；
  `ch28` 的 `next = None`，由 `vn2_leave_chapter()` 交给 `vn2_ending_label()`。
- **四段个人线**：老周 2–7（`zhou`）、蓝羽 8–14（`lan`）、白砚 15–21（`bai`）、青岩 22–28（`qing`）。
- **每章统一骨架**（由生成器保证，不手写）：

  ```
  scene bg X with slow_fade
  $ vn2_enter_chapter("chNN")        # 写上下文 + 解锁章节选择 + 静默自动存档 + 换 BGM
  call vn2_title_card(N, "标题", "第 N 天 • 线名")
  $ vn2_amb("rain|fire|forest|tunnel")
  $ vn2_show("char", pos=..., trans=dissolve_soft)   # 立绘入场
  …… 6–8 句铺垫 ……
  menu: ……三选一（+3～+5 好感，部分带旗标）……
  $ vn2_unlock_cg("cg_xxx")          # 仅第 3/9/18/24 章
  …… 2 句收束 ……
  $ vn2_hide_all(trans=dissolve_soft)
  $ vn2_leave_chapter()
  ```

- **两个结局章**：
  - `end_e01`「归途 • 出林」：出林后按好感最高者收尾（老周 / 蓝羽 / 白砚 / 青岩 四段）
  - `end_e02`「旧站 • 真相」：真相线，需 `know_qing_secret` 且 `aff_qing >= 50`；结局菜单三选一
  - 都记录 `persistent.vn2_endings`（8 个 key：`e01_zhou`…`e02_qing`），供「结局收集」列表

### 2.2 数据驱动的章节文件（**不要手改 ch02–ch28**）

| 文件 | 作用 |
| ---- | ---- |
| `_tools/story_data.py` | 27 章结构化剧本数据：`beats`（铺垫台词）、`menu`（三选项 + 好感 + 旗标 + 分支台词）、`cg`、`close` |
| `_tools/gen_chapters.py` | 数据 → `game/story/ch02.rpy`…`ch28.rpy` 发射器 |
| `_tools/gen_docs.py` | 数据 + 路由表 → `game/_docs/` 三份故事层文档 |

改文案的正确流程：**改 `story_data.py` → `python _tools/gen_chapters.py` → `python _tools/gen_docs.py`**。
直接手改 `ch02.rpy`–`ch28.rpy` 会在下次生成时被覆盖。

### 2.3 写作中踩到的两个 Ren'Py 语法坑（已修，留档）

1. **menu caption 不能用冒号**：caption 是 `menu:` 块内与选项**同缩进**的裸字符串（无冒号），且后面要空一行：
   ```
       menu:
           "选择："
   
           "选项 A":
               ...
   ```
   第一版生成器把 caption 也写成 `"…":` 并把选项多缩进 4 格，生成块非法。
2. **字体缺字**：`game/fonts/SourceHanSansLite.ttf` 缺 `·`(U+00B7) 与 `✓`。
   生成器 `esc()` 统一把 `·` → `•`；正文一律用 `「」` 引号，避开 `"` 转义。

---

## 3. 三套系统（`game/core/`）

### 3.1 状态层 `00_state.rpy`

- 所有跨章变量用 `default` 声明，默认值集中在 `VN2_DEFAULT_VALUES`（改默认值只改一处）。
- 好感：`aff_zhou/lan/bai/qing`，初始 20，读写一律经 `vn2_aff_add()` 夹在 0–100。
- 10 个布尔旗标：`trust_zhou`、`close_lan`、`saved_bai`、`know_qing_secret`、`heard_zhou_past`、
  `lan_map_fixed`、`bai_treated`、`qing_trusted`、`station_key`、`evidence_kept`。
- 存档 schema 版本 `VN2_SAVE_SCHEMA = 1`。

### 3.2 好感层 `10_affinity.rpy`

`vn2_aff_add / vn2_set_aff / vn2_aff_value / vn2_aff_summary / vn2_top_route / vn2_route_label / vn2_reset_run`。
`vn2_flag(name, value=True)` 只接受在 `VN2_DEFAULT_VALUES` 里声明过的旗标，写错名字直接抛 `ValueError`（防呆）。

### 3.3 路由层 `20_router.rpy`

- `CHAPTERS`（28 项：`no/title/route/day/next/hint`）+ `CHAPTER_ORDER` + `VN2_ROUTE_BLOCKS`
- `vn2_enter_chapter(cid)`：写 `vn2_chapter_id/no/title/route_key/route_name/day` → 解锁章节选择 → `renpy.force_autosave(take_screenshot=True, block=True)` → 按线切 BGM
- `vn2_leave_chapter()`：读 `next`，有则 `renpy.jump(next)`，否则 `vn2_ending_label()`
- `vn2_seed_for_chapter(cid)`：章节选择/调试用，按章号回填好感与旗标（避免中途跳章读不到前置旗标）
- `vn2_ending_list()`：8 个结局的展示数据

### 3.4 存档层 `30_save.rpy`

- 手动槽位元数据：`config.save_json_callbacks` 写入 `vn2_schema / vn2_chapter / vn2_chapter_no / vn2_route / vn2_day / vn2_aff / vn2_top`
  （**`FileSave` 不接受 `extra_info`**，自定义字段只能走这个回调）
- 读档界面读自定义字段用 `FileJson(slot, key, missing=..., page=...)`
- 自动存档：`config.autosave_slots = 5`，进新章 + 每次弹选项 + 退出时各存一次
- 缩略图：`config.thumbnail_width/height` 在 `gui.rpy` 已 `define` 过，这里只能 `init python:` 赋值（重复 `define` 报 already defined）
- **兼容层**：`label after_load` → `vn2_repair_state()`：补缺失的 default 变量、校正章节上下文（章节 id 不在表里则回 `ch01`）、旗标强制 bool、好感夹取。`vn2_save_schema_of(slot)` 读老档 schema（没有则 0）。

### 3.5 立绘层 `40_cast.rpy`

- `vn2_show(char, pos=..., trans=...)` / `vn2_hide` / `vn2_hide_all`，`vn2_pose` 用 `xanchor 0.5` + `xpos VN2_POS[pos]`
  （**不能用 `xalign`**：`xalign` 按「父宽 − 子宽」算，0.22/0.78 会把两人挤到左中）
- 三个位置实测立绘中心落点：左 422 / 中 960 / 右 1497；`zoom 0.58`
- 说话高亮（非说话方降亮/降饱和）+ 呼吸动效在 `ui2/00_theme.rpy`

### 3.6 音频层 `50_audio.rpy`

三通道：`vn2_bgm(key)` / `vn2_amb(key)` / `vn2_sfx(key)`，跨章用 `vn2_bgm_for_route(route)` 淡入淡出（`fadeout/fadein`）。
`VN2_BGM` / `VN2_AMB` 指向的 `game/audio/bgm/*.ogg`、`game/audio/amb/*_looped.wav` **当前不存在** → 静默跳过（不报错）。
要出声，按 `game/_docs/audio_README` 的目录约定放文件即可（见本文 §7）。

---

## 4. UI 层（`game/ui2/`，全部 `init offset = 1`）

| 文件 | 内容 |
| ---- | ---- |
| `00_theme.rpy` | 主题色、字号、`vn2_section`、`vn2_line(w,h)`、按钮/输入样式、呼吸与说话高亮、立绘定位 |
| `05_menu_shell.rpy` | 覆盖 `screen game_menu`：`images/ui/shell.png`（1920×1080、alpha 255）底 + 双金框 + 中文「返回」 |
| `10_hud.rpy` | 对话框：`tb.png` 1720×300 底板 + `name.png` 名字牌（浮在框上方）+「回放/回退/快进/自动/存档/设置」工具行；`screen quick_menu()` 只剩 `pass` |
| `20_mainmenu.rpy` | 主菜单重写：背景 `images/bg/jungle.png` + `scrim_left.png` 压字，「开始新游戏」→ `Start("story_start")` |
| `30_saveload.rpy` | 存档/读档：`grid 3 3`（9 槽/页）+ 翻页行 `ypos 878`；卡片 480×270，左上 240×135 截图窗（`fit="cover"`）|
| `40_preferences.rpy` | 设置面板 5 段两栏（显示/文字/其他 + 音量/快进），全部持久化 |
| `50_gallery.rpy` | CG 画廊：`grid 3 2`（6 格），卡 462×380，图窗 426×272 先铺 `Solid("#090e09")` 卡纸；2 个「未公开」纯排版占位 |
| `60_chapters.rpy` | 章节选择：列宽 322、`hbox spacing 16`、28 章不压左侧导航；底部 1240 宽总览带（章节/CG/结局/总好感）|
| `70_history.rpy` | 回想（Backlog）+ 语音重播位（有 voice tag 时显示重播按钮） |
| `80_about.rpy` | 关于/结局收集入口 |

### 4.1 两轮 UI 验收修掉的 8 个视觉缺陷

1. 字体缺 `·`/`✓` → 全工程 `·` 换 `•`（`ui_skin.rpy` 从备份整文件还原，未被批量替换污染）
2. 主菜单无场景图（`gui/main_menu.png` 只是 1280×720 纯色板）→ `images/bg/jungle.png` + `scrim_left.png`
3. 立绘定位偏移（`xalign` 算法）→ `xanchor 0.5` + `xpos`
4. 存档卡缩略图溢出 → `fit="contain"` + `align (0.5,0.5)` + hairline 外框
5. 巨大 divider 色块（`Frame("gui/decor/divider_h.png", 40, 0)` 1185×52 被撑成整屏高）→ `images/ui/hairline.png` + `screen vn2_line(w,h)`
6. 菜单按钮边框花（360×84 原图被压成 340×62 出多层缝线）→ 原生 360×84 + `Frame(...,48,20,48,20)`；左导航用 PIL 降采样的 240×64 三态
7. 对话截图不可信（`renpy.show_screen("say", ...)` 缺 `_widget_properties`）→ 改 `renpy.say(who, what, interact=False)` + `renpy.pause(0.4, hard=True)`
8. 设置面板正文被盖住（`bar value Preference(...)` 未给高度，`gui/bar/bottom.png` 是 25×350 直接铺成 350 高）→ `images/ui/bar_*.png`（400×22）+ `style vn2_bar: ysize 24`

### 4.2 三个「一改就崩」的地方（留档）

- **`style vscrollbar` 继承链会硬崩**：写成 `style vscrollbar` + `unscrollable "hide"` + `style game_menu_vscrollbar is vscrollbar`
  会让 lint 以 `-1073741819 (0xC0000005)` 直接退出。正确写法是直接给 `game_menu_vscrollbar` 设 `xsize/base_bar/thumb`。
- **`screen game_menu` 底图**：用 `gui.game_menu_background`（1280×720 纯色）会在右下漏出剧情立绘 → 必须自己铺一张 1920×1080 `menu_shell.png`。
- **各界面 `fixed` 必须写 `xsize 1470`**：否则 `xalign 0.5/1.0` 按 1920 屏宽而非内容区算，元素会压到左侧导航或跑出右边。

### 4.3 收尾轮修补（截图复核后）

逐张看截图后又改了 5 处，都是「截图里一眼能看出」的问题：

1. **立绘四边羽化**：四张立绘是 1256×1616 的 **RGB 整幅插画（无 alpha）**，直接当立绘用会露出硬边框。
   改用 `AlphaMask("images/chars/*.png", "images/ui/sprite_feather.png")`，遮罩由 `_tools/make_sprite_mask.py`
   生成（左右 150px、上 90px、**下 260px** 羽化，让人物下缘沉进对话框）。
2. **说话高亮改成颜色矩阵**：`vn2_pose` 原来用 `alpha lit`，半透明会把矩形边缘和底下的场景一起透出来；
   改成 `SaturationMatrix(0.24 + 0.76*lit) * BrightnessMatrix(-0.28*(1-lit))`——不透明，只降饱和压暗。
3. **设置分区底板换新图**：`gui/frame.png`（460×460）的金线在 **45px 内缩**，而 `vn2_section` 的 padding 只有
   `(34,20,34,24)` → 内容压在金线上（截图上「全部静音」按钮被金线穿过、音量条被竖线切过）。
   新生成 `images/ui/section.png`（320×320、14px 内缩细线、`Frame(...,18,18,18,18)`），padding 改 `(28,22,28,26)`。
4. **画廊卡标题压到边框**：CG 由 `(584,350) ypos 16` 收到 `(584,320) ypos 14`，
   标题 `ypos 368 → 344`、副标 `374 → 348`，锁定卡锁图标 `126 → 108`。
5. **存档翻页行被屏幕底裁掉**：`ypos 878 → 852`。
6. **左下「返回」压内金框**：`style return_button` 的 `yoffset -30` 让按钮底边正好落在
   `menu_shell.png` 的 24px 内金框上，补一条 `yoffset -52` 提到框内。

另外核实了一件之前的误判：`Preference("all mute", "toggle")` / `Preference("skip", "toggle")` /
`Preference("after choices", "toggle")` 在 8.5.3 里都是**合法名字**（`renpy/common/00preferences.rpy:178 / 367 / 380`），
三个按钮都有效，不需要自己写 `set_mute`。

### 4.4 UI 视觉重设计 V2（本轮：缝线皮革 → 扁平墨板 + 金细线）

用户这轮的五条意见（原话意）→ 对应改法：

| 意见 | 改法 |
| ---- | ---- |
| 「整体 UI 有点丑」 | 皮肤里所有「缝线/虚线皮革」块停用，全部换成 `_tools/make_ui_v2.py` 生成的扁平墨板 + 1px 金细线；统一 `kerning 1.0~1.5` |
| 「名字应该在对话框**上方**」 | `gui.name_ypos=-54`，`name.png` 九宫格名字牌 `xpos 236 ypos 726`，底边正好贴 `tb.png` 顶部金线 |
| 「看不到回放这类按钮」 | 快捷菜单从 overlay 搬进 `screen say`：`hbox xanchor 1.0 xpos 1794 ypos 802`（回放/回退/快进/自动/存档/设置）|
| 「画廊改成 3×2」 | `grid 3 2`，卡 462×380（图窗 426×272），4 张真 CG + 2 个「未公开 / 敬请期待」排版占位 |
| 「排列太不合理」 | 存档 `grid 3 3`（9 槽/页）；章节页底部补 1240 宽总览带填掉近 400px 空白；设置条宽统一 640 |

**新资产（`game/images/ui/`，全部由 `_tools/make_ui_v2.py` 生成，可重跑）**

| 文件 | 尺寸 | 用途 |
| ---- | ---- | ---- |
| `tb.png` | 1720×300 | 对话底板：竖向 #0d120e→#060907、alpha 250→255、左右各 48px 淡出、顶部 1px 金线 + 18px 暖光、底部满 bleed |
| `name.png` | 200×52 | 名字牌九宫格（18px 切），左侧 13..15px 金条 |
| `plate_idle/hover/selected.png` | 96×48 | 小按钮（九宫格 22/6），selected 底部金线 |
| `mbtn_idle/hover.png` | 360×84 | 主菜单按钮：idle 只有底部 hairline，hover 加左侧 4px 金条 + 填充 |
| `nav_idle/hover.png` | 240×64 | 左导航三态 |
| `card.png/card_empty.png/card_hover.png` | 480×270 | 存档卡：左上 240×135 截图窗、y=176 分隔线、右侧文字区 |
| `gcard.png/gcard_locked.png` | 462×380 | 画廊卡：图窗 rect(17,14→444,288)、底部线 y=336 |
| `row.png` / `chap_row.png`,`chap_row_hover.png` | 800×64 / 322×56 | 列表行 / 章节行 |
| `bar_fill.png`,`bar_track.png`,`bar_thumb.png` | 400×14 / 14×14 | 2px 细线滑条 + 菱形滑块 |
| `veil_right.png` | 620×1080 | 主菜单右侧柔光纱（t=x/0.45，t^1.4×205 alpha）|
| `shell.png` | 1920×1080 | 菜单外壳。**alpha 从 246 提到 255**：246 会透出底层 master 层的立绘，章节页能看到「鬼影」|

`_tools/make_section_plate.py` 同步改深（填色 #141c16→#0a0f0b、alpha 232、噪声 σ=3、外框 `#4a5040` a95、
内金线 a125），重生成 `section.png`（320×320）。

**对话框（`10_hud.rpy`）**

- `gui.textbox_height=300`；`style window: ysize 300 / yalign 1.0 / background None`；
  `tb.png` 以 `xpos 100 ypos 780` 铺在 window 里（不放 window background，是为了让 1720 宽的白边外还有 100px bleed）。
- 正文 `dialogue_xpos=236 / dialogue_ypos 856 / dialogue_width 1348 / line_spacing 10`（`say_dialogue` 同样 xpos/xsize）。
- 名字牌 `frame background Frame("images/ui/name.png",18,6,18,6) xpos 236 ypos 726 padding (36,9,26,9)`，
  文字用 `VN2_GOLD_SOFT`。牌底边 726+52=778，正好压在 `tb.png` 的顶线（780）上 2px。
- 工具行 6 个 `vn2_quick_button`，`hbox xanchor 1.0 xpos 1794 ypos 802 spacing 20`——落在底板右上角，
  y=802 在 780 之下，不会跑到场景里。

**为什么快捷菜单不再用 `screen quick_menu`**：`_dev_shots.rpy` 在 `call_in_new_context` 上下文里截图，
overlay 层被抑制；实测 `renpy.show_screen("quick_menu")` 能让 `renpy.get_screen()` 返回对象、`zorder=260`，
但**一张都画不出来**。真实 gameplay 里 overlay 是正常的，但为了「截图可见 + 玩家一定看得见」两头都对，
直接把按钮写进 `screen say`。`screen quick_menu()` 保留为空壳 `pass`——`config.overlay_screens` 仍引用这个名字，
删定义会报错。这条也解释了 §7 里原来的「quick_menu 未取证」项现在已关闭。

**主菜单（`20_mainmenu.rpy`）**：标题块 `xpos 124 ypos 104`（「雾　线」96px kerning 6 + 副标 20px + 380×2 hairline）；
按钮列 `xpos 140 ypos 372 spacing 6`；左下 `hbox xpos 152 ypos 962` 放「关于 / 退出」；
右侧 `veil_right.png xpos 1300` 压暗后放进度条 `vbox xpos 1508 ypos 132 xsize 330`
（标签 #cfc8b2、数字 34px 金、单位 #8c8878）——此前标签用 `VN2_DIM` 压在雾上完全看不见。

**存档（`30_saveload.rpy`）**：`grid 3 3`，`xspacing 10 / yspacing 14 / ypos 28`，`count=9`（自动存档仍 5），
`VN2_SLOT_GAP=10`；卡片：截图窗 `(240,135) fit="cover"`、槽号 `xpos 428 ypos 14`、
`head` 268/28 size16 金、`body` 268/58、好感行 12/186 size13、`FileTime` `xalign 1.0 xoffset -14 ypos 186`。

**画廊（`50_gallery.rpy`）**：`grid 3 2`，`xspacing 42 / yspacing 28 / ypos 46`。4 张真 CG + 2 个
`use vn2_cg_slot_empty()`（「未公开 / 敬请期待」），**占位不计入右上 `2/4` 计数**。
`grid 3 2` 必须恰好 6 个子元素，这就是加占位卡的直接原因（不是美术决定）。
解锁卡先铺 `Solid("#090e09")` 当卡纸再叠 `contain` 的 CG，竖构图两侧的留白才不像漏画。

**设置 / 章节**：`vn2_section` 换新 `section.png`、padding `(28,22,28,26)`；所有 `bar` 宽度 580→**640**。
章节行换 `chap_row*.png`（行仍 322×56、`padding (18,8,14,8)`），并新增底部总览带
`frame background None xalign 0.5 ypos 762 xsize 1240`：hairline + 四个 310 宽 vbox
（已解锁章节 / CG / 结局 / 总好感，数字 38px 金）。

**说话高亮**：`core/40_cast.rpy` 的 `vn2_focus()` 里非说话人 `want = 0.35`（原 0.5），
配合 4.3 的 `SaturationMatrix * BrightnessMatrix`，非说话人明显掉饱和压暗。

**本轮踩的两个坑（留档）**

- **`PermissionError [WinError 32] game\saves\persistent`**：跑截图时反复出现，traceback 在
  `savelocation.py:431 save_persistent`。`Get-Process | ? Path -like "*renpy*"` 杀不掉（进程路径不是 renpy.exe），
  必须 `Get-CimInstance Win32_Process | ? CommandLine -like "*renpy*" | % { Stop-Process -Id $_.ProcessId -Force }`
  再 `Start-Sleep 2`，之后 `Remove-Item game\saves -Recurse -Force` 才成功。
- **PowerShell 里 `python - <<'PY'` 不可用**（`<` 是保留字，heredoc 进不来）；`python -c @'...'@`
  可以用——here-string 作为**单个参数**传给 `-c`，多行批量替换没问题。

**验收**：本轮 6 张截图在 v2.3 上重拍（`exit code=0`、无 `traceback.txt`），逐张目视复核后
又修了 3 处：主菜单进度条对比度（标签提亮 + 纱加宽到 620、起点 1300）、画廊卡纸（竖构图两侧补深色装裱）、
空存档槽描边对比（`card_empty.png` 图窗填充压深、描边 alpha 170→200）。

**交付前补的一条元信息修正（`game/options.rpy`）**：工程是从 Ren'Py 7 模板复制来的，`config.name` 一直是
`"Ren'Py 7 Default GUI"`、`build.name` 是 `"gui"` —— 窗口标题和任务栏会直接露馅。已改为
`config.name = _("雾线")`、`build.name = "wuxian_vn2"`，并显式加 `config.save_directory = "WuxianVN2-1"`
（否则存档目录跟着显示名走，中文名做目录不干净）。`config.window_icon` 从默认的 `gui/window_icon.png`
换成 `images/ui/window_icon.png`（512×512，取自 `wolf_grey.png` 的头部裁切）。

### 4.5 质感与反馈补齐（本轮）

用户四条诉求 → 四组改动：设置页「和谐」、音效补齐、关于页写公告、载入界面要质感；
追加一条：**不只是加载，存档卡片划入与全局灵动**。

#### (1) 音效 / 配乐接线

| 位置 | 内容 |
| ---- | ---- |
| `game/audio/ui/` | `click` / `hover` / `back` / `confirm` / `page` / `save`（Kenney CC0，可商用） |
| `game/audio/bgm/` | `common` / `route_zhou` / `route_lan` / `route_bai` / `route_qing` / `station` / `ending`（Pixabay，可商用、不可独立转售） |
| `game/audio/amb/` | `rain` / `fire` / `forest` / `tunnel` 四条 16s 无缝环境床（`_tools/make_amb_loops.py` 程序化生成，44.1k 立体声，-22~-25 dBFS） |

接线：`core/50_audio.rpy` 全表改 `.mp3` 并新增 `VN2_SFX`、`vn2_menu_music()`（`is_playing` 为真则不打断）；
`00_theme.rpy` 给 `style button` 挂 `activate_sound` / `hover_sound`；`05_menu_shell.rpy` 的返回键加 back 音、
`game_menu` 进菜单播 `page` 音。

#### (2) 载入界面（`ui2/85_loading.rpy`）

`_tools/make_loading_assets.py` 产出 fog_a（2100×520，纵向羽化后 peak α61）、fog_b（2100×700，α46）、
vignette、可平铺 grain（512）、dust（16×16）。屏幕构成：`bg gate` 缓推（1.0→1.055）、双层雾错位漂移、
vignette、grain 平铺、10 颗 dust、标题 rise + 金线展开、2px 进度条、5 档状态文案 + 百分比、4 条 tips、右下版本。
`label splashscreen` 用 2.4s 真实时间轴推进进度（ease-out，`renpy.pause(0.04)` 返回真即可点击跳过），收尾 `Dissolve(0.45)`。

#### (3) 动效层 `ui2/90_motion.rpy`

统一时长 `VN2_M_FAST 0.14 / BASE 0.32 / SLOW 0.46`，只动 alpha / offset / zoom，**不动 xysize / xalign**（避免把面板挤歪）。

| transform | 用在哪 |
| --------- | ------ |
| `vn2_card_in(delay,dx,dy,z0)` | 存档卡、画廊卡：淡入 + 位移 + 0.985→1.0 微缩放，0.32/0.46s |
| `vn2_lift(dy,dur)` | 卡片 hover 抬升 6px，`on idle/hover/selected` 四态 |
| `vn2_nudge(dx)` | 主菜单按钮 hover 右推 7px |
| `vn2_row_in(dx)` | 章节行从左侧 16px 滑入 |
| `vn2_box_up(dy)` | 对话框底板 / 名字牌从下方托上来 |
| `vn2_fade(delay,dur)` | 面板、工具行、状态文字 |
| `vn2_dust` / `vn2_breathe` | 载入界面尘粒、金线呼吸 |
| `vn2_stagger(i,step,cap)` | 列表错峰（存档 0.035/格，画廊 0.05/格，章节 0.012/行，封顶 0.32s） |

接入点：`30_saveload.rpy` 卡片 `at vn2_card_in(delay+0.002*页号), vn2_lift()`（翻页参数变化即重播）；
`50_gallery.rpy` 同；`60_chapters.rpy` 行 `at vn2_row_in(...)`；`20_mainmenu.rpy` 6 按钮 for 循环错峰；
`10_hud.rpy` 对话框底板 0.0/名字牌 0.05/工具行 0.05；设置与关于各板 `at vn2_fade(delay)`。

#### (4) 版面修正

- **设置页**（`40_preferences.rpy`）推倒重来两次：第一版 2×3 定高栅格 → 内容被挤出底板、块与块重叠；
  第二版列内钉底（`yalign 1.0`）→ 与上方块重叠。**现行版**：两列自然堆叠（不设 ysize），
  末尾一条 1430 宽通栏底栏收口（存档与版本 / 快捷键 / 反馈），两列底边由此对齐，无溢出无滚动条。
- **存档页**（`30_saveload.rpy`）：卡片 470×240（`_tools/make_save_cards.py` 按新尺寸重烘皮肤，
  内嵌截图窗 216×122 + y160 分隔线），3 行 = 752，页码条 `yalign 1.0` 钉底，第三行不再被视口切掉、页码条不再压卡。
- **画廊**（`50_gallery.rpy`）：3×2；竖幅立绘改为「离线烘焙缩略图」——`_tools/make_gallery_thumbs.py`
  产 `gthumb_bg_<id>.png`（cover + 压暗 + 轻模糊当背板）与 `gthumb_fg_<id>.png`（contain，透明底），
  运行时零裁切，左右不再有纯黑条，也不会漫出卡片。
- **关于页**（`80_about.rpy`）：`VN2_ANNOUNCE` 5 条公告 + 素材授权（Kenney CC0 / Pixabay / 程序化环境音 /
  AI 立绘背景CG / 思源黑体 / Ren'Py 8.5.x）+ 操作与版本两列；`·`(U+00B7) 全改 `•`（字体缺字）。

#### (5) 本轮踩的坑（都已实测，勿再复用）

1. **`im.FactorScale(img, xscale=, yscale=)` 签名要 `width` 位置参数** → `TypeError`；
   改用 `im.Scale(img, w, h)`，再 `im.Crop`。**lint 报 0 error 也照样会在运行时炸**，以 `log.txt` / `traceback.txt` 为准。
2. **运行时 `im.Crop` / `im.Scale` 放在 screen 里会让整格不渲染**（画廊 6 格全空）→ 改为离线烘焙缩略图（上面 (4)）。
3. **`screen` 上 `modal True` + splash 上下文**：`renpy.pause` 会永久挂起（截图永远不出）→ 载入屏去掉 `modal`。
4. **屏幕 `on "show"` 在 `call_in_new_context`** 里会把整屏刷黑（主菜单截图全黑）→ 改 `label before_main_menu`（`00start.rpy` 的 `_main_menu_screen` 会调用它）。
5. **`Transform(fit="cover")` 在 8.5 只缩放不裁切**（竖图漫出卡片）→ 需要真裁切就离线烘。
6. **`_dev_shots` 与 splash 同名 label 冲突** → 改 `VN2_SPLASH_HOOK`（`define ... = None`，label 首句 `if VN2_SPLASH_HOOK: $ renpy.jump(...)`；harness 用 `init 999 python: store.VN2_SPLASH_HOOK = "_dev_shot_entry"`）。`config.label_overrides` 实测无效。

### 4.6 第二轮 UI 打磨：音效重做 + 动效加强（本轮）

两件主线：六件界面音效整组重做为同一套程序化合成音色；动效幅度与节奏成体系上调一档。
验收：lint 0 error，实跑无 traceback，重拍 10 张界面截图（必需 6 张：主菜单 / 对话 / 存档 / 载入 / 画廊 / 设置）。

#### (1) 音效重做（`game/audio/ui/*.wav`，`_tools/make_ui_sfx.py`）

**设计思路（六件一套）**

- **音色基底**：正弦基音 + 2 次谐波（0.35）+ 3 次谐波（0.12），共同低通顶在 3.2~4.2 kHz，
  六件听感亮度一致，不再是各买各的拼凑；噪声瞬态只在 click / hover / page 上以低增益带通出现。
- **包络**：短攻击（4~18ms）+ 指数衰减；首尾 8ms / 24ms 淡入淡出，首尾样本实测贴近 0，无爆音、无削波。
- **时长量级**：hover 最短（0.09s）→ click 0.13s → page / save 0.24~0.26s → confirm 0.30s → back 最长（0.38s）。
- **为什么 back 要下行柔和**：返回是「退一步」的收束动作，音高 330→196 Hz 下行滑动 + 低八度余韵音，
  攻击放到 18ms、**不加噪声瞬态**，避免硬切换式脆响；低通压到 2.4 kHz，听感低沉有余韵。
- **峰值**：六件归一化到 -12 ~ -18 dBFS 区间，与 BGM 不打架。

**实测数值（44.1 kHz / 16bit / 立体声 WAV，脚本回读浮点复核）**

| 文件（绝对路径） | 时长 | 峰值 dBFS | RMS dBFS | 用途 |
| ---- | ---- | ---- | ---- | ---- |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\click.wav` | 0.130s | -14.0 | -21.1 | 按钮激活 |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\hover.wav` | 0.090s | -17.0 | -23.7 | 悬停提示 |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\back.wav` | 0.380s | -15.0 | -22.3 | 返回（柔和下行余韵） |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\confirm.wav` | 0.300s | -13.0 | -24.2 | 确认（主音 + 五度叠和弦） |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\page.wav` | 0.240s | -15.0 | -26.9 | 翻页（中频噪声扫掠 + 下行短音） |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\save.wav` | 0.260s | -14.0 | -23.7 | 存档（上行琶音两连音） |

**编码器实测**：本机无 `ffmpeg` / `oggenc` / `lame`，SDK 目录内也未附带任何编码器可执行文件；
SDK 自带 python 无 numpy / soundfile。因此产物直接落 **WAV**（Ren'Py 可直接播放，环境床本来也是 WAV），
接线与 `VN2_SFX` 表同步指向 `.wav`；旧六件 Kenney 改名 `.ogg` 已删除，无悬空引用。

**接线点（全部复核过，无其他旧文件名引用）**

- `ui2/00_theme.rpy`：`style button` 的 `activate_sound` → `click.wav`，`hover_sound` → `hover.wav`；
- `ui2/05_menu_shell.rpy`：`return_button` 的 `activate_sound` → `back.wav`；`game_menu` 进菜单 `Play` → `page.wav`；
- `core/50_audio.rpy`：`VN2_SFX` 表六键全部改 `.wav`；
- `ui2/80_about.rpy`：素材授权行由 Kenney 改为程序化合成说明；公告新增本轮一条；
- `ui2/40_preferences.rpy`：「界面反馈」说明文字同步为合成音色与新动效时长。

> **诚实标注（未逐首实听）**：以上六件**没有经过真人耳朵逐首试听**。音色、频段、包络、时长、峰值/RMS
> 都是按合成参数与回读测量判断的；实际听感亮度、与 BGM 的音量平衡、back 余韵是否足够柔和、各音之间
> 是否像同一套，**需要真人在游戏里点一遍确认**，必要时在 `make_ui_sfx.py` 里调谐波比例 / 衰减 / 目标峰值后重跑。
> 另：`confirm` / `save` 目前只在 `VN2_SFX` 表中留位，尚未挂到具体动作上（按钮激活统一走 click），后续接动作时可取表内路径。

#### (2) 动效加强（`ui2/90_motion.rpy` 及调用点）

原则：只动 alpha / offset / zoom，不动 xysize / xalign（不挤版面）；幅度上调但控制在各版面余量内，
不清零、不抖动、不遮挡文字、不引起滚动条。三档时长保持 快:中:慢 ≈ 1:2.25:3.4。

**时长常量（旧 → 新）**

| 常量 | 旧值 | 新值 |
| ---- | ---- | ---- |
| `VN2_M_FAST` | 0.14 | 0.16 |
| `VN2_M_BASE` | 0.32 | 0.36 |
| `VN2_M_SLOW` | 0.46 | 0.54 |

**transform 参数（旧 → 新）**

| transform | 参数 | 旧值 | 新值 |
| ---- | ---- | ---- | ---- |
| `vn2_card_in` | dx | 22 | 30 |
| `vn2_card_in` | dy | 10 | 16 |
| `vn2_card_in` | z0 | 0.985 | 0.972 |
| `vn2_card_in` | alpha / 位移 / 缩放时长 | BASE 0.32 / SLOW 0.46 | BASE 0.36 / SLOW 0.54 |
| `vn2_fade` | dur | 0.30 | 0.34 |
| `vn2_row_in` | dx | -16 | -26 |
| `vn2_box_up` | dy | 22 | 30 |
| `vn2_lift` | dy | -6 | -12 |
| `vn2_lift` | dur | 0.16 | 0.18 |
| `vn2_lift` | selected_idle yoffset | -2 | -5 |
| `vn2_lift` | zoom | 无 | idle 1.0 / hover·selected_hover 1.02（抬升 + 微缩放双重反馈） |
| `vn2_press` | hover zoom | 1.015 | 1.03 |
| `vn2_nudge` | dx | 8 | 12 |
| `vn2_nudge` | 缓动时长 | 0.15 | 0.18 |
| `vn2_breathe` | lo / hi / dur | 0.62 / 0.95 / 1.6 | 0.55 / 1.00 / 1.8 |
| `vn2_rise`（`00_theme.rpy`） | dy / alpha / yoffset | 18 / 0.28 / 0.32 | 24 / 0.30 / 0.36 |
| `vn2_zoom_in`（`00_theme.rpy`） | 起步 zoom / 时长 | 0.96 / 0.30 / 0.34 | 0.95 / 0.32 / 0.36 |
| `vn2_btn_flex`（`00_theme.rpy`） | hover zoom | 1.02 | 1.035 |
| `vn2_slide_in`（`00_theme.rpy`） | dx / 时长 | 42 / 0.26 / 0.30 | 48 / 0.28 / 0.34 |
| `vn2_slide_hover`（`00_theme.rpy`） | xoffset | -10 | -14 |

**调用点显式参数（旧 → 新）**

| 位置 | 调用 | 旧值 | 新值 |
| ---- | ---- | ---- | ---- |
| `20_mainmenu.rpy` | `vn2_card_in(..., dx=0, dy=20)` | dy 20 | dy 24 |
| `20_mainmenu.rpy` | `vn2_nudge(7)` | dx 7 | dx 12 |
| `10_hud.rpy` | 底板 `vn2_box_up(0.0, 20)` | dy 20 | dy 28 |
| `10_hud.rpy` | 名字牌 `vn2_box_up(0.05, 12)` | dy 12 | dy 18 |
| `85_loading.rpy` | 标题 `vn2_rise(0.05, 22)` | dy 22 | dy 28 |
| `85_loading.rpy` | 副题 `vn2_rise(0.72, 12)` | dy 12 | dy 16 |

复核未改参数的调用点：`30_saveload.rpy` 卡片 `vn2_card_in(delay+0.002*页号), vn2_lift()`（翻页参数变化即重播）；
`50_gallery.rpy` 同；`60_chapters.rpy` 行 `vn2_row_in(vn2_stagger(ci*7+ri, 0.012, 0.32))`；
`40_preferences.rpy` / `80_about.rpy` 各板 `vn2_fade(delay)`；HUD 工具行 `vn2_fade(0.05, 0.18)`。
版面约束已核对：存档 3×3（470×240）、画廊 3×2、设置两列自然堆叠 + 1430 通栏底栏、主菜单 `bg/jungle.png`，
新幅度均在余量内，截图未见溢出 / 重叠 / 滚动条。

#### (3) 验收记录

- **lint**：`renpy.py <proj> lint lint_report.txt`，退出码 0，报告无 error / warning。
- **实跑**：杀净 renpy 进程 → 清空 `game/saves` → 启动 SDK python 实跑，harness 走完截图流程自行退出；
  `log.txt` 无 Traceback / Exception / 缺资源警告，根目录与 `game/` 均无 `traceback.txt`。
- **截图**：`shots/` 下重拍 `ui_01_main_menu` / `ui_02_dialogue` / `ui_03_save` / `ui_03b_load` /
  `ui_04_gallery` / `ui_05_preferences`（必需 6 张），另附 `ui_00_loading` / `ui_00_loading_late` /
  `ui_06_chapters` / `ui_07_about`；1920×1080，已逐张目视复核版面。

#### (4) 本轮踩的坑（都已实测，勿再复用）

1. **harness 里 `open("shots/xxx.txt", "w")` 用相对路径**：Ren'Py 相对路径按 `game/` 目录解析，
   `game/shots/` 不存在 → `FileNotFoundError`，lint 0 error 但启动即炸（老教训再次应验）。
   改用 `os.path.join(_DEVSHOT_DIR, ...)` 绝对路径；`_dev_probe.rpy` 已删除，harness 基线里的 `_probe_1..5`
   引用与 `_p*.txt` 调试写入一并清掉，不复活探针。
2. **无 ogg 编码器**：不要假设本机/SDK 能转 `.ogg`；能落 WAV 就落 WAV，接线与音效表必须同步改扩展名，
   不留指向不存在文件的引用。
3. **SDK python 缺 numpy / soundfile，且 3.13 已移除 `audioop`**：合成脚本用带 numpy 的运行时 python +
   标准库 `wave` 写 16bit PCM，不依赖 `soundfile` / `audioop`。
4. **退出时 `persistent` 被占用 → `PermissionError [WinError 32]`**：harness 跑完 `renpy.quit()`，
   收尾 `persistent.update(True)` 先写 `persistent.new` 再 rename 覆盖 `persistent`；若此时 `persistent`
   被另一进程（网盘同步 / 索引扫描的瞬时句柄）锁住，`safe_rename` 里 `os.unlink(new)` 抛错。
   此时游戏流程与截图均已完成，异常只发生在退出落盘阶段，不代表界面代码缺陷；清空 `game/saves` 后重跑即恢复干净。
   交付前必须清空 `game/saves`，并确认没有 `persistent.new` 残留。

#### (5) 本轮收尾补充（命名页重做 + 出品方字标放大）

- **命名页重做**（`ui2/25_name_picker.rpy`）：由「纯黑底一行字 + 320px 小输入框」改为与主菜单同源的雨林底——
  `Transform("images/bg/jungle.png", xysize=(1920,1080), fit="cover")` 铺底 + `#04070ac4` 压暗 +
  `scrim_left` / `vignette` / `grain`（alpha 0.06）；左侧 xpos 160 / ypos 286 起排：eyebrow「序章 • 报名」17px 金 →
  标题 48px → 说明两行 → 560px 无框输入（44px 金色、`length 10`）+ `hairline.png` 560×2 下划线 →
  「确认」按钮 → 「2–10 个字，回车确认」；右下 180px「01」用 `at Transform(alpha=0.12)`，右上版本号。
  回车 / 小键盘回车均可提交，校验仍为 2–10 字（不合规只提示、不静默截断）。
- **出品方字标放大**：`vn2_logo_img` 由 360×235 改为 **460×300**（仍守 859:560 比例），继续用
  `anchor=(0.5,0.5) + xpos=0.5 + ypos=0.5` 保证真居中；开场时序不变：近白底 #f4f2ec，黑场 0.3s → 淡入 0.8s →
  停 2.0s → 淡出 0.8s → 黑场接载入页 → 主菜单。
- **兼容性验证**：除 8.5.3 SDK 外，用用户桌面的 **8.5.2 SDK**（`D:\renpy-8.5.2-sdk\renpy.exe`）直接启动工程，
  运行 12s 到主菜单无 traceback；工程路径已在 `D:\renpy-8.5.2-sdk\projects.txt` 中，Ren'Py 启动器的项目列表可见。
- **交付态**：`_dev_shots.rpy` 回到 `.off` 并删除 `.rpyc`，`shots/_harness_hit.txt`、`lint2/3.txt` 已清，
  `game/saves` 已清空；本轮 12 张 `ui_*.png` 保留在 `shots/` 供比对。

---
## 5. 开发期 harness（**交付时全部为 `.off`，说明见下**）

| 文件 | 作用 | 交付状态 |
| ---- | ---- | -------- |
| `game/autostart.rpy` | 截图用：`label splashscreen` → `jump("start")`（跑 demo 并截图） | `.off` |
| `game/_dbg.rpy` | `init 200` 里 `config.label_overrides["splashscreen"] = "_dbg_splash"` **强抢 splashscreen**，截图后 `renpy.quit()` | `.off` |
| `game/_dev_shots.rpy` | 正式 UI 截图脚本：`VN2_SPLASH_HOOK = "_dev_shot_entry"` 接管 splash → 载入屏 2 帧 + 7 张 UI 图后 `renpy.quit()` | `.off` |
| `game/_dev_playtest.rpy` | 自动试跑：快进 + 菜单自动选第一项 + 记 label 轨迹到 `_dev_playtest.log`，到结局自动退出 | `.off` |

**为什么交付时是 `.off`**：这四件都会在 `splashscreen` 阶段抢启动流程并 `renpy.quit()`——
一旦启用，启动游戏会在截图/试跑后直接退出，玩家永远看不到主菜单。
其中 `autostart.rpy` / `_dbg.rpy` 内容**一字未改**；`_dev_shots.rpy` 只删掉了两行调试用的
`print("TAGS-...")`；`_dev_playtest.rpy` 是本次新增的试跑工具。四件都只是改了后缀。
要复现截图或试跑：把对应文件（连同同名 `.rpyc`）改回原名再跑，跑完改回 `.off`。

**正确的启动路径（交付态）**：启动 → 无 splashscreen → 主菜单 →「开始新游戏」→ `Start("story_start")` → `ch01`。

**`script.rpy` 与 `autostart.rpy` 内容未改**：`script.rpy` 仍是以 `$ _shot(...)`、`$ renpy.quit()` 结尾的 6 句 demo，只是不再被主菜单入口调用。

---

## 6. 验证记录（2026-11-17）

### 6.1 lint

```
Ren'Py 8.5.3.26051504 lint report
The game contains 551 dialogue blocks, containing 560 words and 7,945 characters,
for an average of 1.0 words and 14 characters per block.
The game contains 33 menus, 21 images, and 46 screens.
```
**0 error / 0 warning**（报告落盘：`lint_report.txt`）

**lint 的调用方式（踩过坑，照这个来）**：本机 `renpy.exe <proj> lint` 走不通——
不加重定向会 `-1073741819 (0xC0000005)`，加 `*>` / `Start-Process -RedirectStandardOutput` / `cmd /c >`
三种重定向都会在 `renpy/lint.py` 打印 BOM 时抛 `OSError [Errno 22]`。可用写法只有一种（SDK 自带 python 直调）：

```powershell
& "D:\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" `
  "D:\renpy-8.5.3-sdk\renpy.py" "L:\AI\FurryVN\20261117_uidemo" lint "L:\AI\FurryVN\20261117_uidemo\lint_report.txt"
```

注意 lint 的签名是 `[basedir] [command] [filename]`，**filename 是位置参数，`--filename` 会报 unrecognized**。


### 6.2 自动试跑（`_dev_playtest.rpy`）

- 全流程：`story_start` → `ch01` … `ch28` → `end_e01` → 回主菜单，**29 个菜单自动作答，无 traceback**。
- 真相线：`vn2_seed_for_chapter("ch24")` 起跑 → `ch24`…`ch28` → `end_e02`（含结局菜单）→ 回主菜单，**无 traceback**。
- 试跑日志 `_dev_playtest.log` 逐条记录了每个 label 与每个菜单标题，可作回归基线。

### 6.3 截图

`shots/` 下 6 张（`ui_01_main_menu` / `ui_02_dialogue` / `ui_03_save` / `ui_04_gallery` /
`ui_05_preferences` / `ui_06_chapters`），1920×1080，由 `_dev_shots.rpy` 在**最终构建**上实跑产出
（`text_cps=0` 保证文字全量显示、`afm` 保证无等待）。第 6 张「章节选择」是交接书 §P1 单列的界面，顺手一起拍。
交付要求的 5 张对应前 5 张。**本轮 UI V2 已整组重拍（v2.3）**，仍是这 6 个文件名。

截图脚本的两个必要动作：
- 每张图之间 `renpy.pause(0.35, hard=True)`，让 `config.screen_fade` 走完，否则拍到半透明过渡帧；
- 跑之前先杀掉占着 `game/saves` 的 renpy 进程，否则 `persistent` 被锁会 `PermissionError [WinError 32]`。

---

## 7. 已知未完成 / 待补

1. ~~音频素材缺失~~ → **已由 §4.5 补齐**：7 首 BGM + 6 个 UI 音效 + 4 条程序化环境床已落盘并接线；
   **6 件 UI 音已于 §4.6 整组重做为程序化合成 WAV，但仍未逐首实听**（音量平衡、音色统一度、
   back 余韵是否柔和、与 BGM 的贴合度需要真人试听后再调；BGM / 环境床的循环接缝同样待真人确认）。
2. ~~quick_menu 在 splashscreen 上下文不显示~~ → **已由 §4.4 解决**：按钮改写进 `screen say`，
   截图与真实 gameplay 走同一套绘制路径，不再依赖 overlay。
3. **试跑只覆盖了每个菜单的第一项**：另外两项的分支文本经 lint 校验，但未逐条实跑。
4. 中文字体只验过 `SourceHanSansLite.ttf` 的常用区段；新增文案若用生僻字/表情符号需重新验字形。
5. 动效只做了「截图静止帧」验收：划入 / 抬升 / 错峰的实际手感需要真人跑一遍；
   §4.6 已把幅度与节奏上调一档（0.16–0.54s、位移 ≤30px、缩放 0.972→1.0，hover 另加 1.02 微缩放），
   若仍嫌平可在 `90_motion.rpy` 按三档常量继续统一调。
6. `config.save_directory` 从模板默认值改为 `WuxianVN2-1`，旧 persistent（章节/CG 解锁）不继承，画廊初始 0/4 属正常。
7. `shots/` 里历史遗留的 `dbg_nowin.png` / `dbg_win.png` / `gui_01_main.png` / `gui_02_game.png` 已清理。

---

## 8. 工程约束（交接书要求，本次未动）

- `game/guisupport.rpy`（`init -100 python in gui: scale(n)`）未动
- `game/gui.rpy:12` 的 `gui.init(1920, 1080)` 未动
- `game/fonts/SourceHanSansLite.ttf` 未动
- `game/ui_skin.rpy` 的 `init -2 python:` 块未动（曾因批量替换 `·` 误改注释，已从
  `_backup_vn2_20261117\20261117_uidemo\game\ui_skin.rpy` 整文件还原）
- `game/gui/` 161 件资产未动
- `script.rpy` 的 `$ _shot(...)`、`$ renpy.quit()` 与 `autostart.rpy` 内容未动

---

## 9. 复现 / 二次开发手册

```
L:\AI\FurryVN\20261117_uidemo
├─ game/
│  ├─ story/     ch01…ch28、end_e01、end_e02、story_start
│  ├─ core/      00_state 10_affinity 20_router 30_save 40_cast 45_bg 50_audio 60_gallery
│  ├─ ui2/       00_theme 05_menu_shell 10_hud 20_mainmenu 30_saveload
│  │             40_preferences 50_gallery 60_chapters 70_history 80_about
│  ├─ images/    bg/ chars/ ui/ cg/
│  ├─ audio/     （空，见 §7.1）
│  └─ _docs/     CHAPTER_OUTLINE / CHOICES / ROUTES_ENDINGS / CHANGELOG
├─ _tools/       story_data.py gen_chapters.py gen_docs.py make_sprite_mask.py make_section_plate.py …
├─ shots/        ui_01_main_menu … ui_06_chapters
└─ lint_report.txt
```

**改剧情文案的唯一正确路径**：改 `_tools/story_data.py` → `python _tools/gen_chapters.py` →
`python _tools/gen_docs.py`。`ch02`–`ch28` 是生成器产物，**手改会在下次重跑时被覆盖**；
`ch01`、`end_e01`、`end_e02` 是手写章，直接改 `.rpy`。

**跑游戏**（本机 `renpy.exe <proj>` 会秒退，走 SDK python）：

```powershell
Start-Process -FilePath "D:\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" `
  -ArgumentList @("D:\renpy-8.5.3-sdk\renpy.py", "L:\AI\FurryVN\20261117_uidemo") -WindowStyle Hidden
```

跑之前先 `Get-Process python,pythonw | ? { $_.Path -like "*renpy*" } | Stop-Process -Force`，
并删掉 `game\saves`（否则 persistent 被占会 `WinError 32`）。

**新增章节**：在 `story_data.py` 里追加一条（字段 `cid/no/title/day/route/bg/amb/cast/beats/menu/cg/close`），
重跑生成器；同时补 `core/20_router.rpy` 的 `CHAPTERS` 表（`no/title/route/day/next/hint`），
否则章节选择界面与章末「继续」按钮找不到下一章。
