# llm_agent.py
from openai import OpenAI

API_KEY = "DEEPSEEK_API_KEY" 

client = OpenAI(
    api_key=API_KEY, 
    base_url="https://api.deepseek.com"
)

def generate_report(issues, subtitle):
    print("正在呼叫 DeepSeek 进行归因推理...\n")
    
    # 这里就是我们简历里写的“证据-机制-动作-预期”四要素约束
    prompt = f"""
    你是一个资深的短视频爆款分析师。
    
    【系统规则引擎检测到的异常】：
    {issues}
    
    【视频前15秒字幕】：
    {subtitle}
    
    请结合规则引擎的数据异常和字幕内容，进行归因。
    必须严格按照以下四要素输出，禁止废话，最多输出两条核心建议：
    
    1. 证据：引用具体的异常数据和第X秒的字幕内容。
    2. 机制：解释为什么这里出了问题（平台分发或用户心理角度）。
    3. 动作：给出精确的修改建议（精确到秒，如“砍掉第2-4秒的废话”）。
    4. 预期：修改后，哪个指标会提升。
    """
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个懂数据、懂流量池、说话一针见血的短视频诊断专家。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content
