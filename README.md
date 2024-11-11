# Criminal Face Detection System

A web-based criminal face detection system that uses a live webcam feed or uploaded photos to detect faces, identify gender, and flag suspicious individuals. This project consists of a **React.js frontend** and a **Flask backend** and is deployed on Vercel (frontend) and Render (backend) for free live hosting.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Demo](#demo)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Running the Project Locally](#running-the-project-locally)
- [Deploying the Project](#deploying-the-project)
- [License](#license)

---

## Project Overview

The Criminal Face Detection System allows law enforcement agencies to detect criminal faces, predict gender, and flag suspicious activity using facial recognition. The project utilizes **OpenCV** for face and eye detection, a **pre-trained gender detection model**, and a simulated suspicious activity detection system.

## Features

- **Live Webcam Detection**: Capture real-time images through a webcam.
- **Photo Upload Detection**: Upload photos for analysis.
- **Face, Eye, and Gender Detection**: Uses pre-trained models for accurate results.
- **Suspicion Flagging**: Simulated detection of suspicious activity based on facial encodings.

## Demo

- **Frontend**: [Live on Vercel](https://yourapp.vercel.app)
- **Backend**: [Live on Render](https://yourapp.onrender.com)

## File Structure

```plaintext
criminal-face-detection/
├── backend/
│   ├── app.py
│   ├── models/
│   │   ├── haarcascade_frontalface_default.xml
│   │   ├── haarcascade_eye.xml
│   │   ├── gender_deploy.prototxt
│   │   └── gender_net.caffemodel
│   ├── requirements.txt
│   └── static/
│       └── suspicious_model.h5  # Optional
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── components/
│   └── package.json
├── README.md
