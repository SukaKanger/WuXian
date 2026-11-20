# 《雾线》CG / BG 生产看板

对应清单：`雾线_最终美术清单_44CG_无新增角色_背景需求.md`
工程：`L:\AI\FurryVN\20261117_uidemo`
规格：CG 1920×1080 PNG RGB ≤3MB；BG 1920×1080 PNG RGB 2–5MB；无文字/水印/边框；关键脸与动作在 30–70% / 25–72%。

## 0. 角色锚定（6 人，不得漂移）

| key | 角色 | 物种 | 必须锁死的特征 | 参考图 |
|---|---|---|---|---|
| zhou | 老周 | 灰狼 | 烟灰背/奶白胸腹吻部、左耳缺、左颊三道浅疤、琥珀眼、黑皮胸带、橄榄工装裤+织带、黑靴 | `表情差分_打标\老周 neutral.png` |
| lan | 蓝羽 | 蓝狼 | 钢蓝灰毛、奶白胸、右耳后小辫+蓝珠、耳钉、胸带+卷睡袋背包、橄榄裤、挽袖、宽背砍刀、棕靴 | `蓝羽 neutral.png` |
| bai | 白砚 | 白虎 | 纯白毛+灰黑条纹（脸/前臂）、圆耳、短吻、奶白衬衫挽袖、棕斜挎带+医药包、胸口小红标、米色裤、棕靴、条纹尾 | `白砚 neutral.png` |
| qing | 青岩 | 青龙 | 淡青鳞+奶白胸腹、白吻+长须、深色鹿角、长灰发、金褐眼、棕皮背心敞胸、灰裤、黑靴、长尾 | `青岩 neutral.png` |
| arui | 阿瑞 | 红狐 | 红毛+白腹、部落向导装束、背吹箭筒（只做支线/NPC） | 立绘待补 |
| shiqi | 十七 | 黑豹 | 金褐斑点、黑豹体型、守门人装束（只做石廊/真结局） | 立绘待补 |

## 1. 固定配方（不得随意改）

- 底模：`[S][Furry]indigoVoidFurryFusedXL_noobaiV33_full_fp16.safetensors`
- LoRA：筋肉壮硕 0.18 / Aymbord_Illustrious 0.35 / 体积光 0.30
- 身份：IPAdapter Plus SDXL（`ip-adapter-plus_sdxl_vit-h` + `CLIP-ViT-H-14`），参考图 = 该角色 neutral 立绘头部裁切，权重 0.45–0.55
- 采样：dpmpp_2m + karras，26–28 steps，cfg 6.0，1344×768 出图 → Lanczos 放大到 1920×1080
- 构图：提示词前半段写环境（wide / medium wide shot、environment dominant、character small in the frame），后半段写角色设计锚点与动作
- 效率：单张 33–50s（2 张并行排队 90s 上下）；44 张 ≈ 35–45 分钟无人值守

## 2. 44 张 CG 状态

### 结局（8，必需，优先）

| id | 标题 | 状态 | 动作要点 |
|---|---|---|---|
| cg_end_lan_together | 蓝羽 · 同行 | 待生成 | 两人并肩走出雾，蓝羽回头 |
| cg_end_lan_alone | 蓝羽 · 独行 | 待生成 | 单人背影走向雾中，地图留在石上 |
| cg_end_bai_together | 白砚 · 同行 | 待生成 | 肩并肩坐在站门外台阶，药箱在脚边 |
| cg_end_bai_alone | 白砚 · 独行 | 待生成 | 空药箱与灯留在桌上，人不在画面中央 |
| cg_end_qing_together | 青岩 · 同行 | 待生成 | 铁架下两人一前一后，样本箱在中间 |
| cg_end_qing_alone | 青岩 · 独行 | 待生成 | 档案柜全开，纸张散落，人已走远 |
| cg_end_sealed | 封口 | 待生成 | 封条贴上门缝，手/背影，不给正脸 |
| cg_end_seventh | 第七天 | 待生成 | 雨停的清晨，门口水痕，远处一个人影 |

### 营地 / 休息（12）

| id | 标题 | 状态 |
|---|---|---|
| cg_camp_entry | 入口营地 | 待生成 |
| cg_camp_ridge | 断崖夜营 | 待生成 |
| cg_camp_marsh | 沼泽边 | 待生成 |
| cg_camp_old | 旧营地 | 待生成 |
| cg_camp_gate | 站门外前夜 | 待生成 |
| cg_camp_lan_1 | 蓝羽线·雨夜 | 待生成 |
| cg_camp_lan_2 | 蓝羽线·雾里 | 待生成 |
| cg_camp_bai_1 | 白砚线·火堆分食 | 待生成 |
| cg_camp_bai_2 | 白砚线·药箱夜 | 待生成 |
| cg_camp_bai_3 | 白砚线·站门外 | 待生成 |
| cg_camp_qing_1 | 青岩线·档案夜 | 待生成 |
| cg_camp_qing_2 | 青岩线·遗迹前夜 | 待生成 |

### 副本（8）

| id | 标题 | 状态 |
|---|---|---|
| cg_dungeon_mine_enter | 塌方矿道·入口 | 待生成 |
| cg_dungeon_mine_clear | 矿道·旧队徽 | 待生成 |
| cg_dungeon_hunter_enter | 猎人废营·入口 | 待生成 |
| cg_dungeon_hunter_clear | 废营·旧病历 | 待生成 |
| cg_dungeon_station_enter | 旧气象站·入口 | 待生成 |
| cg_dungeon_station_clear | 气象站·导师记录 | 待生成 |
| cg_dungeon_guardian_enter | 石廊·入口 | 待生成 |
| cg_dungeon_guardian_clear | 石廊·骨珠 | 待生成 |

### 关键剧情（16）

| id | 标题 | 状态 |
|---|---|---|
| cg_zhou | 断崖之后 | 草稿（动作版第 1 轮，环境待强化） |
| cg_lan | 银纹 | 草稿（动作版第 1 轮，毛色偏灰待修正） |
| cg_bai | 灯下 | 草稿（动作版第 1 轮，待验） |
| cg_qing | 守站人 | 草稿（动作版第 1 轮，待验） |
| cg_key_rain | 雨幕 | 待生成 |
| cg_key_fork | 锁线 | 待生成 |
| cg_key_settle | 结算 | 待生成 |
| cg_key_lan_badge | 旧队徽 | 待生成 |
| cg_key_lan_name | 雾里的名字 | 待生成 |
| cg_key_lan_two_paths | 两条路 | 待生成 |
| cg_key_bai_pill | 空药瓶 | 待生成 |
| cg_key_bai_after | 站门外 | 待生成 |
| cg_key_qing_archive | 空的档案柜 | 待生成 |
| cg_key_qing_mentor | 导师记录 | 待生成 |
| cg_key_qing_door | 门后 | 待生成 |
| cg_key_shiqi | 十七的骨珠 | 待生成 |

## 3. 22 张背景（P0 先做）

P0 12：bg_entry_ferry、bg_old_plank、bg_river_valley、bg_waterfall_herb、bg_station_exterior、bg_cable_tower、bg_ruins_mouth、bg_camp_rain、bg_camp_river、bg_camp_old、bg_mine_collapse、bg_guardian_corridor

P1 8：bg_station_interior、bg_archive、bg_guardian_door、bg_hunter_camp、bg_lan_ridge、bg_bai_ward、bg_qing_ruins、bg_camp_ruins

P2 2：bg_after_dawn、bg_seventh_dawn

现有 6 张复用：jungle / cliff / firelight / marsh / gate / hall（只做调色与光照变体）

## 4. 交付与验收

- CG → `game/images/cg/`；缩略图 → `game/images/ui/gthumb_cover_<id>.png`（426×272，8px 圆角，按脸定焦）
- BG → `game/images/bg/`
- 每批附 contact sheet，按 id 分组
- 每批跑 `renpy lint`，0 error 才交
