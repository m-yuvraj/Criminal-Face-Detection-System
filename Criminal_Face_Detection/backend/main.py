import cv2
from PIL import Image
import numpy as np

# Load pre-trained Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def detect_from_image(file):
    # Load image from file and convert it to a numpy array
    image = Image.open(file)
    image_np = np.array(image)

    # Convert the image to grayscale for detection
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # Face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    face_count = len(faces)

    # Initialize counts and lists for results
    eye_count = 0
    suspicious_count = 0  # Define your criteria for this
    gender_list = []  # Placeholder for gender predictions

    # For each detected face, run eye detection and potentially other analyses
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]

        # Eye detection within the face region
        eyes = eye_cascade.detectMultiScale(face_roi)
        eye_count += len(eyes)

        # Placeholder gender detection - append "Male" or "Female" based on some logic or a model
        # For actual implementation, replace this with a call to a pre-trained gender detection model
        gender_list.append("Male" if np.random.rand() > 0.5 else "Female")

        # Suspicious behavior placeholder - increment based on specific logic
        # Define specific criteria for suspicious count if needed
        suspicious_count += 1 if len(eyes) < 2 else 0

    return {
        "faces": face_count,
        "eyes": eye_count,
        "suspicious": suspicious_count,
        "genders": gender_list,
    }
