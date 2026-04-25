# scanner.py

import streamlit as st
import time


# =====================================
# EXTRACT FEATURES FROM URL
# =====================================

def extract_features_from_url(url):

    return [

        1 if "https" in url else 0,

        url.count("."),

        1 if ("@" in url or "-") else 0,

        len(url),

        sum(c.isdigit() for c in url),

        url.count("/")
    ]


# =====================================
# CALCULATE RISK SCORE
# =====================================

def calculate_risk_score(data):

    score = 0

    https, dots, special, length, digits, slashes = data


    # no https
    if https == 0:
        score += 25


    # suspicious symbols
    if special == 1:
        score += 20


    # too many digits
    if digits > 5:
        score += 15


    # many subdomains
    if dots > 3:
        score += 20


    # redirect chains
    if slashes > 5:
        score += 20


    # long obfuscated URL
    if length > 80:
        score += 15


    return min(score, 100)


# =====================================
# SEVERITY LEVEL
# =====================================

def severity_level(score):

    if score >= 85:

        return "CRITICAL"

    elif score >= 70:

        return "HIGH"

    elif score >= 40:

        return "MEDIUM"

    else:

        return "LOW"


# =====================================
# DETECT ATTACK TYPE
# =====================================

def detect_attack_type(data):

    https, dots, special, length, digits, slashes = data


    if https == 0 and special == 1:

        return "Phishing Attack"


    elif digits > 7:

        return "Scam URL"


    elif dots > 4:

        return "Subdomain Spoofing"


    elif slashes > 5:

        return "Redirect Attack"


    elif length > 80:

        return "Obfuscated URL"


    elif special == 1:

        return "Suspicious Pattern"


    else:

        return "Likely Safe"


# =====================================
# EXPLAIN RISKS
# =====================================

def explain_risk(data):

    reasons = []

    https, dots, special, length, digits, slashes = data


    if https == 0:

        reasons.append(
            "❌ Website does not use HTTPS encryption"
        )


    if special == 1:

        reasons.append(
            "⚠ Suspicious characters detected"
        )


    if digits > 5:

        reasons.append(
            "⚠ Excessive numbers detected"
        )


    if dots > 3:

        reasons.append(
            "⚠ Too many subdomains detected"
        )


    if slashes > 5:

        reasons.append(
            "⚠ Possible redirect chain detected"
        )


    if length > 80:

        reasons.append(
            "⚠ URL appears intentionally obfuscated"
        )


    if not reasons:

        reasons.append(
            "✅ No major threat indicators found"
        )


    return reasons


# =====================================
# HACKER TERMINAL EFFECT
# =====================================

def hacker_terminal(prediction):

    terminal = st.empty()

    text = ""

    steps = [

        "Initializing cyber scanner...",

        "Connecting to AI threat engine...",

        "Analyzing URL structure...",

        "Running malware intelligence scan...",

        "Detecting phishing indicators...",

        "Generating enterprise threat report..."
    ]


    for step in steps:

        for char in step:

            text += char

            terminal.markdown(

                f"""

                <div class='terminal'>

                {text}

                </div>

                """,

                unsafe_allow_html=True
            )

            time.sleep(0.01)

        text += "<br>"


    result = (

        "🚨 CRITICAL THREAT DETECTED"

        if prediction == "attack"

        else "✅ TARGET APPEARS SAFE"
    )


    terminal.markdown(

        f"""

        <div class='terminal'>

        {text}

        <br><br>

        {result}

        </div>

        """,

        unsafe_allow_html=True
    )