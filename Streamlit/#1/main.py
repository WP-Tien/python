# st.title(): Tiêu đề lớn của ứng dụng
# Tạo tiêu đề chính, hiển thị với kích thước lớn.
# streamlit run main.py

import streamlit as st

st.title("Dự đoán giá nhà với Machine Learning")

# st.text(): Hiển thị văn bản đơn giản (mono font)
# Hiển thị văn bản kiểu cơ bản, không hỗ trợ định dạng.
st.text("Chào mừng bạn đến với ứng dụng ML đơn giản.")

# st.write(): Hàm "đa năng"
# Tự động định dạng kiểu dữ liệu (chuỗi, số, dict, DataFrame,...)
# Gợi ý: Dùng thay cho print() khi debug hoặc hiển thị linh hoạt.
st.write("Sử dụng mô hình Linear Regression để dự đoán giá nhà.")
st.write("Giá nhà trung bình:", 3.5e9)
st.write({"Mô hình": "Linear Regression", "Điểm số": 0.82})

'''
Bạn hoàn toàn đung khi thấy rằng cả st.text và st.write đều có thẻ được dùng để hiển thị văn bản trong Streamlit. Tuy nhiên, chúng có những điểm khác biệt quan trọng về chức năng và cách sử dụng, khiến cả hai đều cấn thiết tuỳ thuộc vào ngữ cảnh:
1. st.write(): "Con dao đa năng"
- Tính linh hoạt: st.write() là lệnh "Swiss Army knife" của Streamlit. Nó cực kỳ linh hoạt và có thể hiển thị hầu hết mọi thứ bạn đưa và nó:
-- Văn bản: Nếu bạn truyền một chuỗi, st.write() sẽ mặc định xử lý nó như Markdown. Điều này có nghĩa là bạn có thể dễ dàng định dạng văn bản (in đậm, in nghiêng, tiêu đề, danh sách, v.v..), thêm biểu tượng cảm xúc và thậm chí cả biểu thức LaTex.
-- Kiểu dữ liệu khác: Nó cũng có thể hiển thị:
--- Pandas DataFrames (dưới dạng bảng tương tác)
--- Các biểu đồ từ Matplotlib, Altair, Plotly, Bokeh, v.v..
--- Hình ảnh (PIL.Image)
--- Từ điển và danh sách (dưới dạng widget tương tác)
--- Các đối tượng Python khác (nó sẽ cố gắng hiển thị thông tin hữu ích về chúng, ví dụ như tài liệu)
--- Bạn có thể truyền nhiều đối số cùng một lúc và st.write() sẽ hiển thị tất cả chúng.
-- Tự động định dạng: Điểm mạnh lớn nhất của st.write() là nó tự động "phán đoán" loại dữ liệu bạn đưa vào và chọn cách hiển thị phù hợp nhất
2. st.text(): "Văn bản thuần tuý, cố định"
- Văn bản thuần tuý (Plain Text): st.text() chỉ hiển thị văn bản thuần tuý mà không có bất kỳ định dạng Markdown, HTML hay LaTex nào được áp dụng. Nó hiễn thị chính xác chuỗi mà bạn truyền vào.
- Font cố định (Monospace Font): Văn bản được hiển thị bơi st.text() thường có font chữ cố định (monospace font), giống như khi bạn hiên thị code hoặc output từ terminal.
- Không tự động định dạng: Nó không cố gắng hiểu hay định dạng dữ liệu của bạn. Nếu bạn truyền một DataFrame vào st.text(), nó sẽ chỉ hiển thị biểu diễn chuỗi của DataFrame đó, chứ không phải một bảng tương tác đẹp mắt.
'''

# st.markdown(): Viết nội dung với cú pháp Markdown
st.markdown("""
            ### Mục tiêu ứng dụng
            - Nhập thông tin về nhà
            - Dự đoán giá
            - Xem biểu đồ và số liệu
            
            ** Lưu ý:** Kết quả chỉ mang tính chất tham khảo.
            """)
'''
- Markdown hỗ trợ:
-- # đến ###### tạo tiêu đề các cấp
-- **bold**, _italic_, - list, > quote
-- Gắn link, ảnh, và cả HTML đơn giản
'''