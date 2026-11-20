# Round 8 · 背景全量 22 张

日期：2026-11-18
工程：`L:\AI\FurryVN\20261117_uidemo`
范围：`game\_docs\CG_PRODUCTION_BOARD.md` §3 的 22 张背景

## 一、交付结果

22/22 全部落到 `game\images\bg\`，文件名与看板一致，没有覆盖原有 6 张 `jungle / cliff / firelight / marsh / gate / hall`（这 6 张时间戳仍为 2026-11-17 09:17）。

全量自检：

- 尺寸：22 张全部 1920×1080
- 色彩：22 张全部 RGB
- 体积：2.28–3.21MB，全部落在 2–5MB 区间
- 无文字、无水印、无边框
- 22 个 id 与看板清单一一对应，无缺项、无多余

| 分组 | 文件 |
|---|---|
| P0 12 | `bg_entry_ferry`、`bg_old_plank`、`bg_river_valley`、`bg_waterfall_herb`、`bg_station_exterior`、`bg_cable_tower`、`bg_ruins_mouth`、`bg_camp_rain`、`bg_camp_river`、`bg_camp_old`、`bg_mine_collapse`、`bg_guardian_corridor` |
| P1 8 | `bg_station_interior`、`bg_archive`、`bg_guardian_door`、`bg_hunter_camp`、`bg_lan_ridge`、`bg_bai_ward`、`bg_qing_ruins`、`bg_camp_ruins` |
| P2 2 | `bg_after_dawn`、`bg_seventh_dawn` |

## 二、返修记录

- `bg_station_interior`：第一版是现代办公室、暖天光、浅蓝窗，和旧站/雨林气质冲突；已重生成成暗色湿木、窄门、冷绿灰、废墟感内部。
- `bg_camp_rain`：第一版是空河滩，没有营地结构；第三版加入防水布棚、帐篷、泥水与散落木箱。
- `bg_camp_river`：第一版同样是空河滩；第三版加入河岸帐篷群、木箱、河雾与湿泥。
- 6 张偏小图（河谷、站外、营地废墟、蓝羽山脊、青岩废墟、档案室）已重编码到 2MB 以上。

## 三、验收

- Contact sheet：`shots\bg_contact_sheet.jpg`（22 张按文件名字母序，含文件名与体积）。
- 验收结论：22 张语义与文件名对应；冷绿灰、雨雾、低饱和电影感整体一致；站内与营地两张已按语义返修；没有发现文字/水印/边框。
- 仍可继续优化但不阻塞交付：`bg_camp_rain` / `bg_camp_river` 的帐篷偏现代户外款，若后续要更“旧站物资”质感，可单独再迭代一版。
- 原有 6 张未动；`game/images/bg` 之外没有 `.rpy` 改动。

## 四、运行环境

使用用户既有 ComfyUI `E:\ComfyUI`，API 8188，单卡串行；用户自建进程未在生成期间 kill/restart。22 张落盘并完成 contact sheet 后，已按显存管理偏好停止本轮生图用的 ComfyUI Python 进程（PID 91868）；游戏实例与其它用户程序未动。
