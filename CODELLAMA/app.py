import requests
import json
import gradio as gr

url = "https://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}
history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "/n".join(history)

    data = {
        "model":"codeguru",
        "prompt":final_prompt,
        "stream":False

    }
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    