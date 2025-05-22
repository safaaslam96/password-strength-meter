import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

# Theme toggle (top radio buttons)
theme = st.radio("Choose Theme", ["🌸 Light Purple", "🟣 Dark Purple"], horizontal=True)

# Theme CSS
if theme == "🟣 Dark Purple":
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #1a002d, #3d0070);
            color: white;
            transition: background 0.5s ease;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stTextInput > div > div > input {
            background-color: #333;
            color: white;
            border: 1px solid #777;
            border-radius: 8px;
            padding: 12px;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #bb86fc;
            color: black;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: bold;
            transition: background-color 0.4s ease, transform 0.3s ease;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #d3a2ff;
            transform: scale(1.07);
        }
        .strength-emoji {
            font-size: 48px;
            margin-bottom: 10px;
            transition: color 0.5s ease;
        }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #f3e5f5, #d1c4e9);
            color: #2c2c54;  /* Dark purple shade for text for better visibility */
            transition: background 0.5s ease;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stTextInput > div > div > input {
            background-color: #fff;
            color: #2c2c54;  /* Dark purple shade text */
            border: 2px solid #9c27b0;
            padding: 12px;
            border-radius: 8px;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #9c27b0;
            color: white;
            padding: 10px 24px;
            font-weight: bold;
            border-radius: 8px;
            transition: background-color 0.4s ease, transform 0.3s ease;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #ab47bc;
            transform: scale(1.07);
        }
        .strength-emoji {
            font-size: 48px;
            margin-bottom: 10px;
            transition: color 0.5s ease;
        }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🔐 Password Strength Meter")
st.markdown("""
### Welcome!
Use this tool to check how strong your password is and receive real-time suggestions to improve it.  
We'll help you build a **secure password** step by step.  
""")

password = st.text_input("Enter your password", type="password")

score = 0
checks = []

if password:
    if len(password) >= 8:
        checks.append("✅ Password is at least 8 characters long.")
        score += 1
    else:
        checks.append("❌ Password should be at least 8 characters.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        checks.append("✅ Contains both upper and lowercase letters.")
        score += 1
    else:
        checks.append("❌ Add both UPPER and lower case letters.")

    if re.search(r'\d', password):
        checks.append("✅ Contains a number.")
        score += 1
    else:
        checks.append("❌ Add at least one number.")

    if re.search(r'[!@#$%&*]', password):
        checks.append("✅ Contains a special character (!@#$%&*).")
        score += 1
    else:
        checks.append("❌ Add a special character (!@#$%&*).")

    # Emoji & color based on strength
    emoji = "🔴"
    emoji_color = "#ff4d4d"
    message = "Very Weak Password"
    if score == 4:
        emoji = "✅🎉"
        emoji_color = "#00cc44"
        message = "Strong Password"
    elif score == 3:
        emoji = "🟡"
        emoji_color = "#f5c518"
        message = "Medium Strength Password"
    elif score == 2:
        emoji = "🟠"
        emoji_color = "#ff9900"
        message = "Weak Password"

    st.markdown(f'<div class="strength-emoji" style="color:{emoji_color}">{emoji}</div>', unsafe_allow_html=True)

    for item in checks:
        color = "green" if "✅" in item else "red"
        st.markdown(f"<div style='color:{color}; font-weight: 600;'>{item}</div>", unsafe_allow_html=True)

    st.markdown("### 🔋 Strength Meter")
    if score == 4:
        st.success(f"✅ {message}! 🎉")
        st.progress(100)
    elif score == 3:
        st.warning(f"🟡 {message}")
        st.progress(75)
    elif score == 2:
        st.warning(f"🟠 {message}")
        st.progress(50)
    else:
        st.error(f"🔴 {message}")
        st.progress(25)
else:
    st.info("Start typing a password above to check its strength.")
