import os
from PIL import Image
import face_recognition

CRIMINAL_IMAGES_PATH = "criminal_images/"

def upload_criminal_image(file):
    image = Image.open(file)
    image_np = np.array(image)

    face_encodings = face_recognition.face_encodings(image_np)
    if not face_encodings:
        return {"error": "No face detected"}

    filename = file.filename
    file.save(os.path.join(CRIMINAL_IMAGES_PATH, filename))
    return {"status": "Criminal image uploaded successfully", "filename": filename}
