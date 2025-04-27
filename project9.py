import streamlit as st
import datetime
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Wellness Web App", page_icon="🌿", layout="wide")

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Select a page:", ["🏠 Home", "📘 About", "🩺 Health Dashboard", "📬 Contact"])

# ---------------- HOME ----------------
if page == "🏠 Home":
    st.title("🌟 Welcome to Your Wellness Hub")
    st.markdown("""
    Stay on top of your health and lifestyle goals with this all-in-one wellness tracker built using **Streamlit**.
    
    - Use the **Health Dashboard** to log daily wellness metrics.
    - Learn more on the **About** page.
    - Reach out through the **Contact** form.
    """)
    

# ---------------- ABOUT ----------------
elif page == "📘 About":
    st.title("📖 About This Application")
    st.markdown("""
    This is a multi-functional web app created using **Streamlit** to help individuals:
    
    - Track health habits like calories, water intake, and physical activity.
    - Set and monitor wellness goals.
    - Visualize progress over time.

    **Technologies used**:
    - Streamlit (Python)
    - Plotly (Charts)
    - Pandas (Data Management)
    
    Built with ❤️ for a healthier you!
    """)

# ---------------- HEALTH DASHBOARD ----------------
elif page == "🩺 Health Dashboard":
    st.title("🩺 Health Dashboard")

    # Calorie Tracker
    st.subheader("🍎 Calorie Intake")
    calorie_goal = st.number_input("Your daily calorie goal:", 1000, 5000, 2000)
    calories_today = st.number_input("Calories consumed today:", 0, 10000, 0)
    remaining_calories = calorie_goal - calories_today

    if remaining_calories > 0:
        st.success(f"You have {remaining_calories} calories remaining today.")
    else:
        st.error("You've exceeded your calorie goal for today!")

    # Hydration Tracker
    st.subheader("💧 Hydration Check")
    water_goal = st.slider("Daily water goal (liters):", 1.0, 5.0, 2.0, 0.1)
    water_today = st.number_input("Water consumed today (liters):", 0.0, water_goal, 0.0, format="%.1f")

    if water_today >= water_goal:
        st.success("You're well-hydrated today! ✅")
    else:
        st.warning(f"Drink {water_goal - water_today:.1f} more liters to meet your goal.")

    # Step Counter
    st.subheader("🚶‍♀️ Daily Steps")
    step_goal = st.number_input("Your daily step goal:", 1000, 25000, 10000)
    steps_today = st.number_input("Steps taken today:", 0, step_goal * 2, 0)

    if steps_today >= step_goal:
        st.success("Step goal achieved! Great job 🎉")
    else:
        st.info(f"Only {step_goal - steps_today} more steps to go!")

    # Sample Historical Data (for demo)
    st.subheader("📊 Your Weekly Step Progress")
    dates = pd.date_range(end=datetime.date.today(), periods=7)
    data = pd.DataFrame({
        "Date": dates,
        "Steps": [steps_today - i*500 if steps_today - i*500 > 0 else 0 for i in range(7)]
    })
    fig = px.line(data, x="Date", y="Steps", title="Weekly Step Trend", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # PDF Download Placeholder
    st.markdown("📄 **Coming soon:** Export your health summary as a PDF report!")

# ---------------- CONTACT ----------------
elif page == "📬 Contact":
    st.title("📞 Contact Us")
    st.markdown("We'd love to hear from you! Fill out the form below:")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")

        if submit:
            if name and email and message:
                st.success("✅ Thank you! We'll get back to you shortly.")
            else:
                st.error("⚠️ Please fill in all fields before submitting.")
