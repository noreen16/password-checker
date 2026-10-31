import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="Smart Password Checker", page_icon="🔐")

# Title and Subtitle
st.title("🔐 Smart Password Strength Checker")
st.write("Enter your password below to evaluate its security strength in real-time.")

# User Input
password = st.text_input("Enter your password:", type="password")

# Logic Function
def check_password(pwd):
    score = 0
    feedback = []
    
    if len(pwd) >= 8:
        score += 1
    else:
        feedback.append("Must be at least 8 characters long.")
        
    if re.search(r"\d", pwd):
        score += 1
    else:
        feedback.append("Must contain at least one digit (0-9).")
        
    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        feedback.append("Must contain at least one uppercase letter (A-Z).")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 1
    else:
        feedback.append("Must contain at least one special character (!@#$%^&*).")
        
    return score, feedback

# Main App Button & Display Logic
if st.button("Check Strength"):
    if not password:
        st.warning("Please enter a password first!")
    else:
        score, feedback = check_password(password)
        
        # Result Display
        if score == 4:
            st.success("🎉 Strong Password! Your password meets all security criteria.")
        elif score == 3:
            st.info("⚠️ Moderate Password. Consider adding missing elements for better security.")
        else:
            st.error("❌ Weak Password. This password can be easily guessed or cracked.")
            
        # Display Improvements needed
        if feedback:
            st.subheader("Suggestions for Improvement:")
            for item in feedback:
                st.write(f"- {item}")