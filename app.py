import streamlit as st
import pandas as pd
import joblib

# 🌸 إعداد الصفحة
st.set_page_config(
    page_title="AI Mood Flower 🌷 by Haneen",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 🌷 عنوان رئيسي بتصميم بسيط
st.markdown("""
    <style>
    body {background-color: #fffafc;}
    .title {
        text-align: center;
        color: #d86fa7;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .subtitle {
        text-align: center;
        color: #7d5575;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🌷 AI Mood Flower 🌷</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Discover the flower that matches your emotion — by Haneen 💖</p>", unsafe_allow_html=True)
st.markdown("---")

# 🌼 تحميل النموذج والبيانات
pipe = joblib.load("mood_emotion_pipeline_haneen.joblib")
flowers = pd.read_csv("flowers_map.csv")

# 💬 إدخال المستخدم
user_text = st.text_input("✨ Type how you feel:", placeholder="Example: I feel calm and grateful")

# 🚀 زر التنفيذ
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
        st.markdown("<br><p style='text-align:center;'>– Curated by Haneen 🌷</p>", unsafe_allow_html=True)

# ✨ ملاحظة جانبية تحت الصفحة
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#b0839d;'>Made with 💖 by Haneen Al-Shuwimi</p>",
    unsafe_allow_html=True
)
