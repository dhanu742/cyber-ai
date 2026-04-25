# app.py

import streamlit as st
import pandas as pd
import os
import hashlib
import PyPDF2

from styles import load_css
from auth import login_page

from scanner import (
    extract_features_from_url,
    calculate_risk_score,
    detect_attack_type,
    explain_risk,
    severity_level,
    hacker_terminal
)

from ai_engine import get_ai_response

from database import (
    insert_attack,
    get_attacks
)

from predict import predict_attack


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="CYBER-X",
    layout="wide"
)


# =========================================
# LOAD CSS
# =========================================

load_css()


# =========================================
# SESSION STATE
# =========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# =========================================
# PDF SCANNER
# =========================================

def scan_pdf(uploaded_file):

    text = ""

    reader = PyPDF2.PdfReader(uploaded_file)

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted


    suspicious_keywords = [

        "password",
        "bank",
        "verify",
        "urgent",
        "crypto",
        "bitcoin",
        "wire transfer",
        "login",
        "account suspended"
    ]


    score = 0

    findings = []


    for word in suspicious_keywords:

        if word.lower() in text.lower():

            score += 10

            findings.append(word)


    return score, findings


# =========================================
# FILE SCANNER
# =========================================

def scan_file(uploaded_file):

    dangerous_extensions = [

        ".exe",
        ".bat",
        ".scr",
        ".vbs",
        ".ps1"
    ]

    filename = uploaded_file.name.lower()

    risk = 10


    for ext in dangerous_extensions:

        if filename.endswith(ext):

            risk += 60


    file_bytes = uploaded_file.read()

    md5_hash = hashlib.md5(
        file_bytes
    ).hexdigest()


    return risk, md5_hash


# =========================================
# AI CHATBOT UI
# =========================================

def chatbot_ui():

    st.markdown(
        """
        <h1 style='text-align:center;
                   color:#00ffee;
                   text-shadow:0px 0px 25px #00ffee;'>

        🤖 CYBER-X AI ROBOT

        </h1>
        """,
        unsafe_allow_html=True
    )


    # ROBOT PANEL

    st.markdown(
        """
        <div style='
        background:#0d1117;
        padding:25px;
        border-radius:25px;
        border:2px solid #00ffee;
        text-align:center;
        box-shadow:0px 0px 30px #00ffee;
        margin-bottom:20px;
        '>

        <img src='https://cdn-icons-png.flaticon.com/512/4712/4712109.png'
        width='170'>

        <h2 style='color:#00ffee;'>
        CYBER-X
        </h2>

        <p style='color:white;'>

        Advanced AI Cybersecurity Assistant

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown("### 💬 AI Secure Chat")


    # CHAT HISTORY

    for role, msg in st.session_state.chat_history:

        with st.chat_message(role):

            st.write(msg)


    # USER INPUT

    user_input = st.chat_input(
        "Ask anything about hacking, phishing, malware, cybersecurity..."
    )


    if user_input:

        st.session_state.chat_history.append(
            ("user", user_input)
        )


        response = get_ai_response(
            user_input
        )


        st.session_state.chat_history.append(
            ("assistant", response)
        )


        st.rerun()


# =========================================
# MAIN APP
# =========================================

def main_app():

    st.sidebar.title("⚡ CYBER-X")


    menu = st.sidebar.radio(

        "Navigation",

        [

            "AI Chatbot",

            "URL Threat Scanner",

            "PDF Scanner",

            "File Scanner",

            "Threat History",

            "Logout"
        ]
    )


    # =====================================
    # CHATBOT
    # =====================================

    if menu == "AI Chatbot":

        chatbot_ui()


    # =====================================
    # URL THREAT SCANNER
    # =====================================

    elif menu == "URL Threat Scanner":

        st.title("🌐 URL Threat Scanner")


        mode = st.selectbox(

            "Choose Scan Type",

            [

                "URL Scan",

                "Manual Data"
            ]
        )


        # URL MODE

        if mode == "URL Scan":

            url = st.text_input(
                "Enter URL"
            )


        # MANUAL MODE

        else:

            manual = st.text_input(

                "Enter Data",

                "0,1,1,90,9,7"
            )


        # START SCAN

        if st.button("🚀 START SCAN"):


            if mode == "URL Scan":

                data = extract_features_from_url(
                    url
                )

            else:

                data = list(
                    map(
                        int,
                        manual.split(",")
                    )
                )


            prediction = predict_attack(
                data
            )


            score = calculate_risk_score(
                data
            )


            severity = severity_level(
                score
            )


            attack_type = detect_attack_type(
                data
            )


            hacker_terminal(
                prediction
            )


            st.subheader(
                "🧠 Threat Analysis"
            )


            st.write(
                f"### Prediction: {prediction}"
            )


            st.write(
                f"### Attack Type: {attack_type}"
            )


            st.write(
                f"### Risk Score: {score}%"
            )


            st.write(
                f"### Severity: {severity}"
            )


            st.progress(score)


            reasons = explain_risk(
                data
            )


            st.subheader(
                "⚠ Threat Indicators"
            )


            for r in reasons:

                st.write(r)


            if prediction == "attack":

                insert_attack(
                    str(data)
                )


    # =====================================
    # PDF SCANNER
    # =====================================

    elif menu == "PDF Scanner":

        st.title(
            "📄 AI PDF Scanner"
        )


        pdf = st.file_uploader(

            "Upload PDF",

            type=["pdf"]
        )


        if pdf:

            score, findings = scan_pdf(pdf)


            st.write(
                f"### Threat Score: {score}%"
            )


            if findings:

                st.error(
                    "Suspicious content detected"
                )


                for item in findings:

                    st.write(
                        f"⚠ {item}"
                    )

            else:

                st.success(
                    "No suspicious content found"
                )


    # =====================================
    # FILE SCANNER
    # =====================================

    elif menu == "File Scanner":

        st.title(
            "💻 System File Scanner"
        )


        uploaded_file = st.file_uploader(
            "Upload File"
        )


        if uploaded_file:

            risk, md5_hash = scan_file(
                uploaded_file
            )


            st.write(
                f"### File Risk Score: {risk}%"
            )


            st.code(md5_hash)


            if risk >= 60:

                st.error(
                    "Potentially dangerous file"
                )

            else:

                st.success(
                    "File appears safer"
                )


    # =====================================
    # THREAT HISTORY
    # =====================================

    elif menu == "Threat History":

        st.title(
            "📜 Threat Logs"
        )


        history = get_attacks()


        if history:

            df = pd.DataFrame(

                history,

                columns=[
                    "ID",
                    "Threat"
                ]
            )


            st.dataframe(df)

        else:

            st.info(
                "No threat logs available"
            )


    # =====================================
    # LOGOUT
    # =====================================

    elif menu == "Logout":

        st.session_state.logged_in = False

        st.rerun()


# =========================================
# RUN APP
# =========================================

if not st.session_state.logged_in:

    login_page()

else:

    main_app()