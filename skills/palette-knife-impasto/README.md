# 刮刀堆色 / Palette Knife Impasto

将照片中的主体重构为真实可见刮刀方向、油彩堆叠和微阴影的厚涂油画。支持单主体3:4作品和同主体上下双生对比海报。

**Output:** Image  
**Source Case:** [dw-palette-knife-impasto](../../data/cases/dw-palette-knife-impasto.yaml)  
**Tutorial:** [AI绘画每日一词｜刮刀堆色](../../daily-words/2026/11/palette-knife-impasto.md)

[阅读完整 SKILL.md](./SKILL.md)

## 调用示例

```text
使用 palette-knife-impasto 处理我上传的花束照片。
保留花束轮廓和主色，生成3:4单主体暖白纸底刮刀厚涂油画；
强调颜料脊线、沟槽、翘边和左上侧光，不要文字。
```

```text
使用 palette-knife-impasto 的上下双生海报模式。
上半保留我提供的已授权原图，下半将同一主体变成刮刀堆色作品。
上下保持人物与机位一致。
```

## 安装

```bash
cp -R skills/palette-knife-impasto ~/.claude/skills/
```

## 资产与许可

教程已有真实生成案例；9张最终图片目前记录在Case的待上传清单中，**尚无可公开展示的仓库图片链接**，这里不添加占位图。

Skill 指令遵循仓库 [MIT License](../../LICENSE)，视觉资产遵循 [ASSET-LICENSE.md](../../ASSET-LICENSE.md)。
