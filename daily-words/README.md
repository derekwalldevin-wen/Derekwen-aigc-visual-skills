# AI绘画每日一词 · Daily Words

「AI绘画每日一词」是 **DerekWen AIGC Visual Library** 的持续内容来源。

每条内容先作为一个 **Case** 记录；当多个 Case 形成稳定共性后，可以进一步沉淀为 Template；只有具备输入判断、执行逻辑、一致性控制、失败检查和明确交付流程的方法，才适合升级为 Skill。

```text
Daily Word → Case → Template → Skill
```

## Case 状态

- **experimental**：概念或方法已经形成，但可靠实测证据仍不完整。
- **tested**：已经实际执行过。
- **verified**：已经复核并确认可以稳定复用。

历史回填与方法成熟度是两回事。历史条目使用 `source.type: recovered-history`；正文、提示词、图片等恢复程度记录在 `evidence` 中。

## 历史回填原则

如果原始发布日期、最终提示词、模型、图片或权属没有可靠证据，就保留 `null` / `pending` / `not-found`，而不是补造。

仓库优先复用历史真实生成资产；只有历史资产无法找回、不能公开或质量不足时，才重新生成。

## 最新收录 · 2026-09-25

- [玻璃错层 · Glass Layering](./2026/09/glass-layering.md)
- [四图合一 · Four-Reference Fusion](./2026/09/four-image-fusion.md)

两条均已完成图片公开安全检查；测试模型未获得可靠历史证据，因此没有补造具体模型名称。

## 数据入口

- [Case 数据](../data/cases/)
- [Case Schema](../data/CASE-SCHEMA.md)
- [Case 索引](../data/case-index.json)
- [统计](../data/stats.json)
- [Skills](../skills/)

Template 目录在正式 Template 发布后再作为公开入口；规划中的 Template 引用不会计入已发布 Template 数量。
