import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# # Dữ liệu cuộn ngang/dọc
# Có thể thay đổi kích thước, chỉnh màu với st.dataframe(df, use_container_width=True)
df = pd.DataFrame({
    "Diện tích": [60, 80, 100],
    "Giá (tỷ VNĐ)": [3.2, 4.1, 5.6],
    "Điểm": [8.5, 9.0, 7.8],
    "Tuổi": [20, 22, 21],
    "Tên": ["An", "Bình", "Chi"],
})

st.dataframe(df)


# # st.table(): Bảng tĩnh, không tương tác
# Không có thanh cuộn, phù hợp với bảng nhỏ, tĩnh
# Được định dạng đẹp, giống như báo cáo.
st.table(df)

# # st.json(): Hiển thị JSON dạng cây
data = {
    "model": "LinearRegression",
    "metrics": {"R2": 0.81, "MAE": 1200000000}
}
st.json(data)
# Tốt cho hiển thị dữ liệu dạng dict, API response, hoặc cấu hình mô hình

# # Hiển thị biểu đồ nhanh
# Line chart
st.line_chart(df["Điểm"])

# Bar chart
st.bar_chart(df["Tuổi"])

# # Hiển thị biểu đồ nâng cao (Matplotlib)
fig, ax = plt.subplots()
ax.plot(df["Tên"], df["Điểm"])
ax.set_title("Biểu đồ điểm")

st.pyplot(fig)

# # Hiển thị biểu đồ tương tác (Plotly)
fig = px.bar(df, x="Tên", y="Điểm", title="Điểm sinh viên")
st.plotly_chart(fig)
# Biểu đồ zoom, hover, export được

'''

from PIL import Image
img = Image.open("image.png")
st.image(img, caption="Ảnh minh họa", width=300)


file = st.file_uploader("Upload file CSV", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.dataframe(df)

col = st.selectbox("Chọn cột", df.columns)
st.line_chart(df[col])

st.sidebar.header("Tùy chọn")
st.sidebar.dataframe(df)

'''

# streamlit run main.py