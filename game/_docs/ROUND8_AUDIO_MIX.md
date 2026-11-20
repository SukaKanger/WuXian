# VN2 音频混音与设置页修正（2026-11-17）

## 一、问题定位

不是“语音没接进去”，是 **BGM 本身电平明显高于语音**：

| 音轨 | 实测 RMS |
|---|---:|
| `common.mp3` | **-12.0 dBFS** |
| `station.mp3` | -16.4 dBFS |
| `route_qing.mp3` | -17.1 dBFS |
| `route_zhou.mp3` | -18.7 dBFS |
| `route_lan.mp3` | -22.2 dBFS |
| `route_bai.mp3` | -23.3 dBFS |
| `ending.mp3` | -22.2 dBFS |
| 角色语音样本（蓝羽/白砚/青岩） | -17.8 / -16.3 / -20.4 dBFS |

`common.mp3` 比语音高约 4–6 dB，而且它此前承担 ch01–ch15 的通用线 BGM；这就是“角色在说话，但被音乐压住”的直接原因。

## 二、改动

### 1. 通用线换曲

`core/50_audio.rpy` 的 `VN2_BGM["common"]` 从 `common.mp3` 改为 `station.mp3`。

依据是工程自己的记录：`ROUND4_feedback.md` 已写明 `common` “偏紧张”，主菜单曾特意换成更平缓的 `station.mp3`。原曲保留为 `common_tense`，没有删除，随时可以换回。

### 2. 全局限定，不再额外按曲目压电平

`VN2_BGM_LEVEL` 改为空表。音乐默认降到 0.35 后，不需要再叠加通道增益，否则设置页显示 35、实际更低。

原音频没有重编码；`common.mp3` 保留为 `common_tense`，需要时可以换回。

### 3. 语音时自动 duck

- `config.default_emphasize_audio = True`
- `config.emphasize_audio_volume = 0.75`（按 Ren'Py 的 dB 换算，约等于降到 18%）
- `config.emphasize_audio_time = 0.35`

角色语音一开始播放，音乐和其他非 voice 通道自动退到约 18%；语音结束后 0.35 秒恢复。设置页保留开关，玩家可以关掉。

### 4. 默认音量与老存档迁移

- 新玩家默认：**语音 0.90、音乐 0.35、音效 0.35**。
- 已有 persistent 的玩家由 `core/50_audio.rpy` 的一次性迁移处理：一次性写入语音 0.90、音乐 0.35、音效 0.35，并打开 `emphasize_audio`。
- 迁移只执行一次，之后玩家自己的调整不会被重置。

### 5. 设置页

- “语音（本作暂无语音，仅保留通道）”改为 **“语音（角色对白已接入）”**。
- 新增 **“试听语音”**，直接播放 `voice/lan/lan_0001.ogg`。
- 新增 **“角色说话时自动压低音乐”** 开关，默认开，显示“开：音乐自动退到约 18%”。
- `config.sample_voice` 指向蓝羽第一句，拖动语音滑杆时也有试听样本。

## 三、验证

- Ren'Py lint：**0 error / 0 warning**；3,302 dialogue blocks / 107,021 characters。
- 实机截图：设置页已显示新文案、试听按钮、自动压低开关；三条滑杆可正常显示。
- 引擎内音频探针：`vn2_bgm("common")` 实际加载 `audio/bgm/station.mp3`，music 通道 `chan_volume=1.0`，`emphasize_audio=true`，语音滑杆 0.90，`voice/lan/lan_0001.ogg` 可载入。
- 未做：人耳试听新旧 BGM 的主观对比；实际周目里边听边确认 duck 的恢复速度。`common.mp3` 保留为 `common_tense`，可以随时 A/B。

## 四、涉及文件

- `game/core/50_audio.rpy`
- `game/options.rpy`
- `game/ui2/40_preferences.rpy`
- 备份：`_backup_audio_mix_20261117_2217`
