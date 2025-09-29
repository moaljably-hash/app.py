import streamlit as st
import random
import datetime
import matplotlib.pyplot as plt
# Install matplotlib (only needed in some environments)
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])

# --- Title ---
st.title("🏋️‍♂️ FitSmart AI")
st.subheader("Your Personalized Workout Planner — AI Assisted 💡")

# --- User Input ---
goal = st.selectbox("🎯 What's your fitness goal?", ["Build Muscle", "Lose Fat", "Improve Cardio"])
level = st.selectbox("📊 What's your fitness level?", ["Beginner", "Intermediate", "Advanced"])
days = st.slider("📅 How many days per week can you work out?", 1, 7, 3)

# --- Generate Workout Plan Function ---
def generate_workout(goal, level, days):
    plan = []
    for i in range(days):
        if goal == "Build Muscle":
            workouts = [
                "Push-ups", "Dumbbell Rows", "Lunges", "Plank", "Incline Push-ups",
                "Squats", "Glute Bridges", "Bench Dips", "Deadlifts", "Pull-ups"
            ]
        elif goal == "Lose Fat":
            workouts = [
                "Jumping Jacks", "Burpees", "Mountain Climbers", "High Knees", "Squat Jumps",
                "Plank Jacks", "Skater Hops", "Jump Squats", "Speed Lunges", "Side Shuffles"
            ]
        else:
            workouts = [
                "Running", "Cycling", "Jump Rope", "Rowing", "Stair Sprints",
                "Brisk Walking", "High Knees", "Shadow Boxing", "Jumping Jacks", "Battle Ropes"
            ]
        selected = random.sample(workouts, 5)
        plan.append((f"Day {i+1}", selected))
    return plan

# --- Display Workout Plan ---
if st.button("Generate My Workout Plan"):
    st.markdown(f"### ✅ Weekly Workout Plan")
    st.markdown(f"**Goal:** {goal}  \n**Level:** {level}  \n**Days per week:** {days}")
    plan = generate_workout(goal, level, days)
    for day, exercises in plan:
        st.markdown(f"**{day}**")
        for ex in exercises:
            st.markdown(f"- **{ex}** — 3 sets of 12 reps")

# --- Progress Input ---
st.markdown("### 📥 Enter Your Workout Completion for the Past 7 Days")
progress = []
weekdays = [(datetime.date.today() - datetime.timedelta(days=i)).strftime("%A") for i in range(6, -1, -1)]

with st.form("progress_form"):
    for day in weekdays:
        value = st.slider(f"{day} completion (%)", 0, 100, 0, key=day)
        progress.append(value)
    submitted = st.form_submit_button("Show Progress Chart")

# --- Display Chart ---
if submitted:
    st.markdown("### 📈 Your Workout Completion This Week")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(weekdays, progress, marker='o', linewidth=2)
    ax.set_title("Workout Completion Rate")
    ax.set_ylabel("Completion (%)")
    ax.set_xticklabels(weekdays, rotation=45)
    ax.grid(True)
    st.pyplot(fig)

