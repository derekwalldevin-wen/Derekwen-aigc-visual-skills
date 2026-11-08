---
name: everyone-in-the-booth
description: >-
  使用一张朋友、家庭或同事合照制作“全员进棚”上下双生对照：上半忠实保留原始合照，
  下半让数量与顺序完全相同的人进入1980年代复古录音棚演唱；
  严格锁定每张脸、发型、主要服装与相对位置，避免增人、换脸、话筒遮脸。
  用户提到“全员进棚”“合照变合唱团”“朋友出道现场”“谁当主唱”时调用。
compatibility: >-
  实际图片需要宿主提供有权限的图像生成或编辑工具；
  参考图模式必须能读取用户上传合照。Skill本身不是模型，也不安装工具。
metadata:
  author: 德里克文
  version: "1.0.0"
  status: "example-generated"
  source_case: "dw-everyone-in-the-booth"
---

# 全员进棚｜Everyone in the Booth

## 目标

把【源图：合照】转成同一张3:4竖版**上下双生**图：上半为原来的我们，下半为同一群人进入复古录音棚后的合唱画面。上下两组人员能够按原有左右顺序逐个对应，形成“这群人，谁最有主唱相”的社交互动。与单纯换背景不同，必须设计有分工、有视线关系的群像合唱现场。

## 输入参数

- 【源图】清晰合照，优先3–5人；不要求用户提供额外人物表。
- 【主体】原合照的全部人物；禁止新增、删减、合并或替换。
- 【主唱序号】从左到右第【几】人，默认选画面中自然靠近视觉中心者；不改变原有左右顺序。
- 【色彩】上下主体服装主色保持一致；下半使用暖色录音棚灯光和适度胶片颗粒。
- 【构图】3:4竖版，单张上下1:1对照，中间窄硬分隔；主体脸部完整。
- 【输出模式】默认无文字最终成图；教学图或标题设计另行排版，不往核心双生结果叠字。
- 【场景变体】朋友局／家庭局／同事局；统一回到“多人录音棚合唱”的方法，不另造一个Skill。

## 创作步骤

1. **审核素材**：确认照片是用户有权使用的群像；私人、未授权或来源不明真人照片不可公开进入案例库。对单张图记录人数、从左到右序号、每人的发型/服饰/脸部特点和是否被物体遮挡。
2. **建立对应表**：第1到第N人逐一映射，上下人数与顺序不变，尤其不把相似发型的人交换身份。
3. **上半锁定原照**：只保留原图内容，必要时添加中性留边适配画幅；不重画、不变脸、不换衣、不改变真实合照场景。
4. **下半场景重构**：木质吸音墙、卷盘录音机、调音台和暖灯构成1980年代录音棚；一组人围绕话筒，佩戴有线监听耳机。
5. **差异化动作**：指定第【几】人领唱，其余分担看歌词、侧耳听同伴、打拍子、笑场和和声；视线围绕话筒与彼此，而非所有人对镜头摆拍。
6. **遮挡与物理关系**：话筒和防喷罩偏离脸部；歌词纸不高于胸口；耳机贴合头部、佩戴位置与头发遮挡合理。
7. **生成及核验**：在图像工具中输入照片与主提示词，输出一张完整3:4双生图；逐个核对人数、左右顺序、衣着、脸部和动作。

## 5分钟上手版｜当日可核实核心提示词

```text
把上传的合照做成一张3:4竖版上下双生对比图。

上半部分保留原照片，下半部分把同一群人变成复古录音棚里的合唱团。上下人物数量相同，左右顺序一致，每个人的脸、发型、主要服装都能一一对应。

下半部分让大家戴上监听耳机，围着录音话筒演唱：有人投入领唱，有人看着歌词和声，有人笑着打拍子。每个人动作和表情不同，人物之间有自然互动。木质录音棚、暖色灯光、模拟录音设备、轻微胶片颗粒，写实摄影质感。

只输出一张包含上下两部分的完整图片，不增加人物，不遮住脸，不加文字。
```

可追加：
`从左到右，第【几】个人当主唱，其他人负责和声。`

## 完整版｜当日最终教程提示词

```text
使用上传合照作为所有人物的唯一身份参考，生成一张3:4竖版、上下双生的写实摄影对比图。两部分各占约一半高度，中间仅用一条细窄分隔线，不添加其他小图。

【上半部分：原来的我们】
忠实保留原照片中的人物、表情、动作、服装、背景和色彩。完整呈现所有人的脸，不重新设计原照片，不把原照片也改成录音棚。若比例不匹配，使用窄幅中性留边，不拉伸人物。

【下半部分：合唱团出道现场】
把原照片中完全相同的一群人放进复古录音棚。严格保持人物数量及从左到右的对应顺序，保留各自的脸部辨识特征、年龄感、肤色、发型、体型和主要服装。人物大小与上半部分接近，便于逐人比较。

让第【几】个人担任主唱，身体略向话筒前倾，自然张口演唱；其他人根据人数分别安排看歌词和声、侧耳听同伴、抬手打拍子或相视而笑。不要所有人做相同动作，也不要所有人都直视镜头。

人物戴有线监听耳机，耳罩贴合双耳，头梁与头发有正确遮挡。歌词纸拿在胸口以下，话筒与防喷罩略偏离面部，不遮住眼睛、鼻子和嘴。人物视线围绕歌词、话筒和同伴组织，形成正在一起唱歌的关系。

场景使用木质吸音墙、模拟调音台、卷盘录音机与暖色工作灯，表现1980年代录音棚的视觉氛围。肤色自然，衣料和头发有真实细节，轻微胶片颗粒，不做浓重泛黄或塑料磨皮。

上下两部分中的人物必须一一对应；改变场景、动作与表情，不交换身份，不增加或遗漏人物，不复制同一张脸。单张完整成品，无标题、字幕、标志或水印。
```

## 英文复用版（基于上述最终中文版整理，非另行模型实测）

```text
Create a single 3:4 vertical photorealistic top-and-bottom twin comparison from 【source group photo】, using that photo as the sole identity reference for all 【N】 people. Each panel occupies roughly half of the canvas and is separated by a clean narrow divider.

TOP — Original group photo: preserve the original people, count, left-to-right order, faces, hairstyles, main clothing, expressions, environment and visual colors. Do not redraw or reinterpret the original scene. Use thin neutral padding when the source aspect ratio differs; never stretch people.

BOTTOM — Everyone in the Booth: move exactly the same people into a warm 1980s analog recording studio with wood acoustic panels, reel-to-reel tape machines, a mixing console and soft practical lighting. Preserve each person's unique identity, age impression, body shape, hairstyle, clothing palette and exact left-to-right index. Person 【lead singer index】 sings naturally toward a microphone; other people harmonize, read lyric sheets, keep time or exchange amused looks. Each person has a different natural action. Real wired monitoring headphones must sit correctly on the head. Keep microphones, pop filters and papers below or to the side of important facial features. Filmic but natural skin, textile detail, restrained film grain.

The viewer must be able to match every person between panels at a glance. One combined image only. No added or missing people, no swapped faces, no duplicated heads, no hidden faces, no text, logos, captions or watermarks.
```

## 关键控制点

- **人数锁**：上半N人，下半只能N人。
- **身份锁**：每一组“脸—发型—主要服装”能纵向一一对应；不允许通用青年脸替代。
- **顺序锁**：从左到右永不交换；领唱的选定序号固定。
- **动作差异**：每人有角色和互动，禁止整齐站立对镜头合唱。
- **脸部可见**：话筒、防喷罩、歌词纸不得覆盖眼、鼻、嘴；耳机避免与头发穿模。
- **双生完整性**：一张图、上下各半、细分隔线；上方保留原照，下方才进行表演重构。
- **材质与时代感**：木质录音棚、模拟设备、暖光和轻胶片颗粒；避开塑料磨皮和重度黄色滤镜。

## 失败纠偏

| 失败现象 | 纠正方式 |
|---|---|
| 人数增加、减少或两人合一 | 逐行指定“第1人至第N人”并强调数量锁；减小同框拥挤程度 |
| 人物换脸、服装变色、左右顺序乱 | 强化“唯一本人参考 + 左右索引锁 + 主服装颜色延续”，逐人返查 |
| 上半被重画或背景改成录音棚 | 明确“原照只作为上半，禁止重绘；必要时中性留边” |
| 一排人都看镜头或动作相同 | 指定主唱、和声、歌词、节奏、笑场及互看等不同角色 |
| 耳机、话筒、歌词遮脸 | 将道具移到脸旁、纸降至胸口以下，维持正确的耳机佩戴遮挡 |
| 画面过度复古发黄、出现塑料脸 | 退回自然肤色、低强度胶片颗粒和局部暖光 |
| 输出多张分离图片或出现字幕 | 固定“一张完整3:4双生图，默认无字，无logo，无水印” |

## 质量验收

至少核对：①原合照仍被忠实保留；②人物总数及从左到右顺序严格对应；③脸与主要衣着可辨；④复古录音棚空间可信；⑤人物动作有不同分工；⑥脸无遮挡、手/耳机/麦克风关系合理；⑦单张3:4上下双生图，无意外文字。

## 适用场景、来源与实测边界

适合朋友合照互动、家庭“出道曲”、同事下班合唱及小红书/微博/X玩法教学。用户在**2026-11-08（北京时间）**明确选定《全员进棚》的上下双生方向，同日6张3:4教学与示例图片实际生成，见 Case：`data/cases/dw-everyone-in-the-booth.yaml`。快速版和中文版完整版来自当天可核实教程内容；英文版为复用译写。当天6张图是教程演示及合成合照示例，并**不证明**已用用户上传的真实多人合照进行身份保持盲测。具体生成模型版本和逐图API调用参数尚未查实，不编造。实质验证范围为本主题的视觉样例与教程出图。
