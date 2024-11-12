from flask import Flask, request, jsonify
from flask_cors import CORS
from detect_module import detect_from_image
from upload_module import upload_criminal_image

app = Flask(__name__)
CORS(app)

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    result = detect_from_image(file)
    return jsonify(result)

@app.route("/upload_criminal", methods=["POST"])
def upload_criminal():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    result = upload_criminal_image(file)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
