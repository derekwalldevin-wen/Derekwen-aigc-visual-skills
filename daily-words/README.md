# AI绘画每日一词 · Daily Words

「AI绘画每日一词」是 **DerekWen AIGC Visual Library** 的持续内容来源。

每条内容先作为一个 **Case** 记录；当多个 Case 形成稳定共性后，可以进一步沉淀为 Template；只有具备输入判断、执行逻辑、一致性控制、失败检查和明确交付流程的方法，才适合升级为 Skill。

```text
Daily Word → Case → Template → Skill
```

## 最新收录 · 2026-09-23

<table>
<tr>
<td align="center" width="33%"><a href="./2026/09/high-signal-two-color-branding.md"><img src="../assets/daily-words/2026/09/high-signal-two-color-branding.webp" alt="高信号双色品牌视觉" width="100%"></a><br><b>高信号双色品牌视觉</b></td>
<td align="center" width="33%"><a href="./2026/09/night-flash-motion-twin.md"><img src="../assets/daily-words/2026/09/night-flash-motion-twin.webp" alt="夜闪拖影双生" width="100%"></a><br><b>夜闪拖影双生</b></td>
<td align="center" width="33%"><a href="./2026/09/path-narrative-3d-scene.md"><img src="../assets/daily-words/2026/09/path-narrative-3d-scene.webp" alt="路径叙事式3D场景" width="100%"></a><br><b>路径叙事式3D场景</b></td>
</tr>
</table>

[完整视觉 Gallery](../GALLERY.md) · [机器可读 Latest](../data/latest.json)

## Case 状态

- **experimental**：概念或方法已经形成，但可靠实测证据仍不完整。
- **tested**：已经实际执行过。
- **verified**：已经复核并确认可以稳定复用。

历史回填与方法成熟度是两回事。历史条目使用 `source.type: recovered-history`；正文、提示词、图片等恢复程度记录在 `evidence` 中。

## 历史回填原则

如果原始发布日期、最终提示词、模型、图片或权属没有可靠证据，就保留 `null` / `pending` / `not-found`，而不是补造。

仓库优先复用历史真实生成资产；只有历史资产无法找回、不能公开或质量不足时，才重新生成。

## 数据入口

- [完整视觉 Gallery](../GALLERY.md)
- [Latest](../data/latest.json)
- [Case 数据](../data/cases/)
- [Case Schema](../data/CASE-SCHEMA.md)
- [Case 索引](../data/case-index.json)
- [统计](../data/stats.json)
- [Skills](../skills/)

Template 目录在正式 Template 发布后再作为公开入口；规划中的 Template 引用不会计入已发布 Template 数量。
