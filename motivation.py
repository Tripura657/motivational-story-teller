import streamlit as st
import google.generativeai as genai

# Set your API key here securely
API_KEY = "AIzaSyCX5TKAFYkpT3JLnEa0_alXNjwYpe_-S2E"  # Add your Gemini API key
genai.configure(api_keyy=st.secrets["GEMINI_API_KEY"])

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit Page UI
st.set_page_config(page_title="Motivational Chatbot")
st.title("💬 Motivational Story Chatbot")
st.write("Tell me what's on your mind, and I’ll share a story that might lift you up! 💙")

# Ask user about their current situation
situation = st.text_input("🌱 Describe your current situation:")

# If the user enters something
if situation:
    try:
        # Send prompt to Gemini for story generation
        prompt = (
            f"You are a motivational storyteller. The user is going through this: '{situation}'. "
            "Please respond with an inspiring short story that helps them feel strong and positive."
        )
        response = model.generate_content(prompt)
        story = response.text

        # Display the response
        st.subheader("📖 Here's a story for you:")
        st.success(story)

    except Exception as e:
        st.error("Oops! Something went wrong. Please try again later. 💙")
