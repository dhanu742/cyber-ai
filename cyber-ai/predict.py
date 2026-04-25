import numpy as np


# =========================
# SMART RULE ENGINE
# =========================

def predict_attack(data):

    https, dots, special, length, digits, slashes = data

    risk = 0


    # no https
    if https == 0:
        risk += 25


    # suspicious symbols
    if special == 1:
        risk += 20


    # many numbers
    if digits > 5:
        risk += 15


    # too many subdomains
    if dots > 3:
        risk += 20


    # too many redirects
    if slashes > 5:
        risk += 20


    # long obfuscated URL
    if length > 80:
        risk += 15


    # =====================
    # FINAL DECISION
    # =====================

    if risk >= 50:

        return "attack"

    else:

        return "safe"