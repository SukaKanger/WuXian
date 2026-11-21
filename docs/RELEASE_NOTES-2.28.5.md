# 雾线 WuXian — V2.28.5 GA

> 2.28.4 的界面补丁版。不是换皮：胸像底板改成真正不透明的丛林位图，名牌改为读取玩家实际称呼。

## 1. 这版改了什么

### 1.1 胸像底板：真位图，不再 alpha

- 三个胸像 screen（右外侧、对话框右沿、对话框左端）都改为 `frame background "images/ui/portrait_jungle_solid.png"`。
- `portrait_jungle_solid.png` 是从 `images/bg/jungle.png` 取的真实丛林局部，**完全不透明 RGB 位图**，没有 alpha ramp，也没有半透明叠层。
- 名牌底板改成不透明 `Solid("#050805")`，不再用 `#000000cc` 的半透明黑条。

### 1.2 名牌读取玩家称呼

- `vn2_mc_portrait_flush` 与 `vn2_mc_portrait_left` 的 `text "队长"` 改为 `text "[player_name]"`。
- 玩家在开局命名页写入的称呼现在会直接显示在胸像下方；默认“队长”只在玩家没有改名的旧存档里保留。

### 1.3 命名页提交路径

- 输入框加 `default True`，打开即可输入。
- 确认按钮、回车、数字键盘回车统一读提交时的 `_vn2_name_text`，不再使用屏幕构建时的字符串快照。
- 2–10 字长度校验保留，提示仍为“称呼需要 2–10 个字”。

## 2. 验证

- 源码截图验证：自定义名“陆行”显示在左右两个胸像名牌上，底板为不透明丛林图。
- 源码冒烟：在临时存档目录写入 `qa-2285-1-LT1.save`（7,957 字节），随后读取；存档文件生成与读回均无异常。
- 源码 lint：Ren'Py 8.5.3，0 error。
- Windows 构建：2.28.5 源码重新生成 `build/windows`，含新版 `10_hud.rpyc` 与 `portrait_jungle_solid.png`。

## 3. 产物

- `WuXian-2.28.5.apk`
- `WuXian-Setup-2.28.5.exe`
- `WuXian-2.28.5-win.zip`
- `SHA256SUMS-2.28.5.csv`

校验值以 `dist/SHA256SUMS-2.28.5.csv` 为准。

## 4. 已知限制

- Windows 端到端存读档仍以 2.28.5 的冒烟测试为准；未做全路线逐章回归。
- Android 2.28.5 未重新安装到真机，只做构建与签名检查。
