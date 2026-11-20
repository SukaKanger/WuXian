# Round 9 · 一代 CG 接入与游戏进程清理

日期：2026-11-18
工程：`L:\AI\FurryVN\20261117_uidemo`
素材来源：`D:\Desktop\cg_原图备份`（24 张 PNG，2048×1152）
签名 key：`D:\Desktop\WuXian-key.jks` 已收到；本轮未打开、未复制、未写入任何文件，敏感口令不进入文档。

## 一、游戏进程

- 已停止 `renpy.exe` PID 88132（窗口标题“雾线”，工程 `L:\AI\FurryVN\20261117_uidemo`）。
- 未动两个 Ren'Py Launcher 进程（92952 / 90268），它们是启动器窗口，不是游戏实例。
- 实机验证时另外启动的测试实例 PID 71088 已停止。

## 二、CG 入库

24 张原图全部处理为 **1920×1080 RGB PNG**，写入 `game/images/cg/`：

| 类别 | 文件 |
|---|---|
| 开篇 / 营地 | `cg_camp_fire_v1`、`cg_key_four_people_v0` |
| 关键剧情 | `cg_key_archive_v1`、`cg_key_badge_v2`、`cg_key_crush_v0`、`cg_key_dawn_v2`、`cg_key_gate_v1`、`cg_key_half_map_v2`、`cg_key_half_name_v0`、`cg_key_half_pill_v2`、`cg_key_rope_anchor_v2`、`cg_key_settle_v2`、`cg_key_surgery_v1` |
| 路线场景 | `cg_route_bai_ward_v0`、`cg_route_lan_ridge_v0`、`cg_route_qing_ruins_v0` |
| 结局 | `cg_end_lan_together_v1`、`cg_end_lan_alone_v0`、`cg_end_bai_together_v1`、`cg_end_bai_alone_v0`、`cg_end_qing_together_v0`、`cg_end_qing_alone_v1`、`cg_end_sealed_v1`、`cg_end_seventh_v0` |

原有四张 `cg_zhou / cg_lan / cg_bai / cg_qing` 未覆盖。

## 三、CG 模式

新增 `game/core/65_cg_story.rpy`：

- `vn2_cg_show(img, trans=None)`：全屏显示 CG，隐藏全部立绘 tag；**保留 `vn2_stage`**，不破坏角色位置/表情记录。
- `vn2_cg_hide(trans=None)`：收起 CG，并按 `vn2_stage` 恢复立绘。
- `config.scene_callbacks` 监听 `scene`：任何正常 `scene bg ...` 都会自动退出 CG 模式并清掉 CG 层。
- `vn2_show` / `vn2_focus` / `vn2_set_expr` 在 CG 模式下**只更新舞台记录，不渲染立绘**；语音、对话、HUD 照常。
- CG 层使用 `zorder 30`，在立绘之上；不新增存档变量，不新增具名角色。

## 四、植入位置

按章节/结局共 24 张全部接入：

| 位置 | CG |
|---|---|
| ch01 开篇 | `cg_camp_fire_v1` |
| ch03 断崖 | `cg_key_rope_anchor_v2` |
| ch04 夜哨 | `cg_key_four_people_v0` |
| ch15 门口 | `cg_key_gate_v1` |
| ch16 旧队徽 | `cg_key_badge_v2` |
| ch17 雾里的名字 | `cg_key_half_name_v0`；节点 5 切 `cg_route_lan_ridge_v0` |
| ch18 两条路 | `cg_key_half_map_v2` |
| ch19 空药瓶 | `cg_key_half_pill_v2`；节点 5 切 `cg_key_crush_v0` |
| ch20 手术 | `cg_key_surgery_v1` |
| ch21 站门外 | `cg_route_bai_ward_v0` |
| ch22 门后 | `cg_key_archive_v1` |
| ch24 守站人 | `cg_route_qing_ruins_v0` |
| ch25 结算 | `cg_key_settle_v2` |
| ch28 后日谈 | `cg_key_dawn_v2` |
| 八个结局 | 对应的 `cg_end_*` 各一张 |

结局在 `vn2_hide_all` 之后调用 `vn2_cg_hide`，避免返回主菜单时 CG 残留。

## 五、验证

- `renpy.exe ... lint` 返回 `EXIT=0`。
- 使用 `--warp story/ch01.rpy:23` 实机验证：CG 全屏显示、无叠加立绘、对话与 HUD 正常，截图 `shots/cg_ingame_window.jpg`。
- 测试进程已停止；当前没有运行中的“雾线”实例。
- 24 张 CG 尺寸全部为 1920×1080 RGB；新图体积 1.38–2.63MB。

## 六、后续

- 这轮只做**剧情内 CG 接入**，没有把 CG 画廊强行扩成 24 格；画廊仍是原有的四格正式 CG 结构。
- 等新立绘到位后，CG 模式可以直接保留；CG 段仍不会显示立绘，只播放语音。
- 画廊若要扩成 24 格，需要单独做分页与缩略图烘焙，避免 3×2 网格溢出。
