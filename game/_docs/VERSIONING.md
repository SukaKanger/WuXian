# 版本号规则（VERSIONING）

> 单一真值文件：`game/core/05_version.rpy`。全仓界面只通过 `[config.version]` 插值引用，
> 不得在任何 `.rpy` 里硬编码版本串。`game/options.rpy` 不再重复赋值。

## 1. 规则

### 1.1 内部版本号

- 结构：**年份（4 位）+ 第几代序号（4 位）**，无分隔符。
- 形如 `20260002`：年份 `2026`，代序号 `0002`。
- 代序号只有在**新一代/大改版**时才 +1；普通章节推进、补丁不动内部号。

### 1.2 外部版本号

- 结构：`V<大版本>.<章节数>.<补丁号> <阶段>`，形如 `V2.28.0 Beta`。
- **第一位（大版本）**：`1` 为初版系列，`2` 为 2.x 系列；只有大改版才动。
- **第二位（章节数）**：已完成章节数；每完成一章 +1。
- **第三位（补丁号）**：修 bug / 小修 +1；发新章节时归零。
- **阶段后缀**：早期测试带 `Demo`，公开测试带 `Beta`，转正带 `GA`（与版本号之间一个空格）。

> 因为第二位是章节数，2.x 的第一版是 **`V2.28.0 Beta`**，不是 `V2.0.0`。
> `V2.0.0` 会表示“2.x 系列、0 章完成”，与当前工程事实不符。

### 1.3 当前取值

| 项 | 值 | 来源常量 |
| -- | -- | -------- |
| 内部版本 | `20260002` | `VN2_VERSION_YEAR` + `VN2_VERSION_GEN` |
| 外部版本 | `V2.28.0 Beta` | `VN2_VERSION_MAJOR` / `VN2_VERSION_CHAPTERS` / `VN2_VERSION_PATCH` / `VN2_VERSION_STAGE` |

## 2. 常量清单（`game/core/05_version.rpy`）

| 常量 | 当前值 | 含义 | 什么时候动 |
| ---- | ------ | ---- | ---------- |
| `VN2_VERSION_MAJOR` | `2` | 大版本号 | 仅大改版 |
| `VN2_VERSION_YEAR` | `2026` | 内部版本年份 | 跨年换代时 |
| `VN2_VERSION_GEN` | `2` | 第几代序号（内部号补零到四位） | 新一代/大改版 |
| `VN2_VERSION_CHAPTERS` | `28` | 已完成章节数（ch01–ch28） | 每完成一章 +1 |
| `VN2_VERSION_PATCH` | `0` | 补丁号 | 修 bug / 小修 +1 |
| `VN2_VERSION_STAGE` | `"Beta"` | 阶段：`"Demo"` 早期测试 / `"Beta"` 公开测试 / `"GA"` 转正 | 进入 Beta 或转正时改 |

拼合产物（一般不需要手改）：

- `VN2_VERSION_INTERNAL` = `"%04d%04d" % (VN2_VERSION_YEAR, VN2_VERSION_GEN)` → `20260002`
- `config.version` = `"V%d.%d.%d %s" % (...)` → `V2.28.0 Beta`

## 3. 以后要改哪一行

| 场景 | 只改这一处 | 外部号变化 | 内部号变化 |
| ---- | ---------- | ---------- | ---------- |
| 新写完一章 | `VN2_VERSION_CHAPTERS` +1 | 第二位 +1（如 `28 → 29`） | 不变 |
| 修 bug / 小修 | `VN2_VERSION_PATCH` +1 | 第三位 +1；随新章节发布时归零 | 不变 |
| 转正 GA | `VN2_VERSION_STAGE` 改为 `"GA"` | 后缀 `Beta → GA` | 不变 |
| 进入公开测试 | `VN2_VERSION_STAGE` 改为 `"Beta"` | 后缀 `Demo → Beta` | 不变 |
| 大改版 / 新一代 | `VN2_VERSION_MAJOR` +1；`VN2_VERSION_GEN` +1；`VN2_VERSION_PATCH` 归零 | 第一位 +1，其余归零 | 代序号 +1 |
| 跨年 | `VN2_VERSION_YEAR` 改为新年份 | 不变 | 年份段更新 |

> 章节数变化只动 `VN2_VERSION_CHAPTERS` 这一个常量，内部号与外部号章节位同时由拼合公式更新。

## 4. 转 GA 怎么做

1. 在 `game/core/05_version.rpy` 把 `VN2_VERSION_STAGE` 从 `"Beta"` 改成 `"GA"`。
2. 收尾调试入口与关于页里的**描述性文案**（不是版本串本身）：关于页「版本」区块不再保留「开发版」状态说明。
3. 归档/构建前确认 `VN2_VERSION_PATCH` 已归零、`VN2_VERSION_CHAPTERS` 与实际完稿章节一致。

## 5. 补丁号怎么加

- 修 bug、改文案、调数值等小修：`VN2_VERSION_PATCH` +1。
- 随新章节发布时，补丁号归零，章节数 +1。
- 2.x 系列起步使用 `VN2_VERSION_PATCH = 0`。

## 6. 界面引用约定

- 界面文本一律写 `text "[config.version]"`（方括号插值），不要写 `"v" + config.version`，也不要手写 `V2.x.x`。
- `config.version` 在全仓只赋值一次（`game/core/05_version.rpy`）；`game/options.rpy` 仅留指向注释。
- 与存档 schema 区分：`VN2_SAVE_SCHEMA`（`core/00_state.rpy`）是存档兼容层版本，与游戏版本号无关，独立维护。
- 默认模板 `game/screens.rpy` 里的 `[config.version]` 文本为 Ren'Py 自带界面，保留不动。

## 7. 2.x 起步状态

- 外部版本：`V2.28.0 Beta`
- 内部版本：`20260002`
- 章节：ch01–ch28
- 阶段：公开测试，不标 GA
- `config.save_directory = "WuxianVN2-1"` 保持不变，1.28.x 存档继续可读
- 发行目录：`WuXian-2.28.0-beta`
- Android `build.version`：`2.28.0`；`versionCode` 由 Ren'Py 构建时按时间戳递增，不手写
