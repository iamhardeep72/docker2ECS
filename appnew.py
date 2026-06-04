from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load your trained model
model = pickle.load(open("best_rf_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get all values from form
        features = [
            float(request.form["LIMIT_BAL"]),
            float(request.form["AGE"]),
            float(request.form["PAY_1"]),
            float(request.form["PAY_2"]),
            float(request.form["PAY_3"]),
            float(request.form["PAY_4"]),
            float(request.form["PAY_5"]),
            float(request.form["PAY_6"]),
            float(request.form["BILL_AMT1"]),
            float(request.form["BILL_AMT2"]),
            float(request.form["BILL_AMT3"]),
            float(request.form["BILL_AMT4"]),
            float(request.form["BILL_AMT5"]),
            float(request.form["BILL_AMT6"]),
            float(request.form["PAY_AMT1"]),
            float(request.form["PAY_AMT2"]),
            float(request.form["PAY_AMT3"]),
            float(request.form["PAY_AMT4"]),
            float(request.form["PAY_AMT5"]),
            float(request.form["PAY_AMT6"])
        ]

        # Convert to numpy array
        final_features = np.array([features])

        # Prediction
        prediction = model.predict(final_features)[0]

        # probability
        prob = model.predict_proba(final_features)[0][1]

        return jsonify({"prediction": int(prediction), "prob": float(prob)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
    
if __name__ == "__main__":
    app.run()