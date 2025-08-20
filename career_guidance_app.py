
import streamlit as st
import pandas as pd

# Sample career paths database
career_paths = pd.DataFrame([
    {
        "career_name": "Data Scientist",
        "required_skills": ["Python", "Statistics", "Machine Learning"],
        "recommended_courses": ["IBM Data Science", "Coursera ML by Andrew Ng"],
        "estimated_time_months": 6,
        "platforms": ["Coursera", "edX", "Udemy"]
    },
    {
        "career_name": "Frontend Developer",
        "required_skills": ["HTML", "CSS", "JavaScript", "React"],
        "recommended_courses": ["Meta Frontend Developer", "freeCodeCamp"],
        "estimated_time_months": 4,
        "platforms": ["Coursera", "freeCodeCamp", "Udemy"]
    },
    {
        "career_name": "AI Product Manager",
        "required_skills": ["Product Management", "AI Concepts", "Communication"],
        "recommended_courses": ["AI for Everyone by Andrew Ng", "Product School"],
        "estimated_time_months": 5,
        "platforms": ["Coursera", "Product School"]
    }
])

# Streamlit UI
st.title("🎯 Agnetic AI Career Guidance Agent")

# Dropdowns for skills and goals
all_skills = sorted(set(skill for skills in career_paths["required_skills"] for skill in skills))
selected_skills = st.multiselect("✅ Select your skills:", options=all_skills)

goals = career_paths["career_name"].tolist()
selected_goal = st.selectbox("🎯 Select your career goal:", options=goals)

# Text input for challenges
user_challenges = st.text_area("💬 Describe your current challenges:")

# Submit button
if st.button("🔍 Get Career Guidance"):
    # Filter career path based on selected goal
    career_info = career_paths[career_paths["career_name"] == selected_goal].iloc[0]

    # Display career guidance
    st.subheader("📌 Recommended Career Path")
    st.write(f"**Career:** {career_info['career_name']}")
    st.write(f"**Required Skills:** {', '.join(career_info['required_skills'])}")
    st.write(f"**Estimated Time to Reach Goal:** {career_info['estimated_time_months']} months")
    st.write(f"**Recommended Courses:** {', '.join(career_info['recommended_courses'])}")
    st.write(f"**Platforms:** {', '.join(career_info['platforms'])}")

    # Display user challenges
    st.subheader("🧠 Your Challenges")
    st.write(user_challenges)

    # Placeholder for web search integration
    st.subheader("🌐 Explore More")
    st.write("You can search for LinkedIn profiles or additional resources online based on your selected goal.")
