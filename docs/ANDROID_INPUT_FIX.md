# Android 中文输入热修（2.28.3）

## 问题

命名 / 改名输入框在 Android 上弹出密码键盘，中文 IME 无法正常上屏。原因是 Ren'Py 8.5.3 的 Android SDL 模板把 `DummyEdit` 的输入类型写死为：

```java
InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_VISIBLE_PASSWORD
```

`VISIBLE_PASSWORD` 会让系统把它当成密码/ASCII 输入，中文输入法被切成不可用状态。

## 修复

改成标准文本输入：

```java
InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_NORMAL
```

需要同时改两份模板，否则换构建入口还会复发：

- `D:\renpy-8.5.3-sdk\rapt\project\renpyandroid\src\main\java\org\libsdl\app\SDLActivity.java`
- `D:\renpy-8.5.3-sdk\rapt\prototype\renpyandroid\src\main\java\org\libsdl\app\SDLActivity.java`

位置都在 `DummyEdit.onCreateInputConnection(EditorInfo outAttrs)` 里。

## 重新构建

```powershell
$py='D:\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe'
& $py 'D:\renpy-8.5.3-sdk\renpy.py' 'D:\renpy-8.5.3-sdk\launcher' android_build 'L:\AI\FurryVN\20261117_uidemo' --destination 'L:\AI\FurryVN\20261117_uidemo\dist'
```

构建后把新 APK 统一改名为 `WuXian-2.28.3-beta.apk`，并重新生成 `SHA256SUMS-2.28.3.csv`。

## 验证点

- 新游戏命名页点输入框：系统键盘是普通文本键盘，不是密码键盘。
- 切换中文输入法可以上屏；确认后 `player_name` 正常写入。
- 改名入口同样验证一次。
- 旧 APK 的哈希作废，以 `SHA256SUMS-2.28.3.csv` 的新值为准。
