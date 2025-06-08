
import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="IPL Win Predictor", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏆 IPL Win Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Predict match outcome probabilities based on current match situation</h4>", unsafe_allow_html=True)
st.markdown("---")

teams = [
    'Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab',
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]

cities = [
    'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Hyderabad', 'Chennai', 'Bangalore',
    'Jaipur', 'Pune', 'Ahmedabad', 'Nagpur'
]

# Sidebar input
st.sidebar.title("🎯 Match Details")
batting_team = st.sidebar.selectbox("🏏 Batting Team", sorted(teams))
bowling_team = st.sidebar.selectbox("🎯 Bowling Team", sorted([t for t in teams if t != batting_team]))
city = st.sidebar.selectbox("📍 Match City", sorted(cities))

target = st.sidebar.number_input("🎯 Target Score", min_value=1)
current_score = st.sidebar.number_input("🏏 Current Score", min_value=0, max_value=target-1)
overs_done = st.sidebar.number_input("⏱ Overs Completed", min_value=0.0, max_value=20.0, step=0.1, format="%.1f")
wickets_fallen = st.sidebar.slider("💔 Wickets Fallen", 0, 10, 2)

# Calculate features
runs_left = target - current_score
balls_left = int((20 - overs_done) * 6)
wickets_in_hand = 10 - wickets_fallen
crr = current_score / overs_done if overs_done > 0 else 0
rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

# Create input DataFrame
input_df = pd.DataFrame({
    'batting_team': [batting_team],
    'bowling_team': [bowling_team],
    'city': [city],
    'runs_left': [runs_left],
    'balls_left': [balls_left],
    'wickets_in_hand': [wickets_in_hand],
    'total_runs_x': [target],
    'crr': [crr],
    'rrr': [rrr]
})

# Load model and predict
try:
    pipe = joblib.load("ipl_model.pkl")
    result = pipe.predict_proba(input_df)
    win_prob = np.round(result[0][1] * 100, 2)
    lose_prob = np.round(result[0][0] * 100, 2)

    # Layout: Two columns for team prediction
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### 🟢 <span style='color:#28a745'>{batting_team}</span>", unsafe_allow_html=True)
        st.markdown(f"#### Win Probability: `{win_prob}%`")
        st.progress(int(win_prob))
    with col2:
        st.markdown(f"### 🔴 <span style='color:#dc3545'>{bowling_team}</span>", unsafe_allow_html=True)
        st.markdown(f"#### Win Probability: `{lose_prob}%`")
        st.progress(int(lose_prob))

    # Summary below
    st.markdown("---")
    st.markdown(f"**Match Situation Summary**")
    st.markdown(f"- 🏏 **Current Score:** {current_score}/{wickets_fallen}")
    st.markdown(f"- 🎯 **Target Score:** {target}")
    st.markdown(f"- ⏱ **Overs Completed:** {overs_done}")
    st.markdown(f"- 🔁 **Balls Left:** {balls_left}")
    st.markdown(f"- 💪 **Wickets in Hand:** {wickets_in_hand}")
    st.markdown(f"- ⚡ **Current Run Rate (CRR):** {round(crr, 2)}")
    st.markdown(f"- 🚀 **Required Run Rate (RRR):** {round(rrr, 2)}")

except Exception as e:
    st.error("⚠️ Model could not make a prediction. Please check the inputs or make sure the model is saved as `ipl_model.pkl`.")
    st.text(str(e))

