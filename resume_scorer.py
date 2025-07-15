
import requests
import json


API_KEY = "*****"
MODEL = "gemini-2.0-flash"

def suggest_improvements(resume_text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Suggest improvements for this resume:\n\n{resume_text}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"❌ API Error or invalid response:\n\n{json.dumps(result, indent=2)}"


