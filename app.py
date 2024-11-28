from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Flask 설정
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 파일 크기 제한: 2MB

# 모델 로드
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'emotion_model.keras')

try:
    model = load_model(MODEL_PATH)
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
    print("Model loaded successfully.")
except Exception as e:
    raise RuntimeError(f"Failed to load model. Check the file path: {MODEL_PATH}. Error: {str(e)}")

# 이미지 전처리 함수
def preprocess_image(file):
    try:
        img = Image.open(file).convert('RGB').resize((48, 48))  # 이미지 변환 및 크기 조정
        img_array = np.array(img) / 255.0  # 정규화
        img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가
        return img_array
    except Exception as e:
        raise ValueError(f"Error during image preprocessing: {str(e)}")

# 홈 페이지 엔드포인트
@app.route('/')
def home():
    return render_template('index.html')  # 템플릿 렌더링

# 예측 엔드포인트
@app.route('/predict', methods=['POST'])
def predict():
    # 파일 유효성 검사
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded. Please upload an image file.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected. Please upload an image file.'}), 400

    try:
        # 이미지 전처리 및 예측
        img_array = preprocess_image(file)
        predictions = model.predict(img_array)
        emotion = emotions[np.argmax(predictions)]  # 가장 높은 확률의 감정 추출
        return jsonify({'emotion': emotion, 'confidence': float(np.max(predictions))})
    except ValueError:
        return jsonify({'error': 'Invalid image format. Please upload a valid image.'}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

# favicon.ico 처리 (브라우저 요청 방지)
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
