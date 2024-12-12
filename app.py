from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

# Import the predict_emotion function from emotion_analysis.py
from emotion_analysis import predict_emotion  # Assuming it's in the same directory

app = Flask(__name__)

# Flask settings
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # Max file size: 10MB

# Home page endpoint
@app.route('/')
def home():
    return render_template('index.html')  # Render template

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded. Please upload an image file.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected. Please upload an image file.'}), 400

    try:
        # Use the predict_emotion function from emotion_analysis
        emotion, confidence = predict_emotion(file)
        return jsonify({'emotion': emotion, 'confidence': confidence})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

# Favicon.ico handler
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
