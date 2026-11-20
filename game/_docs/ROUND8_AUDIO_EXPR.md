# Round 8 · 音量默认与表情差分接入

日期：2026-11-18
工程：`L:\AI\FurryVN\20261117_uidemo`
签名 key：`D:\Desktop\WuXian-key.jks`（仅确认存在，未打开、未上传、未写入仓库）

## 一、音量默认

- `game/options.rpy`
  - `config.default_music_volume = 0.50`
  - `config.default_sfx_volume = 0.50`
  - `config.default_voice_volume = 0.90` 不变
  - `config.emphasize_audio_volume = 0.18`，与设置页“音乐自动退到约 18%”的文案对齐；此前配置是 0.75，和界面文案不一致，也是语音容易被音乐压住的直接原因之一。
- `game/core/50_audio.rpy`
  - 旧 persistent 的一次性迁移从 `vn2_mix_v3` 改为 `vn2_mix_v4`，写入音乐 0.50、音效 0.50、语音 0.90；之后玩家手动调整不会被每次启动重置。
  - BGM 电平注释同步改成 50%。

## 二、表情差分：之前确实没有接入

`game/images/chars/v2/` 已有完整素材：

- 6 个角色：`zhou / lan / bai / qing / arui / shiqi`
- 每人 6 个表情：`neutral / happy / sad / angry / shy / surprised`
- 共 36 张 1256×1616 RGBA 透明底立绘，`manifest.json` 完整。

但剧情里 100 多处 `vn2_show(...)` 全部没有传 `expr`，`vn2_show` 会回退到 `prefix`，也就是 `neutral`。所以“角色一直一张脸”不是素材缺失，而是调用层没有接表情。

本轮接入：

1. **显式锚点**——按剧情情绪给关键场景指定表情：
   - `ch09` 蓝羽银纹：`shy`
   - `ch12` 白砚旧营地：`sad`
   - `ch15` 十七门口：`surprised`
   - `ch16` 蓝羽旧队徽：`happy`
   - `ch24` 青岩石门对峙：`angry`
2. **自动切换**——`game/core/40_cast.rpy` 新增：
   - `vn2_expr_guess(what)`：只抓“笑 / 谢谢 / 对不起 / 凭什么 / 愣 / 脸红 / 耳根”等明确情绪词，避免“死、忽然、别碰”这类剧情常用词误触发。
   - `vn2_set_expr()`：只给已经在舞台上的角色换表情，保留位置与压暗值，不改存档变量。
   - `vn2_char_cb`：角色说话时按当前台词切换。
   - `vn2_narrator_cb`：旁白/独白时，只有场上恰好一个角色才帮它接情绪；多角色场景不猜，避免切错人。
3. **没有新增存档变量**，没有改动任何表情素材，也没有把 36 张图重生成。

## 三、验证

- `renpy.exe ... lint` 返回 `EXIT=0`。
- 36 张表情素材已导出对照表：`shots/vn2_expression_sheet.jpg`（6 行角色 × 6 列表情，透明底棋盘格）。
- 代码层确认：`vn2_show` 的 `expr` 路径、`vn2_set_expr` 的舞台回写、显式锚点均已编译通过。
- 未做逐章逐句的实机截图回归；本轮只做了素材对照与 lint/编译验证。

## 四、签名 key

- `D:\Desktop\WuXian-key.jks` 存在，2166 bytes，文件头 `FE ED FE ED`，是合法 JKS。
- 没有读取 alias、密码或证书内容，没有复制进工程，也没有上传。
- 后续做 Android 打包时需要 keystore alias 与密码；不要把密码贴在聊天里，构建时在本地环境输入即可。
