from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/signal', methods=['POST'])
def relay_signal():
    try:
        data = request.json
        print("📥 دریافت سیگنال:", data)

        # ارسال به سرور واقعی مصطفی (لوکال یا ngrok)
        forward_url = "http://YOUR_SERVER_ADDRESS/signal"
        response = requests.post(forward_url, json=data, timeout=5)
        return jsonify({"status": "relayed", "from": "Render", "result": response.json()})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/')
def index():
    return '✅ Signal API Relay is Live'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
