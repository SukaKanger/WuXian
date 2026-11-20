<div align="center">

# 雾线 · WuXian

**一支四人小队，二十七天，穿过一张地图上没有的雨林。**

[![itch.io](https://img.shields.io/badge/itch.io-WuXian-fa5c5c?style=flat-square)](https://sukakanger.itch.io/wuxian)
[![License: MIT](https://img.shields.io/badge/code-MIT-3da639?style=flat-square)](LICENSE)
[![Story: CC BY 4.0](https://img.shields.io/badge/story-CC%20BY%204.0-ef9421?style=flat-square)](LICENSE-ASSETS.txt)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Android-4c8bf5?style=flat-square)](#下载)
[![Version](https://img.shields.io/badge/version-2.28.2%20Beta-d4a017?style=flat-square)](https://github.com/SukaKanger/WuXian/releases)

</div>

---

## 这是什么

《雾线》是一部兽人题材的视觉小说：四名队员带着一张残缺的地图进入雨林，去找一座「从地图上消失」的旧站。二十七天，一条共同线加三条恋爱线，28 章，8 个结局。

- 全程免费，无内购、无广告、无付费墙
- Ren'Py 制作，Windows / Android 双端
- 24 张正片 CG，每张有独立的入画演出（滑入、推近、黑场、换曲）
- 游戏内「笔记本」会随每一局记录你查到的情报

## 下载

| 平台 | 获取方式 |
| --- | --- |
| Windows | [最新 Release](https://github.com/SukaKanger/WuXian/releases) 里的 `WuXian-Setup-2.28.2.exe`（解压式安装向导，可选路径与快捷方式） |
| Android | 同一 Release 里的 `WuXian-2.28.2-beta.apk` |
| 全部版本 | [itch.io](https://sukakanger.itch.io/wuxian) |

校验：APK 使用项目自有 keystore 签名；Windows 安装包已写入 Authenticode 签名（自签名证书 `CN=WuXianSukaKanger`，DigiCert 时间戳），但自签名根不受公共信任，其他机器仍可能提示“未知发布者”。完整校验值见 Release 里的 `SHA256SUMS-2.28.2.csv`。

## 许可

| 内容 | 许可 |
| --- | --- |
| 代码（Ren'Py 脚本、界面、工具） | **MIT** — 见 [LICENSE](LICENSE) |
| 原创剧情、角色设定、文本 | **CC BY 4.0** — 见 [LICENSE-ASSETS.txt](LICENSE-ASSETS.txt) |
| AI 生成图像素材 | 随作品开放二创，注明来源 |
| 引擎与第三方库 | 各自许可（Ren'Py / Python / SDL2 等） |

商用、修改、再分发都允许；保留版权声明，别把改版冒充官方原版，别把本体拿去卖。

## 免责声明（摘要）

完整版见 [DISCLAIMER.txt](DISCLAIMER.txt)。

- **虚构作品**：人物、地点、事件均为原创或虚构，与现实无关。
- **内容提示**：兽人角色、同性恋爱分支、轻度暴力、伤病、死亡与失踪描写、家庭创伤与药物相关描写；无露骨性内容。未满 16 岁请在监护人知情下游玩。
- **AI 参与**：立绘、表情差分、背景、CG 与配音使用 AI 生成并经人工筛选；可能存在细节偏差。
- **按现状提供**：不附带任何担保，作者不对因使用本作产生的损失负责。

## 玩家交流

QQ 群 **1134240122**（报版本号，方便定位 bug）

其他入口：[B站](https://b23.tv/3dPhiDD) · [爱发电](https://afdian.com/a/RoryMarshall) · [VLink 聚合](https://vlink.cc/sukakanger) · [itch.io](https://sukakanger.itch.io/wuxian)

## 从源码构建

需要 Ren'Py 8.5.2 SDK 与 JDK 21（Android）。

```bash
# 桌面运行
renpy.exe /path/to/WuXian

# Windows 包
renpy.exe launcher distribute /path/to/WuXian --package win --destination build

# Android
renpy.exe launcher android_build /path/to/WuXian
cd rapt/project && gradlew.bat --no-daemon assembleRelease

# Web
renpy.exe launcher web_build /path/to/WuXian
```

工程结构：

```
game/
  core/     系统层：版本、音频、存档、CG 演出、画廊数据
  story/    28 章正文与 8 个结局
  ui2/      主菜单、HUD、笔记本、画廊、关于页
  images/   背景、立绘、CG（cg01–cg24）、界面素材
  audio/    BGM、环境音、界面音效
_tools/     构建与素材处理脚本
```

## 致谢

Ren'Py 引擎与开源社区；所有在 itch.io、GitHub 和群里反馈过 bug 的玩家。

> 这是我 SukaKanger 的第一部作品。它还有很多不足，但我不会设付费墙，也会一直做下去。
