from flask import Blueprint, request, jsonify
import cv2
import numpy as np
from ml_utils import match_face

bp = Blueprint('detection', __name__)

@bp.route('/detect_photo', methods=['POST'])
def detect_photo():
    image = request.files['image']
    image_np = np.fromstring(image.read(), np.uint8)
    img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    results = []
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        match = match_face(face_roi)
        results.append(match)

    return jsonify({'detected_faces': results})
