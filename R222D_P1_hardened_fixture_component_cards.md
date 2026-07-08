# R222D-P1 Hardened Fixture Component Cards

```text
stage_id=1013R_R222D_P1_COMPONENT_PEDAGOGICAL_HARDENING
status=static_pedagogical_hardening_only
fixture_component_count=12
active_component_count=0
```

P1 只加厚 12 个 fixture 组件，不启动 R223，不开 UI，不动 R97B，不接大屏 runtime。

## 比一比 (`compare_two_images`)

- Component type: `comparison_judgment`
- Student problem solved: 学生能看到两张图或两个作品不一样，但说不清差异服务哪个美术知识点，容易停留在“好看/不好看”“像/不像”的直觉判断。
- Why use: 对比能把抽象标准放到同一视野里，让学生从线条、形状、色彩、构图、材料效果或正误差异中找到可说的依据，比教师单向讲解更容易形成判断证据。
- How to use:
  1. 先明确比较目的，例如比较印痕清晰度、字形图像关系、剪纸线条力量或文具设计是否解决问题。
  2. 并列呈现两张有可比差异的图，差异数量控制在1-3个关键点。
  3. 让学生先独立指出“我先看到哪里不同”，再小组补充。
  4. 教师追问“你从线条、形状、颜色、材料还是使用效果上看出来”。
  5. 把学生判断收束成一个可迁移标准。
  6. 留下对比表或标注截图，作为后续修改或评价证据。
- Media requirements detail:
  - image_count: 至少2张
  - image_type: 问题图/改进图、普通作品/优秀作品、材料效果A/B、正误示例
  - learning_sheet_fields: 我看到的差异, 我的判断理由, 可借鉴或修改处
  - annotatable_regions: 圈选、箭头、关键词贴纸
  - preset_keywords: 线条, 形状, 色彩, 构图, 材料效果, 使用效果
- Sample use cases:
  - 有趣的纸印: 比较两张试印作品，判断哪一张印痕更清楚、更有层次。 Evidence: 圈出边缘、纹理或按压痕迹，并写出纸材或按压方法原因。
  - 有趣的文字和图画: 比较只装饰字形的字卡和图文关系清楚的字卡。 Evidence: 说明图形如何帮助别人理解字义。
  - 我为文具代言: 比较普通铅笔盒与改进方案，判断哪个设计更解决真实使用问题。 Evidence: 给出使用情境和改进理由。
- Teacher language examples:
  - 请你看这两张纸印作品，哪一张印痕更清楚？先找边缘、纹理和按压痕迹。
  - 这两张字卡都很醒目，但哪一张更能让别人看懂字的意思？你从哪个图形变化看出来？
- Screen prompt examples:
  - 比一比：找差异，说依据。
- Evidence examples:
  - 对比表：对象A/对象B/差异/判断/证据位置。
- Misuse boundary: 不能把它用成投票谁更好看；必须有明确比较维度和证据输出。若只是找细节位置，应降为找不同变体。
- Component relation: 上位比较组件 / variants: spot_difference 观察型变体, right_wrong_compare 纠错型变体, before_after_compare 修改型变体

## 圈一圈 (`circle_and_annotate`)

- Component type: `observation_discovery`
- Student problem solved: 学生说“我看到了”，但观察点散乱，不能把关键线条、结构、动作方向、纹样或材料痕迹指给别人看。
- Why use: 圈画和标注能把口头观察变成可见证据，尤其适合美术课从整体欣赏进入局部分析，帮助教师判断学生是否真的看到了关键视觉信息。
- How to use:
  1. 给出观察目标，例如圈出手势最能表达情绪的地方、纸印最清楚的纹理、字形最像图画的部分。
  2. 展示图片、学生作品或局部放大图，限制圈画数量为1-3处。
  3. 学生用圈、箭头或颜色标出观察点，并写一个关键词。
  4. 同桌互看标注，说“我圈这里是因为……”。
  5. 教师挑选2-3个标注追问视觉依据。
  6. 把高频关键词沉淀到学习单或大屏词库中。
- Media requirements detail:
  - image_count: 至少1张主图，可配1张局部放大图
  - image_type: 作品图、教材图、学生草图、手势图、材料痕迹图
  - learning_sheet_fields: 我圈的位置, 关键词, 我这样判断的原因
  - annotatable_regions: 圈、框、箭头或编号
  - preset_keywords: 线条, 方向, 纹样, 结构, 表情, 痕迹
- Sample use cases:
  - 会说话的手: 圈出手势中最能表达“欢迎/拒绝/害怕”的手指方向或掌心位置。 Evidence: 手势图上有圈注和情绪关键词。
  - 有趣的文字和图画: 圈出字形中最像图画的线条、形状或方向变化。 Evidence: 能说出字义和图形变化的关系。
- Teacher language examples:
  - 请只圈一处最有用的地方，不是圈最多。你圈的地方要能帮助别人看懂这个手势。
  - 这个字哪里最像图画？请圈出来，再写一个关键词，比如“弯”“尖”“像山”。
- Screen prompt examples:
  - 圈一圈：圈关键处，写理由。
- Evidence examples:
  - 观察记录栏：我圈的位置/关键词/它说明了什么。
- Misuse boundary: 不能把圈画当热闹互动；没有观察目标、没有关键词、没有追问时不应使用。
- Component relation: 观察标注基础组件 / variants: zoom_detail 局部放大变体, mark_key_structure 结构标注变体

## 连连看 (`match_cards`)

- Component type: `classification_matching`
- Student problem solved: 学生知道一些名称或图像，却不能建立图像、术语、方法、用途之间的对应关系，容易把美术门类、材料技法或文字含义混在一起。
- Why use: 连线匹配把关系显性化，能快速暴露概念误连，比口头问答更适合检查“是否能对应”和“为什么这样对应”。
- How to use:
  1. 准备两组或三组卡片，例如图片卡、名称卡、用途卡、方法卡。
  2. 先让学生独立连一组，再小组讨论有争议的连线。
  3. 要求每条连线至少说一个视觉或功能依据。
  4. 教师保留1-2条容易误连的例子做全班讨论。
  5. 把正确连线沉淀为关系图或分类表。
  6. 用未匹配卡片追问“还缺什么信息才能判断”。
- Media requirements detail:
  - image_count: 6-12张卡片素材
  - image_type: 图像卡、术语卡、方法卡、生活场景卡、作品用途卡
  - data_required: 卡片ID、正确关系、可接受的多解关系
  - learning_sheet_fields: 我的连线, 理由, 我改过的一条连线
  - preset_keywords: 属于, 使用, 表现, 适合, 对应
- Sample use cases:
  - 美术大家庭: 把校园雕塑、海报、建筑装饰、书法作品连到对应的美术大家庭成员。 Evidence: 至少说明一个生活位置和一个用途。
  - 有趣的文字和图画: 把象形字、图画提示和字义连起来。 Evidence: 说明字形变化与含义的对应。
- Teacher language examples:
  - 这条线不是随便连的，你要告诉大家：这张校园图片为什么属于这个美术家庭成员？
  - 你把这个字和这幅图连在一起，是因为外形像，还是意思像？请选一个理由说清楚。
- Screen prompt examples:
  - 连连看：连图、连词、连理由。
- Evidence examples:
  - 匹配表：图片卡编号/我连到/理由关键词。
- Misuse boundary: 不能设计成单纯记忆题；至少要有一类视觉或生活依据。若任务是分类而非一一对应，应使用分一分变体。
- Component relation: 关系匹配组件 / variants: sort_and_group 分类变体, relation_map 关系图变体

## 猜一猜 (`guess_from_clue`)

- Component type: `observation_discovery`
- Student problem solved: 学生进入作品或材料观察前兴趣不足，或者面对陌生图像不知道从哪里看起，只等待教师公布答案。
- Why use: 线索猜测能制造观察动机，但重点不是猜中，而是让学生用局部、材料、动作或语义线索提出证据化判断。
- How to use:
  1. 遮挡整体，只呈现局部、材料触感、轮廓、声音或一句功能线索。
  2. 请学生说“我猜是……因为我看到/摸到/想到……”。
  3. 逐步增加第二、第三条线索，让学生修正判断。
  4. 公布整体后回看哪些线索最有用。
  5. 把有效线索转成后续观察标准。
  6. 留下猜测记录，区分“猜测”和“证据”。
- Media requirements detail:
  - image_count: 1张整体图加2-4张局部或遮挡图
  - image_type: 局部纹理图、轮廓图、材料特写、作品细节
  - physical_material_required: 材料课可使用真实材料袋或盲盒
  - learning_sheet_fields: 第一次猜测, 我的线索, 修正后的判断
  - preset_keywords: 我猜, 因为, 线索, 修正
- Sample use cases:
  - 有趣的纸印: 只展示印痕局部，让学生猜是哪种纸材或哪种按压方式造成。 Evidence: 写出纹理、边缘或深浅作为线索。
  - 我为文具代言: 展示一个文具局部结构，猜它解决了什么使用问题。 Evidence: 把局部结构和使用场景对应起来。
- Teacher language examples:
  - 先不要急着喊答案。你猜它是什么，要带上一条线索：我是从哪里看出来的？
  - 现在我多给一条线索，你要不要修改刚才的猜测？修改也可以，但要说清为什么。
- Screen prompt examples:
  - 猜一猜：先找线索，再判断。
- Evidence examples:
  - 线索记录：我猜/我看到的线索/我后来是否修改。
- Misuse boundary: 不能只当课堂游戏或抢答；如果没有证据追问，会降低为热身活动。猜测结束必须回到观察标准或学习任务。
- Component relation: 观察启动组件 / variants: mystery_crop 局部猜测, function_clue 功能线索猜测

## 材料盲盒 (`material_mystery_box`)

- Component type: `inquiry_experiment`
- Student problem solved: 学生对材料只停留在名称层面，不知道纸张、布料、墨色、工具触感会怎样影响作品效果。
- Why use: 真实材料探摸和试验能把材料特性变成身体经验，适合引出“材料决定效果”的美术判断，比直接讲材料特点更可靠。
- How to use:
  1. 准备3-5种安全材料，遮住名称，只让学生摸、看、轻折或试印。
  2. 每组抽取一种材料，说出触感或视觉特点。
  3. 用同一工具做一次小试验，例如拓印、滚印、折剪、粘贴。
  4. 记录材料带来的效果差异，而不是只记录喜欢哪一种。
  5. 教师追问“这种材料适合表现什么，不适合什么”。
  6. 把发现转入正式创作的材料选择理由。
- Media requirements detail:
  - image_count: 可选1张材料对照图或结果图
  - image_type: 材料特写、试验结果对照
  - physical_material_required: 必须有真实材料，建议3-5种
  - data_required: 材料名称、触感词、效果词记录
  - learning_sheet_fields: 材料, 触感/视觉特点, 试验效果, 适合表现
  - preset_keywords: 粗糙, 光滑, 吸水, 清楚, 模糊, 层次
- Sample use cases:
  - 有趣的纸印: 摸不同纸材并试印，发现粗糙纸、光滑纸对印痕清晰度的影响。 Evidence: 保留一张试印小样和材料效果记录。
  - 剪3 / 红红的剪纸: 比较不同纸张折剪后的挺度、破损和纹样边缘效果。 Evidence: 记录哪种纸更适合连续剪纹样。
- Teacher language examples:
  - 今天先不说哪张纸最好，我们先让材料自己说话：摸一摸、试一试，它留下了什么痕迹？
  - 同样的工具，为什么这张纸印得清楚，那张纸变模糊了？请把原因写在试印旁边。
- Screen prompt examples:
  - 材料盲盒：摸特点，试效果。
- Evidence examples:
  - 材料试验表：材料编号/触感词/试印效果/适合表现。
- Misuse boundary: 不能变成单纯摸盲盒或抽奖；必须连接材料效果和后续创作选择。危险材料不得进入盲盒。
- Component relation: 材料探究启动组件 / variants: paper_property_test 纸材测试变体, tool_effect_test 工具效果变体

## 技法拆解 (`technique_step_demo`)

- Component type: `technique_demo`
- Student problem solved: 学生知道要做什么，但关键技法步骤、手势、顺序和常见错误不清楚，容易一上手就失败。
- Why use: 技法拆解把教师示范切成可观察、可模仿、可检查的步骤，降低操作负担，同时保留学生自主创作空间。
- How to use:
  1. 说明本节只拆解一个关键技法，不把完整作品全部示范完。
  2. 用实物投影、步骤图或短视频展示3-5个关键步骤。
  3. 每一步指出手的位置、工具方向、力度或等待时间。
  4. 展示一个常见错误例，让学生判断错在哪里。
  5. 学生做一次小练习，不直接进入最终作品。
  6. 教师用步骤核对表巡视，发现共性问题后短暂停顿再修正。
- Media requirements detail:
  - image_count: 3-5张步骤图，或1个分段短视频
  - image_type: 步骤图、教师示范手部图、错误例
  - video_required: 技法动作连续性强时需要
  - physical_material_required: 教师示范材料和学生练习材料
  - learning_sheet_fields: 步骤1, 步骤2, 我容易错的地方, 我修正的方法
  - preset_keywords: 方向, 力度, 顺序, 停顿, 对齐, 清理
- Sample use cases:
  - 有趣的纸印: 拆解滚印或拓印的上色、按压、揭起、清理四步。 Evidence: 完成一条试印并标出自己最需要注意的步骤。
  - 会说话的手: 拆解手印角色从印手形到添加眼睛、衣服、表情的步骤。 Evidence: 保留一个半成品步骤照片或步骤核对勾选。
- Teacher language examples:
  - 我现在只示范关键四步，不帮大家设计作品。你要盯住我的手：颜料多少、按压力度、揭起来的方向。
  - 这一步最容易急，急了印痕会糊。请你先在试印纸上练一次，再进正式作品。
- Screen prompt examples:
  - 技法拆解：看步骤，试一次。
- Evidence examples:
  - 步骤核对表：我完成了/我卡住了/我怎样修正。
- Misuse boundary: 不能把技法拆解变成教师包办完整作品；只示范关键方法，不统一学生最终造型。
- Component relation: 技法学习核心组件 / variants: common_mistake_repair 错误修正变体, micro_demo 微示范变体

## 分层挑战 (`tiered_challenge`)

- Component type: `creation_scaffold`
- Student problem solved: 同一创作任务中学生差异明显，有的学生无从下手，有的很快完成却缺少继续深化方向。
- Why use: 分层挑战给出保底、进阶、拓展三档任务，让学生都围绕同一学习目标推进，而不是简单降低要求或额外加作业。
- How to use:
  1. 把目标拆成基础达成、方法提升、创意拓展三层。
  2. 用图标或任务卡说明每层必须留下的作品证据。
  3. 先要求全班完成基础层，确保不掉队。
  4. 学生根据时间和能力选择进阶或拓展，不用互相比较快慢。
  5. 教师巡视时按层给提示，避免统一话术。
  6. 展示时让学生说明自己挑战了哪一层和为什么。
- Media requirements detail:
  - image_count: 1张任务层级图，可配2-3张不同完成度样例
  - image_type: 基础/进阶/拓展示例，避免唯一标准答案
  - physical_material_required: 根据创作任务配置基础和拓展材料
  - learning_sheet_fields: 我选择的层级, 我完成的证据, 我还想挑战
  - preset_keywords: 基础, 进阶, 挑战, 选择理由
- Sample use cases:
  - 有趣的文字和图画: 基础层完成字卡，进阶层让图形更能表达字义，拓展层加入图文故事。 Evidence: 标注自己的层级和图文关系说明。
  - 有趣的纸印: 基础层试印清楚，进阶层做层次变化，拓展层组合纹理形成画面。 Evidence: 试印记录加最终作品层级说明。
- Teacher language examples:
  - 先把基础挑战稳稳完成：让别人看懂你的字和图有什么关系。完成后再选进阶，不用抢速度。
  - 如果你已经印得很清楚，可以挑战第二层：让两种纹理有前后或疏密变化。
- Screen prompt examples:
  - 分层挑战：先保底，再升级。
- Evidence examples:
  - 层级任务卡：基础完成证据/进阶尝试/我选择的理由。
- Misuse boundary: 不能按学生好坏贴标签；层级是任务路径，不是学生等级。不能让拓展层偏离本课核心目标。
- Component relation: 创作支架组件 / variants: choice_board 选择板变体, extension_task 拓展任务变体

## 作品画廊 (`gallery_walk`)

- Component type: `display_evaluation`
- Student problem solved: 学生展示作品时只看自己的作品，不会带着标准观察同伴作品，也不知道从哪里学习和改进。
- Why use: 作品画廊把展示变成有路径的欣赏和评价，让学生在走看、停看、记录中收集同伴作品证据，而不是排队式展示。
- How to use:
  1. 确定1-2个观看任务，例如找清楚印痕、找图文关系、找手势表达。
  2. 将作品按桌面、墙面或电子墙呈现，给每件作品编号。
  3. 学生带记录卡走看，至少停留两件作品。
  4. 每人写下一个优点关键词和一个想提问的地方。
  5. 教师选取高频关键词做全班反馈。
  6. 允许学生回到自己的作品做一次小修改或补充说明。
- Media requirements detail:
  - image_count: 电子场景需至少6张作品图，线下可不用图片
  - image_type: 学生作品、过程样本、编号作品墙
  - student_work: 必须有学生作品或过程样本
  - data_required: 作品编号、作者或小组、评价关键词
  - learning_sheet_fields: 作品编号, 我看到的优点, 我的问题或建议
  - preset_keywords: 我发现, 我学习, 我建议, 证据
- Sample use cases:
  - 会说话的手: 走看手印角色，找哪个角色的手势最能表达情绪。 Evidence: 记录作品编号和情绪判断依据。
  - 有趣的纸印: 观看试印和成品，找最清楚或最有层次的一处印痕。 Evidence: 关键词贴或评价记录卡。
- Teacher language examples:
  - 看作品时不要只说“漂亮”。请带着今天的任务走：哪一件作品让你看到了清楚的印痕？
  - 每人选一件同伴作品，写一个关键词，再写一句你从哪里看出来。
- Screen prompt examples:
  - 作品画廊：看作品，说证据。
- Evidence examples:
  - 画廊记录卡：作品编号/关键词/我看到的证据/我想借鉴。
- Misuse boundary: 不能变成自由参观或表扬大会；必须有观看任务和记录证据。若只是评价一句话，应使用关键词评价。
- Component relation: 展示评价组织组件 / variants: peer_review_wall 同伴评价墙, silent_gallery 静默画廊

## 关键词评价 (`keyword_feedback`)

- Component type: `display_evaluation`
- Student problem solved: 学生评价作品时语言空泛，只会说好看、不错、很有创意，缺少对应美术语言和证据。
- Why use: 关键词能把评价从情绪判断拉回本课目标，让学生用线条、色彩、材料、结构、表达等词汇进行短而准的反馈。
- How to use:
  1. 从本课目标中给出3-6个评价关键词。
  2. 教师示范一句“关键词+证据”的评价。
  3. 学生选择一个关键词评价自己或同伴作品。
  4. 必须补一句“我从哪里看出来”。
  5. 教师收集高频关键词，判断学生是否抓住本课重点。
  6. 将关键词反馈转化为一个修改建议或作品说明。
- Media requirements detail:
  - image_count: 可选作品图1张以上
  - image_type: 学生作品或过程照片
  - student_work: 需要作品或过程样本
  - data_required: 关键词库和评价记录
  - learning_sheet_fields: 我选的关键词, 对应作品位置, 我的证据句
  - preset_keywords: 清楚, 有层次, 有变化, 像图画, 有力量, 能表达
- Sample use cases:
  - 有趣的纸印: 用“清楚、有层次、有变化”评价纸印作品。 Evidence: 指出对应印痕位置。
  - 会说话的手: 用“有力量、像在说话、有表情”评价手势或手印角色。 Evidence: 指出手指方向、掌心位置或角色表情。
- Teacher language examples:
  - 今天评价不能只说好看，请你选一个关键词：清楚、有层次、有变化。然后说从哪里看出来。
  - 你说这个手势“有力量”，力量藏在哪儿？是手指张开、方向，还是画面位置？
- Screen prompt examples:
  - 关键词评价：选1词，说证据。
- Evidence examples:
  - 评价句式卡：我用“___”评价，因为我看到___。
- Misuse boundary: 关键词不能变成固定套话；词必须来自本课目标。不能用“棒、漂亮、认真”等泛评价替代美术证据。
- Component relation: 评价语言支架组件 / variants: star_rubric 星级量规变体, two_stars_one_wish 两优一建议变体

## 学习单记录 (`learning_sheet_record`)

- Component type: `evidence_collection`
- Student problem solved: 课堂过程发生了，但课后看不到学生怎样观察、试验、选择和修正，教师也难以依据过程证据调整教学。
- Why use: 学习单记录把短时活动沉淀为可追踪证据，适合承接观察、比较、试验和评价，不只是填空，而是保存学习过程。
- How to use:
  1. 只为关键节点设置1-3个记录栏，避免整节课都在写。
  2. 记录栏直接对应学生动作，例如圈一处、试一次、连一条、写一句理由。
  3. 教师说明记录会用于后续创作或评价。
  4. 学生完成后用同桌互看或举例反馈校准记录质量。
  5. 教师收集典型记录判断是否需要补充示范。
  6. 课后可进入学生作品档案或备课反馈。
- Media requirements detail:
  - image_count: 可选，适合贴试印小样或标注截图
  - image_type: 学习单、试印小样、标注截图
  - data_required: 字段名、记录类型、是否必填、对应组件ID
  - learning_sheet_fields: 任务, 我的记录, 证据位置, 我还需要帮助
  - preset_keywords: 观察, 试验, 理由, 修改, 证据
- Sample use cases:
  - 有趣的纸印: 记录纸材、印法、印痕效果，作为创作前选择依据。 Evidence: 试印记录表和小样。
  - 美术大家庭: 记录一个生活中的美术例子及其所属门类。 Evidence: 生活例子加关系连接。
- Teacher language examples:
  - 这张学习单不是作业纸，它帮你留下今天的发现。请只写最有用的一条。
  - 试印以后不要马上扔掉，请把最清楚的一次贴在记录栏里，旁边写原因。
- Screen prompt examples:
  - 学习单记录：留下关键发现。
- Evidence examples:
  - 三栏记录：我做了什么/我发现什么/证据在哪里。
- Misuse boundary: 不能把学习单变成机械填空或额外负担；每个栏位必须对应课堂决策、作品修改或评价证据。
- Component relation: 证据沉淀组件 / variants: exit_ticket 离场条变体, process_log 过程记录变体

## 小测验 (`mini_quiz`)

- Component type: `evidence_collection`
- Student problem solved: 教师无法快速判断学生是否理解关键概念、步骤或判断标准，学生也可能带着误解进入创作。
- Why use: 小测验用1-3个轻量题即时检查关键理解，适合在创作前或收束时做保底判断，不把美术课变成知识考试。
- How to use:
  1. 只选择本节最容易误解的1-3个点。
  2. 题型优先图像判断、步骤排序、材料选择或一题一理由。
  3. 学生快速作答后立即显示或讨论关键理由。
  4. 教师根据错误集中点决定是否补示范或调整任务。
  5. 保留班级层面的错误类型，不把分数作为主要评价。
  6. 将结果连接到后续创作提醒。
- Media requirements detail:
  - image_count: 图像题建议1-2张图
  - image_type: 判断图、步骤图、匿名作品图
  - data_required: 题干、选项、可接受答案、错误类型解释
  - learning_sheet_fields: 我的选择, 我的理由, 我需要提醒自己
  - preset_keywords: 判断, 排序, 选择, 理由
- Sample use cases:
  - 有趣的纸印: 判断哪一步会导致印痕变糊，或给滚印步骤排序。 Evidence: 答案和错误类型统计。
  - 有趣的文字和图画: 判断哪张字卡更像图文关系表达，而不是单纯装饰。 Evidence: 选择并写一句理由。
- Teacher language examples:
  - 我们用两道小题检查一下，不是考试，是看看等会儿创作前还要提醒什么。
  - 选完以后请加一句理由。只有选项没有理由，我不知道你是不是真的看懂了。
- Screen prompt examples:
  - 小测验：选答案，说理由。
- Evidence examples:
  - 即时检查：题号/我的选择/理由/教师需补充点。
- Misuse boundary: 不能把美术学习压缩成选择题；题目只检查关键障碍，不评价全部学习质量。
- Component relation: 即时理解检查组件 / variants: exit_ticket 出门条变体, step_order_check 步骤排序变体

## 拍照提交 (`photo_submit`)

- Component type: `evidence_collection`
- Student problem solved: 学生作品和过程证据分散，教师难以及时看到阶段成果、发现共性问题或留下课堂档案。
- Why use: 拍照提交把过程小样、半成品、标注图和最终作品转成可回看证据，适合支持即时展示、教师巡视后反馈和课后反思。
- How to use:
  1. 明确拍什么：试印小样、圈注图、半成品、最终作品或材料选择。
  2. 规定拍摄角度、光线和是否需要包含学习单编号。
  3. 学生或小组在指定节点提交，不全程频繁拍。
  4. 教师快速筛选2-3张共性例子反馈。
  5. 照片与组件记录绑定，例如比较、示范、画廊。
  6. 课后保留为作品档案或下次课改进依据。
- Media requirements detail:
  - image_count: 每个关键节点1张，通常整课1-3张
  - image_type: 过程小样、半成品、最终作品、学习单局部
  - student_upload: 需要学生或小组上传图片
  - data_required: 学生/小组、组件ID、提交节点、教师标记
  - learning_sheet_fields: 照片编号, 提交内容, 我想让老师看哪里
  - preset_keywords: 过程, 半成品, 最终, 需要帮助
- Sample use cases:
  - 会说话的手: 提交手势线稿或手印角色半成品，教师选择典型作品做反馈。 Evidence: 过程照片和教师标记。
  - 有趣的纸印: 提交最清楚的一次试印和最终作品，对比材料试验是否迁移到创作。 Evidence: 试印照片加最终作品照片。
- Teacher language examples:
  - 现在只拍一张你最想让老师看的证据，不是拍桌面。请让作品占满画面。
  - 如果你遇到问题，也可以拍半成品。提交时写一句：我想让老师看哪里。
- Screen prompt examples:
  - 拍照提交：拍证据，写看点。
- Evidence examples:
  - 提交记录：照片/组件节点/作品说明/教师反馈标记。
- Misuse boundary: 不能为了收集而频繁打断课堂；照片必须服务反馈、展示或档案。涉及隐私时优先拍作品不拍脸。
- Component relation: 数字证据采集组件 / variants: process_photo 过程照, final_work_submit 成品提交
