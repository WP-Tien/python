'''
Streamlit là thư viện Python giúp dựng ứng dụng Web tương tác cho Data Science/ML cực nhanh (chỉ với file .py). Bạn viết Python như thường, thêm vài st.widget, là có UI chạy ngay.

Điểm mạnh:
- Nhanh & đơn giản: Không cần HTML/CSS/JS, chỉ Python
- Tương tác tức thì: Widgets: st.slider, st.selectbox, st.button, ...
- Tích hợp khoa học dữ liệu: Hiển thị matplotlib, seaborn, plotly, bảng pandas.
'''

# Ví dụ cơ bản
import streamlit as st

st.title("Xin chào Streamlit")
st.write("Đây là ứng dụng Streamlit đơn giản đầu tiên của bạn.")

name = st.text_input("Nhập tên của bạn: ")
if name:
    st.success(f"Chào {name}!")
    
# Run cmd: streamlit run ./6.0.Streamlit.py