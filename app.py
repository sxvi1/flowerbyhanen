import streamlit as st
import pandas as pd
from joblib import load

# ----------------------
# Basic page setup
# ----------------------
st.set_page_config(
    page_title="AI Mood Flower — by Haneen",
    page_icon="🌸",
    layout="centered"
)

# Light styling (subtle, elegant)
st.markdown(
    """
    <style>
    .title { 
        text-align:center; 
        font-size: 2.0rem; 
        font-weight: 700; 
        letter-spacing: .3px;
    }
    .subtitle {
        text-align:center;
        opacity: 0.85;
        margin-bottom: 1.2rem;
    }
    .footer {
        text-align:center;
        opacity: 0.7;
        font-size: 0.9rem;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🌷 AI Mood Flower — by Haneen 🌷</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Type how you feel and I\'ll suggest a symbolic flower.</div>', unsafe_allow_html=True)

# ----------------------
# Load resources
# ----------------------
@st.cache_resource
def load_model():
    return load("mood_emotion_pipeline_haneen.joblib")

@st.cache_data
def load_flowers():
    df = pd.read_csv("flowers_map.csv")
    # ensure expected columns exist
    expected = {"emotion", "flower", "color", "meaning"}
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"flowers_map.csv is missing columns: {', '.join(sorted(missing))}")
    return df.set_index("emotion")

pipe = load_model()
flowers = load_flowers()

# ----------------------
# UI
# ----------------------
with st.form("mood_form"):
    user_text = st.text_input("How do you feel?", placeholder="e.g., I feel calm and grateful")
    submitted = st.form_submit_button("Suggest a flower 🌼")

if submitted:
    if not user_text.strip():
        st.warning("Please type a short mood sentence.")
    else:
        # Predict emotion
        emo = pipe.predict([user_text])[0]
        # Map to flower info
        if emo in flowers.index:
            row = flowers.loc[emo]
            flower = row["flower"]
            color = row["color"]
            meaning = row["meaning"]
        else:
            flower, color, meaning = "Lavender", "Purple", "Calm • serenity • peace"
        # Result card
        st.success(f"**Detected Emotion:** {emo}")
        st.write(f"**Suggested Flower:** {flower} ({color})")
        st.write(f"**Meaning:** {meaning}")
        st.markdown("---")
        st.caption("— curated by Haneen 🌹")

with st.expander("Need ideas? Example inputs"):
    st.write(
        "- I feel calm and grateful\n"
        "- I am tired but hopeful\n"
        "- I feel anxious and worried\n"
        "- I am angry about this situation"
    )
