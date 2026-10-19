
import streamlit as st
from rule_engine import diagnose_metrics
from llm_agent import generate_report

st.title("🎬 短视频归因分析 Agent")
st.write("基于规则引擎与 LLM 双层架构")

# 做个输入框
retention = st.slider("3秒留存率 (%)", 0, 100, 18) / 100
likes = st.number_input("点赞数", value=12)
play_count = st.number_input("播放量", value=320)
subtitle = st.text_area("视频字幕", "(0-3秒) 大家好，我是你们的老朋友小明...")

if st.button("开始诊断"):
    data = {"play_count": play_count, "like_count": likes, "3s_retention": retention, "completion_rate": 0.12}
    issues = diagnose_metrics(data)
    report = generate_report(issues, subtitle)
    st.markdown("### 诊断报告")
    st.success(report)
