from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1406646932650070178/bOuPa3OB0hB_x_uxvONLLCO7LHTd6e57Q1kr6sqtYesa8SyBZWeFOcWPePc8gciJY0qt"

@app.route("/roblox-message", methods=["POST"])
def roblox_message():
    data = request.json
    if not data or "message" not in data:
        return {"error": "No message provided"}, 400

    content = data["message"]
    # Send to Discord
    response = requests.post(DISCORD_WEBHOOK_URL, json={"content": content})

    if response.status_code == 204:
        return {"status": "Message sent to Discord!"}, 200
    else:
        return {"error": "Failed to send message"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
