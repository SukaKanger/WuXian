# 雾线 VN2 · 系统层修复记录（Round7 System Fix）

日期：2026-11-17  
工程：`L:\AI\FurryVN\20261117_uidemo`  
备份：`_backup_round7_systemfix_20261117_1918`（`game\core` + `game\story`）

## 一、修复目标

不改 229 个普通选项，不扩写正文，只修三个系统层问题：

1. 真结局/同行结局只靠好感就能拿到，日常选项刷满 60 即可；
2. `ch27` 两个证据选项不写 `evidence_kept`，导致旁白与后文分支自相矛盾；
3. 部分早期选择没有任何持久后果，队伍线/白砚线的关键选择缺少回声。

## 二、改动清单

### 1. 结局判定加入“路线承诺”门槛

文件：`game/core/20_router.rpy`

新增 `vn2_route_bond(route)`：

| 路线 | 承诺旗标 | 现有置位点 |
|---|---|---|
| 蓝羽 | `close_lan` | ch11 / ch16 / ch17 |
| 白砚 | `saved_bai` | ch12「抢在他前面接住杆子」 |
| 青岩 | `qing_trusted` | ch23「当面问青岩」 |

`vn2_decide_ending()` 新顺序：

1. `force_sealed` 或 `route == "solo"` → `sealed`
2. 真结局：`trust_shiqi` + `evidence_kept` + 本线好感 ≥ 60 + 本线承诺 → `seventh`
3. 同行：本线好感 ≥ 40 + 本线承诺 → `*_together`
4. 否则 → `*_alone`

这样“每处选第 2 项”把好感刷到 60，不再自动等于真结局；没走过本线关键选择，会落到本线独行。

结局收集页的 `cond_text` 已同步写明“交过底 / 救过手 / 当面信过你 / 完成本线承诺”。

### 2. 封站优先于真结局

`force_sealed=True` 现在在判定最前，封站不会再被真结局条件覆盖。`ch25` 的封站选项因此真正有效。

### 3. 修 `ch27` 证据旗标错位

文件：`game/story/ch27.rpy`

- 「档案贴身带出去」：写入 `evidence_kept = True`；
- 「档案封回站里」：写入 `evidence_kept = False`；
- 该选项加条件 `if vn2_ending_key != "seventh"`：真结局下不再显示“封回”，避免 `ch27` 结尾与 `ch28` 真结局演出自相矛盾。

### 4. 新增一个轻量旗标 `bai_rationed`

文件：`game/core/00_state.rpy`、`game/core/30_save.rpy`、`game/story/ch21.rpy`、`game/story/ch25.rpy`、`game/story/ch28.rpy`

- `ch21` 药份菜单：
  - 「三份平均留」→ `bai_rationed = False`
  - 「全压在一个人身上」→ `bai_rationed = True`
  - 「记账」→ `bai_rationed = False`
- `ch25` 白砚线“三样东西”处按该旗标给一句不同旁白；
- `ch28` 白砚同行/独行各加一句后日谈回声。

`VN2_SAVE_SCHEMA` 不升版本；旧档由 `vn2_repair_state()` 从 `VN2_DEFAULT_VALUES` 补齐 `bai_rationed=False`。

### 5. 早期选择加后文回声

- `ch01`「把守夜的班次先排出来」→ `trust_team`
- `ch13`「跟在队尾，一段一段清点人数」→ `trust_team`

`trust_team` 已在 `ch09 / ch17 / ch18` 被读取，因此这两个早期选择会在后文产生可见分支，不新增变量。

## 三、验证

### lint

Ren'Py 8.5.3 lint 通过：

- 3,302 dialogue blocks
- 107,021 characters
- 87 menus
- 62 images
- 52 screens
- 报告 0 error / 0 warning

说明：lint 报告本身干净；命令退出时命中了 `game\saves\persistent` 被外部进程占用的 Windows 文件锁，属于环境锁，不是脚本错误。

### 结局判定用例（引擎内真实调用 `vn2_decide_ending`）

| 用例 | 结果 |
|---|---|
| 蓝羽 aff=60、有承诺、trust_shiqi、带证据 | `seventh` |
| 蓝羽 aff=60、无承诺、trust_shiqi | `lan_alone` |
| 蓝羽 aff=40、有承诺 | `lan_together` |
| 白砚 aff=40、有承诺 | `bai_together` |
| 青岩 aff=40、有承诺 | `qing_together` |
| 青岩 aff=60、无承诺、trust_shiqi | `qing_alone` |
| 独线 | `sealed` |
| 蓝羽 aff=60、有承诺、trust_shiqi、带证据，但 `force_sealed=True` | `sealed` |

8 个用例全部符合预期。

## 四、本轮未做

- 没有重写 229 个只加好感的普通选项；
- 没有新增小游戏；
- 没有改动 14 张新背景与 CG 的生产流程；
- 没有跑完整 28 章人手周目；本轮只做 lint + 结局判定引擎内用例，完整周目沿用 Round7 C 批的实机结果。
