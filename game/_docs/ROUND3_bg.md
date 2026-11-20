# ROUND3 场景背景（VN2《雾线》）

- 工程：`L:\AI\FurryVN\20261117_uidemo`（Ren'Py 8.5.3，虚拟分辨率 1920×1080）
- 交付：六张 1920×1080 RGB PNG，同名覆盖 `game/images/bg/`，工程代码零改动即可吃上。
- 可复跑脚本：`_tools/make_bg_comfy.py`（无参=连 ComfyUI 全量生成；传场景名=只跑指定；`--regrade`=离线用 raw 缓存重跑后处理；`--record`=离线重建记录 JSON；`--sheet`=拼联表）。
- 机器可读记录：`_tools/_bg_run_record.json`；联表：`shots/bg_contact_sheet.jpg`。

## 1. 模型选型（为什么没有用 indigoFurryMix）

- 优先候选（与兽人立绘同源）：`[A+][Furry]indigoFurryMix_v120Hybrid_pruned_fp16.safetensors`。
- 实测探针：该模型在生成纯环境背景时，稳定倾向画出人形/拟人角色（firelight 探针出现三个人形角色），触碰「绝不出现人物/人形/兽人/动物主体」红线；其人物先验对空场景景别不合格。
- 因此整组切换到风景向模型 **`Scene_LandscapeRealisticPro_5p1.safetensors`**，六张全部由这同一个 checkpoint 产出（无 LoRA、无混模型）。
- 六张同一 checkpoint 确认：是，`Scene_LandscapeRealisticPro_5p1.safetensors`。
- 已知风格差距：该风景模型成片质感偏摄影/写实渲染，与兽人立绘的厚涂半写实存在一定距离；受本机 8G 显存与模型池限制，未再尝试其他风景模型。

## 2. 统一采样与后处理管线

| 项 | 值 |
|---|---|
| checkpoint | `Scene_LandscapeRealisticPro_5p1.safetensors`（六张同一） |
| steps | 28 |
| cfg | 4.8 |
| sampler | `dpmpp_2m` |
| scheduler | `karras` |
| denoise | 1.0 |
| 基础尺寸 | 1344×768（OOM 降级 1024×576，本组未触发降级） |
| 放大方式 | Pillow LANCZOS 1344×768 → 1920×1080；UnsharpMask r=1.2 / p=35 / t=2；底部渐变压暗 start=0.70、floor=0.55 |
| 第一轮统一轻调色 | sat=0.95，bright=0.98，contrast=1.03，R=0.985，B=1.015，vignette=0.03（幅度均在 ±6% 以内） |
| 第二轮统一压暗 | 曝光 ×0.90，饱和 ×0.96，阴影端 R×0.96 / B×1.05 推青灰，四角暗角 0.06；>150/255 高光明柔化膝点（压整片亮雾/亮块，不压光柱芯） |
| 水印处理 | 角落伪文字/签名按检测触发，相邻同条地面水平镜像克隆覆盖，内部全填充、外缘 12px 羽化 |

## 3. 逐张记录

### jungle
- checkpoint：`Scene_LandscapeRealisticPro_5p1.safetensors`
- seed：**26111711**
- steps：28 ｜ cfg：4.8 ｜ sampler：`dpmpp_2m` ｜ scheduler：`karras`
- 基础尺寸：1344×768 ｜ 放大：LANCZOS → 1920×1080 + UnsharpMask + 统一轻调色 + 底部压暗
- 最终文件：`L:\AI\FurryVN\20261117_uidemo\game\images\bg\jungle.png`
- prompt：`masterpiece, best quality, highly detailed, painterly semi-realistic concept art, matte painting, cinematic film still, volumetric fog, soft diffused light, muted teal-grey palette with restrained warm accents, atmospheric depth, light film grain, environment only, wide establishing shot, middle and upper areas kept calm and uncluttered for character sprites and text, dark quiet foreground, deep inside a tropical rainforest, wet moss-covered tree trunks and tangled aerial roots, broad damp leaves, thin mist drifting between trunks, faint pale light seeping through gaps in the canopy, humid still air, layered depth`
- negative：`(people:1.7), (human:1.7), (character:1.7), (anthro:1.5), (animal:1.4), (creature:1.3), (text:1.6), (letters:1.6), (watermark:1.6), (signature:1.6), artist name, username, corner text, scribbled writing, logo, UI element, interface, frame, border, anime, cel shading, flat color, cartoon, lineart, 3d render, cgi, low-poly, plastic, oversaturated, HDR vivid colors, neon, glossy, lowres, blurry, jpeg artifacts, distorted perspective, deformed, daylight, daytime, sunny sky, multiple campfires, two fires`
- 专用修补：无；统一轻调色 + 角落水印克隆去除（按检测触发）。

### firelight
- checkpoint：`Scene_LandscapeRealisticPro_5p1.safetensors`
- seed：**26111727**
- steps：28 ｜ cfg：4.8 ｜ sampler：`dpmpp_2m` ｜ scheduler：`karras`
- 基础尺寸：1344×768 ｜ 放大：LANCZOS → 1920×1080 + UnsharpMask + 统一轻调色 + 底部压暗
- 最终文件：`L:\AI\FurryVN\20261117_uidemo\game\images\bg\firelight.png`
- prompt：`masterpiece, best quality, highly detailed, painterly semi-realistic concept art, matte painting, cinematic film still, volumetric fog, soft diffused light, muted teal-grey palette with restrained warm accents, atmospheric depth, light film grain, environment only, wide establishing shot, middle and upper areas kept calm and uncluttered for character sprites and text, dark quiet foreground, (night:1.3), deep dark night in a forest clearing, the whole frame dominated by dark blue-teal night shadows, exactly one single lone campfire in the lower center-right third, tall bright fire tongues over a pile of glowing logs, this campfire is the only and dominant light source, warm golden light spilling onto nearby tree trunks, wet ground and drifting fog, a soft glowing halo around the fire, cold dark tree silhouettes, deep shadows, rising sparks, thin smoke haze, faint moonlit mist`
- negative：`(people:1.7), (human:1.7), (character:1.7), (anthro:1.5), (animal:1.4), (creature:1.3), (text:1.6), (letters:1.6), (watermark:1.6), (signature:1.6), artist name, username, corner text, scribbled writing, logo, UI element, interface, frame, border, anime, cel shading, flat color, cartoon, lineart, 3d render, cgi, low-poly, plastic, oversaturated, HDR vivid colors, neon, glossy, lowres, blurry, jpeg artifacts, distorted perspective, deformed, daylight, daytime, sunny sky, multiple campfires, two fires, tent, canvas, chair, bench, furniture, camp gear, backpack, bright fog, white sky, overcast day, moon, sun, light disc, lens flare, second light source, glowing orb, two campfires, multiple campfires, several fires, second campfire, pair of fires, scattered fires`
- 专用修补：raw 横向镜像（FL_MIRROR=True，主火由偏左翻到中下偏右）；夜间压暗：暖火光/高亮火芯掩膜保护，冷色环境 R×0.90 / B×1.06 偏青；第二堆火椭圆柔和压暗（中心 594,739，rx210/ry140，羽化 80px，融合 0.82，掩膜内亮暖 ×0.55）压成雾里远处一点余烬；未做逐像素抠除（避免斑块）。
- 废 seed（未采用）：26111722 / 26111723 / 26111724 / 26111725 / 26111726。

### marsh
- checkpoint：`Scene_LandscapeRealisticPro_5p1.safetensors`
- seed：**26111703**
- steps：28 ｜ cfg：4.8 ｜ sampler：`dpmpp_2m` ｜ scheduler：`karras`
- 基础尺寸：1344×768 ｜ 放大：LANCZOS → 1920×1080 + UnsharpMask + 统一轻调色 + 底部压暗
- 最终文件：`L:\AI\FurryVN\20261117_uidemo\game\images\bg\marsh.png`
- prompt：`masterpiece, best quality, highly detailed, painterly semi-realistic concept art, matte painting, cinematic film still, volumetric fog, soft diffused light, muted teal-grey palette with restrained warm accents, atmospheric depth, light film grain, environment only, wide establishing shot, middle and upper areas kept calm and uncluttered for character sprites and text, dark quiet foreground, misty swamp wetland, still dark water with a faint cold shimmer, dead gnarled trees and bare branches reflected on the surface, thick fog hovering low over the water, desaturated green-grey, quiet empty wetland`
- negative：`(people:1.7), (human:1.7), (character:1.7), (anthro:1.5), (animal:1.4), (creature:1.3), (text:1.6), (letters:1.6), (watermark:1.6), (signature:1.6), artist name, username, corner text, scribbled writing, logo, UI element, interface, frame, border, anime, cel shading, flat color, cartoon, lineart, 3d render, cgi, low-poly, plastic, oversaturated, HDR vivid colors, neon, glossy, lowres, blurry, jpeg artifacts, distorted perspective, deformed, daylight, daytime, sunny sky, multiple campfires, two fires`
- 专用修补：无；统一轻调色 + 角落水印克隆去除（按检测触发）。

### gate
- checkpoint：`Scene_LandscapeRealisticPro_5p1.safetensors`
- seed：**26111704**
- steps：28 ｜ cfg：4.8 ｜ sampler：`dpmpp_2m` ｜ scheduler：`karras`
- 基础尺寸：1344×768 ｜ 放大：LANCZOS → 1920×1080 + UnsharpMask + 统一轻调色 + 底部压暗
- 最终文件：`L:\AI\FurryVN\20261117_uidemo\game\images\bg\gate.png`
- prompt：`masterpiece, best quality, highly detailed, painterly semi-realistic concept art, matte painting, cinematic film still, volumetric fog, soft diffused light, muted teal-grey palette with restrained warm accents, atmospheric depth, light film grain, environment only, wide establishing shot, middle and upper areas kept calm and uncluttered for character sprites and text, dark quiet foreground, exterior view approaching an old stone checkpoint gate half swallowed by mist in the woods, weathered stone blocks covered in moss and lichen, rusted old iron hinges and bars, one dim warm lantern hanging by the doorway, damp stone path, overgrown weeds at the base`
- negative：`(people:1.7), (human:1.7), (character:1.7), (anthro:1.5), (animal:1.4), (creature:1.3), (text:1.6), (letters:1.6), (watermark:1.6), (signature:1.6), artist name, username, corner text, scribbled writing, logo, UI element, interface, frame, border, anime, cel shading, flat color, cartoon, lineart, 3d render, cgi, low-poly, plastic, oversaturated, HDR vivid colors, neon, glossy, lowres, blurry, jpeg artifacts, distorted perspective, deformed, daylight, daytime, sunny sky, multiple campfires, two fires`
- 专用修补：无；统一轻调色 + 角落水印克隆去除（按检测触发）。

### hall
- checkpoint：`Scene_LandscapeRealisticPro_5p1.safetensors`
- seed：**26111705**
- steps：28 ｜ cfg：4.8 ｜ sampler：`dpmpp_2m` ｜ scheduler：`karras`
- 基础尺寸：1344×768 ｜ 放大：LANCZOS → 1920×1080 + UnsharpMask + 统一轻调色 + 底部压暗
- 最终文件：`L:\AI\FurryVN\20261117_uidemo\game\images\bg\hall.png`
- prompt：`masterpiece, best quality, highly detailed, painterly semi-realistic concept art, matte painting, cinematic film still, volumetric fog, soft diffused light, muted teal-grey palette with restrained warm accents, atmospheric depth, light film grain, environment only, wide establishing shot, middle and upper areas kept calm and uncluttered for character sprites and text, dark quiet foreground, interior of an old timber-and-stone hall, rough stone walls and heavy wooden beams, a fire brazier on one side casting warm glow, shafts of dusty light falling through a high window, long depth receding down the hall, still empty room`
- negative：`(people:1.7), (human:1.7), (character:1.7), (anthro:1.5), (animal:1.4), (creature:1.3), (text:1.6), (letters:1.6), (watermark:1.6), (signature:1.6), artist name, username, corner text, scribbled writing, logo, UI element, interface, frame, border, anime, cel shading, flat color, cartoon, lineart, 3d render, cgi, low-poly, plastic, oversaturated, HDR vivid colors, neon, glossy, lowres, blurry, jpeg artifacts, distorted perspective, deformed, daylight, daytime, sunny sky, multiple campfires, two fires`
- 专用修补：黄昏/火盆将熄厅堂专属调色——整体曝光 ×0.72（光柱芯保留），阴影推青，受光面加暖 #c98a4a（≤12%），丁达尔光束保留，底部 1/4 压暗。

### cliff
- checkpoint：`Scene_LandscapeRealisticPro_5p1.safetensors`
- seed：**26111706**
- steps：28 ｜ cfg：4.8 ｜ sampler：`dpmpp_2m` ｜ scheduler：`karras`
- 基础尺寸：1344×768 ｜ 放大：LANCZOS → 1920×1080 + UnsharpMask + 统一轻调色 + 底部压暗
- 最终文件：`L:\AI\FurryVN\20261117_uidemo\game\images\bg\cliff.png`
- prompt：`masterpiece, best quality, highly detailed, painterly semi-realistic concept art, matte painting, cinematic film still, volumetric fog, soft diffused light, muted teal-grey palette with restrained warm accents, atmospheric depth, light film grain, environment only, wide establishing shot, middle and upper areas kept calm and uncluttered for character sprites and text, dark quiet foreground, view from a cliff top looking down over a sea of clouds and a fog-filled valley, layered cold blue-grey distant mountain ridges, sparse pines on the rocky rim, overcast diffused sky, vast lonely vista`
- negative：`(people:1.7), (human:1.7), (character:1.7), (anthro:1.5), (animal:1.4), (creature:1.3), (text:1.6), (letters:1.6), (watermark:1.6), (signature:1.6), artist name, username, corner text, scribbled writing, logo, UI element, interface, frame, border, anime, cel shading, flat color, cartoon, lineart, 3d render, cgi, low-poly, plastic, oversaturated, HDR vivid colors, neon, glossy, lowres, blurry, jpeg artifacts, distorted perspective, deformed, daylight, daytime, sunny sky, multiple campfires, two fires`
- 专用修补：底部中央彩虹光斑大范围柔和覆盖（中心 1025,990，rx160/ry60，羽化 60px，GaussianBlur 45，融合 0.92）；下半部云海额外压暗 0.56；峰顶信标建筑保留不动。

## 4. 验收亮度指标（1920×1080，亮度均值 0–255）

| 场景 | 底部 1/4 平均亮度 | 全图平均亮度 | 全图 >150 占比 | 中上部 2/3 >150 占比 |
|---|---|---|---|---|
| jungle | 27.7 | 84.8 | 23.6% | 35.2% |
| firelight | 38.8 | 57.3 | 0.1% | 0.0% |
| marsh | 41.3 | 98.0 | 25.7% | 38.5% |
| gate | 43.9 | 82.6 | 12.7% | 19.0% |
| hall | 37.0 | 48.6 | 0.0% | 0.0% |
| cliff | 43.3 | 94.7 | 14.2% | 21.2% |

- 底部 1/4 平均亮度：六张均 ≤45/255（say 文字框区可读）。
- 中上部 >150 占比：firelight / hall 接近 0；jungle / marsh / gate / cliff 的高亮度区为环境浓雾/云海（连续雾气而非整块高光），已过高光膝点回收一档，未再继续压暗以免丢雾感。

## 5. 已知偏差 / 未达标项（如实记录，待联表评审后决定是否换 seed 重跑）

- **firelight**：左侧仍残留一点极淡的远景余烬光晕（已用椭圆柔和压暗收到「雾里很远一点余烬」程度；像素抠除已验证会留斑块，未强行抹除）；主火位于中下偏右但略偏画面中线。
- **marsh**：成片偏水淹林倒影，枯树沼泽的荒疏感偏弱；中上部雾带仍偏亮。
- **gate**：未生成暖灯；右侧建筑偏墓园小礼拜堂而非石砌关卡。
- **hall**：未生成火盆（靠黄昏调色与受光面暖调 #c98a4a 补足氛围）；已从白昼天光压成黄昏/将熄厅堂，丁达尔光束保留。
- **cliff**：峰顶小建筑按评审意见保留（读作信标塔，契合世界观）；底部中央彩虹光斑已用云雾纹理柔和覆盖去除；下半部云海已额外压暗。
- **角落残留**：gate / marsh / hall 克隆覆盖边缘各残留 1–2px 小点，轻微，联表尺寸下不可辨。
- **风格**：整体偏摄影/写实渲染，与兽人立绘厚涂半写实有差距（见第 1 节模型选型说明）。

## 6. 回滚

原图备份目录：`game/images/bg/_backup_20261117/`（六张原始 PNG，脚本不覆盖已有备份）。

一行回滚（PowerShell）：

```powershell
Copy-Item "L:\AI\FurryVN\20261117_uidemo\game\images\bg\_backup_20261117\*.png" "L:\AI\FurryVN\20261117_uidemo\game\images\bg\" -Force
```

## 7. ComfyUI 进程状态

- ComfyUI 为本机用户自有进程，全程未 kill、未为腾显存杀任何进程、未清他人队列；脚本只排队等待。
- 期间 ComfyUI 曾被另一任务线按旧习惯误杀（非本任务操作）；本轮收尾前再次探测到端口拒绝连接，轮询 `http://127.0.0.1:8188/system_stats` 满 3 分钟仍未起、无 main.py 进程，遂按授权口径用原参数重启一次：`E:\ComfyUI\python_embeded\python.exe main.py --port 8188 --lowvram`，工作目录 `E:\ComfyUI\ComfyUI`，stdout/stderr 重定向 `E:\ComfyUI\_vn2_bg_run.log` / `E:\ComfyUI\_vn2_bg_run.err.log`（PID 74848）。
- 收尾状态：**ComfyUI 被误杀后已重启，当前仍在运行**（v0.24.0，`--port 8188 --lowvram`）；全程未 kill ComfyUI、未为腾显存杀任何进程、未清他人队列，只结束过本任务自己起的提交脚本。
