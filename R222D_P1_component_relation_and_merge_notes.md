# R222D-P1 Component Relation And Merge Notes

| Component | Role | Variants / Merge Notes | Misuse Boundary |
| --- | --- | --- | --- |
| 比一比 (`compare_two_images`) | 上位比较组件 | spot_difference 观察型变体; right_wrong_compare 纠错型变体; before_after_compare 修改型变体; 开发时可共用比较内核，通过 comparison_mode 区分。 | 不能把它用成投票谁更好看；必须有明确比较维度和证据输出。若只是找细节位置，应降为找不同变体。 |
| 圈一圈 (`circle_and_annotate`) | 观察标注基础组件 | zoom_detail 局部放大变体; mark_key_structure 结构标注变体; 可与局部放大、关键词评价组合，但不能替代评价。 | 不能把圈画当热闹互动；没有观察目标、没有关键词、没有追问时不应使用。 |
| 连连看 (`match_cards`) | 关系匹配组件 | sort_and_group 分类变体; relation_map 关系图变体; 与 art_cognition_classification skill 组合时，可作为低负担检查入口。 | 不能设计成单纯记忆题；至少要有一类视觉或生活依据。若任务是分类而非一一对应，应使用分一分变体。 |
| 猜一猜 (`guess_from_clue`) | 观察启动组件 | mystery_crop 局部猜测; function_clue 功能线索猜测; 可与圈一圈串联，先猜再圈关键线索。 | 不能只当课堂游戏或抢答；如果没有证据追问，会降低为热身活动。猜测结束必须回到观察标准或学习任务。 |
| 材料盲盒 (`material_mystery_box`) | 材料探究启动组件 | paper_property_test 纸材测试变体; tool_effect_test 工具效果变体; 可与学习单记录绑定为材料试验证据链。 | 不能变成单纯摸盲盒或抽奖；必须连接材料效果和后续创作选择。危险材料不得进入盲盒。 |
| 技法拆解 (`technique_step_demo`) | 技法学习核心组件 | common_mistake_repair 错误修正变体; micro_demo 微示范变体; 可和小测验组合检查步骤理解，可和拍照提交组合收过程证据。 | 不能把技法拆解变成教师包办完整作品；只示范关键方法，不统一学生最终造型。 |
| 分层挑战 (`tiered_challenge`) | 创作支架组件 | choice_board 选择板变体; extension_task 拓展任务变体; 可与学习单记录绑定，记录学生选择与完成证据。 | 不能按学生好坏贴标签；层级是任务路径，不是学生等级。不能让拓展层偏离本课核心目标。 |
| 作品画廊 (`gallery_walk`) | 展示评价组织组件 | peer_review_wall 同伴评价墙; silent_gallery 静默画廊; 可与关键词评价组合，先走看再关键词评价。 | 不能变成自由参观或表扬大会；必须有观看任务和记录证据。若只是评价一句话，应使用关键词评价。 |
| 关键词评价 (`keyword_feedback`) | 评价语言支架组件 | star_rubric 星级量规变体; two_stars_one_wish 两优一建议变体; 可作为作品画廊后的轻量评价输出。 | 关键词不能变成固定套话；词必须来自本课目标。不能用“棒、漂亮、认真”等泛评价替代美术证据。 |
| 学习单记录 (`learning_sheet_record`) | 证据沉淀组件 | exit_ticket 离场条变体; process_log 过程记录变体; 可与几乎所有组件组合，但不应替代真实操作。 | 不能把学习单变成机械填空或额外负担；每个栏位必须对应课堂决策、作品修改或评价证据。 |
| 小测验 (`mini_quiz`) | 即时理解检查组件 | exit_ticket 出门条变体; step_order_check 步骤排序变体; 可与技法拆解前后组合，形成示范前诊断或示范后检查。 | 不能把美术学习压缩成选择题；题目只检查关键障碍，不评价全部学习质量。 |
| 拍照提交 (`photo_submit`) | 数字证据采集组件 | process_photo 过程照; final_work_submit 成品提交; 与作品画廊、关键词评价、学习单记录组合形成作品证据链。 | 不能为了收集而频繁打断课堂；照片必须服务反馈、展示或档案。涉及隐私时优先拍作品不拍脸。 |