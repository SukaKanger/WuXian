# 雾线 WuXian — V2.28.3 Beta

**重点不是加内容，是把“AI 写出来的顺滑感”拆掉。**

## 这一版改了什么

### 1. 旁白/内心全量去 AI 味

- 30 个 `game/story/*.rpy` 加 `directors_cut.rpy`，只改 `nar` / `think`。
- 角色台词 541 行、`voice` 引用 482 条逐一比对，0 改动；不需要重配音。
- 全书 `像……` 从 142 处降到 48 处；`一道一道 / 一点一点 / 一层压一层` 类排比从 67 处降到 1 处。
- 清掉 `像在确认 / 像在等 / 像怕` 这类替读者猜心理的句子；清掉“同行结局 / 可攻略路线 / 好感够不够 / 选择里”这类把叙事当 UI 的元叙述。
- 合并重复复读、物件清单、章末格言收束；`ch26` 开场与随身清点从 7 段压到 3 段。
- 体量：对话块 2037 → 2030，字符 108,608 → 105,822；100 菜单、8 结局不变。

### 2. 结局不再被隐藏好感分干扰

- `vn2_decide_ending` 不再读 `aff_lan / aff_bai / aff_qing` 的 36 / 52 阈值。
- 同行：本线交底（`close_lan / saved_bai / qing_trusted` 等）+ ch25 明确选择“和身边的人一起离开”（`route_commit`）。
- 第七天：本线交底 + `trust_shiqi` + `evidence_kept`，不再要求好感 52。
- `ch27` 的后日谈分支改用 `vn2_ending_key`，不再按 `aff >= 60` 分叉。
- 结局矩阵条件文案同步去掉好感阈值；ch25 进章时重置 `route_commit`。

### 3. ZCode 单代理修复，子代理禁用

- ZCode 0.17.3，`--disallowed-tools "Agent Task"` + `--workflow-mode disabled`。
- 只留一个主代理跑 `directors_cut.rpy`，ZCode 内置子代理全程未启用。
- 审计报告：`_qa_headless_20261121_ai/zcode_ai_audit.txt`。

### 4. Android 中文输入热修

- 修正 Android 端软键盘被强制成 `TYPE_TEXT_VARIATION_VISIBLE_PASSWORD` 的问题；命名/改名输入现在走标准文本键盘，可以正常唤起中文 IME。
- 只改 Ren'Py Android 模板的 `SDLActivity` 输入类型，不改游戏文本与存档。

## 校验

- lint：0 error / 0 warning。
- 角色台词/voice 引用：541 / 482，均未改动。
- 产物与 SHA256 见 `SHA256SUMS-2.28.3.csv`。
- Windows 安装包仍使用项目自签名证书 `CN=[已脱敏]`；自签名根不受公共信任，其他机器可能提示“未知发布者”。

## 产物

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `WuXian-Setup-2.28.3.exe` | 362,371,592 | `909EEBE634B0DFFF335758021D08F56F70D04860AE0C129FEC60442820F902B8` |
| `WuXian-2.28.3-beta.apk` | 406,111,759 | `749E9B68BDB2AD2AF2C4B70E477D1F82275A98AACFB64BE93CBAADDEB8301435` |
| `WuXian-2.28.3-beta-win.zip` | 379,924,931 | `46170D0798BF355EC47E4FE6F38C022B40B06206AB2AC29600730173567D545A` |
