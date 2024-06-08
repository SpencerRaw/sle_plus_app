import openai
from openai import OpenAI
import streamlit as st

st.set_page_config(
    page_title="S+ app",
    page_icon=":shamrock:",
)
st.title('🤖💬 S+ SLE问诊机器人')
st.sidebar.success("选择上面的一个版块")

# 输入API key
api_key = st.sidebar.text_input('请输入API key:', type='password')
base_url = "https://api.moonshot.cn/v1"

if api_key:
    client = OpenAI(api_key=api_key, base_url=base_url)
    st.success('API key 已经输入，可以开始对话了!', icon='✅')
else:
    st.warning('请输入API key以继续。', icon='⚠️')

# 关键词触发机制
keywords_responses = {
    "系统性红斑狼疮": "系统性红斑狼疮（SLE）是一种自身免疫性疾病，主要影响皮肤、关节、肾脏和其他器官。",
    "症状": "系统性红斑狼疮的常见症状包括疲劳、关节痛、皮疹和发烧。",
    "治疗": "系统性红斑狼疮的治疗通常包括免疫抑制剂、抗炎药物和支持性治疗。"
}

if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用户输入
if prompt := st.chat_input("你好，请问有什么事情吗?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response_content = ""
    for keyword, response in keywords_responses.items():
        if keyword in prompt:
            response_content = response
            break

    if not response_content:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # 调用Moonshot API生成响应
            for response in client.chat.completions.create(
                model="moonshot-v1-32k",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                temperature=0.3,
                stream=True):
                
                if response.choices[0].delta.content is not None:
                    full_response += response.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            response_content = full_response

    st.session_state.messages.append({"role": "assistant", "content": response_content})

    # 显示助手的响应
    with st.chat_message("assistant"):
        st.markdown(response_content)
