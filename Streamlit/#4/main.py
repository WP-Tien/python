import streamlit as st

# st.button() - Nút bấm
st.title("Ví dụ st.button")

if st.button("Nhấn vào đây"):
    st.success("Bạn đã nhấn nút!")
# Lưu ý
# st.button() trả về True khi được nhấn
# Sau khi reload sẽ về False

# st.checkbox() - Ô chọn (True/False)
st.title("Ví dụ st.checkbox")

agree = st.checkbox("Tôi đồng ý với điều khoản")

if agree:
    st.write("Cảm ơn bạn đã đồng ý!")

'''
    Ứng dụng:
- Bật/tắt hiển thị dữ liệu
- Xác nhận lựa chọn
'''

# st.radio() - Chọn 1 trong nhiều lựa chọn
st.title("Ví dụ st.radio")

gender = st.radio(
    "Giới tính:",
    ("Nam", "Nữ", "Khác")
)

st.write("Bạn chọn:", gender)

# Đặc điểm
# Chỉ chọn 1 giá trị
# Hiển thị dạng danh sách học

# st.selectbox() - Hộp chọn thả xuống
st.title("Ví dụ st.checkbox")

city = st.selectbox(
    "Chọn thành phố:",
    ["Hà Nội", "Đà Nẵng", "TP.HCM"]
)

st.write("Thành phố bạn chọn:", city)

# Khác với radio()
# Gọn gàng hơn
# Phù hợp danh sách dài



# streamlit run main.py