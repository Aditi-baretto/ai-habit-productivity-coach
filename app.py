import streamlit as st
from langchain_ollama import OllamaLLM
import matplotlib.pyplot as plt

# Load AI model
llm = OllamaLLM(model="tinyllama")

# Function for habit analysis
def analyze_habits(sleep, study, exercise, screen):

    prompt = f"""
    A student has these daily habits:

    Sleep: {sleep} hours
    Study: {study} hours
    Exercise: {exercise} minutes
    Screen time: {screen} hours

    Analyze the productivity level and give suggestions to improve habits.
    Also provide a productivity score out of 100 and a short daily routine suggestion.
    """

    response = llm.invoke(prompt)

    return response


# Page settings
st.set_page_config(page_title="AI Habit Coach", page_icon="🧠")

st.title("🧠 AI Habit & Productivity Coach")
st.write("Improve your daily routine using AI insights.")

st.divider()

# Input layout
col1, col2 = st.columns(2)

with col1:
    sleep = st.number_input("😴 Sleep Hours", 0, 12)
    study = st.number_input("📚 Study Hours", 0, 12)

with col2:
    exercise = st.number_input("🏃 Exercise Minutes", 0, 120)
    screen = st.number_input("📱 Screen Time Hours", 0, 12)

# Button
if st.button("🔍 Analyze My Habits"):

    # AI analysis
    result = analyze_habits(sleep, study, exercise, screen)

    st.subheader("📊 AI Analysis")
    st.success(result)

    # Productivity score
    score = max(0, min(100, (sleep*10 + study*15 + exercise*5 - screen*5)))

    st.subheader("⚡ Productivity Score")
    st.progress(score / 100)
    st.write(f"Your score: **{score}/100**")

    # Chart
    data = {
        "Sleep": sleep,
        "Study": study,
        "Exercise": exercise,
        "Screen": screen
    }

    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())

    st.subheader("📈 Habit Overview")
    st.pyplot(fig)

    # Motivation
    st.subheader("💡 Daily Motivation")
    st.info("Small improvements in daily habits lead to big success 🚀")