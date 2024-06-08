import streamlit as st
import random

st.set_page_config(
    page_title="S+ app",
    page_icon=":shamrock:",
)

st.title("预测应用")
st.sidebar.success("选择上面的一个版块")

image = st.file_uploader("上传病人的病历：", type=["png", "jpg", "jpeg"])
if image:
    st.image(image=image)
    print(image)

if st.button("提交病例"):
    # 随机生成是否有系统性红斑狼疮
    sle_diagnosis = random.choice(["有", "无"])
    st.subheader("预测结果")
    st.write(f"系统性红斑狼疮诊断：{sle_diagnosis}")

    # 如果有系统性红斑狼疮，生成其他预测结果
    if sle_diagnosis == "有":
        # 随机生成未来得病的可能性（百分比）
        future_disease_probability = random.uniform(0, 100)
        st.write(f"未来得病的可能性：{future_disease_probability:.2f}%")
        
        # 随机生成未来得病的走向轨迹
        worse_probability = random.uniform(0, 100)
        better_probability = 100 - worse_probability
        worse_indicators = random.sample(["高血压", "蛋白尿", "贫血"], k=2)
        better_indicators = random.sample(["正常血压", "正常尿液分析", "红细胞恢复"], k=2)
        st.write(f"未来病情变重的概率：{worse_probability:.2f}%")
        st.write(f"未来病情变轻的概率：{better_probability:.2f}%")
        st.write(f"恶化的可能指标：{', '.join(worse_indicators)}")
        st.write(f"缓解的可能指标：{', '.join(better_indicators)}")

        # 随机生成严重程度
        severity_score = random.randint(1, 11)
        severity_label = random.choice(["严重", "无", "较轻"])
        st.write(f"严重程度评分：{severity_score}，程度：{severity_label}")

        # 随机生成推荐药物
        recommended_drugs = random.choice(["无", "药物A", "药物B", "药物C"])
        st.write(f"推荐药物：{recommended_drugs}")
    else:
        # 如果没有系统性红斑狼疮，只显示未来得病的可能性
        future_disease_probability = random.uniform(0, 100)
        st.write(f"未来得病的可能性：{future_disease_probability:.2f}%")

#1）病历-->json-->不同预测api-->api处理结果
#2）病例-->json-->添加到数据库-->到一定数量重新训练模型