import streamlit as st
# streamlit run main.py

# 1. st.title() - Hiển thị tiêu đề chính của ứng dụng
st.title("Relax - Thứ Bảy, Ngày 24")
st.write('---')

# 2. st.header() - Hiển thị tiêu đề cấp 2 (sub-header)
st.header("1. Học Streamlit 60 phút!")

st.markdown("""
#### Tự học Streamlit trong 60 phút!
##### *Nội dung buỏi học*:
- Hiển thị text: st.title(), st.text, st.write(), st.markdown()
- Hiển thị dữ liệu: ...            
            """)

st.code("""
        st.title("Đây là tiêu đề chính")
        st.text("Hiển thị chữ cơ bản")
        st.write("Hiển thị chữ đa dạng")
        st.mardown("Hiển thị chữ theo form setup")
        st.code("Hiển thị code")
        """)

st.write("---")

st.markdown("[Link tới Google](http://google.com)")