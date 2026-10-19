# main.py
from rule_engine import diagnose_metrics
from llm_agent import generate_report

# 1. 模拟一条你后台的真实数据（你可以自己改数字测试）
video_data = {
    "play_count": 320,
    "like_count": 12,
    "3s_retention": 0.18, # 3秒留存只有18%
    "completion_rate": 0.12 # 完播率12%
}

# 2. 模拟视频前十几秒的语音字幕
video_subtitle = """
(0-3秒) 大家好，我是你们的老朋友小明。
(4-7秒) 今天给大家分享一个超级好用的Excel快捷键。
(8-12秒) 大家平时做表格是不是觉得很麻烦？那一定要看完今天这期视频。
"""

# 3. 运行规则引擎找异常
print("【1】正在运行规则引擎...")
issues = diagnose_metrics(video_data)
print(f"检测到的问题：{issues}\n")

# 4. 将异常和字幕喂给大模型
report = generate_report(issues, video_subtitle)

# 5. 打印最终诊断报告
print("============== 最终诊断报告 ==============")
print(report)
