# 🏏 IPL Win Predictor

This project predicts the winning probability of a team in an ongoing IPL (Indian Premier League) T20 cricket match using machine learning. The model is trained on past IPL match data and allows users to interact with a **Streamlit-based GUI** for real-time predictions.

---

## 🚀 Features

- Predicts win probability using **Random Forest Classifier**
- Uses match context: runs left, balls left, wickets, current/required run rate
- Clean Streamlit interface for user interaction
- Visual match progression graph (win/lose %, runs, wickets)

---

## 📊 Model Performance

- **Train Accuracy:** ~99.99%
- **Test Accuracy:** ~99.95%
- **F1-Score:** 1.00

> The model generalizes well with very low misclassification, thanks to well-engineered features and balanced classes.

---

## 🧠 Model Inputs (Features)

- Batting Team
- Bowling Team
- City
- Runs Left
- Balls Left
- Wickets in Hand
- Total Runs Target
- Current Run Rate (CRR)
- Required Run Rate (RRR)

---

## 🖼️ App Preview



![App Screenshot](screenshots/app_screenshot.png)

> ✅ Green Line: Win Probability  
> ❌ Red Line: Lose Probability  
> 📊 Blue Bars: Runs scored per over  
> 💥 Yellow Line: Wickets lost per over

---

## ✨ Author

**Abdul Hadi**  
AI Undergraduate | Machine Learning Enthusiast  
[LinkedIn]([https://www.linkedin.com/in/abdul-hadi-969b48244/](https://www.linkedin.com/in/abdul-hadi-070727259/))
