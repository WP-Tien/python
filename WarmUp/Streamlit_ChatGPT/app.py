import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="Chat với GPT-4o", page_icon="")

# 1) Lấy API key (ưu tiên secrets, fallback ENV)
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
if not OPENAI_API_KEY:
    st.error("Chưa có OPENAI_API_KEY trong st.secrets hoặc biến môi trường!")
    st.stop()
    
client = OpenAI(api_key=OPENAI_API_KEY)

# Khung giao diện & lưu lịch sử
st.title("Chat với GPT-4o")

# 2) Khởi tạo lịch sử hội thoại
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# 3) Hiển thị lịch sử tin nhắn đã có
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
# 4) Gửi tin nhắn & gọi OpenAI - Ô nhập chat ở cuối trang
if prompt := st.chat_input("Nhập câu hỏi của bạn..."):
    # Hiển thị tin nhắn người dùng + lưu lịch sử
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 5) Gọi OpenAI chat Conmpletions
    try:
        response = client.responses.create(
            model="gpt-4o",
            input=st.session_state.messages,
            temperature=0.7
        )
        reply = response.output_text
    except Exception as e:
        reply = f"(Lỗi gọi API: {e})"
        
    # Hiển thị và lưu phản hồi
    st.chat_message("assistant").write(reply)
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )