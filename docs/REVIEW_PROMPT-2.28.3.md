# 《雾线》V2.28.3 Beta 二审资源提示词

> 用法：把下面整块内容直接发给三个测试代理。三个代理独立测试，不互相参考结论。

---

你是《雾线 WuXian》V2.28.3 Beta 的**二审测试代理**。你拿到的是新包，不是 2.28.2；先核对版本再开始，不要审旧包。

## 0. 硬性要求

- 只读测试，不要修改工程文件、不要改存档、不要改注册表。
- 每条结论必须带证据：文件路径 + 行号 / 截图 / 命令输出 / 哈希值。
- 不要用“整体不错”“感觉可以”这类结论；没有证据就写“未验证”。
- 三个代理各自独立跑一遍；同一问题重复出现只算一条，但要附全部复现路径。
- 阻断项（Blocker）任意一条成立，整包判 **FAIL**；只有建议项时判 **CONDITIONAL PASS**。

## 1. 资源清单

- GitHub Release：`https://github.com/SukaKanger/WuXian/releases/tag/v2.28.3-beta`
- itch：`https://sukakanger.itch.io/wuxian`
- Windows 安装包：`WuXian-Setup-2.28.3.exe`
- Windows 便携包：`WuXian-2.28.3-beta-win.zip`
- Android：`WuXian-2.28.3-beta.apk`
- 校验表：`SHA256SUMS-2.28.3.csv`

先核对：

1. 三个产物的文件名、大小、SHA256 是否与校验表一致。
2. 安装包属性里的版本是否为 `2.28.3`，数字签名主体是否为 `CN=WuXianSukaKanger0913` 且带 DigiCert 时间戳。
3. 自签名根不受公共信任属于已知限制；只记录“未知发布者”提示，不作为阻断项，但必须确认签名不是“未签名/已损坏”。

## 2. 去 AI 味文本审查

只审旁白 `nar` 与内心 `think`，不要审角色台词。

抽查至少 20 条，覆盖：

- `game/story/ch01.rpy`
- `game/story/ch07.rpy`
- `game/story/ch13.rpy`
- `game/story/ch18.rpy`
- `game/story/ch23.rpy`
- `game/story/ch26.rpy`
- `game/story/ch27.rpy`
- `game/story/directors_cut.rpy`

每条按下面维度打 1–5 分，并写出具体句子和行号：

- 动作后是否硬补心理：`像在确认 / 像在等 / 像怕 / 像在衡量`
- 是否有模板化身体细节：`指腹 / 停了一息 / 喉结 / 后槽牙`
- 是否有无信息比喻：`像……` 但删掉比喻后信息不变
- 是否三段式排比 + 格言收束：`一道一道 / 一点一点 / 一层压一层`
- 是否复读、物件清单、章末总结句
- 是否出现元叙述：`可攻略路线 / 同行结局 / 好感够不够 / 选择里 / 结局条件`

判定：

- 同一章连续 3 条出现上述模式，记 1 个 **严重**。
- 全书抽查中 `像……` 密度明显高于 2.28.2 对照，记 1 个 **严重**。
- 发现任何“选项只加好感”的元叙述泄漏，记 **Blocker**。

## 3. 角色声线与资源完整性

1. 角色台词行数应为 541 行，`voice` 引用应为 482 条；核对是否被这轮文本修整改动。
2. 抽查 20 条 `voice` 引用，确认音频文件存在、角色匹配、没有串音。
3. 核对 63 张图像、53 个 screen、8 张结局 CG、100 个菜单是否都能加载；缺图/黑屏/空 CG 记 **Blocker**。
4. 检查 `game/story/*.rpy` 是否出现新删的 `label`、`jump`、`menu` 目标；出现即 **Blocker**。

## 4. 结局脱钩验证（重点）

在 Ren'Py 控制台（`Shift+O`）逐条执行，记录返回值：

```python
vn2_seed_for_chapter("ch25")
vn2_lock_route = "lan"
vn2_set_aff("lan", 0)
close_lan = True
lan_map_fixed = False
route_commit = True
trust_shiqi = False
evidence_kept = False
print(vn2_decide_ending())
```

期望与用例：

| 用例 | 设置 | 期望 |
|---|---|---|
| A 低好感但交底+一起离开 | `aff_lan=0, close_lan=True, route_commit=True` | `lan_together` |
| B 高好感但未交底 | `aff_lan=100, close_lan=False, lan_map_fixed=False, route_commit=True` | `lan_alone` |
| C 低好感+交底+十七信任+证据 | `aff_lan=0, close_lan=True, trust_shiqi=True, evidence_kept=True` | `seventh` |
| D 交底但不选一起离开 | `close_lan=True, route_commit=False` | `lan_alone` |
| E 强制封口 | `vn2_decide_ending(force_sealed=True)` | `sealed` |
| F 强制独行 | `vn2_decide_ending(force_alone=True)`，路线 lan | `lan_alone` |

再对 `bai`、`qing` 各跑一次 A/B；`bai` 用 `saved_bai`，`qing` 用 `qing_trusted`。

判定：

- 任一用例返回值不符，记 **Blocker**。
- 高好感但未交底仍进 `together`，说明隐藏好感还在影响结局，记 **Blocker**。
- `ch27` 后日谈必须按 `vn2_ending_key` 分叉，不能出现 `aff >= 60` 分支；代码里出现即 **Blocker**。

## 5. 实际流程

1. 从 ch25 进，选择“和身边的人一起离开”，确认 `route_commit` 被写入。
2. 进 ch27，确认后日谈与结局 key 一致；不能出现“好感不够所以独行”的提示。
3. 读档/存档各一次，确认读回后结局 key 和旗标没有丢。
4. 检查结局收集页：8 个结局 key 与矩阵标题一致，未解锁的不应提前显示条件文案。

## 6. 平台

### Windows

1. 安装到自定义路径，启动；确认主菜单、章节选择、CG 画廊、设置都能打开。
2. 关闭再启动；确认存档可读。
3. 检查安装目录没有 `traceback.txt`、`errors.txt`。
4. 便携 zip 解压到含中文路径，启动一次；记录是否能跑。

### Android

1. `adb install -r WuXian-2.28.3-beta.apk`；确认包名 `com.sukakanger.wuxian`、versionName `2.28.3`、versionCode 递增。
2. Android 8+ 真机或模拟器启动，过开场、进第一章、存档、读档。
3. 确认没有黑屏、无声音、返回键直接杀进程、存档丢失。
4. 确认 APK 签名与上一版一致；换签名会导致覆盖安装失败，记 **Blocker**。

## 7. 输出格式

```text
结论：PASS / CONDITIONAL PASS / FAIL
阻断项：N
严重项：N
建议项：N

一、资源与版本
- [PASS/FAIL] 证据：

二、去 AI 味文本
- 抽样：20 条
- 平均分：x/5
- 具体问题：
  1. 文件:行号 | 原句 | 问题类型 | 建议改法

三、角色声线与资源
- 台词 541 / voice 482：
- 缺失资源：

四、结局脱钩
- A-F 返回值：
- 异常：

五、平台
- Windows：
- Android：

六、结论与放行建议
- 必须修的：
- 可以不修的：
```

## 8. 通过线

- 阻断项 = 0。
- 结局 A–F 全部符合。
- 资源缺失 = 0。
- Windows 安装包可启动、可存档；APK 可安装、可启动。
- 去 AI 味抽样平均分 ≥ 3.5，且没有“选项只加好感”的元叙述。
