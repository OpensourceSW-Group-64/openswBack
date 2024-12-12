# Face Expression Detection💁

## ✋ Introduction
 이 프로젝트는 가천대학교 오픈소스 64조가 진행한 팀 프로젝트입니다.
 얼굴 사진을 이미지 혹은 사진 촬영으로 입력받고, 표정 상태를 예측합니다.<br><br>
### Front&Back
 Users can upload an image to the page, which then sends the image to the backend server for emotion recognition. The server returns the predicted emotion and confidence score, which are displayed directly on the page.
### Model 
 Emotion Analysis Dashboard is a real-time emotion recognition system that combines facial emotion analysis using a dataset and convolutional neural network (CNN) and text sentiment analysis powered by a Hugging Face's Transformers library. The application is built with Streamlit for easy deployment and interactivity.
### Model2
  By utilizing a pre-trained neural network and facial detection algorithms, it achieves accurate emotion recognition and classification.


## Key Features

- **Emotion Prediction**: Automatically sends the uploaded image to the `/predict` endpoint for analysis.
- **Text Sentiment Analysis**: Type text in the provided input field to analyze the sentiment (e.g., Positive, Negative, Neutral).
- **Facial Emotion Recognition**: Turn on your webcam to recognize facial emotions in real time (e.g., Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise).
 
## 📚 Packages
### Install libraries
| Package      | Version | Description                              |
|--------------|---------|------------------------------------------|
| TensorFlow   | 2.6+    | For training and testing the facial recognition model |
| Streamlit    | 1.1+    | For building the web app interface       |
| OpenCV       | 4.5+    | For reading and loading the FER2013 dataset |
| Transformers | 4.11+   | For sentiment analysis using Hugging Face |
| Keras        | 3.7+   | For sentiment analysis prediction         |
 ```sh
 pip install opencv-python numpy keras flask transformers  torch torchvision torchaudio tensorflow streamlit
 ```
 ***⚠️ Maybe you should upgrade/downgrade your installed packages for compatibility ***
### Download files
  - [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) : Used for face recognization, OpenCV file
  - [emotion_model.hdf5](https://github.com/petercunha/Emotion/blob/master/models/emotion_model.hdf5) : Used for distinct face expression

 *****You need to download raw files.***
## How to Execute
1. Activate conda virtual environment
  ```sh
 python -m venv ex // 가상환경 활성화
ex\Scripts\activate
 ```
2. Execute python app file
  ```sh
 python app.py 
ex\Scripts\activate
 ```
3. Open a web browser and access a localhost address
```sh
http://localhost:5000/ or http://127.0.0.1:5000
 ```
## 📋 System Architecture
![System architectur](https://github.com/user-attachments/assets/db5e24f1-5caf-4944-b32b-abbb67025e40)
## 📹 Demo

사진 업로드를 이용한 표정 예측<br>
![image](https://github.com/user-attachments/assets/9a463035-81aa-43fd-8975-f58c4edcce61)
![image](https://github.com/user-attachments/assets/068788f2-9213-44bd-888f-122b485e03a5)


## 👀 References
Below are the materials and resources used in developing this project:
- **Dataset**: [FER2013 Facial Emotion Recognition Dataset](#)
- **Tutorials and Resources**:
  - Streamlit Documentation
  - Hugging Face Tutorials
  - TensorFlow Tutorials
- **Libraries**:
  - OpenCV
  - TensorFlow
  - Keras
- **Blogs and Code Snippets**:
  - Blog article on facial emotion recognition using TensorFlow
  - Tips for integrating OpenCV with Streamlit
  - [Implementing emotion analysis model](https://blog.naver.com/tmvmffpsej/223104743267)
## 👨 Team members
  - 202033624 한민섭 [minsobhan22@gachon.ac.kr] : Back-end, Integrate
  - 202034331 이시웅 [jasper01675@gachon.ac.kr] : Front-end
  - 202035384 전지우 [bisha0821@gachon.ac.kr] : Modeling
  - 202131791 한원근 [cjcj12074@gachon.ac.kr]: Modeling
### **More information, Contact us!!**

