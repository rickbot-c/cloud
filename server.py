from flask import Flask, request
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1406646932650070178/bOuPa3OB0hB_x_uxvONLLCO7LHTd6e57Q1kr6sqtYesa8SyBZWeFOcWPePc8gciJY0qt"

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    # Discord expects {"content": "message here"}
    payload = {"content": data.get("message", "")}
    response = requests.post(DISCORD_WEBHOOK, json=payload)
    if response.status_code == 204:
        return {"status": "ok"}
    else:
        return {"status": "error", "details": response.text}, 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
