# ROUND4 剧情重排交付文档

> 项目：`L:\AI\FurryVN\20261117_uidemo`（Ren'Py 8.5.3 / VN2《雾线》）
> 口径：`game\_docs\STORY_CANON.md`（v3 定稿）+ `game\_docs\ROUND4_CONTRACT.md`（本轮冻结契约）
> 本轮只做剧情 / 章节路由 / 结局 / 好感旗标闭环。探索层（地图、物品栏、食物分配、副本入口）、立绘 V2 绘制、正式 CG **不在本轮**。

---

## 1. 结构变更总览

| 项 | 旧（本轮前） | 新（本轮后） |
|---|---|---|
| 骨架 | 四段串联：ch01–07 老周 → 08–14 蓝羽 → 15–21 白砚 → 22–28 青岩，共 28 章一条线走到底 | 1–13 共同线 → 14 锁线 → 15 门口 → 16–24 三线并行（每条 3 章，单周目只走本线）→ 25 结算 → 26–28 结局演出 |
| 单周目章数 | 28 | **22**（1–15 + 本线 3 章 + 25–28） |
| 玩家 | ch01–07 把老周写成 NPC（递水壶、拍肩、"帮[player_name]收绳"） | 玩家即老周；旁白第二人称「你」，玩家发声用 `zhou "..."`，名牌显示 `[player_name]` |
| 好感 key | `lan/bai/qing/zhou`，初始 20 | `lan/bai/qing/ari`，初始 **10**，**删 `aff_zhou`** |
| 结局 | 2 个 label（`end_e01/e02`）× 4 route = 8 格，含 zhou | **8 个独立 label**（`vn2_end_*`），key 与展示名一一对应 |
| 存档 schema | 1 | **2**（新增 `vn2_lock_route`、`trust_team`、`trust_shiqi`、`ari_helped`、`evidence_copied`；摘除 `aff_zhou`/`trust_zhou`/`heard_zhou_past`） |
| 立绘 | V1 `images/chars/wolf_*.png` + `AlphaMask` 羽化 | V2 `images/chars/v2/*.png`（36 张 6 角色 × 6 表情），**去羽化遮罩** |

---

## 2. 章节矩阵（28 条，全部可达）

| 章节 | 路线 | 本线序号 | 天数 | 标题 | 前置条件 | menu | 写入变量 | 读取变量 | next |
|---|---|---|---|---|---|---|---|---|---|
| ch01 | common | 1 | 1 | 雨停之后 | — | 2 | aff_lan/bai/qing | — | ch02 |
| ch02 | common | 2 | 2 | 三里旧栈道 | — | 2 | aff_lan/bai/qing | — | ch03 |
| ch03 | common | 3 | 3 | 断崖 | — | 2 | **trust_team**、aff | — | ch04 |
| ch04 | common | 4 | 4 | 夜哨 | — | 2 | aff_lan/bai | — | ch05 |
| ch05 | common | 5 | 5 | 绳结 | — | 2 | aff_lan/bai/qing | — | ch06 |
| ch06 | common | 6 | 6 | 雨幕（刀点） | — | 2 | **trust_team**、aff | — | ch07 |
| ch07 | common | 7 | 7 | 第一块站牌 | — | 2 | aff_lan/bai/qing | — | ch08 |
| ch08 | common | 8 | 8 | 沼泽边 | — | 2 | **ari_helped**、**aff_ari**、aff | ari_helped | ch09 |
| ch09 | common | 9 | 9 | 银纹 | — | 2 | **trust_team**、aff | trust_team | ch10 |
| ch10 | common | 10 | 10 | 改过的地图（刀点） | — | 2 | **lan_map_fixed**、aff | lan_map_fixed | ch11 |
| ch11 | common | 11 | 11 | 第二座信标 | — | 2 | **close_lan**、aff | lan_map_fixed | ch12 |
| ch12 | common | 12 | 12 | 旧营地 | — | 2 | **saved_bai**、aff | — | ch13 |
| ch13 | common | 13 | 13 | 分岔 | — | 2 | **know_qing_secret**、aff | — | ch14 |
| ch14 | lock | —（显示「锁线」） | 14 | 锁线 | 菜单内判 `aff ≥ 25` | 1（四选一） | **vn2_lock_route** | aff_lan/bai/qing | ch15 |
| ch15 | common | 15 | 15 | 门口 | 已有锁线结果 | 1 | **station_key** / **trust_shiqi**（互斥分支） | vn2_lock_route | 动态：lan→ch16 / bai→ch19 / qing→ch22 / solo→ch25 |
| ch16 | lan | 1 | 16 | 旧队徽 | 锁线 lan（aff≥25） | 2 | close_lan、aff_lan | close_lan、lan_map_fixed | ch17 |
| ch17 | lan | 2 | 17 | 雾里的名字（刀点） | 同上 | 2 | close_lan、aff_lan（含 −4 分支） | lan_map_fixed、know_qing_secret | ch18 |
| ch18 | lan | 3 | 18 | 两条路 | 同上 | 2 | aff_lan | close_lan、station_key、trust_team、ari_helped | ch25 |
| ch19 | bai | 1 | 19 | 空药瓶 | 锁线 bai | 2 | aff_bai | saved_bai | ch20 |
| ch20 | bai | 2 | 20 | 手术（刀点） | 同上 | 2 | **bai_treated**、aff_bai | saved_bai | ch21 |
| ch21 | bai | 3 | 21 | 站门外 | 同上 | 2 | aff_bai | bai_treated、station_key | ch25 |
| ch22 | qing | 1 | 22 | 门后 | 锁线 qing | 2 | aff_qing | know_qing_secret | ch23 |
| ch23 | qing | 2 | 23 | 空的档案柜（刀点） | 同上 | 2 | **qing_trusted**、**evidence_copied**、trust_shiqi、aff_qing | know_qing_secret | ch24 |
| ch24 | qing | 3 | 24 | 守站人 | 同上 | 2 | **evidence_kept**、trust_shiqi、aff_qing | ari_helped、qing_trusted、evidence_copied | ch25 |
| ch25 | common | 25 | 25 | 结算 | 已走完本线 | 1（决定性） | **evidence_kept**、**vn2_ending_key** | vn2_lock_route | ch26 |
| ch26 | end | 26 | 26 | 结局 | key 已落定 | 0 | — | vn2_ending_key → `call expression` | ch27 |
| ch27 | end | 27 | 27 | 清算 | 同上 | 1 | station_key | trust_shiqi、station_key、evidence_kept、ending_key | ch28 |
| ch28 | end | 28 | 28 | 后日谈 | 同上 | 1 | — | 8 条线旗标 + ending_key | None → 主菜单 |

**锁线与并行隔离**：ch14 菜单四项，蓝羽/白砚/青岩仅在对应 `aff ≥ 25` 时可进（不足时 `vn2.notify` 报「还差 N 点（当前 X / 25）」并回环重选，不是静默死选项），「独自进入」恒可选 → `vn2_lock_route = "solo"` → ch15 直接跳 ch25。

---

## 3. 结局矩阵（8 个）

判定顺序由 `vn2_decide_ending(force_sealed=False)` 实现，**真结局 > 封口 > 同行 > 独行**：

| key | 路线 | 展示名 | 条件 | 真结局 |
|---|---|---|---|---|
| `lan_together` | lan | 蓝羽 · 同行 | 蓝羽线 · aff ≥ 40 | 否 |
| `lan_alone` | lan | 蓝羽 · 独行 | 蓝羽线 · aff < 40 | 否 |
| `bai_together` | bai | 白砚 · 同行 | 白砚线 · aff ≥ 40 | 否 |
| `bai_alone` | bai | 白砚 · 独行 | 白砚线 · aff < 40 | 否 |
| `qing_together` | qing | 青岩 · 同行 | 青岩线 · aff ≥ 40 | 否 |
| `qing_alone` | qing | 青岩 · 独行 | 青岩线 · aff < 40 | 否 |
| `sealed` | common | 封口 | ch25 选「把站封掉」，或 route == solo 且未达真结局 | 否 |
| `seventh` | common | 第七天 | `trust_shiqi` ∧ `evidence_kept` ∧ route ≠ solo ∧ 本线 aff ≥ 60 | **是** |

- 8 个 key 各对应 `story\endings.rpy` 里一个 `vn2_end_<key>` label（15–25 行，末行 `return`）；`ch26` 用一行 `call expression ("vn2_end_" + vn2_ending_key)` 派发，回来后继续 ch26 收束 → ch27 → ch28。
- 达成即写入 `persistent.vn2_endings`；`vn2_endings_matrix()` 是唯一真值，`vn2_ending_list()` 与画廊计数都读它，**不再写死 4×2 或 `/8`**。

### 数值可达性（实算，非估算）
按"每个 menu 取该线最大加值"累加（脚本 `_tools\calc_aff_ceiling.py`，初始 10）：

| 线 | 共同线 1–13 最大累计 | ch13 末上限 | 专属 3 章最大累计 | 终值上限 |
|---|---|---|---|---|
| lan | +81 | 91 | +39 | **130** |
| bai | +85 | 95 | +25 | **120** |
| qing | +71 | 81 | +28 | **109** |

结论：锁线阈值 25、同行 40、真结局 60 三档都在可达范围内；真结局需要玩家在共同线就集中偏向同一位。**副作用**：共同线好感给得很宽，若玩家平均分配，ch14 时三条线可能都 ≥25，「独行」（<40）需要刻意压低本线好感才能拿到——这是设计允许但偏松的分布，见 §6 残留风险 R2。

---

## 4. 旗标闭环表（12 个，全部有写有读）

| 旗标 | 写入点 | 读取点 | 状态 |
|---|---|---|---|
| `trust_team` | ch03、ch06、ch09（单分支） | ch09 章末、ch18 | 闭环 |
| `close_lan` | ch11、ch16、ch17（追出分支） | ch16、ch18、ch28 | 闭环 |
| `lan_map_fixed` | ch10（当面摊牌分支） | ch10、ch11、ch16、ch17 | 闭环 |
| `saved_bai` | ch12（接住杆子分支） | ch19、ch20、ch28 | 闭环 |
| `bai_treated` | ch20（三个分支都完成手术） | ch21、ch28 | 闭环 |
| `know_qing_secret` | ch13（看见塞纸回箱） | ch17、ch22、ch23、ch28 | 闭环 |
| `qing_trusted` | ch23（当面对质分支） | ch24、ch28 | 闭环 |
| `station_key` | ch15、ch27 | ch18、ch21、ch27 | 闭环 |
| `evidence_kept` | ch24、ch25 | `vn2_decide_ending()`、ch27、ch28 | 闭环 |
| `evidence_copied` | ch23（抄名单分支） | ch24 | 闭环 |
| `trust_shiqi` | ch15、ch23（锁回柜子分支）、ch24 | `vn2_decide_ending()`、ch27、ch28 | 闭环 |
| `ari_helped` | ch08（蹚水救人分支） | ch08、ch18、ch24、ch28 | 闭环 |

无「只读不写」旗标；无「只写不读」旗标。

---

## 5. findings 修复记录

审查线共跑四轮（基线 → ch08–13/ch16–18 → 终审），只读、不改文件。

| # | findings | 严重度 | 修法 | 状态 |
|---|---|---|---|---|
| 1 | 结局层只有 `end_e01/e02` 两个 label，8 个 key 的 `vn2_end_*` 全不存在 | BLOCKER | 新建 `story\endings.rpy` 8 个 label；删旧两文件及 .rpyc；ch26 改 `call expression` 派发 | 已修 |
| 2 | 锁线无分派机制：无 `vn2_lock_route`、无 25 阈值、ch15 后静态串联、solo 无落点 | BLOCKER | ch14 四选一 + `vn2_lock_pick()`；ch15 按 route 动态跳；solo→ch25 | 已修 |
| 3 | 旗标写读错位、schema 仍 1、新变量未 default、旧档迁移未清理 | BLOCKER | schema 升 2；补 5 个新变量 default + repair 白名单；摘除 3 个旧变量 | 已修 |
| 4 | ch16–18 六处 `menu:` 提示语带冒号且选项多缩进一级（Ren'Py 解析期报错） | BLOCKER | 改为 caption 无冒号 + 与选项同级 | 已修（C1 回改） |
| 5 | ch19–24 十二处同类冒号错误（lint 实跑报 `choice menuitem expects a non-empty block`） | BLOCKER | 定位后去冒号、缩进不动 | 已修（本轮 lint 前） |
| 6 | `aff_zhou` 仍在好感表、19 处选项给玩家自己刷好感、初始值 20 | MAJOR | 删 key、全部改 lan/bai/qing，初始 10 | 已修 |
| 7 | 阈值体系不符（旧 50/deep 50） | MAJOR | 25 锁线 / 40 同行 / 60 真结局，按优先级落 key | 已修 |
| 8 | 路线归属错位：ch16–18 挂 bai、三线未隔离 | MAJOR | CHAPTERS 按契约整表重写（16–18 lan、19–21 bai、22–24 qing） | 已修 |
| 9 | `vn2_ending_list()` 2 kind × 4 AFF_KEYS，含 zhou，画廊显示 4 个 zhou 格 | MAJOR | 改读 `vn2_endings_matrix()`；画廊计数改 `len(matrix)` | 已修 |
| 10 | NPC 未接入：无 `arui`/`shiqi` Character、`aff_ari`/`trust_shiqi`/`ari_helped` 缺失 | MAJOR | 补两 NPC 全套（Character + 6 表情 image + cast）；`ari` 别名兼容 ch08 旧台词 | 已修 |
| 11 | ch01–07 把玩家写成第三人（递水壶/拍肩/"帮[player_name]收绳"） | MAJOR | 七章全部重写：旁白「你」、玩家发声 `zhou`、NPC 递送动作改成玩家自取 | 已修 |
| 12 | 显示口径用目录号，无 disp；章节列按 zhou 四段 | MAJOR | CHAPTERS 补 `disp`；`vn2_chapter_label()` 产出「蓝羽线 · 第 3 章」；章节页分 6 段 | 已修 |
| 13 | ch28 `day=28` 与「二十七日」品牌冲突；标题卡写成「第 28 天」 | MAJOR | 统一为 27 天主线：ch28 `day=27`、章节页显示「后日谈」、标题卡改「二十七天后 / 后日谈」 | 已修 |
| 14 | `vn2_hide_all()` 遍历 `VN2_AFF_KEYS`，删 zhou/加 ari 后会清错场 | MAJOR | 独立 `VN2_SPRITE_TAGS` 表 | 已修 |
| 15 | 玩家 Character 挂「· 队长」后缀 | MAJOR | 改字面量 `[player_name]`，职位只在台词里写 | 已修 |
| 16 | ch27 事后回写 `evidence_kept`，可把 sealed/alone 翻成带证据，与已播结局矛盾 | MAJOR | ch27 不再写 `evidence_kept`，分支改实写台词差异 | 已修 |
| 17 | 全仓无 `vn2_unlock_cg()` 调用，4 张 CG 永久锁死、画廊恒 0/4 | MAJOR | ch03/ch09/ch20/ch24 各补一处解锁；CG 副题改本线序号 | 已修 |
| 18 | `aff_ari` 零写入，好感摘要恒 10 | MAJOR | ch08 帮阿瑞分支 +3 | 已修 |
| 19 | ch10 刀点回扣引用了只在 ch05 单分支出现的台词 | MAJOR | 改成不依赖具体选项的泛述 | 已修 |
| 20 | ch09 `trust_team` 三分支全置位，旗标失去区分度 | MAJOR | 只留「交地图」分支置位，章末加 if/else 读 | 已修 |
| 21 | `evidence_copied` 章节内本地 `default`，与状态层重复声明风险 | MAJOR | 章节内删 default，注册进状态层与修复白名单 | 已修 |
| 22 | `vn2_seed_for_chapter()` 漏回填 `evidence_copied` | MINOR | 按 `no >= 23` 补 | 已修 |
| 23 | ch14 标题卡显示「第 14 章」，未走「锁线」 | MINOR | 锁线章不显示序号 | 已修 |
| 24 | `VN2_BGM` 残留 `"zhou"` 死键 | MINOR | 删键，素材保留 | 已修 |
| 25 | `vn2_top_route()` 无调用者（死代码） | MINOR | 确认无引用后删除 | 已修 |
| 26 | ch27 第一人称串线「我带出去」 | MINOR | 改「你带出去」 | 已修 |
| 27 | ch18 `getattr(store,…)` 与直读混用 | MINOR | 统一直读 | 已修 |
| 28 | `script.rpy` 开发 demo `label start` 可能被默认 Start() 命中（引擎启动硬编码找 `start`，不读 `config.start_label`） | MAJOR | `label start` 改成 `jump story_start`；旧 demo 体（21 行、V1 立绘、把玩家写成第三人）删除，只留说明注释 | 已修 |

**明确未修的（本轮范围外，已登记）**
- 探索层相关：旧队徽/绳索矿灯"无副本获取状态背书"（副本未建，来源台词属假定前置）。
- 旧 V1 立绘文件（`images/chars/wolf_*.png` 等 4 张）与 `script.rpy` 顶部的旧 `Character`/`image`/`transform` 声明保留作备份（用户要求旧图不删），但已无任何剧情引用。
- 旧自动生成文档 `CHAPTER_OUTLINE.md` / `CHOICES.md` / `ROUTES_ENDINGS.md` 与 `_tools/` 生成脚本仍写旧「老周线」口径，未重生成。
- `testcases.rpy` 仍是模板用例，未覆盖 VN2 锁线/结局分支。

---

## 6. 残留风险（静态证明不了，必须跑游戏确认）

| # | 风险 | 怎么验证 |
|---|---|---|
| R1 | 主菜单 `Start()` 是否真进 `story_start` 而不是旧 demo（demo 末尾 `renpy.quit()`） | 启动 → 点「开始新游戏」→ 确认进命名页 → ch01，未出现黑屏退出 |
| R2 | 好感给得偏宽：共同线最大可累计 81/85/71，平均分配时三条线在 ch14 可能都 ≥25，"独行"（<40）较难拿 | 三条线各走「平均选项」一遍，记 ch25 终值；若确实普遍 ≥40，需下调共同线加值或上调同行阈值 |
| R3 | 真结局四条件 AND 的实际可玩性（需 trust_shiqi + evidence_kept + 非 solo + aff≥60） | 走一遍「青岩线 + ch15 信十七 + ch24 带证据 + 专注青岩」到 ch25，确认拿到 `seventh` |
| R4 | schema 1 旧档迁移：摘旧变量、补 12 个新变量、bool 校正、章节上下文回填 | 放一个旧档载入，查无 AttributeError、章节标签与 disp 正确 |
| R5 | `call expression` 派发后 8 个 label `return` 是否回到 ch26 续演（不跳主菜单） | 8 个结局各跑一遍，确认 return 后 ch26 收束 → ch27 → ch28 接续正常 |
| R6 | V2 立绘运行期解析：`ari`→`arui` 别名、表情图缺失回退 neutral、`far_left/far_right` 站位不越界 | 走到 ch08/ch15/ch23/ch24 与 sealed/seventh 结局，确认舞台无缺图、无报错、不压对话框 |
| R7 | 章节选择跳转后 rollback：章节上下文、立绘、BGM 是否一致 | 任跳一章 → 回滚一步 → 读自动存档，核对 ch id / 立绘 / route BGM |
| R8 | 旧周目 `persistent.vn2_endings` 里残留旧 key（如 `e01_zhou`）会否干扰计数与点亮 | 手写一个旧 key 后开收集页，核对计数 = 8 且旧项不点亮 |
| R9 | ch14 未达标选项的 notify 回环会不会重复扣状态 | 故意压低好感点未达标项，反复回环后进 solo，核对 aff/旗标未变 |

---

## 7. 文件清单

**新建**
- `game\story\endings.rpy`（8 个结局 label）
- `game\_docs\ROUND4_CONTRACT.md`（本轮契约，冻结版）
- `game\_docs\ROUND4_story.md`（本文档）
- `_tools\check_empty_blocks.py`、`_tools\fix_menu_caption.py`、`_tools\calc_aff_ceiling.py`（静态检查与数值核算脚本，可复跑）

**删除**
- `game\story\end_e01.rpy`、`end_e01.rpyc`、`end_e02.rpy`、`end_e02.rpyc`

**重写 / 改写**
- 章节：`game\story\ch01.rpy` – `ch28.rpy`（28 个）
- 状态与路由：`core\00_state.rpy`、`core\10_affinity.rpy`、`core\20_router.rpy`、`core\30_save.rpy`、`core\40_cast.rpy`、`core\50_audio.rpy`、`core\60_gallery.rpy`
- 界面：`ui2\60_chapters.rpy`、`ui2\30_saveload.rpy`、`ui2\50_gallery.rpy`（仅结局列表段）、`ui2\10_hud.rpy`（仅锁线标题卡段）
- 入口：`story\story_start.rpy`、`game\script.rpy`（`label start` 改跳正式入口，旧 demo 体移除）

---

## 8. lint

命令（SDK python 入口，**不要用 `renpy.exe`**，本机不回传 stdout）：
```
"D:\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" "D:\renpy-8.5.3-sdk\renpy.py" "L:\AI\FurryVN\20261117_uidemo" lint "L:\AI\FurryVN\20261117_uidemo\lint_round4.txt"
```
结果：**EXIT = 0，0 error / 0 warning**（含"不可达语句"告警也已清零）
- dialogue blocks 803 / words 814 / characters 15,289
- menus 51 / images 62 / screens 51
- 报告文件：`L:\AI\FurryVN\20261117_uidemo\lint_round4.txt`
- 静态辅助检查：`_tools\check_empty_blocks.py` → `BAD_COUNT=0`（无 menu 提示语误带冒号 / 空选项块）

未启动 Ren'Py 游戏进程、未写 `game\saves`、未覆盖 `game\images\cg\cg_*.png` 与 `gthumb_cover_*`。
