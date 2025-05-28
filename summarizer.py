def summarize_with_ollama(text):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": f"Summarize the following article:\n\n{text}"
        }
    )
    return res.json()["response"]

