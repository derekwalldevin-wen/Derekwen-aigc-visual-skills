---
name: clay-sculpt-graymodel
description: >-
  将照片中的人物、宠物、器物、产品、植物、建筑或原创角色转为细节可读的单色雕刻灰模，
  或制作上半彩色参考、下半雕刻灰模的3:4上下双生海报。保留主体形态、姿势、
  关键结构和材质纹理，但统一表面为中性灰黏土/树脂雕塑表现；
  适用于视觉教程、创作挑战、角色或产品造型研究。关键词：雕刻灰模、灰模、
  clay sculpt、clay render、上下双生。
metadata:
  author: 德里克文
  version: "1.0.0"
  source_case: "dw-clay-sculpt-graymodel"
  evidence: "12 model-generated images dated 2026-11-06; exact original prompting not recovered"
---

# 雕刻灰模｜Clay Sculpt Graymodel

## 任务

将一个现实/彩色主体重构为**有三维体积、连续实体表面、真实微阴影、可读结构**的中性灰雕塑。既能输出纯灰模，也能将彩色参考与灰模上下对照展示。所有说明均将“视觉风格化图像”与可供制造的真实3D模型分开：输出是**静态图像**，不等于已生成网格、贴图、可旋转3D资产或可打印文件。

> 实证边界：2026-11-06当天找到6张「雕刻灰模」教程图及6张「雕刻灰模上下双生」成图。两种输出模式均有实际生成的图像证据；但无法直接取回逐字生图提示词、修改对话与模型调用日志。因此，下文是依据实际视觉结果总结的**可复用提示词方案**，不是逐字复刻的已实测原始Prompt；精确测试模型保持未知。

## 何时使用

- 拟把【源照片】或【指定主体】变成单色雕塑/工业灰模概念图；
- 需要展示「彩色外观→雕塑结构」的视觉对照；
- 角色、宠物、家用器物、微缩玩具、植物、建筑的外形研究；
- 小红书/微博/海外X的3:4创意教程图；
- 不适用：直接导出STL/OBJ、真正3D建模、精确测量或逆向工程。

## 输入与变量

| 变量 | 要求 |
| --- | --- |
| 【源图】 | 可选：有权使用的照片/自己生成的原图；没有源图时只能生成虚构的彩色示例，不能称为“真实原照” |
| 【主体】 | 一名人物、一只宠物、一件物品、一组明确主次的植物、一栋建筑或原创角色 |
| 【锁定特征】 | 主体轮廓、姿势、朝向、五官/表情、比例、标志性零件、重要形体细节 |
| 【灰模材料】 | 默认中性灰、哑光、黏土/树脂般连续表面，可选择细腻雕刻痕迹 |
| 【构图】 | 3:4竖版，单体清楚；上下双生时上下约1:1 |
| 【光线】 | 柔和侧上方棚拍光，明确形体起伏与阴影 |
| 【输出模式】 | A：纯灰模单图；B：彩色参考／灰模上下双生；C：同图教学海报（明确要求才加标题） |
| 【背景】 | 单色灰模默认浅灰/白无缝棚拍背景；双生上半参考场景可保留，下半可改干净背景 |
| 【色彩】 | A与B的灰模区统一中性灰，避免局部保留原色；上半彩色保留物体原色 |

## 生成步骤

1. **确认源图身份与公开权限。** 如果是上传的个人照片、他人肖像或商业产品素材，先明确能否公开。生成中的彩色上半画面如果没有真实源图，只能标记为AI生成的视觉示范。
2. **提取不变锚点。** 在原始主体上列出3—6个最易辨识的轮廓或结构：人物的发型/服装/姿态，宠物的耳朵/口鼻/躺卧姿态，器物的手柄/旋钮/壶嘴，建筑的门窗/屋顶/楼层比例。
3. **只转换材料，不随意重设计。** 将表面统一为哑光中性灰的雕刻实体；布料褶皱、毛发层次、植物叶脉、鞋面缝线、建筑砖缝以浅浮雕/几何起伏保留。
4. **重建体积感。** 用雕塑表面高光、阴影、轮廓遮挡和物体接地说明真实凸凹关系；不能仅降低饱和度或套黑白滤镜。
5. **输出选择。** A模式单张全灰模；B模式3:4，上半彩色、下半灰模，尽量固定拍摄角度、构图与主体身份；C模式可使用图上大标题/中英副标，不遮挡主体。
6. **检查不变项。** 对比原物体与灰模的结构、姿势、比例、道具数量和透视。若原图身份有明显改变，则不应宣称“严格一致”。
7. **图片与来源验收。** 所用案例必须是已经生成、可解码且权属可审的原图；不能用占位图。

## 5分钟中文版快速提示词（规范化复刻版）

```text
请参考【源图】中的【主体】，生成一张3:4竖版【输出模式】作品。
保持【主体】的身份、主要轮廓、姿态、朝向、比例、标志性特征和【锁定细节】。
把主体完整重构为真实三维雕刻灰模：全体统一中性灰哑光黏土/树脂材质，
形体连续且有厚度；保留真实凹凸结构、浅浮雕细节、边缘转折、缝线/纹路，
通过柔和侧上方灯光表现结构投影和接触阴影。
【输出模式】=单张灰模时：只显示灰模，干净浅灰或白色棚拍背景。
【输出模式】=上下双生时：一张竖版图上下各约一半；上半为彩色参考视图，
下半是同一主体、相近构图与姿态的中性灰雕刻灰模；下方不是简单黑白滤镜，
不保留原场景色彩。画面清楚、形体可比较、背景不干扰主体。
默认无文字。若指定【标题】，可在留白位置加醒目的中英标题。
禁止额外人物、结构丢失、错乱手指、漂浮道具、塑料玩具高反光、
彩色残留、纯去饱和滤镜、未要求的水印或商标。
```

## English reusable prompt (for X / image creation)

```text
Create a vertical 3:4 【OUTPUT MODE】 image based on 【SOURCE PHOTO】 of 【SUBJECT】.
Preserve the recognizable silhouette, proportions, pose, viewpoint, identity cues and
【LOCKED STRUCTURAL DETAILS】. Rebuild the subject as a cohesive neutral-gray
clay-sculpt maquette: a continuous matte sculptural material, with readable physical
volume, raised and recessed details, sculpted folds / seams / fur strands / leaf veins /
architectural relief as appropriate. Use soft directional studio lighting, nuanced
self-shadowing and credible contact shadows. This must look like a modeled solid,
NOT a monochrome photo or a desaturation filter.

For SINGLE mode: show one full gray maquette on a seamless light studio background.
For TWIN mode: create one 3:4 poster with a roughly 50/50 vertical split, colorful
reference scene in the upper half and the corresponding neutral gray sculpted subject
in the lower half. Keep the composition and pose as consistent as the reference permits.
Use minimal editorial typography only if requested: 【TITLE】.
Avoid changed anatomy, lost features, fragmented geometry, floating accessories,
shiny plastic, retained original colors in the clay section, extra objects, watermarks
and unauthorized brand logos.
```

## 控制点

- **灰模≠黑白滤镜：** 纹理变为可触知的雕刻起伏和形体高差。
- **主体识别：** 从色彩去除后仍能辨认原对象；眼睛、口鼻、发丝、鞋带、机械旋钮、植物叶缘等不能变成模糊团块。
- **一体材料：** 灰模区域主要是统一中性灰哑光材料，允许光影明暗，不允许彩色残留。
- **结构连续：** 附件、脚爪、枝叶、壶嘴或楼体结构要连接到主体。
- **双生对照：** 上下两半应表达同一主体，但已见案例中有构图、道具与姿态细微差异，不宣称像素级锁定。
- **原创与授权：** 没有真实照片时，上半彩色示意视为AI生成画面，不得冒充真实原照；未知真人或含第三方商标的示例不公开。

## 常见失败与纠偏

| 问题 | 修正 |
| --- | --- |
| 仅灰度照片、仍保留皮肤/布料实拍质地 | 强调 `fully modeled neutral clay maquette, solid relief geometry`，删除原色材质关键词 |
| 细节糊成一块 | 列出必须保留的3—6个识别点；使用浅浮雕、独立边线与柔光微阴影 |
| 身体比例、动物结构或建筑立面变化 | 锁定主体比例、姿态、门窗数量、足部数量与结构对应 |
| 局部仍是彩色或金属高光 | 禁止局部彩色，统一 `matte neutral gray, non-metallic` |
| 像光滑塑料玩具 | 增加哑光雕塑材质、微表面与雕刻形体，降低高光 |
| 双生上/下不匹配 | 锁定同一主体、朝向、三大构图锚点，并减少其他改造 |
| 社媒标题压住主体 | 标题移到留白；优先留住主角，非必要不加字 |
| 生成真人不像源图 | 使用有权编辑的真实参考图、明确脸部身份锚点；失败时放弃公开对比版本 |

## 质量验收

**必须具备：** 真实单色灰模体积、结构辨识、完整主体、合理接触阴影、清楚构图；双生模式要求上下可对比。**不要求：** 假称可输出真正3D模型、精准相同角度或特定模型100%稳定复现。任何源图/图片的版权和隐私权限都须单独审查。

## 来源与现有案例

- 来源日期：2026-11-06（北京时间）。用户文件库当天生成12张图，其中6张为「2026-11-06_雕刻灰模_01—06」，6张为「雕刻灰模上下双生_1—6」。文件记录为 `model_generated: true`。
- 安全审核：有未知面孔的人像双生第1张、带清晰第三方运动鞋标志的双生第3张，**不进入公开图集**；其余10张为待上传的公开候选。
- **精确模型、原始逐字提示词及用户最后修改对话均未能核实，禁止编造。** 本文件的完整复刻提示词是根据已见视觉作品抽象整理，尚无独立复测结论。
- 关联Case：`data/cases/dw-clay-sculpt-graymodel.yaml`。
