# 雾线 V2.28.2 Beta

> 一支四人小队，二十七天，穿过一张地图上没有的雨林。

这是《雾线》2.x 的全量旁白修整版。30 个剧情文件全部过稿，71 处连续短句完成合流，`ch01` 的开场与 `ch25` 的封站段单独重写；角色台词与 482 条配音引用未动，不需要重配。

## 本次更新

- 全量旁白 / 内心节奏重排，减少连续断句造成的翻页碎片感。
- `ch01` 无线电冷开场、晨起清点、折地图、青岩绕绳四段重写。
- `ch25` 封站玩家台词改为“封。连来路一起留在里面。”
- 8 个结局与结局 CG 全部保留；三条恋爱线 + 封口 + 第七天。
- lint：0 error / 0 warning；2037 个对话块、108,608 字、100 个菜单、286 个选择。

## 下载

| 文件 | 大小 | SHA256 |
| --- | ---: | --- |
| `WuXian-Setup-2.28.2.exe` | 327,261,528 | `00013C0ECAC6EF584C20D7B72D0E57257DB49AF2E763DF19EE05CCA111D175E3` |
| `WuXian-2.28.2-beta-win.zip` | 344,142,782 | `E7216486B214EF62549D1ABC1796C665E35CF1FF9D68D71EEB03426EDF177B16` |
| `WuXian-2.28.2-beta.apk` | 370,322,648 | `23C646FE69BB4FA8B29847202DC064D1E9961578584071109A5CE9BF6ADE2A87` |

Windows 安装包已写入 Authenticode 签名，证书为自签名 `CN=WuXianSukaKanger`，时间戳由 DigiCert 提供。自签名根不受公共信任，其他机器仍可能显示“未知发布者”；这不是 CA 签发证书，正式分发前应替换为 OV/EV 代码签名证书。

Android APK 使用项目自有 keystore 签名，包名 `com.sukakanger.wuxian`，versionName 2.28.2，versionCode 1795195859，minSdk 21，targetSdk 36。

## 已知限制

- 2.28.2 只提供 Windows 与 Android 构建，没有重新生成 Web 构建。
- Android APK 已完成元数据与签名校验，尚未在本轮做真机首启。
- 安装包为自签名，SmartScreen 仍可能拦截；校验值以 `SHA256SUMS-2.28.2.csv` 为准。

完整变更记录见 `game/_docs/CHANGELOG.md`。
