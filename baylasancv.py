import streamlit as st

# Configure the page
st.set_page_config(
    page_title="بيلسان المقاطي | عالمة بيانات",
    page_icon="📊",
    layout="centered"
)

# Custom CSS for dark theme and background image
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0e1117;
            color: #f0f0f0;
            font-family: 'Cairo', sans-serif;
            background-image: url('https://your-background-image-link.jpg');
            background-size: cover;
            background-position: center;
        }
        h1, h2, h3 {
            color: #ffb703;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        }
        a {
            color: #8ecae6;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        a:hover {
            color: #ffb703;
        }
        .stMarkdown p {
            line-height: 1.8;
        }
        .stButton > button {
            background-color: #ffb703;
            color: #0e1117;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #e68a00;
        }
        .stSlider > div {
            background-color: #8ecae6;
            border-radius: 10px;
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

# Add interactivity with a button and slider
st.markdown("## 🛠️ تجربة تفاعلية")
if st.button('اضغط هنا لمعرفة المزيد'):
    st.write("شكرًا للنقر! يمكنني الآن عرض المزيد من التفاصيل حول مشاريعك.")
    
# Add a slider to interact with the user
slider_value = st.slider("اختار قيمة للعرض", 1, 100, 50)
st.write(f"القيمة المختارة هي: {slider_value}")

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
- 💼 لينكدإن: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)
- 🐙 GitHub: [github.com/yourusername](https://github.com/yourusername)
""")

# Footer with interactive hover effect
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


