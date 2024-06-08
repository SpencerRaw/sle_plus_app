import streamlit as st
import time
import random
import os

st.set_page_config(
    page_title="S+ app",
    page_icon=":shamrock:",
)

st.title("自动机器学习训练")
st.sidebar.success("选择上面的一个版块")
st.subheader("输入数据背景")
data_background = st.text_area("请输入数据的背景信息：")

def simulate_process(step, sleep_time=10):
    st.write(f"{step} 已经完成")
    time.sleep(sleep_time)

uploaded_file = st.file_uploader("上传数据文件（CSV或Excel）", type=["csv", "xlsx"])

if uploaded_file:
    st.write("数据载入中，请稍候...")
    time.sleep(60)  # 模拟数据载入时间
    st.write("数据载入完成")
    
    steps = [
        "数据探索",
        "研究目标",
        "文献搜索 I",
        "相似论文搜索",
        "目标验证",
        "假设测试计划",
        "数据分析",
        "表格设计",
        "写作"
    ]
    
    # 模拟每一步完成
    for step in steps:
        simulate_process(step)
        
        # 随机分支逻辑
        if step == "数据探索" and random.choice([True, False]):
            simulate_process("数据探索 - 额外步骤")
        
        if step == "研究目标" and random.choice([True, False]):
            simulate_process("研究目标 - 额外步骤")
    
    # 模拟完成数据分析后提供下载模型和代码
    model_zip_path = "code_model.zip"
    st.write("数据分析完成")
    st.download_button("下载模型和代码", data=open(model_zip_path, "rb"), file_name="model_and_code.zip")

    # 模拟完成表格设计后提供下载表格
    table_csv_path = "table_design.csv"
    st.write("表格设计完成")
    st.download_button("下载表格CSV", data=open(table_csv_path, "rb"), file_name="table_design.csv")
    
    # 模拟完成写作后提供下载论文
    paper_pdf_path = "writing.pdf"
    st.write("写作完成")
    st.download_button("下载论文PDF", data=open(paper_pdf_path, "rb"), file_name="writing.pdf")

