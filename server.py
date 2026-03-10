from flask import Flask, request, jsonify

app = Flask(__name__)

alerts = []

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    alerts.append(data)
    print("ALERT:", data)
    return jsonify({"status":"ok"})

@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

app.run(host="0.0.0.0", port=5000)
