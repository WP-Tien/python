import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Scatter Plot với Seaborn")
df = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax)
ax.set_title("Quan hệ giữa Total Bill và Tip")
st.pyplot(fig)

# streamlit run ./6.1.Streamlit_seaborn_matplotlib.py