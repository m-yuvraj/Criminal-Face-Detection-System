# Criminal Face Detection System

This project enables the detection of criminal faces in images using face recognition and facial detection models.

## Features
- **Criminal Detection**: Detects and identifies known criminals by comparing faces in images.
- **Data Handling**: Annotation, augmentation, deduplication, and encryption.
- **Secure Storage**: Encrypts images for secure storage.

## Setup

### Requirements
- Install required libraries with `pip install -r requirements.txt`
- Download Haar cascade files for face detection:
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_eye.xml`

Place these in the project directory.

### Running the Server
1. Run `python app.py` to start the Flask server.
2. Use endpoints:
   - `/detect` to detect and identify criminals.
   - `/upload_criminal` to add criminal images.

### Database Configuration
1. Connect to your MySQL database.
2. Run the table creation SQL from the main script.

## How to Annotate Data
- Use LabelImg for annotating images.
- Save annotations in XML format.

## Encryption for Secure Storage
- Encryption key stored as `encryption_key.key`.
- Run the encryption script to secure images.

## Criminal Detection Process
1. **Face Detection**: Detects faces in uploaded images.
2. **Recognition**: Compares detected faces with known criminal images.
3. **Alert**: Identifies and sends a notification if a match is found.

---

## Contributors
- **Gauri Mahadik**
- **Yuvraj Mandlik**
- **Kaustubh Begede**
- **Murari Mishra**

## License
MIT License
