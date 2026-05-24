import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.subheader("Khảo sát hàm số với slider")
func = st.selectbox("Chọn hàm:", ["sin", "cos", "exp", "log"])
x = np.linspace(-10, 10, 500)

if func == "sin":
    y = np.sin(x)
elif func == "cos":
    y = np.cos(x)
elif func == "exp":
    y = np.exp(x)
else:
    x = np.linspace(0.1, 10, 500) # log cần x>0
    y = np.log(x)
    
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True)
ax.set_title(f"Đồ thị hàm {func}(x)")
st.pyplot(fig)