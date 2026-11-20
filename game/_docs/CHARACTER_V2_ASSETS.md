# 角色立绘 V2 交付记录

日期：2026-11-17
来源：`D:\Desktop\VN2_表情差分_打标` / `D:\Desktop\VN2_表情差分_打标.zip`

## 一、收到什么

- 6 个角色 × 6 个表情 = 36 张 PNG。
- 原始尺寸 1024×1024，RGBA 透明底。
- 同一角色的六个表情 alpha 边界一致，只有面部表情变化，适合做差分。

## 二、归一化结果

- 输出目录：`game/images/chars/v2/`
- 尺寸：1256×1616 RGBA，透明底，脚底对齐、底部居中。
- 共 36 张，文件名格式：`<key>_<expr>.png`

角色映射：

| 中文名 | 内部 key | 物种 |
|---|---|---|
| 老周 | `zhou` | 灰狼 |
| 蓝羽 | `lan` | 蓝狼 |
| 白砚 | `bai` | 白虎 |
| 青岩 | `qing` | 青龙 |
| 阿瑞 | `arui` | 红狐 |
| 十七 | `shiqi` | 黑豹 |

表情名：

`neutral` / `happy` / `sad` / `angry` / `shy` / `surprised`

示例：

```text
game/images/chars/v2/zhou_neutral.png
game/images/chars/v2/zhou_happy.png
game/images/chars/v2/lan_sad.png
game/images/chars/v2/shiqi_surprised.png
```

完整清单和每张的缩放参数见 `game/images/chars/v2/manifest.json`。

## 三、运行时接入约定

- 本轮剧情执行线会把 `40_cast.rpy` 的 `image` 定义切到 V2 路径。
- 新图是干净透明底，不再使用 `AlphaMask` / `sprite_feather`。
- 老周的基础图指向 `zhou_neutral.png`，其余表情用 `zhou happy`、`zhou sad` 等 image 名。
- 阿瑞、十七要补进 `VN2_CAST`、`Character` 与 `image` 声明；他们只做 NPC，不进恋爱/结局判定。
- 旧的 `game/images/chars/wolf_grey.png`、`wolf_blue.png`、`tiger_white.png`、`dragon_green.png` 保留作备份，不删除。
- CG 空白占位路径 `game/images/cg/cg_*.png` 不要覆盖；正式 CG 到位后单独替换。
