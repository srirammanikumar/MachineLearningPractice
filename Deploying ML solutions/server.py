import numpy as np
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load(open('models/rfr_model_checkpoint.joblib', 'rb'))
loaded_model = model['model']


@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = loaded_model.predict(data["x"])
    output_text = "Text: " + str(data["x"])
    output = "Price: " + str(prediction)
    return jsonify(output_text, output)


if __name__ == 'main':
    app.run(port=8080, debug=True)
