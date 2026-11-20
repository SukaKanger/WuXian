# ROUND3 · 音频打磨记录（返回音重做 + 打字音系统）

> 范围：只重做 `back.wav`、新增三个打字 tick、新增打字音接线文件；其余五件界面音
> （click / hover / confirm / page / save）参数一个未改，复跑后字节大小与基线一致。
> **本轮未跑 Ren'Py 实跑开窗、未截图，全部音效仍未经过人耳试听**；下列数字均为
> 程序化回读测量（44.1 kHz / 16bit / 立体声 WAV，双声道均值），听感需收尾环节人耳复核。

## 1. 改动文件清单（绝对路径）

| 文件 | 动作 |
| ---- | ---- |
| `L:\AI\FurryVN\20261117_uidemo\_tools\make_ui_sfx.py` | 重写：back 重做、新增 type_1/2/3、内置回读测量；五件界面音生成参数未改 |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\back.wav` | 重做覆盖 |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\type_1.wav` | 新增 |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\type_2.wav` | 新增 |
| `L:\AI\FurryVN\20261117_uidemo\game\audio\ui\type_3.wav` | 新增 |
| `L:\AI\FurryVN\20261117_uidemo\game\ui2\95_typing.rpy` | 新建：通道注册、全局回调、ATL ticker、音量跟随、打断收声 |
| `L:\AI\FurryVN\20261117_uidemo\lint_check_audio.txt` | lint 报告（0 error） |

未改动：say 屏组织结构、quick_menu、history 回想、story 正文 ch01–ch28、
`game/gui/` 资产与字体；未触碰其他 agent 正在改的
`50_gallery.rpy / 30_saveload.rpy / 20_mainmenu.rpy / 85_loading.rpy / 80_about.rpy / 25_name_picker.rpy / options.rpy`。

## 2. back 返回音：新旧对照

### 2.1 对照表

| 指标 | 旧 back（重做前实测） | 新 back（重做后实测） | 硬指标 | 达标 |
| ---- | ---------------------- | ---------------------- | ------ | ---- |
| 时长 | 0.380 s | **0.210 s** | ≤0.25s（目标 0.20–0.22s） | ✅ |
| 峰值 | -15.2 dBFS | **-17.1 dBFS** | -16 ~ -18 dBFS | ✅ |
| RMS | -22.5 dBFS | **-25.3 dBFS** | 记录项（更柔更轻） | ✅ |
| 基频 f0 | 255.7 Hz（中段 FFT；设计为 330→196 下行） | **149.7 Hz**（固定 155Hz） | 140–170 Hz | ✅ |
| attack | 12.7 ms（旧口径：10%→90% 上升沿） | **20.3 ms**（onset→峰值，包络斜坡 28ms） | 20–30 ms | ✅ |
| 有无滑音 | **有**：330→196Hz 明显下行，drift 36.8%；0.16s 处再叠 196Hz 低八度余韵 | **无**：固定音高，drift **0.0%** | 无滑音，漂移 ≤5% | ✅ |
| 2 次谐波 h2 | 0.16 | **0.16** | ≤0.25 | ✅ |
| 3 次谐波 h3 | 0.03 | **0.02** | ≤0.08 | ✅ |
| 低通截止 | 2.4 kHz（主音）/ 1.8 kHz（余韵） | **1.5 kHz** | ≤1.6 kHz | ✅ |
| 噪声瞬态 | 无 | **无** | 不加噪声瞬态 | ✅ |
| 尾部处理 | 长余韵（0.24s 低八度叠音） | **指数衰减 + 末尾 35% 长度平滑淡出**；首末样本 = 0，无削波 | 指数衰减到静音、尾段淡出、首尾贴近 0 | ✅ |

> attack 口径说明：旧值来自重做前的临时测量脚本（10%→90% 上升沿）；新值为本轮
> 脚本统一口径「首次过 10% 峰值 → 峰值样本（onset-to-peak）」。包络起音斜坡
> 设计值 28ms，落在 20–30ms 区间内。

### 2.2 新 back 合成参数（`_tools/make_ui_sfx.py` `make_back`）

- 基频 155Hz 固定（无 f1 滑音参数）；谐波 `(1.0, 0.22, 0.06)`；低通 1.5kHz。
- attack 28ms，指数衰减 decay 7.0；时长 0.21s；末尾 35% 长度线性淡出。
- 峰值归一化到 -17.0 dBFS；无 `noise_tick` 叠音。
- 音色基底与其余五件同一套：正弦基音 + 谐波 + FFT 低通 + 指数包络 + 首尾淡出，
  峰值区间 -13 ~ -18 dBFS，整组仍是一套而不是拼素材。

### 2.3 其余五件复跑测量（参数未改，仅记录一致性）

| 文件 | 时长 | 峰值 | RMS | f0 | 与基线 |
| ---- | ---- | ---- | ---- | -- | ------ |
| click.wav | 0.130 s | -14.4 dBFS | -21.5 dBFS | 923.3 Hz | 一致 ✅ |
| hover.wav | 0.090 s | -17.5 dBFS | -24.2 dBFS | 1174.7 Hz | 一致 ✅ |
| confirm.wav | 0.300 s | -13.3 dBFS | -24.4 dBFS | 657.1 Hz | 一致 ✅ |
| page.wav | 0.240 s | -15.8 dBFS | -27.2 dBFS | 512.0 Hz | 一致 ✅ |
| save.wav | 0.260 s | -14.4 dBFS | -24.0 dBFS | 989.0 Hz | 一致 ✅ |

五件复跑后文件字节大小与重做前基线逐一相同（22976 / 15920 / 52964 / 42380 / 45908）。

## 3. 打字 tick 三变体参数表

### 3.1 合成参数（`make_type(variant)`，同一基底，仅细微差别）

| 变体 | 设计基频 | 衰减 decay | 增益 | 谐波 | 低通 | onset 噪声 |
| ---- | -------- | ---------- | ---- | ---- | ---- | ---------- |
| type_1 | 1040 Hz | 26 | 0.50 | (1.0, 0.18, 0.05) | 3.0 kHz | 3ms 带通 1.8–3.8kHz，增益 0.07 |
| type_2 | 1085 Hz | 30 | 0.48 | (1.0, 0.18, 0.05) | 3.0 kHz | 同上 |
| type_3 | 1130 Hz | 34 | 0.46 | (1.0, 0.18, 0.05) | 3.0 kHz | 同上 |

### 3.2 回读测量

| 文件 | 时长 | 峰值 | RMS | 实测 f0 | attack | drift | h2 | h3 |
| ---- | ---- | ---- | ---- | ------- | ------ | ----- | -- | -- |
| type_1.wav | 0.040 s | -24.4 dBFS | -31.4 dBFS | 1072.1 Hz | 1.4 ms | 0.0% | 0.10 | 0.01 |
| type_2.wav | 0.040 s | -24.4 dBFS | -31.8 dBFS | 1072.1 Hz | 1.4 ms | 0.0% | 0.14 | 0.02 |
| type_3.wav | 0.040 s | -24.4 dBFS | -32.1 dBFS | 1143.6 Hz | 1.8 ms | 0.0% | 0.13 | 0.02 |

达标核对：

- 时长 0.03–0.05s：三件均 **0.040s** ✅
- 峰值 -22 ~ -26 dBFS：三件均 **-24.4 dBFS**（明显轻于界面音 -13 ~ -17）✅
- 三变体同族，仅基频 / 衰减 / 增益细微差别；播放时 `renpy.random.choice` 随机轮换，
  避免机关枪感 ✅
- 实测 f0 与设计值的小偏差来自 40ms 短帧 FFT 频率分辨率（约 25Hz/ bin），非音高漂移。

## 4. 接线点清单（文件 : 行号）

新建文件：`game\ui2\95_typing.rpy`（`init offset = 1`）

| 行号 | 接线点 | 说明 |
| ---- | ------ | ---- |
| L27–29 | `renpy.music.register_channel("vn2_type", mixer="sfx", loop=False, stop_on_mute=True)` | 专用通道；mixer 接 **sfx**；不循环；静音时收声 |
| L31–35 | `VN2_TYPE_TICKS` | 三个 tick 变体相对路径表 |
| L38 | `vn2_type_interval = 0.30` | ticker 循环间隔初值，每句按 cps 重算 |
| L41–53 | `vn2_type_allowed()` | 守卫：`renpy.is_skipping()` / `config.skipping == "fast"` / `text_cps <= 0` 任一成立即禁播 |
| L56–65 | `vn2_type_stop()` | 停通道 + 隐藏 ticker 屏，幂等可重复调用 |
| L68–78 | `vn2_type_tick(trans, st, at)` | ATL function 块：每循环一次随机播一个变体；不满足条件静默空转 |
| L81–87 | `vn2_type_start()` | 间隔 = `3 / cps`，夹逼 0.06–0.60s；`show_screen("vn2_type_ticker", _transient=True)` |
| L90–101 | `vn2_type_cb(event, interact, **kwargs)` | 全局角色回调：`begin` 清残留；`show`（且 interact 且 allowed）启动；`slow_done / interact_done / end` 停声收屏 |
| L104–105 | `config.all_character_callbacks.append(vn2_type_cb)` | 注册全局回调（8.5.3 无 `typing_sound`，角色自身 callback 由 character.py 合并） |
| L108–109 | `config.fast_skipping_callbacks.append(vn2_type_stop)` | Ctrl 快进起步即停兜底（fast skip 路径不走 say 回调） |
| L116–118 | `screen vn2_type_ticker()` | 不可见 ticker 屏；间隔以 transform 参数传入 |
| L121–124 | `transform vn2_type_ticker_atl(interval)` | ATL：`function vn2_type_tick` → `pause interval` → `repeat` |

音量滑杆链路核对：

- `game\ui2\40_preferences.rpy:162`：音效滑杆 `Preference("sound volume")`。
- SDK 映射 `renpy\common\00preferences.rpy:625`：`"sound" : "sfx"`，即该滑杆控 **sfx** mixer。
- 本通道 `mixer="sfx"`，因此滑杆拉到 0 打字音无声，推动时实时跟随；与既有
  `game\core\50_audio.rpy:14` 的 `ambient` 通道同一 mixer。

## 5. 节奏、打断与静音逻辑

- **节奏**：间隔 = `3 / cps`，cps 取 `renpy.game.preferences.text_cps`（当前实际文字速度）；
  夹逼 0.06–0.60s，极端速度下既不机关枪也不拖拍。
- **触发时机**：仅在角色回调 `show` 事件、`interact=True` 且 `vn2_type_allowed()` 为真时启动；
  `slow_done`（逐字打完）、`interact_done`（交互结束）、`end`（台词结束）立即停；
  `begin` 先清上一句残留。
- **不出声的情形**：`text_cps <= 0`（瞬时文本）、`renpy.is_skipping()` 为真、
  `config.skipping == "fast"`、非交互行（`interact=False`）。
- **打断收声**：点击继续 / 空格、Ctrl 快进、auto 自动前进、AFM、退出对话或打开菜单，
  都会结束交互触发 `interact_done`/`end` → 停通道 + 收屏；通道 `loop=False`，
  单次播放不循环；`fast_skipping_callbacks` 兜底快进起步即停。
- **实现重量**：触发由不可见 ticker 屏 + ATL `function / pause / repeat` 循环完成；
  未在 `render()` 里每帧跑 Python，未用 `sleep` / `renpy.pause` 轮询。
- **回想（history）**：未改 history 屏与 `history_callbacks`；回想重播不走 say 交互，
  `interact` 守卫下不会起 tick。

## 6. 进游戏后人耳验证步骤（待收尾环节执行）

> 前置：设置 →「文字速度」调到非 0（建议 20–30 cps）；「音效 / 环境音」滑杆先置中。

1. **慢速文本**：进入剧情，看一句逐字打出的长台词。
   - 预期：每隔约 `3 / cps` 秒一记轻短 tick，三个音色细微轮换；文字打完 tick 即停，
     等待点击期间不再响。
2. **Ctrl 快进**：打字过程中按住 Ctrl。
   - 预期：tick 立刻停，不残留、不把后续循环放出来；松开后新台词按规则判断是否起 tick。
3. **自动前进（auto）**：点对话框右上角「自动」。
   - 预期：打字期间有 tick；打完等待自动翻页期间无 tick；翻到下一句重新起。
4. **AFM**：让长文本触发 AFM 等待。
   - 预期：逐字打字期间有 tick；AFM 停留等待期间无 tick。
5. **点继续打断**：打字中途点击鼠标 / 按空格。
   - 预期：立刻停声，当前 tick 之后不再循环，不与 BGM 抢。
6. **音效滑杆到 0**：设置 →「音效 / 环境音」拉到 0。
   - 预期：打字音无声；推回滑杆后实时恢复，无需重启。
7. **返回音**：在任一菜单点返回 / 后退。
   - 预期：短、柔、低频的收束音；**没有** 330→196 那种下行滑音，没有「啵嘤」拖尾。
8. **瞬时文本**：设置 →「文字速度」调到 0。
   - 预期：台词瞬间显示，全程无 tick。

## 7. lint 结果

- 命令（任务指定）：`"D:\renpy-8.5.3-sdk\renpy.exe" "L:\AI\FurryVN\20261117_uidemo" lint > lint_check_audio.txt`
- 本机实测：`renpy.exe` 启动器派生子进程后不回传 stdout（重定向文件 0 字节；第二次运行
  退出码 `0xC0000005` 访问冲突）。改用 SDK 自带 Python 直调等价入口：
  `D:\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe D:\renpy-8.5.3-sdk\renpy.py <project> lint`，
  报告写入同一文件 `lint_check_audio.txt`。
- 结果：**EXIT=0，报告无 error / warning**；统计 50 screens（含新增 `vn2_type_ticker`）。
- 其他 agent 正在改的文件本轮未触碰；本次 lint 报告中未出现落在那些文件上的报错。

## 8. 未达标 / 待确认项

- **人耳试听：未做。** 本轮仅完成程序化合成、回读测量与 lint；back 的「自然 / 不啵嘤」、
  tick 的「木质纸感 / 不机关枪」、三变体轮换听感，均需按 §6 步骤进游戏人耳复核。
- 短帧 FFT 频率分辨率有限（40ms tick 约 25Hz/bin），tick 实测 f0 与设计值存在 ±1 个 bin
  的偏差，已在 §3.2 标注；不影响达标判定。
- `renpy.exe` 启动器在本机的 stdout 回传 / 偶发访问冲突问题未排查（与本任务代码无关），
  lint 以 SDK Python 直调结果为准。
