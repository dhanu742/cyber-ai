# ai_engine.py

import requests


# =========================================
# AI RESPONSE ENGINE
# =========================================

def get_ai_response(user_input):

    prompt = f"""

You are CYBER-X.

You are an advanced AI cybersecurity assistant.

You behave like:

- ethical hacker
- SOC analyst
- penetration tester
- malware analyst
- cybersecurity expert

You answer naturally like ChatGPT.

You understand normal human language.

User message:

{user_input}

Rules:

- answer naturally
- answer clearly
- explain deeply
- explain cybersecurity correctly
- use examples
- sound intelligent
- be conversational
- never ask for feedback
- do not repeat answers

"""


    try:

        response = requests.post(

            "http://localhost:11434/api/generate",

            json={

                "model": "phi",

                "prompt": prompt,

                "stream": False
            },

            timeout=120
        )


        result = response.json()


        return result.get(

            "response",

            "No response generated."
        )


    except Exception as e:

        return f"AI Error: {e}"