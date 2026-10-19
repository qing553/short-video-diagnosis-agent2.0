# Short-Video Diagnosis Agent (MVP)

An AI Agent MVP built on a **"Rule Engine + LLM" dual-layer architecture**. It is designed to solve the "Cold Start attribution dilemma" for short-video creators.

## 🎯 Problem & Solution
- **The Pain Point**: Creators often see cold data like "3-second retention dropped to 18%", but lack actionable insights on exactly *which second* and *which script* caused the drop.
- **The Solution**: A lightweight Agent that uses a Python Rule Engine for deterministic math and metric validation (preventing LLM hallucinations), and calls the DeepSeek LLM to analyze subtitle semantics, generating structured diagnostic reports.

## 🏗️ Product Architecture
To ensure stability and control, the system decouples deterministic calculation from probabilistic reasoning:
1. `rule_engine.py` (**Deterministic Layer**): Calculates metrics (e.g., completion rate), compares them with baseline thresholds, and flags anomalies.
2. `llm_agent.py` (**Probabilistic Layer**): Uses a strictly constrained Prompt Schema to analyze the text and output a 4-element report: `Evidence - Mechanism - Action - Expectation`.
3. `app.py` (**Interaction Layer**): A Streamlit-based Web UI for data input and report generation.

## 🚀 Quick Start (Demo)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt



















# 短视频归因分析 AI Agent (MVP)

这是一个基于“规则引擎 + LLM”双层架构的短视频数据分析 Agent MVP，旨在解决创作者在冷启动期“数据差但不知为何差”的痛点。

## 🎯 业务痛点 & 解决方案
- **痛点**：创作者只能看到“3秒留存低”的冰冷数据，缺乏精确到秒的内容归因与修改建议。
- **方案**：通过 Python 规则引擎处理数值计算（防大模型幻觉），调用 DeepSeek API 处理字幕语义，输出带有“证据-机制-动作-预期”四要素的结构化诊断报告。

## 🏗️ 产品架构
1. `rule_engine.py`：确定性规则层。负责计算指标并与基线比对，定位异常点。
2. `llm_agent.py`：概率性推理层。基于 Prompt 强约束，对异常点进行语义归因。
3. `app.py`：基于 Streamlit 的交互层。提供数据输入与报告生成的 User Flow。

## 🚀 如何体验 (Demo)
1. 安装依赖：`pip install -r requirements.txt`
2. 配置环境变量：`export DEEPSEEK_API_KEY="你的Key"`
3. 运行：`streamlit run app.py`

## 📈 业务成效
- 利用该工具成功诊断并优化个人账号视频，产出播放 3 万+、互动率 60.7% 的爆款内容。
- 建立了 7 天回测追踪机制，持续校准归因准确度。
