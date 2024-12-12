# Face Expression Detection💁

## ✋ Introduction
 이 프로젝트는 가천대학교 오픈소스 64조가 진행한 팀 프로젝트입니다.
 얼굴 사진을 이미지 혹은 사진 촬영으로 입력받고, 표정 상태를 예측합니다.
 
## 📚 Packages
### Install libraries
  - ***OpenCV : Version 4.10***
  - ***Numpy : Version 1.26.4***
  - ***Keras : Version  3.7***

 ```sh
 pip install opencv-python numpy keras flask transformers  torch torchvision torchaudio
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
데모 영상/사진 추가

## 👀 Reference
https://blog.naver.com/tmvmffpsej/223104743267

## 👨 Team members
  - 202033624 한민섭 [minsobhan22@gachon.ac.kr] : Back-end, Integrate
  - 202034331 이시웅 [jasper01675@gachon.ac.kr] : Front-end
  - 202035384 전지우 [bisha0821@gachon.ac.kr] : Modeling
  - 202133333 한원근 [sample1234@gachon.ac.kr]: Modeling
### **More information, Contact us!!**
