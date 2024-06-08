import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="S+ app",
    page_icon=":shamrock:",
)
st.title("研究成果展示")
st.sidebar.success("选择上面的一个版块")

# 因果溯源图
st.subheader("病的因果溯源")

def draw_causal_graph():
    G = nx.DiGraph()
    for i in range(20):
        G.add_node(i, color='blue')
    
    # 添加因果关系，多一些分叉
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9),
             (4, 10), (5, 11), (5, 12), (6, 13), (6, 14), (7, 15), (8, 15), (9, 16),
             (10, 16), (11, 17), (12, 17), (13, 18), (14, 18), (15, 19), (16, 19),
             (17, 19), (18, 19)]
    G.add_edges_from(edges)
    
    # 最后一个节点作为因节点
    G.nodes[19]['color'] = 'red'

    pos = nx.spring_layout(G)
    colors = [G.nodes[i]['color'] for i in G.nodes]
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, node_color=colors, with_labels=True, node_size=500, arrowsize=20, font_size=10)
    st.pyplot(plt)

draw_causal_graph()

# 医学概念学习和网络
st.subheader("医学概念学习和网络")

def draw_concept_network():
    G = nx.Graph()
    node_colors = ['blue', 'green', 'yellow', 'purple']
    
    for i in range(20):
        G.add_node(i, color=node_colors[i % 4])
    
    # 添加无向边，多一些子图
    edges = [(i, (i + np.random.randint(1, 5)) % 20) for i in range(20)]
    sub_edges = [(i, (i + np.random.randint(5, 10)) % 20) for i in range(10)]
    G.add_edges_from(edges)
    G.add_edges_from(sub_edges)

    pos = nx.spring_layout(G)
    colors = [G.nodes[i]['color'] for i in G.nodes]
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, node_color=colors, with_labels=True, node_size=500, font_size=10)
    st.pyplot(plt)

draw_concept_network()

# 病人分类散点图
st.subheader("病人的分类")

def draw_patient_classification():
    x = np.random.normal(size=100)
    y = np.random.normal(size=100)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y)
    
    # 绘制不规则椭圆形轮廓
    ellipse = plt.Circle((0, 0), 2, fill=False, edgecolor='r', linestyle='--')
    plt.gca().add_patch(ellipse)
    
    plt.title("patient t-SNE")
    plt.xlabel("t-SNE1")
    plt.ylabel("t-SNE2")
    st.pyplot(plt)

draw_patient_classification()
