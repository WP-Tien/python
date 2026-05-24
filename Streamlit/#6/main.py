import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# streamlit run main.py
# Chuẩn bị dữ liệu
df = pd.DataFrame({
    "Năm": [2019, 2020, 2021, 2022, 2023],
    "Doanh thu": [120, 150, 180, 210, 250]
})

# st.line_chart() - Cách nhanh nhất
st.subheader("st.line_chart")
st.line_chart(df.set_index("Năm"))

'''
Ưu điểm
- Nhanh, ít code
- Phú hợp demo, dashboard đơn giản

Hạn chế
- Ít tuỳ biến
- Không kiểm soát chi tiết
'''

# Matplotlib – Kiểm soát chi tiết
st.subheader("Matplotlib")
fig, ax = plt.subplots()
ax.plot(df["Năm"], df["Doanh thu"], marker='o')
ax.set_title("Doanh thu theo năm")
ax.set_xlabel("Năm")
ax.set_ylabel("Doanh thu")

st.pyplot(fig)

'''
Khi dùng
- Biểu đồ học thuật
- Cần tuỳ chỉnh kỹ
'''


# Seaborn - Đẹp & thống kê
st.subheader("Seaborn")

fig, ax = plt.subplots()
sns.lineplot(data=df, x="Năm", y="Doanh thu", marker="o", ax=ax)
ax.set_title("Doanh thu theo năm (Seaborn)")

st.pyplot(fig)

'''
Khi dùng
- Phân tích dữ liệu
- Biểu đồ thống kê, phân phối
'''

# Plotly - Tương tác mạnh
st.header("Plotly")

fig = px.line(
    df,
    x="Năm",
    y="Doanh thu",
    title="Doanh thu theo năm (Plotly)",
    markers=True
)

st.plotly_chart(fig)

'''
Ưu điểm
- Zoom, hover, export
- Rất phù hợp dashboard
'''

# Ví dụ chọn biểu đồ bằng widget
chart_type = st.selectbox(
    "Chọn loại biểu đồ",
    ["st.line_chart", "Matplotlib", "Seaborn", "Plotly"]
)

if chart_type == "st.line_chart":
    st.line_chart(df.set_index("Năm"))

elif chart_type == "Matplotlib":
    fig, ax = plt.subplots()
    ax.plot(df["Năm"], df["Doanh thu"], marker='o')
    st.pyplot(fig)

elif chart_type == "Seaborn":
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x="Năm", y="Doanh thu", marker="o", ax=ax)
    st.pyplot(fig)

else:
    fig = px.line(df, x="Năm", y="Doanh thu", markers=True)
    st.plotly_chart(fig)