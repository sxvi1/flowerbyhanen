import streamlit as st
import pandas as pd
from joblib import load

# 💐 إعدادات الصفحة
st.set_page_config(page_title="AI Mood Flower by Haneen 🌸", page_icon="🌷", layout="centered")

# 🎀 عنوان الواجهة
st.markdown("<h1 style='text-align: center; color: #d94e8f;'>🌸 AI Mood Flower 🌸</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #888;'>Curated with love by Haneen 💕</h4>", unsafe_allow_html=True)
st.markdown("---")

# 📦 تحميل الملفات
pipe = load('mood_emotion_pipeline_haneen.joblib')
flowers = pd.read_csv('flowers_map.csv')

# 🌺 إدخال المستخدم
st.markdown("### ✨ كيف تشعر اليوم؟")
user_text = st.text_input("اكتب شعورك بالإنجليزية مثل: I feel calm and grateful 💭")

# 🔍 عند الإدخال
if user_text:
    emo = pipe.predict([user_text])[0]
    row = flowers[flowers["emotion"] == emo].iloc[0]
    flower = row["flower"]
    color = row["color"]
    meaning = row["meaning"]

    st.success(f"**Detected Emotion:** {emo}")
    st.info(f"**Suggested Flower:** 🌼 {flower} ({color})")
    st.write(f"**Meaning:** {meaning}")
    st.markdown("<p style='text-align: center;'>– curated by Haneen 🌷</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: center; color:gray;'>💭 Waiting for your mood input...</p>", unsafe_allow_html=True)
