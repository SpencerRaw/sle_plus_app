import streamlit as st

st.set_page_config(
    page_title="S+ app",
    page_icon=":shamrock:",
)

st.title("主页")
st.sidebar.success("选择上面的一个版块")

st.header("项目简介")
st.write("""
欢迎来到 S+ app 主页！

我们的项目旨在通过人工智能技术，特别是自然语言处理（NLP）和机器学习（ML），来帮助诊断和管理系统性红斑狼疮（SLE）等复杂疾病。我们的目标是为医生和患者提供有价值的工具，帮助他们更好地了解病情，制定治疗计划，并持续监测病情的变化。
""")

st.header("主要功能")
st.write("""
1. **自动数据分析**：上传患者的病历数据，自动进行数据分析，提供详细的分析报告。
2. **AI 诊断与预测**：基于输入的病历数据，利用机器学习模型进行疾病诊断和未来病情预测。
3. **研究成果展示**：展示我们团队的研究成果，包括病因溯源、医学概念学习和病人分类。
4. **AI 聊天机器人**：通过聊天机器人，提供疾病相关的咨询和建议。
""")

st.header("项目背景")
st.write("""
系统性红斑狼疮（SLE）是一种复杂的自身免疫性疾病，影响多个系统和器官。传统的诊断和治疗方法常常需要大量的专业知识和经验。本项目通过结合人工智能技术，旨在提供一种高效、准确且可扩展的解决方案，辅助医生进行疾病诊断和治疗。

我们的团队来自苏州大学物理学院软物质交叉研究院，致力于利用人工智能解决各种疾病问题，并与多家医院合作开展研究。我们特别关注SLE及其他免疫相关疾病，希望通过大数据和机器学习技术，推动疾病诊断和治疗的进步。
""")
