import streamlit as st

st.title("Ứng dụng khảo sát nhỏ")

name = st.text_input("Nhập tên của bạn")

agree = st.checkbox("Tôi đồng ý tham gia khảo sát")

gender = st.radio("Giới tính", ["Nam", "Nữ", "Khác"])

city = st.selectbox("Thành phố", ["Hà Nội", "Đà Nẵng", "TP.HCM"])

if st.button("Gửi thông tin"):
    if agree:
        st.success("Thông tin của bạn:")
        st.write("Tên:", name)
        st.write("Giới tính:", gender)
        st.write("Thành phố:", city)
    else:
        st.warning("Bạn cần đồng ý để tiếp tục")

# streamlit run main.py