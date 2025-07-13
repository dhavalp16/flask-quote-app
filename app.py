from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_quote():
    api_url = "https://zenquotes.io/api/random"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return f"<h2>Quote of the Moment:</h2><p>{data[0]['q']} — <strong>{data[0]['a']}</strong></p>"
    else:
        return "Failed to fetch quote."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
