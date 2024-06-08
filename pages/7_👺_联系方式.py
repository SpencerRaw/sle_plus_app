import streamlit as st

st.set_page_config(
    page_title="S+ app - 联系我们",
    page_icon=":shamrock:",
)

st.title("联系我们")
st.sidebar.success("选择上面的一个版块")

st.write("""
如有任何问题或建议，请随时与我们联系。

**邮箱**: [your-email@example.com](mailto:your-email@example.com)
**电话**: +86-123-4567-8901
**地址**: 苏州大学物理学院软物质交叉研究院
""")
