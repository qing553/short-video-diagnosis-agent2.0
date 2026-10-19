# rule_engine.py

def diagnose_metrics(data):
    """
    规则引擎：负责算数据、定层级、找异常
    """
    # 假设这是你的历史基线（你可以随便改）
    baseline = {
        "3s_retention": 0.35, # 3秒留存基线 35%
        "completion_rate": 0.10 # 完播率基线 10%
    }
    
    issues = []
    
    # 规则1：流量池判定
    if data['play_count'] < 500:
        issues.append("播放量不足500，卡在冷启动池。核心问题在第一关（首屏吸引力）。")
        
    # 规则2：留存异常判定
    if data['3s_retention'] < baseline['3s_retention']:
        issues.append(f"3秒留存率仅为 {data['3s_retention']*100}%，远低于行业基线 {baseline['3s_retention']*100}%，说明开局没抓住人。")
        
    # 规则3：互动异常判定
    if data['completion_rate'] > baseline['completion_rate'] and data['like_count'] < 50:
        issues.append("整体完播率尚可，但点赞极低。说明内容能看下去，但缺乏情绪价值或认同感，观众看完就走。")
        
    return issues

# 测试一下这个规则引擎（你可以不用运行这个文件，我们会在main里调用）
