import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model you saved from the Jupyter notebook
with open('trained_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['GET'])
def predict():
    data = request.get_json()
    
    # Extract features from the JSON data
    features = [data['airline'], data['source_city'], data['departure_time'], data['stops'], 
                data['arrival_time'], data['destination_city'], data['class'], 
                data['duration'], data['days_left']] 
    
    # Predict using the loaded model
    prediction = model.predict([features])
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
