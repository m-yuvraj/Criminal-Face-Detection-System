import cv2
import face_recognition
import numpy as np
from PIL import Image
import os

CRIMINAL_IMAGES_PATH = "criminal_images/"
KNOWN_ENCODINGS = []
KNOWN_NAMES = []

def load_criminal_encodings():
    global KNOWN_ENCODINGS, KNOWN_NAMES
    for filename in os.listdir(CRIMINAL_IMAGES_PATH):
        image = face_recognition.load_image_file(os.path.join(CRIMINAL_IMAGES_PATH, filename))
        encoding = face_recognition.face_encodings(image)[0]
        KNOWN_ENCODINGS.append(encoding)
        KNOWN_NAMES.append(os.path.splitext(filename)[0])

load_criminal_encodings()

def detect_from_image(file):
    image = Image.open(file)
    image_np = np.array(image)
    rgb_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb_image)
    encodings = face_recognition.face_encodings(rgb_image, faces)
    
    results = {"faces": len(faces), "matches": []}
    
    for encoding in encodings:
        matches = face_recognition.compare_faces(KNOWN_ENCODINGS, encoding)
        name = "Unknown"
        if True in matches:
            match_index = matches.index(True)
            name = KNOWN_NAMES[match_index]
        results["matches"].append(name)
    
    return results
