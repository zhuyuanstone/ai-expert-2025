&lt;!-- AI-Expert-Roadmap-v6.1.md --&gt;
# AI 专家深度通关路线图 v6.1（单文件版）
&gt; 源自 v6.0 坚韧务实版，保留全部「读哪页书→25 min 微任务→沟通一句话」闭环，可断点续跑。

## 0 启动准备（一次性 6 h）
| 任务 | 检查标准 | 补救资源 |
|------|----------|----------|
| ① 知识库目录 | Notion 4 子页面就绪 | 模板见 `templates/` |
| ② 环境验证 | `python -c "import torch; print(torch.__version__)"` 成功 | `docs/env_setup.md` |
| ③ 基础自测 | 线性代数 + Python ≥80 % | `prep/refresher.ipynb` |
| ④ 学习契约 | 公开写下目标 & 每周投入 | 本文件底部 |

## 1 概念破壁（Week 1-2）
| 周 | 读哪页书 | 25 min 微任务 | 沟通一句话 |
|----|----------|---------------|------------|
| 1 | 《AIMA》第 1 章前 20p | PyTorch 线性回归预测波士顿房价 | 「AI 就是让机器表现出通常需要人类智能的行为」 |
| 2 | 《Hands-On ML》1-2 章 30p | Kaggle Titanic ≥0.78 | 「三者是不同层次的工具，选哪个看数据量」 |

## 2 原理攻坚（Week 3-8）
| 阶段 | 读哪页书 | 手推/编码 25 min | 交付物 |
|------|----------|------------------|--------|
| 3-4 | 《Deep Learning》4-6 章 40p | 梯度下降手推 + NumPy 逻辑回归 | ③ 反向传播手稿 |
| 5-6 | 《Hands-On ML》6-7 章 50p | NumPy CART + 随机森林 | ④ 算法对比矩阵 |
| 7-8 | 《百面 ML》1-4 章 35p | ROC 手画 + k 折交叉验证 | ⑤ 模型诊断报告 |

## 3 系统构建（Week 9-12）
| 周 | 读哪页书 | 编码 25 min | 系统产出 |
|----|----------|-------------|----------|
| 9 | 《PyTorch 源码剖析》2-3 章 25p | 自定义激活 + 计算图可视化 | ⑥ 计算图解读视频 |
| 10 | ResNet 论文前 6 页 | ResNet-18 CIFAR-10 ≥85 % | ⑦ 架构演进图 |
| 11 | BatchNorm/Dropout 原论文 10p | 消融实验 | ⑧ 训练日志分析报告 |
| 12 | 《Designing ML Systems》1-5 章 40p | MLflow/W&B + Docker 打包 | ⑨ MLOps 流水线图 |

## 4 大模型实战（Week 13-16）
| 周 | 读哪页书 | 实验 25 min | 核心产出 |
|----|----------|-------------|----------|
| 13 | Attention 论文前 3 节 10p | NumPy Transformer Encoder | ⑩ 注释版 Transformer |
| 14 | LoRA 论文 + HF PEFT 20p | LoRA 微调 GPT-2 情感分析 | ⑪ 微调对比表 |
| 15 | InstructGPT 博客 + TRL 20p | SFT+Reward+PPO 对话跑通 | ⑫ RLHF 三步泳道图 |
| 16 | LangChain 概念教程 15p | Chroma+LangChain 本地 QA | ⑬ RAG 架构图 + 评估 |

## 5 价值呈现（Week 17-20）
| 周 | 读哪页书 | 关键任务 25 min | 交付物 |
|----|----------|-----------------|--------|
| 17 | 《Designing ML Systems》7-8 章 30p | 六部分白皮书 ≤10 页 | ⑭ 解决方案白皮书 |
| 18 | Chip Huyen 路演章节 20p | 1-3-10 故事线 PPT + 双录屏 | ⑮ 路演套件 |
| 19 | HF Contributing.md 10p | 提交 1 个 Merged PR / 技术文章 | ⑯ 社区贡献证明 |
| 20 | 无 | 端到端毕业项目 + 雷达图更新 | ⑰ 项目报告 & ⑱ 雷达图 |

## 6 长期演进
- 季度主题：多模态 / AI 系统工程 / 边缘推理 择一
- 输入：每月 2 篇顶会论文 + 关注 3 位大牛
- 输出：博客/Newsletter 每季度 ≥1 深度文章

## 7 每周日三问模板（复制填写）

```text
Week XX 复盘：
① 学-练-讲闭环：✅/❌  
② 产出可展示：✅/❌  
③ 计划调整：无 / 拆周 / 暂停 / 其他：________
```

## 8 毕业认证（打钩 ✅）
- [ ] ⑩ 注释版 Transformer
- [ ] ⑪ 微调对比表
- [ ] ⑫ RLHF 三步泳道图
- [ ] ⑬ RAG 架构图
- [ ] ⑭ 白皮书
- [ ] ⑮ 路演套件
- [ ] ⑯ 社区贡献
- [ ] ⑰ 项目报告
- [ ] ⑱ 雷达图

**全部完成 → Profile 置顶「AI 实战专家」徽章**

---
🔗 本文件永久链接：`https://github.com/zhuyuanstone/ai-expert-2025/blob/main/AI-Expert-Roadmap-v6.1.md`
