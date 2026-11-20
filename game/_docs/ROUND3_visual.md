# ROUND3 · 视觉改动记录（UI 三件事）

- 工程：`L:\AI\FurryVN\20261117_uidemo`（Ren'Py 8.5.3，虚拟 1920×1080，`ui2` 目录 `init offset = 1`）
- 范围：全站底板圆角、画廊六卡满幅缩略图、存档改 3×2 六槽。
- 约束遵守：未跑 Ren'Py（不 lint、不开窗、不截图）；未改 `game/gui/` 默认资产、`gui.init`、字体；未改 story 正文 ch02–ch28；未动 `90_motion.rpy` 动效参数；未碰 `audio/`、`images/bg/`、`20_mainmenu / 85_loading / 80_about / 25_name_picker / options.rpy`。

---

## 1. 圆角半径分级

蒙版做法：4 倍超采样画布上画圆角矩形蒙版 → LANCZOS 缩回原尺寸抗锯齿 → 蒙版 alpha 乘到原图 alpha；RGB 沿用旧图（颗粒 / 金边 / 内框线不动），**只切四角，不画圆角描边**。蒙版外缘振铃残量硬清零（mask < 16/255 置 0，成品 alpha < 8 置 0）。

| 分级 | 半径 | 资产 |
|---|---|---|
| 大卡（470×380、462×380 档） | **12 px** | `card.png` `card_empty.png` `card_hover.png` `gcard.png` `gcard_locked.png` |
| 中板（56–84 px 高） | **10 px** | `chap_row.png` `chap_row_hover.png` `row.png` `nav_idle.png` `nav_hover.png` `nav_pressed.png` `mbtn_idle.png` `mbtn_hover.png` |
| 小板（48 px 高） | **8 px** | `plate_idle.png` `plate_hover.png` `plate_selected.png` |
| 画廊缩略图 | **8 px** | `gthumb_cover_cg_*.png` ×4、`gthumb_empty.png` |

未处理（按要求排除）：`grain / vignette / fog_a / fog_b / scrim_left / veil_right / hairline / bar_* / scroll_* / logo_* / sprite_feather / dust / section / tb / name / shell / menu_shell / window_icon / tb` 等。

### 1.1 资产旧 / 新尺寸对照

| 文件 | 改前尺寸 | 改后尺寸 | 说明 |
|---|---|---|---|
| `card.png` | 470×240 | **470×380** | 按新存档槽位重烘（内嵌截图窗 / 分隔线同步），未拉伸旧图 |
| `card_empty.png` | 470×240 | **470×380** | 同上 |
| `card_hover.png` | 470×240 | **470×380** | 同上 |
| `gcard.png` | 462×380 | 462×380 | 仅 alpha 蒙版切角，尺寸不变 |
| `gcard_locked.png` | 462×380 | 462×380 | 仅切角 |
| `chap_row.png` | 322×56 | 322×56 | 仅切角 |
| `chap_row_hover.png` | 322×56 | 322×56 | 仅切角 |
| `row.png` | 800×64 | 800×64 | 仅切角 |
| `nav_idle.png` | 240×64 | 240×64 | 仅切角（细线板） |
| `nav_hover.png` | 240×64 | 240×64 | 仅切角 |
| `nav_pressed.png` | 240×64 | 240×64 | 仅切角 |
| `mbtn_idle.png` | 360×84 | 360×84 | 仅切角（细线板） |
| `mbtn_hover.png` | 360×84 | 360×84 | 仅切角 |
| `plate_idle.png` | 96×48 | 96×48 | 仅切角 |
| `plate_hover.png` | 96×48 | 96×48 | 仅切角 |
| `plate_selected.png` | 96×48 | 96×48 | 仅切角 |
| `gthumb_empty.png` | 426×272（RGB） | 426×272（**RGBA**） | 重烘：压暗模糊铺底 + 8px 圆角蒙版 |
| `gthumb_cover_cg_zhou/lan/bai/qing.png` | — | 426×272（RGBA） | 新增满幅 cover 缩略图 |
| `gthumb_bg_cg_*.png` ×4 | 426×272 | 426×272 | **磁盘保留，运行时已无引用** |
| `gthumb_fg_cg_*.png` ×4 | 426×272 | 426×272 | **磁盘保留，运行时已无引用** |

---

## 2. 画廊六卡满幅缩略图

### 2.1 几何一致性（六卡同一 xysize / 图区偏移 / 文字基线）

卡面 462×380；图区 426×272，相对卡面 `xalign 0.5`（即 x 偏移 18）、`ypos 15`；标题基线 `(32, 296)`；副标题右对齐、`xoffset -32`、`ypos 300`。

固定块 `xsize 1470`，左上角绝对坐标 `(375, 120)`（内容框宽 1580，块居中左偏 55；外框 top_padding 120）。

| 槽 | x（相对 fixed） | y（相对 fixed） | w | h | 绝对左上（预览实测） | 状态 |
|---|---|---|---|---|---|---|
| 1 | 0 | 46 | 462 | 380 | (375, 166) | cover `cg_zhou` |
| 2 | 504 | 46 | 462 | 380 | (879, 166) | cover `cg_lan` |
| 3 | 1008 | 46 | 462 | 380 | (1383, 166) | cover `cg_bai` |
| 4 | 0 | 454 | 462 | 380 | (375, 574) | cover `cg_qing` |
| 5 | 504 | 454 | 462 | 380 | (879, 574) | 未公开占位（`gthumb_empty`） |
| 6 | 1008 | 454 | 462 | 380 | (1383, 574) | 未公开占位（`gthumb_empty`） |

列间距 42：`462 + 42 = 504`；行间距 28：`380 + 28 = 408`，`46 + 408 = 454`。三列总宽 `3×462 + 2×42 = 1470`，左右对称。未解锁格与「未公开」占位共用同一图区几何与同一 8px 圆角 `gthumb_empty`。

### 2.2 缩略图裁切焦点（源图 + 裁切框）

源图均为 `game/images/chars/*.png`，1256×1616（RGB，立绘自带背景）。cover 缩放比 `s = 426/1256 ≈ 0.3392`，缩放后 426×548，纵向裁 272；焦点 `(fx, fy)` 为源图归一化坐标，出界自动夹紧，脸不切。

| id | 源文件 | 焦点 (fx, fy) | 缩放后 (w×h) | 裁切框 (left, top) | 输出文件 |
|---|---|---|---|---|---|
| `cg_zhou` | `chars/wolf_grey.png` | (0.45, 0.27) | 426×548 | (0, 12) | `gthumb_cover_cg_zhou.png` |
| `cg_lan` | `chars/wolf_blue.png` | (0.52, 0.26) | 426×548 | (0, 6) | `gthumb_cover_cg_lan.png` |
| `cg_bai` | `chars/tiger_white.png` | (0.55, 0.30) | 426×548 | (0, 28) | `gthumb_cover_cg_bai.png` |
| `cg_qing` | `chars/dragon_green.png` | (0.56, 0.20) | 426×548 | (0, 0) | `gthumb_cover_cg_qing.png` |

四张均已肉眼复核：耳朵 / 角 / 脸完整入框，胸口入镜，无切脸。

### 2.3 动效与运行时约束

- 保留原接线：`vn2_slide_left(delay)`、`vn2_lift()`、`vn2_stagger(idx, 0.05)` 未改。
- 全部裁切 / 圆角离线烘焙；运行时**未引入** `im.Crop` / `im.Scale`（8.5 会整格不渲染），`Transform(fit=...)` 仅保留在原有 `vn2_cg_view` 大图查看弹层。

---

## 3. 存档 3×2 六槽（回炉版：470×380）

### 3.1 真机截图实测、坐标算式与卡高依据

**证据化实测**（`shots/ui_03_save.png`，2433×1368，缩放 `s = 2433/1920 = 1.2671875`；扫描脚本 `_tools/measure_save_layout.py`，numpy 逐行统计边框色 / 金色像素）：

- 采样竖线：三卡列中心虚拟 x = 610 / 1110 / 1610（物理 773 / 1407 / 2040）；卡内条带虚拟 x 340–790。配色基准：页面底 `(7,10,8)`，面板 `(12,17,12)`，卡边框 `(46,51,38)`。
- ① **行1 卡上边缘**：物理 y=198 → 虚拟 **156.3**（边线 rgb(39,44,33)；上方 bg(9,13,10)；卡内 (9,15,9)）。
- ② **行3 卡下边缘**：物理 y=1149 → 虚拟 **906.7**（边线 rgb(51,56,43)；下方 bg(7,10,8)）。
- ③ **页码「1」按钮**（金色边框，x 虚拟 794.7–853.9）：上边缘物理 1274.5 → 虚拟 **1005.8**；下边缘物理 1328.5 → 虚拟 **1048.4**（底边线 rgb(200,168,106)；按钮内 (24,31,22)；下方 (5,8,6)）；按钮高 **42.6px**。
- 反推（旧代码 `ypos 26`）：`content_top = 156.3 − 26 = 130.3`；`content_bottom = 1048.4`；**`content_h = 918.1`**；按钮顶相对 content_top = **875.5**。
- 旧布局校验：旧 `3×240 + 2×16`、`ypos 26` 模型行3 底 rel 778 → abs 908.3，实测 906.7，偏差 1.6px（AA 容差），实测模型成立。

**卡高反推**（实测 content_h，净空目标 32–56px）：

- 行2 底 rel = `t + 2H + GY`；净空 = `875.5 − (t + 2H + GY)`。
- 取 `t=36`、`GY=24`：净空 ∈ [32,56] → `379.8 ≤ H ≤ 391.8`；与 340–380 上限相交 → **H=380**（区间内唯一可取整值），实测净空 **55.5px**。H 降到 378 时净空 59.5 >56，故不收行 ypos / 行距。
- 槽位 `VN2_SLOT_W=470`、`VN2_SLOT_H=380`；列间距 `VN2_SLOT_GAP_X=30`；行间距 `VN2_SLOT_GAP_Y=24`；截图窗 `VN2_SLOT_THUMB=(300,169)`（16:9）。
- 列 x（相对 fixed）：`x_c = c × (470 + 30) = 0 / 500 / 1000`；`3×470 + 2×30 = 1470`，块宽等于内容宽，左右边距对称。
- 行 y（相对 fixed）：`y_r = 36 + r × (380 + 24) = 36 / 440`；行 2 底 `= 440 + 380 = 820`。
- 净空：按钮顶 rel 875.5 − 行2 底 820 = **55.5px**（∈ 32–56），不出滚动条、不被条压住。
- 副标题 `vn2_small` 18px，`ypos -14`，行底 ≈ rel 8；行1 卡顶 rel 36，二者净空 **28px**（≥28 要求）。
- 自动存档页仍 **5 槽**：`count = 5 if is_auto else 6`，第 6 格 `null`（不画残卡）；翻页条保留 `< / 自动 / 1–9 / >` 与 `FilePage / FilePagePrevious / FilePageNext` 原交互。

| 槽 | x_rel | y_rel | w | h | 绝对左上（content_top=130.3） | 状态 |
|---|---|---|---|---|---|---|
| 1 | 0 | 36 | 470 | 380 | (375, 166.3) | loaded 占位 |
| 2 | 500 | 36 | 470 | 380 | (875, 166.3) | loaded 占位 |
| 3 | 1000 | 36 | 470 | 380 | (1375, 166.3) | loaded 占位 |
| 4 | 0 | 440 | 470 | 380 | (375, 570.3) | 空槽位 |
| 5 | 500 | 440 | 470 | 380 | (875, 570.3) | 空槽位 |
| 6 | 1000 | 440 | 470 | 380 | (1375, 570.3) | 空槽位 |

### 3.2 卡内坐标（与重烘皮肤一一对应）

| 元素 | 坐标 / 尺寸 |
|---|---|
| 截图窗 | `(16, 18)`，300×169（16:9，contain 不变形） |
| 槽号（右上） | `(424, 16)` |
| 章节·路线（head） | `(332, 34)`，xmaximum 122，15px 金色 |
| 章名（body） | `(332, 74)`，xmaximum 122，23px |
| 玩家名（cname） | `(332, 116)`，xmaximum 122，13px |
| 分隔线 | `y = 232`，x 16 → 454 |
| 好感（caff） | `(16, 280)`，xmaximum 438 |
| 时间（FileTime） | 右对齐 `xoffset -16`，`ypos 330` |
| 空槽位标题 | `(332, 74)`，24px；提示副标 `(332, 116)`；空槽提示行 `(16, 280)` FAINT |

卡内纵向空白带（loaded 卡，H=380）：截图窗底 187 → 分隔线 232 = 45px；分隔线 232 → 好感行 280 = 48px；好感行 280 → 时间行 330 = 50px；时间底 ≈346 → 卡底 380 = 34px，均 ≤52px，无超过 60px 的水平空白带。

皮肤板由 `_tools/make_save_cards.py` 按 470×380 重烘（内嵌截图窗描边 / 深色窗底 / 分隔线全部按新尺寸画），再由圆角脚本统一切 r12；未拉伸旧 470×240 图。

---

## 4. 引用清理证据

### 4.1 旧两层叠加已无运行时引用

在 `game/ui2/`、`game/core/` 全部 `.rpy` 中检索 `gthumb_bg|gthumb_fg`：**0 匹配**。

磁盘上仍保留（未被引用，未删除）：

```
gthumb_bg_cg_bai.png  gthumb_bg_cg_lan.png  gthumb_bg_cg_qing.png  gthumb_bg_cg_zhou.png
gthumb_fg_cg_bai.png  gthumb_fg_cg_lan.png  gthumb_fg_cg_qing.png  gthumb_fg_cg_zhou.png
```

新引用仅三处（`game/ui2/50_gallery.rpy`）：

```
77:  add ("images/ui/gthumb_cover_%s.png" % item["id"]) xalign 0.5 ypos 15
82:  add "images/ui/gthumb_empty.png" xalign 0.5 ypos 15
107: add "images/ui/gthumb_empty.png" xalign 0.5 ypos 15
```

### 4.2 无运行时裁切 / 缩放

在 `50_gallery.rpy`、`30_saveload.rpy` 检索 `im.Crop|im.Scale`：仅命中一行注释（说明刻意不用），**无代码调用**。

### 4.3 动效接线保留

`vn2_slide_left` / `vn2_lift` / `vn2_stagger` / `vn2_rise_in` 调用点与参数未改；`90_motion.rpy` 未修改。

---

## 5. 像素自检结果

### 5.1 底板圆角自检（`_tools/make_round_corner.py`，16 件全部 OK）

判定口径：四角 2×2 alpha=0；角象限内圆外无近不透明残留（alpha>128）；半透环带无近白（RGB 全 >190）像素；TL 角蒙版中值轮廓按圆心 (r,r) 做圆拟合，偏差 ≤1.6px。

```
[OK]  card.png           470x380  r=12  四角 alpha max=0  残留 0  近白 0  圆拟合 mean 12.6 偏差 0.7
[OK]  card_empty.png     470x380  r=12  四角 0  残留 0  近白 0  mean 12.6 偏差 0.7
[OK]  card_hover.png     470x380  r=12  四角 0  残留 0  近白 0  mean 12.6 偏差 0.7
[OK]  gcard.png          462x380  r=12  四角 0  残留 0  近白 0  mean 12.6 偏差 0.7
[OK]  gcard_locked.png   462x380  r=12  四角 0  残留 0  近白 0  mean 12.6 偏差 0.7
[OK]  chap_row.png       322x56  r=10  四角 0  残留 0  近白 0  mean 10.6 偏差 0.8
[OK]  chap_row_hover.png 322x56  r=10  四角 0  残留 0  近白 0  mean 10.6 偏差 0.8
[OK]  row.png            800x64  r=10  四角 0  残留 0  近白 0  mean 10.6 偏差 0.8
[OK]  nav_idle.png       240x64  r=10  四角 0  残留 0  近白 0  mean 10.6 偏差 0.8
[OK]  nav_hover.png      240x64  r=10  四角 0  残留 0  近白 0  mean 10.6 偏差 0.8
[OK]  nav_pressed.png    240x64  r=10  四角 0  残留 0  近白 0  mean 10.6 偏差 0.8
[OK]  mbtn_idle.png      360x84  r=10  四角 0  残留 0  近白 0  mean 10.6 偏差 0.8
[OK]  mbtn_hover.png     360x84  r=10  四角 0  残留 0  近白 0  mean 10.6 偏差 0.8
[OK]  plate_idle.png      96x48  r=8   四角 0  残留 0  近白 0  mean 8.6  偏差 0.6
[OK]  plate_hover.png     96x48  r=8   四角 0  残留 0  近白 0  mean 8.6  偏差 0.6
[OK]  plate_selected.png  96x48  r=8   四角 0  残留 0  近白 0  mean 8.6  偏差 0.6
ROUND3 ROUND-CORNER SELF-CHECK: ALL PASS
```

圆拟合 mean 比名义半径大约 0.6px，是 4×SS 蒙版 LANCZOS 缩回后的中值轮廓位置，偏差 ≤0.8px，四角同一半径。

### 5.2 画廊缩略图自检（426×272）

| 文件 | 四角 alpha max | 角区半透 fringe | 角区近白像素 |
|---|---|---|---|
| `gthumb_cover_cg_zhou.png` | 0 / 0 / 0 / 0 | 48 | 0 |
| `gthumb_cover_cg_lan.png` | 0 / 0 / 0 / 0 | 48 | 48（见注 1） |
| `gthumb_cover_cg_bai.png` | 0 / 0 / 0 / 0 | 48 | 11（见注 1） |
| `gthumb_cover_cg_qing.png` | 0 / 0 / 0 / 0 | 48 | 0 |
| `gthumb_empty.png` | 0 / 0 / 0 / 0 | 48 | 0 |

注 1：`cg_lan`（伞面 / 亮天空）、`cg_bai`（白花）圆角角区 fringe 里的近白像素是**照片自身亮部**落在抗斜坡内，不是合成产生的白边 / 亮边；在深色卡面上呈亮部到透明的自然过渡，预览放大图未见描边状亮圈。

---

## 6. 静态预览（PIL 离线合成，1920×1080）

| 文件 | 内容 | 尺寸 |
|---|---|---|
| `shots/preview_gallery.png` | 画廊 3×2 整屏：四满幅 cover + 两未公开占位 | 1920×1080 |
| `shots/preview_save.png` | 存档 3×2 整屏：三 loaded 占位 + 三空槽 + 底部页码条 | 1920×1080 |
| `shots/preview_gallery_zoom.png` | 行 0 第 1/2 卡边界区域 2× 放大 | 1972×800 |
| `shots/preview_save_zoom.png` | 第 1/2 卡边界，纵向从行1 卡顶裁到页码条：覆盖整条卡高 + 行2 底与页码条之间净空段 | 1980×1804 |

预览中左侧导航仅画深色示意块；卡面 / 缩略图 / 文字占位均按本文件第 2、3 节真实坐标落位。

---

## 7. 改动 / 新增文件清单（绝对路径）

修改的运行时文件：

- `L:\AI\FurryVN\20261117_uidemo\game\ui2\50_gallery.rpy`
- `L:\AI\FurryVN\20261117_uidemo\game\ui2\30_saveload.rpy`

重烘 / 切角的资产（`game\images\ui\`）：

- `card.png` `card_empty.png` `card_hover.png`（470×380，r12）
- `gcard.png` `gcard_locked.png`（462×380，r12）
- `chap_row.png` `chap_row_hover.png` `row.png` `nav_idle.png` `nav_hover.png` `nav_pressed.png` `mbtn_idle.png` `mbtn_hover.png`（r10）
- `plate_idle.png` `plate_hover.png` `plate_selected.png`（r8）
- `gthumb_empty.png`（426×272 RGBA，r8）

新增资产：

- `game\images\ui\gthumb_cover_cg_zhou.png`
- `game\images\ui\gthumb_cover_cg_lan.png`
- `game\images\ui\gthumb_cover_cg_bai.png`
- `game\images\ui\gthumb_cover_cg_qing.png`

可复跑脚本（`_tools\`）：

- `make_round_corner.py`（圆角烘焙 + 自检，`python _tools/make_round_corner.py`）
- `make_gallery_thumbs.py`（满幅 cover 缩略图 + 焦点裁切 + 圆角，重写）
- `make_save_cards.py`（470×380 存档卡重烘，回炉版）
- `make_previews.py`（四张静态预览 + 放大，`python _tools/make_previews.py`）
- `measure_save_layout.py`（真机截图行/列扫描，实测卡边与页码条边，`python _tools/measure_save_layout.py`）

备份：`game\images\ui\_backup_round3\`（改前 25 件：`card* / gcard* / gthumb* / plate* / chap_row* / row* / nav* / mbtn*`）。

预览图：见第 6 节 `shots\` 四个文件。

---

## 8. 未达标 / 遗留事项

1. **未实跑 Ren'Py**（按任务约束）：所有坐标为静态 PIL 合成核算，未在引擎内验证文本换行、按钮热区与翻页行为；正式截图与 lint 由收尾环节统一执行。
2. `plate_*` 在 `00_theme.rpy` 里以 `Frame(..., 22, 6, 22, 6)` 拉伸：r8 圆角顶部有约 2px 落在纵向 6px 拉伸切片内，实际弧形会被轻微拉伸；尺寸未动，视觉影响很小。
3. `cg_lan / cg_bai` 缩略图角区 fringe 含照片亮部像素（见 5.2 注 1），若实机查看认为偏亮，可在 `make_gallery_thumbs.py` 里把蒙版半径再内缩 1px 或对边缘做 1px 压暗。
4. `row.png` 当前在 `.rpy` 中无运行时引用（遗留资产），已按任务清单一并切角；如后续确认废弃可再清理。
5. **进程硬约束**：本轮起不再 kill 任何进程。ComfyUI（`E:\ComfyUI\python_embeded\python.exe main.py --port 8188 --lowvram`）是用户自有的生图服务，背景生图线依赖它，必须保持运行；本任务及后续收尾环节都不得停止 ComfyUI 或任何 python 进程，用户自带的 Godot / 网盘 / 工具进程同样不动。
6. **画廊本轮冻结**：满幅 cover 缩略图、六卡几何、标题 / 副题基线均未改动；重跑流水线时仅按原参数复现同版资产。
7. 存档页卡高按实测 content_h=918.1、净空 32–56px 反推，H=380 是区间内唯一可取整值，实测净空 55.5px，距 56px 上界仅约 0.5px 余量；若收尾实机发现内容框 top/bottom padding 与真机截图有偏差导致净空被吃掉，优先把 `VN2_SLOT_H` 收到 378（净空 59.5px），不要压缩卡内截图窗。
