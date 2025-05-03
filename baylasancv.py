import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Baylasan Almuqati | Data Science Portfolio",
    page_icon="📊",
    layout="centered"
)

# Main header
st.title("👩‍💻 Baylasan Almuqati")
st.subheader("Data Scientist | Analyst | Business Enthusiast")
st.markdown("---")

# About Section
st.markdown("## 🌟 About Me")
st.markdown("""
Hello! I'm **Baylasan Almuqati**, a passionate and aspiring data scientist currently studying at **Princess Nourah bint Abdulrahman University**.

My interests lie at the intersection of **data, business, and technology** — I love turning raw data into meaningful insights that drive smart decisions. From analyzing user behavior to predicting trends, I enjoy every step of the data journey.

I'm particularly interested in:
- 📈 Business Intelligence
- 🧠 Machine Learning
- 📊 Data Visualization
- 💼 Strategic Analysis
""")

# Project Section
st.markdown("---")
st.markdown("## 🚀 Featured Project")

st.markdown("""
### 📞 Telecom Churn Prediction
This project uses machine learning (SVM model) to predict whether a customer is likely to churn from a telecom service. It was built with **Google Colab**, **Streamlit**, and deployed using **Streamlit Cloud**.

🔗 [Live Website](https://your-streamlit-app-link)  
📂 [GitHub Repository](https://github.com/yourusername/telecom-churn)

**Skills used:** Python, Pandas, Scikit-learn, Data Cleaning, Model Deployment
""")

# Education
st.markdown("---")
st.markdown("## 🎓 Education")
st.markdown("""
**Princess Nourah bint Abdulrahman University**  
_Bachelor’s in Data Science_  
📍 Riyadh, Saudi Arabia  
""")

# Footer
st.markdown("---")
st.markdown("## 📫 Get in Touch")
st.markdown("""
- 📧 Email: [your-email@example.com](mailto:your-email@example.com)
- 💼 LinkedIn: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)
- 🐙 GitHub: [github.com/yourusername](https://github.com/yourusername)
""")

st.markdown("----")
st.markdown("Made with ❤️ using Streamlit")

