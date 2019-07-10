import json
import pickle
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)


with open('columns.json') as fh:
    columns = json.load(fh)

with open('model.pickle', 'rb') as fh:
    model = pickle.load(fh)

with open('dtypes.pickle', 'rb') as fh:
    dtypes = pickle.load(fh)


@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json()
    obs = pd.DataFrame([text], columns=columns).astype(dtypes)
    proba = model.predict(obs)
    return jsonify({
        'category': proba[0]
    })


if __name__ == "__main__":
    app.run(debug=True)