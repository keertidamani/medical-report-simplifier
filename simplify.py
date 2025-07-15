import requests

def simplify_medical_text(text):
    prompt = f"""
You are a friendly medical assistant. Simplify this medical report into short, clear bullet points for each input so that a non-medical person can easily understand.

For each abnormal value:
- Clearly name the test and whether it’s high or low.
- Briefly explain what that result might mean in simple, reassuring language.
- Mention common causes (like low iron, dehydration, etc.) only if relevant.
- Keep the tone calm and helpful. Do not repeat exact numeric values.

At the end, add a single friendly sentence encouraging the user to consult their doctor for clarity and next steps.

Medical Report:
\"\"\"{text}\"\"\"

Output:
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]