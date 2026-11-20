# 《雾线》VN2 角色语音接入记录（Round 8）

生成日期：2026-11-17
工程：`L:\AI\FurryVN\20261117_uidemo`
引擎：Ren'Py 8.5.3

## 一、范围与成品

本轮为 5 名可发声角色生成全库角色对白语音，玩家/老周不配音，旁白不配音。

| 角色 key | 角色 | 句数 | OGG 总时长 | OGG 体积 |
|---|---:|---:|---:|---:|
| `lan` | 蓝羽 | 162 | 8.06 分钟 | 2.74 MB |
| `bai` | 白砚 | 132 | 6.23 分钟 | 2.18 MB |
| `qing` | 青岩 | 98 | 5.53 分钟 | 1.94 MB |
| `ari` | 阿瑞 | 6 | 0.40 分钟 | 0.15 MB |
| `shiqi` | 十七 | 14 | 0.79 分钟 | 0.29 MB |
| **合计** |  | **412** | **21.02 分钟** | **7.65 MB** |

- 游戏内路径：`game/voice/{key}/{key}_{index:04d}.ogg`
- 命名：按角色独立从 `0001` 连续编号，编号与 `voice_map.json` 一一对应。
- 格式：OGG Vorbis，24 kHz，单声道；逐条峰值归一化到约 -0.45 dBFS。
- 原始 WAV 源文件保留在 `_voice_source_wav/{key}/`，不随游戏打包。
- 生成方式：BreezeTTS 2 本地常驻服务，`clon` 任务，5 个已确认锚点作 `voice_ref`，锚点原文作 `reference_text`，各角色固定 `instruct` 与 `seed=0`。
- 实测：412 句全部成功，0 失败；服务端合成总耗时约 39 分钟（含换角色时重新准备参考音色）。

## 二、游戏接入

1. 在 26 个 `game/story/*.rpy` 文件中，为 412 句角色对白插入了：
   ```renpy
   $ vn2_current_voice = "voice/lan/lan_0001.ogg"
   voice "voice/lan/lan_0001.ogg"
   lan "……"
   ```
   共 412 条 `voice` 语句、412 条 `vn2_current_voice` 赋值，均与对白同缩进，未改变对白文本和显示文本。
2. `game/core/50_audio.rpy` 的 `vn2_history_voice` 改为属性赋值，并只在蓝羽/白砚/青岩/阿瑞/十七的台词上挂语音；旁白与玩家/老周不挂，避免回想里把上一句角色语音误挂到旁白。
3. 回想界面已有 `Play("voice", h.voice)` 重播位；现在 `h.voice` 是实际 OGG 路径。
4. `config.has_voice = True` 沿用工程原设置。

## 三、质检结果

- Ren'Py lint：**0 error / 0 warning**；3,302 dialogue blocks / 107,021 characters / 87 menus / 62 images / 52 screens。
- Ren'Py 载入检查：**412 个 OGG 全部 `renpy.loadable` 成功，missing=0**。
- 音频结构检查：412/412 为 24 kHz 单声道 PCM 源，OGG 转换后全部可解码；最短 0.96 秒，最长 8.16 秒，无空文件、无静音异常。
- 未做：逐句人耳复听；完整周目带语音实机试听；跳过/回退时语音截断的手感复验。

## 四、已知限制

1. **3 句含 `[player_name]` 的台词**：`story/ch06.rpy:16`、`story/ch16.rpy:194`、`story/endings.rpy:37`。游戏显示仍保留玩家自定义名，TTS 文本按默认名读作“队长”。若玩家改名，这 3 句音频与显示名会不完全一致。需要时可只重做这 3 句，按实际玩家名生成多版本。
2. **玩家/老周 59 句不配音**；旁白不配音；这两类是刻意排除，不是漏生成。
3. **全库 412 句覆盖分支台词**，单周目只会听到其中一部分；`ari` 仅 6 句，`shiqi` 14 句。
4. 语音为本地 BreezeTTS 2 非商用权重生成；商业发行仍需授权或换官方 API。
5. 本轮没有删除或改写任何角色对白；只插入语音语句和修正回想回调。

## 五、文件

- 语音成品：`game/voice/{lan,bai,qing,ari,shiqi}/*.ogg`
- 对白到音频映射：`game/_docs/voice_map.json`
- 载入检查记录：`game/_docs/VOICE_LOAD_CHECK.txt`
- WAV 源：`_voice_source_wav/{lan,bai,qing,ari,shiqi}/*.wav`
- 生成脚本：workspace `run_voice_server.py`、`convert_voice_ogg.py`、`insert_voice_statements.py`
- 备份：`_backup_voice_20261117_2145`（接入前的 `story/` 与 `50_audio.rpy`）
