# Round7 隐藏分闭环审计（只记录，不改判定）

- 审计对象：`game/core/20_router.rpy`（`vn2_decide_ending`、`vn2_seed_for_chapter`、`vn2_lock_options`、`vn2_lock_pick`）、`game/core/00_state.rpy`（旗标默认值表）
- 审计日期：2026-11-17
- **本轮未修改任何判定逻辑**，以下四项需主 Agent / 用户拍板后才动 `core`

## 1. solo 不是 aff<40 的 fallback，而是独立路线且必然封口

`vn2_decide_ending` 的实际顺序（`20_router.rpy:217–240`）：

```
if trust_shiqi and evidence_kept and route != "solo" and route_aff >= 60:  key = "seventh"
elif force_sealed or route == "solo":                                     key = "sealed"
elif route in VN2_ROMANCE_KEYS and route_aff >= 40:                       key = "..._together"
else:                                                                     key = "..._alone"
```

结论：
- `route == "solo"` 是**硬绑 sealed**，不是"好感不够的兜底"。
- 三个「独行」结局（`lan_alone` / `bai_alone` / `qing_alone`）只能由**恋爱线 + aff<40** 达成。
- 因此「小线路 solo 4 小时」在现结构下**没有专属结局**，玩家走 solo 线无论好感多少都只能拿封口。若 solo 要成为可玩的小线路，需要 3 个新的「solo 专属结局」或让 solo 也能进 `_alone` 分支——这属于结局 key 与判定改动，本轮不动。

**建议（待拍板）**：把 `elif force_sealed or route == "solo"` 拆成两支，`route=="solo"` 走 `..._alone`（复用现有 3 个独行 label，不新增 key），只让 `force_sealed` 走 sealed。改动面 1 行，但会改变结局分布，需明确授权。

## 2. `force_sealed` 会被真结局覆盖

真结局判定在 `if` 的第一位，`force_sealed` 在 `elif` 第二位。所以只要玩家同时满足 `trust_shiqi + evidence_kept + route!=solo + 本线 aff>=60`，即使 ch24 选了「封门」（若将来给 force_sealed 透传），结局仍是第七天。

这是"优先级 真结局 > 封口"的正常体现，但也意味着**玩家在 ch24 做的封门选择可能被静默无视**。当前 ch24 的「封门」只写意图、不落旗标（Round7 Phase A 的已知取舍），所以现在不会触发；一旦给封门加上透传，就必须决定：真结局条件下封门意图是否算数。

**建议（待拍板）**：给玩家一次"确认"（真结局条件满足时，封门选项变灰或加一句提示），而不是静默覆盖。

## 3. `vn2_seed_for_chapter` 的旧旗标残留（章节选择与真实流程不一致）

`20_router.rpy:260–310`。这不是 bug，是"章节选择/回看"的便利回填，但它有 5 处与真实流程对不上，会让章节选择的结局演出和真实结算不同：

| # | 代码 | 问题 | 影响 |
|---|---|---|---|
| a | `store.vn2_lock_route = route if route in VN2_ROMANCE_KEYS else "solo"`（:300） | ch25–ch28 的 route 不是 romance，一律被置成 `solo` | **从章节选择进 ch25/ch26 的玩家，结局必然是 sealed**（见 §1）。这是本组最严重的一条 |
| b | `if no >= 24: vn2_flag("evidence_kept", True)`（:297–298） | 无条件回填"留下证据" | 章节选择进 ch26–28 时，`sealed`/`seventh` 分支的读点与真实流程（ch25 可能选择"不留"）不一致 |
| c | `if route == "bai" or no >= 20: vn2_flag("bai_treated", True)`（:287–288） | 进 ch19（bai 线 no=19）就已经带 `bai_treated` | ch19 里若有 `bai_treated` 的读点，章节选择会读到"手术已发生" |
| d | `if cid == "ch15" or route == "bai": vn2_flag("station_key", True)`（:291–292） | 进 ch19 就带钥匙 | 同上 |
| e | `if no >= 15: vn2_flag("trust_shiqi", True)`（:293–294） | 真实流程里 `trust_shiqi` 只在 ch15/ch23/ch24 的特定选项写 | 章节选择进 ch16+ 一律带"十七信任"，会把真结局门槛变松 |

另：`base = min(35, 10 + int(no*1.2))` 使 ch14（no=14）三线好感都是 26 ≥ 锁线门槛 25 → **从章节选择进 ch14 时三个恋爱选项全部可点**，玩家看不到"未达标置灰"的真实状态，也无法验证置灰分支。这不是错误，但意味着**锁线置灰只能在真实周目里验证**。

## 4. 没有正式 NG+

`persistent` 只用两处：`vn2_unlocked`（章节解锁）与 `vn2_endings`（结局收集）。没有跨周目继承（好感/旗标/物品）也没有 NG+ 开关；章节选择是"回看/调试"入口，靠 §3 的 seed 回填让章节能独立跑起来。

**建议（待拍板）**：如果最终要做 NG+（继承好感、解锁隐藏选项），需要新增 `persistent.vn2_ng_plus_*` 与开局回填逻辑；这是结构性改动，建议等 C 批（营地/副本容器）落地、存档 schema 升级时一并做，避免两次升级 schema。

## 5. 与文档口径的偏差（无风险，仅记录）

- `STORY_CANON.md §6` 仍写着"工程目前把 zhou 当第四条好感线""router 是顺序四段"等**重排前的历史状态**，实际代码已重排完成。这份文档的 §6 已过期，建议在下一轮文档整理时改写为"已完成项 + 剩余差异"，以免后来者按过期描述改动 `core`。
- `STORY_CANON.md` 的刀点/甜点章号（第 6、10、17、20、23、25 刀点；第 2、3、13、16、19、22、28 甜点）与本轮 Phase B 的 27 场甜点连锁表（`ROUND7_PHASE_B.md §3`）**扩展了但不冲突**：原 7 个甜点仍是锚点，新增甜点是加密，符合 §4「密度提高到每 2–3 章一场」。

## 6. 本轮结论

四项需要拍板的改动（①solo 的结局归属 ②force_sealed 与真结局的优先级冲突 ③seed 回填的 5 处不一致 ④是否做 NG+）**均属 `core` 改动，本轮按约束未动**。当前可确认的安全边界：真实周目（不使用章节选择）的判定链路是正确的，结局 key、阈值、旗标集合与 `endings.rpy` 的 8 个 label 一一对应，没有孤儿 label 或不可达结局——`lan/bai/qing × together/alone + sealed + seventh` 的八条路径在真实流程里都可达（together 需 aff≥40、alone 需 aff<40、sealed 需 solo 或 force_sealed、seventh 需四项条件齐）。
