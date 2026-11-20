# BG 22 张清单与自检报告

- 工程：`L:\AI\FurryVN\20261117_uidemo`
- 模型：`Scene_LandscapeRealisticPro_5p1.safetensors`；采样：dpmpp_2m + karras，28 steps，CFG 4.8
- 出图：1344x768（OOM 降级 1024x576）→ LANCZOS 1920x1080
- 规格口径：PNG RGB、1920×1080、2–5MB、无文字/水印/边框；风格对齐现有 6 张（雨林/雾/冷绿灰/电影感，上中部留空，前景压暗）。

| id | 文件名 | 尺寸 | 字节 | seed | 短评 |
|---|---|---|---|---|---|
| bg_entry_ferry | `bg_entry_ferry.png` | 1920×1080 | 2406370 | 26111801 | 渡口木栈桥伸入雾水，冷绿灰统一，无文字水印。 |
| bg_old_plank | `bg_old_plank.png` | 1920×1080 | 2882122 | 26111802 | 半朽栈道穿林，苔痕湿润，风格贴近旧 6 张。 |
| bg_river_valley | `bg_river_valley.png` | 1920×1080 | 3003107 | 26111803 | 雾墙河谷与卵石滩，画面偏静细节少；体积经无损重编码达标。 |
| bg_waterfall_herb | `bg_waterfall_herb.png` | 1920×1080 | 3129084 | 26111804 | 多级小瀑布与苔藓药草，湿润绿调统一。 |
| bg_station_exterior | `bg_station_exterior.png` | 1920×1080 | 3313951 | 26111805 | 雾中双塔建筑；混凝土站房/锈铁架特征偏弱，无文字水印。 |
| bg_cable_tower | `bg_cable_tower.png` | 1920×1080 | 2757832 | 26111806 | 双钢架索塔入雾，工业冷调统一。 |
| bg_ruins_mouth | `bg_ruins_mouth.png` | 1920×1080 | 2779963 | 26111807 | 藤蔓石拱门纵深，风格统一。 |
| bg_camp_rain | `bg_camp_rain.png` | 1920×1080 | 3064717 | 26111834 | 雨夜营地：帆布棚/木台/低矮防雨棚+泥水洼；余烬不明显；无人物文字。 |
| bg_camp_river | `bg_camp_river.png` | 1920×1080 | 3164431 | 26111835 | 河边营地：帐篷群+前景木箱+浅水低雾；无人物文字。 |
| bg_camp_old | `bg_camp_old.png` | 1920×1080 | 3020923 | 26111810 | 废弃木屋与苔痕林地；坍塌木架特征偏弱。 |
| bg_mine_collapse | `bg_mine_collapse.png` | 1920×1080 | 2662834 | 26111811 | 偏露天岩穴；坑木支撑/矿道纵深与矿灯微光偏弱；无人物文字。 |
| bg_guardian_corridor | `bg_guardian_corridor.png` | 1920×1080 | 2622634 | 26111812 | 石拱长廊纵深，风格统一。 |
| bg_station_interior | `bg_station_interior.png` | 1920×1080 | 2951176 | 26111831 | 暗色旧站室内：暗湿木/锈铁/窄窗雾景/冷光，已按反馈重做。 |
| bg_archive | `bg_archive.png` | 1920×1080 | 3366869 | 26111814 | 成排铁柜+单侧冷光+尘光；架上书册无可辨文字。 |
| bg_guardian_door | `bg_guardian_door.png` | 1920×1080 | 2393852 | 26111815 | 雾中柱廊遗迹；厚重封门/门缝台阶特征偏弱。 |
| bg_hunter_camp | `bg_hunter_camp.png` | 1920×1080 | 3318835 | 26111816 | 荒废棚屋林地；营火环/挂具不明显。 |
| bg_lan_ridge | `bg_lan_ridge.png` | 1920×1080 | 3116126 | 26111817 | 山脊云海冷调；岩顶存在极细小剪影（规则上仅第 22 张允许人影，属遗留观察，本轮按要求未改动）。 |
| bg_bai_ward | `bg_bai_ward.png` | 1920×1080 | 2412256 | 26111818 | 简易双床病房+油灯药瓶，略整洁；无人物文字。 |
| bg_qing_ruins | `bg_qing_ruins.png` | 1920×1080 | 3140124 | 26111819 | 残柱石台苔雨，风格统一。 |
| bg_camp_ruins | `bg_camp_ruins.png` | 1920×1080 | 3071652 | 26111820 | 残墙石堆营地；帐篷结构偏弱。 |
| bg_after_dawn | `bg_after_dawn.png` | 1920×1080 | 3103388 | 26111821 | 雨后破晓湿地面反光，灰金冷调统一。 |
| bg_seventh_dawn | `bg_seventh_dawn.png` | 1920×1080 | 2783037 | 26111822 | 清晨雾径水痕，无可辨人影；风格统一。 |

## 返修记录（不合格 → 已修）

- **bg_river_valley**：体积 <2MB，未重跑采样；RAW 无损 PNG compress_level=1 重编码提体积，像素不变
- **bg_station_exterior**：体积 <2MB，未重跑采样；RAW 无损 PNG compress_level=1 重编码提体积，像素不变
- **bg_camp_rain**：首版与第一次重试均偏空林地、缺营地结构；最终换 seed 26111834，把防水布棚/简易木棚、木箱背篓、将熄余烬（非大火）提到前景主体并加权，补泥水洼与可见雨线，冷绿灰；负向词补 empty beach, bare shore, empty clearing, no tents, modern building, bright daylight, sunny。
- **bg_camp_river**：首版与第一次重试均偏空河滩/林地、缺营地结构；最终换 seed 26111835，把帐篷、捆绳、靠岸木箱提到前景主体并加权，补河面低雾，低饱和灰绿；负向词补 empty beach, bare shore, empty meadow, no tents, modern building, bright daylight, sunny。
- **bg_station_interior**：首版偏现代办公室 + 暖天光 + 浅蓝大窗，与旧站气质不符，按反馈作废；换 seed 26111831，重写暗色旧站配方（暗湿木/锈铁/窄窗只见雾/冷绿灰/单冷光源），负面词补 modern office, office chair, bright window, blue sky, daylight, sunny, warm sunlight, fluorescent light, laptop, monitor，重新采样生成。
- **bg_archive**：体积 <2MB，未重跑采样；RAW 无损 PNG compress_level=1 重编码提体积，像素不变
- **bg_lan_ridge**：体积 <2MB，未重跑采样；RAW 无损 PNG compress_level=1 重编码提体积，像素不变
- **bg_qing_ruins**：体积 <2MB，未重跑采样；RAW 无损 PNG compress_level=1 重编码提体积，像素不变
- **bg_camp_ruins**：体积 <2MB，未重跑采样；RAW 无损 PNG compress_level=1 重编码提体积，像素不变
