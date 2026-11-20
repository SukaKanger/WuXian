# 《雾线》Round7 · 实机跑（Playtest）报告

> 时间：2026-11-17 17:26–17:46（UTC+8）
> 环境：Windows 11 / Ren'Py **8.5.3.26051504**（`D:\renpy-8.5.3-sdk`），工程 `L:\AI\FurryVN\20261117_uidemo`
> 版本串（实机启动时读到的）：`雾线 V1.28.1 Beta`（`config.version`）

## 0. 一句话结论

真机跑通了：**一整条周目从 ch01 走到 ch28 结束、8 个结局 key 全部实机派发成功、ch28 收尾崩溃已定位并修复**。但没有走鼠标点击式的“人手试玩”——本环境桌面控制能力不可用（见 §1），实际是**引擎内自动驱动**（真实渲染、真实对话推进、真实菜单选择、引擎内截图），驱动是临时文件，跑完已删除，`lint` 复验仍 0/0。

## 1. 为什么不是“鼠标点着玩”

`computer_use_tool(plane="cu")` 在本环境直接返回
`{"error_code":40003,"error_msg":"computer_use_tool method not supported for plane cu"}`
——不能切 pip 虚拟桌面、不能 list_apps/launch_app、不能点鼠标；`mac_computer_use_tool` 是 macOS 专用，本机不适用。

所以改用 **Ren'Py 引擎自身**跑：

| 环节 | 做法 |
|---|---|
| 跳过启动器/主菜单 | 官方环境变量 `RENPY_SKIP_SPLASHSCREEN=1`、`RENPY_SKIP_MAIN_MENU=1` |
| 进入游戏 | `config.label_overrides["start"] = "_pt_start"`（只覆盖入口，不动任何既有 label） |
| 推进对话 | 每个 interaction 向引擎事件队列投一个合成的 `KEYDOWN(K_RETURN)`（**必须带 `repeat` 属性**，否则引擎在 `behavior.skipping` 里抛 `AttributeError` → 错误屏 → 反复重启，这是本轮踩到的第一个坑） |
| 选菜单 | `config.auto_choice_delay` + 把 `renpy.exports.random` 换成“只取第 N 项”的壳（确定性，避免随机选到“封站”） |
| 截图 | `renpy.screenshot()`（引擎把当前帧写盘，非 OS 截屏） |
| 日志 | 交互回调写 `playtest_log.txt`：章号、结局 key、菜单、截图路径 |

临时文件 `game/zz_pt_autoplay.rpy`（+`zz_pt_loadcheck.rpy`/`zz_pt_ui.rpy`）**已全部删除**，`.rpyc` 一并删除；工程内复跑 `lint` → **0 error / 0 warning**（3,298 blocks / 106,881 chars / 87 menus / 62 images / 52 screens，`lint_round7_c_final.txt`）。

> 也试过完全无头（`SDL_VIDEODRIVER=dummy` + `RENPY_RENDERER=sw`）：引擎能启动，但截图是**全黑**且跳过循环不推进，等于没有画面证据，所以放弃无头，改走真实窗口（窗口在用户桌面弹出，全程未点击、未抢键鼠）。

## 2. 跑了哪些

### 2.1 完整周目（跑到 ch28 收尾时撞上崩溃；修复后同路径复验成功）

`story_start`（命名页 → 开场卡）→ ch01 … ch18（ch14 锁线选了蓝羽）→ **ch19–ch24 不进入**（那是白砚/青岩线章）→ ch25 结算 → **结局 key = `seventh`** → ch26 结局 → ch27 清算 → ch28 后日谈（进章时引擎计数 **@line 1728**）→ **在 ch28 收尾处撞上 §3 的崩溃**。

逐章进章点（引擎推进计数）：ch01 @1、ch02 @71、ch03 @159、ch04 @224、ch05 @325、ch06 @402、ch07 @471、ch08 @553、ch09 @627、ch10 @712、ch11 @804、ch12 @917、ch13 @994、ch14 @1081、ch15 @1122、ch16 @1229、ch17 @1326、ch18 @1416、ch25 @1546、ch26 @1595、ch27 @1672、ch28 @1728。

整条周目共弹 **11 个 menu**（@24 / @149 / @303 / @422 / @536 / @688 / @841 / @979 / @1183 / @1341 / @1502），全部正常弹出并按预定项落选（本次统一取第 2 项，避开 ch25 第一项“把站封掉”）。**结局派发点：`seventh` @line 1591。**

**这一条本身就验证了**：启动无报错、章首三件套正常、C 批新增容器（ch02 扎营选址、ch04 轮值、ch07 站牌、ch09 天线、ch11 一份电、ch15 石门外、ch18 断崖勘察）全部在实际流程里被走到。

### 2.2 八结局派发（逐 key 实测）

做法：预置 `vn2_lock_route` / `aff_*` / `trust_shiqi` / `evidence_kept`，从 ch25 进入，走完 ch25→ch26→ch27→ch28，读 `vn2_ending_key`。

| 预置状态 | 期望 key | 实机 key | 结果 |
|---|---|---|---|
| route=solo | `sealed` | `sealed` | ✅ |
| lan + aff 100 | `lan_together` | `lan_together` | ✅（第 3 批重跑；前两批因菜单随机落到“封站”误出 sealed） |
| lan + aff 10 | `lan_alone` | `lan_alone` | ✅（第 2 批；第 1 批误出 sealed） |
| bai + aff 100 | `bai_together` | `bai_together` | ✅ |
| bai + aff 10 | `bai_alone` | `bai_alone` | ✅（第 3 批；前两批误出 sealed） |
| qing + aff 100 | `qing_together` | `qing_together` | ✅（第 3 批；第 2 批误出 sealed） |
| qing + aff 10 | `qing_alone` | `qing_alone` | ✅ |
| 完整周目（lan + 高好感 + `trust_shiqi` + `evidence_kept`） | `seventh` | `seventh` | ✅ |

**8/8 全派发成功。** 顺带印证了 `ROUND7_PHASE_B_AUDIT.md` 记的结构问题：只要在 ch25 选“把记录和证据带出去”，`evidence_kept` 会自动置真，`seventh` 的门槛实际只剩“好感 60 + `trust_shiqi`”。

### 2.3 存档 / 读档

- 每次进章 `vn2_autosave_entry()` 都会落盘：`%APPDATA%\RenPy\WuxianVN2-1\` 下有 `auto-1..auto-4` 等，**单个约 200 KB**，时间戳与各次实机跑一致 → 写入正常。
- 读档：`RENPY_AUTO_LOAD=auto-1` 启动，载入后**从存档点继续推进**、无异常、无 `traceback.txt` → 读档可用。
- **未覆盖**：手动存档页/读档页的 UI 操作（要鼠标点，本环境做不到）。

## 3. 本轮实机抓到的 bug（已修）

**`ch28` 通关必崩**：`game/core/20_router.rpy:147` 在最后一章结束时
`renpy.jump("main_menu")` —— 但工程里**没有**名为 `main_menu` 的 label（主菜单是 `_main_menu` label + `main_menu` screen）。于是每次通关都抛：

```
renpy.script.LabelNotFound: could not find label 'main_menu'.
  File "game/story/ch28.rpy", line 144, in script
    $ vn2_leave_chapter()
  File "game/core/20_router.rpy", line 147, in vn2_leave_chapter
    renpy.jump("main_menu")
```

玩家侧表现＝**看完后日谈就弹“An exception has occurred”**，不会回到主菜单。

已改为官方 API：

```python
# 最后一章（ch28）：回主菜单
# 注意：工程没有名为 main_menu 的 label（主菜单是 _main_menu + screen），
# 原先 renpy.jump("main_menu") 会抛 LabelNotFound；统一用 full_restart 回主菜单。
renpy.full_restart()
```

修复后回归：同一场景再跑一次（`run_verify`，预置 sealed），ch25→ch28 走完后日志落到
`CH 1  @line 211` + `=== RETURNED TO MAIN MENU after 211 lines, ending=sealed ===`，**正常回主菜单、无 `traceback.txt`**。
> 这是本轮唯一改动的非 C 批文件（`core/20_router.rpy` 1 行 + 3 行注释）。属“实机验收必修”，已在 `ROUND7_PHASE_C.md` 与本节记录在案。

## 4. UI 观察（截图留档）

截图目录：`C:\Users\Administrator\Doubao\chats\2026-11-17\new-chat\artifacts\playtest\shots\`（**44 张**：逐章入口 + 每 150 行一张 + 少量转场帧），另 `preview\` 为缩小版便于查看。

| 检查项 | 结论 |
|---|---|
| 启动报错 | 无。`traceback.txt` 只在 ch28 崩（已修）与我自己写坏的合成事件时出现，现均已清除 |
| 对话框 | 正常：底部深色框 + 白色旁白/台词 + 右上角快讯菜单（回想/回退/快进/自动/存档/设置），见 `preview\004_n00150.png`、`t750.png` |
| 立绘 | 正常：蓝羽（白狼，双刀）、白砚（白虎，药箱）、青岩（绿龙，样本箱）位置与缩放都对，双人同框不打架（`t750.png`） |
| 好感提示 | 正常：左上角 `蓝羽 +3` / `白砚 +2` toast 会弹（`t750.png`、`004_n00150.png`） |
| 章节标题卡 | **没能截到成帧画面**：抓到的 `001_ch25_title` / `001_ch26_title` 两帧都是纯黑转场帧。进章调用（`vn2_title_card`）每次都执行且无报错，但“第 N 章 / 标题”那张卡长什么样，本轮没有画面证据；你上一轮给的截图里它是正常的（“第 3 章 / 断崖”）。 |
| 章节切换后的场景/旁白 | 正常：逐章入口帧背景、环境光、旁白都在（`002_ch01_entry.png` … `034_ch28_entry.png`）；ch27 帧内文案「第 26 天。雾还没全散，但天是亮的。」 |
| 选择 menu | 正常显示，C 批新增的 ch02「今晚扎在哪一处？」三选项在实机里正确弹出（`004_n00150.png`，该帧为淡入瞬间，选项文字偏淡属截图时机，不是样式问题） |
| 结局提示 | 正常：进入结局章时左上角弹「结局：第七天」（`033_ch27_entry.png`） |
| **名字牌（角色名牌）** | **本轮没能截到可信特写**——自动驱动推进时抓到的多是旁白帧，未取得“蓝羽 / 白砚 / 青岩”开口说话那一帧。你上一轮给的截图里名牌处有缺字方框（「蓝羽 ☒ 向导」）的问题，**本轮未复验**，需下次人手试玩或补一次定点截图确认 |
| 音乐/音效 | 未验（无头/自动跑不判断听感） |

## 5. 27/28 口径

实机读到的文案与文档一致：
- ch27 章内：**「第 26 天」**（不是 27 天），截图 `033_ch27_entry.png` 旁白原文「第 26 天。雾还没全散，但天是亮的。」。
- ch28 进章帧旁白「人还在。只是有些东西从这一天起，回不去了。」（`034_ch28_entry.png`）；章节页显示「后日谈」这一点由 `vn2_title_card(28, "后日谈", ...)` 保证，但**那张卡本轮没抓到成帧截图**（见 §4）。
- ch26 内无「二十七天」字样。

## 6. 时长观感

- 自动跑（无阅读时间）：整条周目约 3 分钟跑完（引擎推进计数从 @1 走到 @1728 进 ch28）。
- 玩家实际时长：按 C 批单周目 71,773–72,126 汉字估算，**@200 字·分 ≈ 6.0h，@240 字·分 ≈ 5.0h**；实机没有“读多久”的客观读数，这两个数仍是字数换算，不是实测钟点。

## 7. 未完成 / 未覆盖（明确记录）

1. **人手鼠标试玩未做**（环境不支持桌面控制）。
2. **名字牌缺字方框未复验**（见 §4）。
3. **手动存档/读档页面操作未验**（只验了 autosave 写入 + autoload 续跑）。
4. 音频、CG 全屏展示、回想/历史界面、设置页未逐项操作验证。
5. 本章实机只走了一条路线（蓝羽）；白砚线（ch19–21）与青岩线（ch22–24）的**逐章实跑**没有做（结局 key 用场景法覆盖了，但路线章节正文只经 lint 与文本通读）。
