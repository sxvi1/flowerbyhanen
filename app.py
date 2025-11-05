import streamlit as st
import pandas as pd
import joblib

# 🌸 إعداد الصفحة
st.set_page_config(
    page_title="AI Mood Flower by Haneen",
    page_icon="🌷",
    layout="centered",
)

# 🌷 تنسيق الألوان والخلفية
st.markdown("""
    <style>
    body {
        background: linear-gradient(180deg, #fff7fb, #ffeef5);
        color: #5a3d4e;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .title {
        text-align: center;
        color: #d86fa7;
        font-size: 38px;
        font-weight: bold;
        margin-bottom: -10px;
    }
    .subtitle {
        text-align: center;
        color: #7d5575;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .footer {
        text-align: center;
        color: #9c7b8c;
        font-size: 14px;
        margin-top: 40px;
    }
    div.stButton > button {
        background-color: #e4b7d0;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #d396b8;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# 🌺 العنوان الرئيسي
st.markdown("<h1 class='title'>AI Mood Flower</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Discover the flower that matches your emotion — by Haneen</p>", unsafe_allow_html=True)
st.markdown("---")

# 💫 رسالة ترحيب تظهر مرة واحدة
st.toast("Welcome Haneen 🌷 Ready to discover your mood flower?", icon="🌸")

# 🌼 تحميل النموذج والبيانات
pipe = joblib.load("mood_emotion_pipeline_haneen.joblib")
flowers = pd.read_csv("flowers_map.csv")

# 💭 إدخال المستخدم
st.markdown("### ✨ How do you feel today? 💭")
user_text = st.text_input("Type how you feel:", placeholder="Example: I feel calm and grateful")

# 🌸 زر التشغيل ونتيجة العرض
if st.button("Show My Flower 🌸"):
    if user_text.strip() == "":
        st.warning("Please type something first 💬")
    else:
        emo = pipe.predict([user_text])[0]
        row = flowers[flowers["emotion"] == emo].iloc[0]
        flower = row["flower"]
        color = row["color"]
        meaning = row["meaning"]

        st.success("🌼 Result:")
        st.write(f"**Detected Emotion:** {emo}")
        st.write(f"**Suggested Flower:** {flower} ({color})")
        st.write(f"**Meaning:** {meaning}")

st.markdown("<p class='footer'>© 2025 — Designed & Curated by Haneen 🌷</p>", unsafe_allow_html=True)
