def explain_attack(data, prediction):
    if prediction == "attack":
        return """
⚠️ The system detected unusual behavior:
- Pattern similar to known attacks
- Possible suspicious network activity

Recommendation:
- Monitor traffic
- Check system security
"""
    else:
        return """
✅ Network activity appears normal:
- No unusual patterns detected

Recommendation:
- Continue monitoring
"""