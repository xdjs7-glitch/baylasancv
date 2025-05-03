import streamlit as st

# Configure the page
st.set_page_config(
    page_title="بيان السان المقاطي | عالمة بيانات",
    page_icon="📊",
    layout="centered"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0e1117;
            color: #f0f0f0;
            font-family: 'Cairo', sans-serif;
        }
        h1, h2, h3 {
            color: #ffb703;
        }
        a {
            color: #8ecae6;
        }
        .stMarkdown p {
            line-height: 1.8;
        }
    </style>
""", unsafe_allow_html=True)

# Arabic content
st.title("👩‍💻 بيلسان خالد المقاطي")
st.subheader("عالمة بيانات | محللة | شغوفة بالأعمال")
st.markdown("---")

# About Me
st.markdown("## 🌟 عني")
st.markdown("""
مرحبًا! أنا **بيلسان المقاطي**، طالبة في **جامعة الأميرة نورة بنت عبد الرحمن** وشغوفة بعلم البيانات وتحليل الأعمال.

أؤمن بأن البيانات هي مفتاح النجاح في العصر الحديث، وأسعى لاستخدامها لفهم الأنماط، دعم اتخاذ القرار، وتقديم رؤى قيّمة تساعد في تطوير الاستراتيجيات.

**اهتماماتي تشمل:**
- 📈 ذكاء الأعمال
- 🤖 تعلم الآلة
- 📊 التصوير البياني للبيانات
- 💼 تحليل الأسواق والاستراتيجيات
""")

# Projects
st.markdown("---")
st.markdown("## 🚀 مشروع مميز")

st.markdown("""
### 📞 التنبؤ بمغادرة العملاء في قطاع الاتصالات
مشروع يستخدم نموذج تعلم الآلة (SVM) للتنبؤ باحتمالية مغادرة العميل لخدمة الاتصالات. تم تطويره باستخدام **Google Colab** و**Streamlit** وتم نشره عبر **Streamlit Cloud**.

🔗 [رابط الموقع](https://your-streamlit-app-link)  
📂 [رابط GitHub](https://github.com/yourusername/telecom-churn)

**المهارات المستخدمة:** بايثون، معالجة البيانات، Scikit-learn، النشر عبر السحابة
""")

# Education
st.markdown("---")
st.markdown("## 🎓 التعليم")
st.markdown("""
**جامعة الأميرة نورة بنت عبد الرحمن**  
_بكالوريوس في علم البيانات_  
📍 الرياض، المملكة العربية السعودية
""")

# Contact
st.markdown("---")
st.markdown("## 📫 تواصل معي")
st.markdown("""
- 📧 البريد الإلكتروني: [baylasanalmuqati@gmail.com](mailto:baylasanalmuqati@gmail.com)
- 💼 لينكدإن: [linkedin.com/in/baylasan-almuqati](https://linkedin.com/in/baylasan-almuqati)

""")

# Footer
st.markdown("----")
st.markdown("تم الإنشاء بكل ❤️ من قبل baylasana")
# Hide Streamlit default menu and footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

