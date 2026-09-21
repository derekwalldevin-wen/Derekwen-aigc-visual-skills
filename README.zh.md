<div align="center">

**中文** · [English](./README.md)

# 德里克文 AIGC 视觉 Skills

**一套来自「AI绘画每日一词」长期实战的开源视觉生成 Skill 集合。**

![Skills](https://img.shields.io/badge/SKILLS-10-2ea44f?style=flat-square&labelColor=333)
![Version](https://img.shields.io/badge/COLLECTION-1.0.0-214f9b?style=flat-square&labelColor=333)
![License](https://img.shields.io/badge/LICENSE-MIT-e37f2c?style=flat-square&labelColor=333)
![Author](https://img.shields.io/badge/AUTHOR-%E5%BE%B7%E9%87%8C%E5%85%8B%E6%96%87-7d4cdb?style=flat-square&labelColor=333)

</div>

这不是一组零散 Prompt，而是一套可部署的视觉工作流。每个 Skill 都包含：触发入口、输入路由、构图 / 风格逻辑、主体一致性规则、实际工具执行规则、失败判定与质量检查。

## 当前 Skills

| Skill | 用途 | 默认交付 |
|---|---|---|
| [昼夜双生海报](./skills/day-night-dual-poster/) | 同一主体与构图，在昼 / 夜两个时间状态之间建立高稳定对照 | 图片 |
| [几何平涂双生海报](./skills/geometric-flat-twin-poster/) | 原图 + 现代主义几何平涂转译 | 图片 |
| [怪诞手绘双生海报](./skills/quirky-handdrawn-twin-poster/) | 原图 + 彩铅 / 蜡笔 / 圆珠笔的情绪人格化手绘转译 | 图片 |
| [蚀刻概念双生海报](./skills/etched-concept-twin-poster/) | 原图 + 黑白复古蚀刻版画概念转译 | 图片 |
| [今昔胶片双生海报](./skills/then-now-film-twin-poster/) | 同一个人、同一个瞬间，在 2026 与 1985 两个年代重新发生 | 图片 |
| [角色设定板](./skills/character-sheet-board/) | 锁定角色身份、三视图 / 四视图、配色、表情、姿态、服装和手部系统 | 图片 |
| [材质化解释图](./skills/materialized-explainer/) | 把流程、层级、闭环、网络、对比等抽象关系变成白底实体模型解释图 | 图片 |
| [记忆切片肖像海报](./skills/memory-tile-portrait-poster/) | 用同一张连续肖像网格嵌入少量真实记忆 | 图片 |
| [影子剧场双生海报](./skills/shadow-theater-twin-poster/) | 真人 / 产品不变，只把真实投影转换为另一身份 | 图片 |
| [旗舰发布广告片](./skills/premium-product-launch-film/) | 按产品类型设计高级新品发布片，优先单次端到端生成完整广告视频 | 视频 |

## 为什么不是普通 Prompt 库

这套 Skills 重点解决的是**稳定执行**：

- 上传参考图时，主体身份与关键结构优先保留；
- 构图类 Skill 会根据画幅、主体轴向和裁切损失做判断，而不是机械套模板；
- 双生系列强调硬分割、同构图与禁止跨框；
- 解释图先判断信息结构，再决定流程 / 层级 / 闭环 / 网络等实体模型；
- 视频 Skill 默认以最终视频为完成标准，不用 Shot List 冒充成片；
- 每个 Skill 都写有失败条件与质量检查，可用于自动重试与团队协作。

## 安装

克隆仓库：

```bash
git clone https://github.com/derekwalldevin-wen/Derekwen-aigc-visual-skills.git
```

如果你的 Agent 以独立目录加载 Skills，可以复制需要的 Skill。以 Claude Code 为例：

```bash
cp -R Derekwen-aigc-visual-skills/skills/day-night-dual-poster ~/.claude/skills/
```

其他支持 `SKILL.md` 的 Agent 环境，可按各自的 Skill / 指令加载机制使用对应目录中的 `SKILL.md`。

## 快速试用

```text
用 day-night-dual-poster 处理这张照片。人物与机位保持不变，另一状态改成可信的夜景。
```

```text
用 geometric-flat-twin-poster 处理这张旅行照。原图保持构图，另一框转成现代主义几何平涂。
```

```text
用 shadow-theater-twin-poster。真人完全不变，但把我的真实影子变成消防员。
```

```text
用 character-sheet-board 处理这个角色，建立统一的角色设定板。
```

```text
用 materialized-explainer 解释 AI Agent 工作流：输入 → 理解 → 工具调用 → 执行 → 检查 → 输出。
```

## 开源策略

Skill 指令、说明文档与验证脚本采用 MIT License。视觉示例单独管理：只有确认拥有公开发布权的图片才进入 `examples/`，避免把测试素材或第三方图片直接并入开源许可。

详见 [`ASSET-LICENSE.md`](./ASSET-LICENSE.md)。

## 贡献

欢迎：

- 报告模型兼容性问题；
- 提交失败案例；
- 改进布局 / 一致性 / 光影物理规则；
- 提议新的「AI绘画每日一词」Skill；
- 补充适配不同图像 / 视频模型的实践经验。

请阅读 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

---

作者：**德里克文** · GitHub [@derekwalldevin-wen](https://github.com/derekwalldevin-wen) · X [@derek_wall90176](https://x.com/derek_wall90176)