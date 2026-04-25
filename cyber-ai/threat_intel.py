import requests


def check_url_reputation(url):

    suspicious_keywords = [
        "login",
        "verify",
        "secure-update",
        "banking",
        "free-money"
    ]

    score = 0

    for keyword in suspicious_keywords:

        if keyword in url.lower():
            score += 20

    if "@" in url:
        score += 30

    if len(url) > 80:
        score += 20

    return {
        "risk": min(score, 100),
        "status": "malicious" if score >= 50 else "safe"
    }