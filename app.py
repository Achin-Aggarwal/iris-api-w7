from flask import Flask, request, jsonify
import time, random

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST", "GET"])
def predict():
    # Simulate inference time
    work = random.uniform(0.02, 0.2)
    time.sleep(work)
    sample = request.json if request.is_json else {"sample": "none"}
    return jsonify({
        "input": sample,
        "prediction": random.choice(["setosa", "versicolor", "virginica"]),
        "inference_time_s": round(work, 3)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
