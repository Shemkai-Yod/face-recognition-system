# 👤 Face Recognition System — Computer Vision Pipeline

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green?logo=opencv)
![Deep Learning](https://img.shields.io/badge/Deep_Learning-Face_Embeddings-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A complete face recognition system built with OpenCV and deep learning face embeddings. Detects and analyses faces in uploaded images, compares faces across images for similarity, and includes a real-time webcam detection script for local deployment.

---

## ✨ Features

- 🔍 **Face Detection** — detect all faces in any uploaded image with bounding boxes and labels
- 🧠 **Deep Learning Embeddings** — uses 128-dimension face encodings for accurate recognition
- 👥 **Multi-Face Analysis** — crops and analyses each face individually with size and position data
- 🔄 **Face Comparison** — compares faces across two images with similarity score and distance metric
- 📷 **Real-Time Webcam Detection** — live face detection script optimised for smooth performance
- 📊 **Professional Visualisations** — annotated output images saved automatically

---

## 🔍 Project Pipeline

1. **Image Loading** — supports JPG, JPEG, PNG formats
2. **Face Detection** — HOG-based face location using face_recognition
3. **Face Encoding** — 128-dimension deep learning embeddings per face
4. **Annotation** — bounding boxes, labels, and colour-coded face markers
5. **Individual Analysis** — padded face crops with pixel dimensions
6. **Similarity Comparison** — Euclidean distance between face encodings with match/no-match verdict
7. **Webcam Deployment** — optimised real-time detection processing every 3rd frame for performance

---

## 📁 Repository Structure
face-recognition-system/
├── face_recognition_system.ipynb  # Main Colab notebook
├── webcam_detection.py            # Local real-time webcam script
├── annotated_output.png           # Sample detection output
├── face_crops.png                 # Individual face crop analysis
└── face_comparison.png            # Face similarity comparison result
---

## 🚀 How to Run

### On Google Colab (Recommended)
1. Open `face_recognition_system.ipynb` in Google Colab
2. Run the first cell to install dependencies:
```bash
!pip install face-recognition
Run all cells — upload any image when prompted
View annotated results directly in the notebook
Locally
pip install opencv-python face-recognition pillow matplotlib numpy
python webcam_detection.py
🧠 How It Works
Face recognition uses deep learning under the hood:
A pre-trained CNN detects facial landmarks (eyes, nose, mouth, jawline)
The model generates a 128-dimension face embedding — a unique numerical fingerprint for each face
Embeddings are compared using Euclidean distance — faces with distance < 0.6 are considered a match
This approach achieves 99.38% accuracy on the Labeled Faces in the Wild benchmark dataset
📈 Key Visualisations
Face Detection with Bounding Boxes
�
Load image
Individual Face Crops
�
Load image
Face Similarity Comparison
�
Load image
🛠️ Skills Demonstrated
Python OpenCV Computer Vision Deep Learning Face Recognition CNN Embeddings NumPy Matplotlib Pillow Real-Time Processing Google Colab
📦 Dependencies
Library
Purpose
face-recognition
Deep learning face detection & encoding
OpenCV
Image processing & webcam capture
NumPy
Array operations & image manipulation
Pillow
Image loading & format handling
Matplotlib
Visualisation & annotated output
