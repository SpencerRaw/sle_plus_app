import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="S+ app",
    page_icon=":shamrock:",
)
st.title("数据库信息")
st.sidebar.success("选择上面的一个版块")

# 初始化数据库
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        'Metric': ['Age', 'BMI', 'Cholesterol', 'Blood Pressure'],
        'Mean': [np.random.uniform(20, 50) for _ in range(4)],
        'Std Dev': [np.random.uniform(5, 15) for _ in range(4)],
        'N': 1000
    })

def refresh_data():
    st.session_state.data['N'] += 1
    st.session_state.data['Mean'] = [mean + np.random.uniform(-0.5, 0.5) for mean in st.session_state.data['Mean']]
    st.session_state.data['Std Dev'] = [std + np.random.uniform(-0.1, 0.1) for std in st.session_state.data['Std Dev']]

# 显示当前数据
st.subheader("数据库元数据")
st.write(st.session_state.data)

# 数据可视化
st.subheader("数据可视化")

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# 平均值条形图
ax[0].bar(st.session_state.data['Metric'], st.session_state.data['Mean'], yerr=st.session_state.data['Std Dev'], capsize=5)
ax[0].set_title("mean and std")
ax[0].set_ylabel("mean")

# 数据量折线图
ax[1].plot([st.session_state.data['N'][0]] * len(st.session_state.data['Metric']), marker='o')
ax[1].set_title("data num")
ax[1].set_ylabel("num")
ax[1].set_xticks(range(len(st.session_state.data['Metric'])))
ax[1].set_xticklabels(st.session_state.data['Metric'])

st.pyplot(fig)

# 刷新按钮
if st.button("刷新"):
    refresh_data()
    st.experimental_rerun()
