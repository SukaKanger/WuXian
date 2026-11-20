# ROUND4 剧情重排契约（冻结版，2026-11-17）

> 本文件是**唯一契约**。写作线、数据线、审查线都以它为准；任何偏离必须先回报，不得自行改口径。
> 上游口径见 `STORY_CANON.md`（v3）。本契约只解决"怎么落到代码里"。

## 1. 玩家与角色

- 玩家 = 老周（灰狼队长）。`player_name` 由开局命名页写入，默认「队长」。
- **玩家发声**仍用 `zhou "..."` 这个 Character，但其显示名改成 `[player_name]`：
  `define zhou = Character("[player_name]", color="#e8b96a", callback=vn2_char_cb("zhou"))`
  → 名牌显示玩家自己填的名字，不再是 NPC「老周」。
- 旁白一律第二人称「你」；提到玩家写成 `[player_name]`，绝不出现把玩家当第三人的句子（如"他递给你水壶""拍了拍你的肩"）。
- 立绘 tag `zhou` 只在群像 / 背影 / 玩家自己看得到的镜头出现；单人对白默认不 show 玩家自己。
- 角色：`lan` 蓝羽、`bai` 白砚、`qing` 青岩（可攻略）；`ari` 阿瑞、`shiqi` 十七（NPC，不参与恋爱判定）。

## 2. 状态层（存档 schema = 2）

好感（初始 **10**，0–100）：
```
aff_lan / aff_bai / aff_qing            # 三条恋爱线
aff_ari                                  # NPC，只影响支线与交易，不进结局判定
```
删除 `aff_zhou`（玩家不给自己刷好感）；`VN2_AFF_KEYS = ("lan","bai","qing","ari")`，`VN2_ROMANCE_KEYS = ("lan","bai","qing")`。

旗标（全部 bool，必须"有写有读"，不许留死旗标）：
| 旗标 | 写入章 | 读取点 |
|---|---|---|
| `trust_team` | ch03 / ch06 / ch09 | ch14 锁线判定提示、ch25 结算 |
| `close_lan` | ch11 / ch16 | ch18 / ch25 |
| `lan_map_fixed` | ch10 | ch17 台词、ch25 |
| `saved_bai` | ch12 | ch20 / ch25 |
| `bai_treated` | ch20 | ch21 / ch25 |
| `know_qing_secret` | ch13 | ch23 / ch25 |
| `qing_trusted` | ch23 | ch24 / ch25 |
| `station_key` | ch15（守门人交易） | ch21 / ch25 |
| `evidence_kept` | ch24 / ch25 选择 | ch26–28、真结局判定 |
| `trust_shiqi` | ch15 / ch24 | ch25 真结局判定 |
| `ari_helped` | ch08 支线选择 | ch24 阿瑞回报（给补给） |

> 旧的 `trust_zhou` / `heard_zhou_past` 随 schema 升到 2 一并移除；旧存档迁移时只保留能映射的项（aff_lan/bai/qing、close_lan、saved_bai、know_qing_secret、station_key、evidence_kept、player_name），其余回默认。

## 3. 章节表（28 条）

`no` = 内容目录编号；`disp` = 界面显示号（本线内序号，不跳号）；`route` = 归属。

| no | id | route | disp | day | title | next |
|---|---|---|---|---|---|---|
| 1 | ch01 | common | 1 | 1 | 雨停之后 | ch02 |
| 2 | ch02 | common | 2 | 2 | 三里旧栈道 | ch03 |
| 3 | ch03 | common | 3 | 3 | 断崖 | ch04 |
| 4 | ch04 | common | 4 | 4 | 夜哨 | ch05 |
| 5 | ch05 | common | 5 | 5 | 绳结 | ch06 |
| 6 | ch06 | common | 6 | 6 | 雨幕 | ch07 |
| 7 | ch07 | common | 7 | 7 | 第一块站牌 | ch08 |
| 8 | ch08 | common | 8 | 8 | 沼泽边 | ch09 |
| 9 | ch09 | common | 9 | 9 | 银纹 | ch10 |
| 10 | ch10 | common | 10 | 10 | 改过的地图 | ch11 |
| 11 | ch11 | common | 11 | 11 | 第二座信标 | ch12 |
| 12 | ch12 | common | 12 | 12 | 旧营地 | ch13 |
| 13 | ch13 | common | 13 | 13 | 分岔 | ch14 |
| 14 | ch14 | lock | — | 14 | 锁线 | 动态 |
| 15 | ch15 | common | 15 | 15 | 门口 | 动态 |
| 16 | ch16 | lan | 1 | 16 | 旧队徽 | ch17 |
| 17 | ch17 | lan | 2 | 17 | 雾里的名字 | ch18 |
| 18 | ch18 | lan | 3 | 18 | 两条路 | ch25 |
| 19 | ch19 | bai | 1 | 19 | 空药瓶 | ch20 |
| 20 | ch20 | bai | 2 | 20 | 手术 | ch21 |
| 21 | ch21 | bai | 3 | 21 | 站门外 | ch25 |
| 22 | ch22 | qing | 1 | 22 | 门后 | ch23 |
| 23 | ch23 | qing | 2 | 23 | 空的档案柜 | ch24 |
| 24 | ch24 | qing | 3 | 24 | 守站人 | ch25 |
| 25 | ch25 | common | 25 | 25 | 结算 | ch26 |
| 26 | ch26 | end | 26 | 26 | 结局 | ch27 |
| 27 | ch27 | end | 27 | 27 | 清算 | ch28 |
| 28 | ch28 | end | 28 | 28 | 后日谈 | 结束 |

- 单周目实际走 22 章：1–15 + 本线 3 章 + 25–28。
- `to_next_after_lock()`：ch14 选线后 → ch15；ch15 结束按 `vn2_lock_route` 跳：`lan→ch16 / bai→ch19 / qing→ch22 / solo→ch25`。
- 界面显示：`vn2_chapter_label()` 返回「共同线 · 第 6 章」/「蓝羽线 · 第 3 章」/「锁线」/「结局 · 第 2 章」。**显示 disp，不显示 no**。

## 4. 锁线与结局

锁线（ch14）菜单四项，判定在 `vn2_lock_options()`：
- 蓝羽 / 白砚 / 青岩：仅当对应 `aff >= 25` 可选（不足则该项文案变灰并给提示，走 `vn2_nudge` 反馈，不要 NullAction）；
- 独自进入：永远可选 → `vn2_lock_route = "solo"`。

结局 8 个（key → 展示名）：
```
lan_together 「蓝羽 · 同行」   lan_alone 「蓝羽 · 独行」
bai_together 「白砚 · 同行」   bai_alone 「白砚 · 独行」
qing_together「青岩 · 同行」   qing_alone「青岩 · 独行」
sealed        「封口」          seventh    「第七天」
```
ch25 结算：先给一个决定性选择（`menu` 三项），再按**优先级 真结局 > 封口 > 同行 > 独行** 落 key：
1. `第七天`（真结局）：`trust_shiqi and evidence_kept and route != "solo" and aff(route) >= 60`
2. `封口`：玩家选「把站封掉」（任何时候可选），或 `route == "solo"` 且真结局条件不满足
3. `同行`：`aff(route) >= 40`
4. `独行`：其余
写成 `vn2_endings_matrix()` 返回 8 项的 dict（key/路线名/标题/达成条件文案/是否真结局），结局收集页直接读它，**不要**再写死 4×2。

**结局 label 约定**（`story/endings.rpy` 由数据线写，ch26 由写作 D 调用）：
- 8 个 label，命名 `vn2_end_<key>`：`vn2_end_lan_together`、`vn2_end_lan_alone`、`vn2_end_bai_together`、`vn2_end_bai_alone`、`vn2_end_qing_together`、`vn2_end_qing_alone`、`vn2_end_sealed`、`vn2_end_seventh`。
- 每个 label 15–25 行，只演"这一刻"的场景与对白，**最后一行必须是 `return`**（不 jump、不 leave_chapter）。
- `ch26` 用 `call expression ("vn2_end_" + vn2_ending_key)` 派发，回来继续走 ch27/ch28。

## 5. 写作规范（所有章节文件统一）

```renpy
# 第 N 章 • 标题（第 D 天 / 路线标签）

label chNN:

    scene bg <场景> with slow_fade
    $ vn2_enter_chapter("chNN")
    call vn2_title_card(<disp>, "<标题>", "第 <D> 天 • <路线标签>")

    nar "旁白，第二人称。"
    think "玩家内心。"
    lan "对白。"
    zhou "玩家自己说的话（名牌显示玩家名）。"

    menu:
        "选项 A":
            $ vn2_aff_add("lan", 4)
            ...
        "选项 B":
            $ vn2_aff_add("bai", 4)
            $ vn2_flag("saved_bai")
            ...

    $ vn2_leave_chapter()
```
- 每章 **2 个 menu**（锁线/结算章除外，可 1 个决定性 menu）；每个选项**必须有后果**（好感 / 旗标 / 后续台词三者至少一个，且能被后面读到）。
- 单章 40–70 行，文风沿用现有：短句、少形容词、雨与雾的体感、不写解释性旁白。
- 场景只许用 `bg jungle/firelight/marsh/gate/hall/cliff/forest` 与已有 `vn2_amb()` 环境名；CG 一律不新增（`cg_*.png` 现在是空白占位，禁止覆盖）。
- 不新增立绘文件；表情差分不存在时只用 `vn2_show(tag, pos=...)`。
- 刀点（6/10/17/20/23/25）各章必须至少一处前面埋过的伏笔回收；甜点（2/3/13/16/19/22/28）必须有一处明确的暖场。

## 6. 文件分工（并行写，互不越界）

| 责任 | 文件 |
|---|---|
| 数据线 | `core/00_state.rpy`、`core/10_affinity.rpy`、`core/20_router.rpy`、`core/30_save.rpy`、`core/60_gallery.rpy`、`ui2/60_chapters.rpy`、`ui2/30_saveload.rpy`、`story/story_start.rpy`、`story/ch14.rpy`、`story/ch15.rpy`、`story/ch25.rpy`、`story/endings.rpy`（新建，8 个 label） |
| 写作 A | `story/ch01.rpy`–`ch07.rpy` |
| 写作 B | `story/ch08.rpy`–`ch13.rpy` |
| 写作 C1 | `story/ch16.rpy`–`ch18.rpy` |
| 写作 C2 | `story/ch19.rpy`–`ch21.rpy` |
| 写作 C3 | `story/ch22.rpy`–`ch24.rpy` |
| 写作 D | `story/ch26.rpy`–`ch28.rpy` |
| 审查线（只读） | 不改任何文件，只出 findings |

> `story/end_e01.rpy` / `end_e02.rpy` 由数据线改写成 8 个结局 label 的 `endings.rpy` 并删除旧文件；其它线一律不碰这两个文件。
