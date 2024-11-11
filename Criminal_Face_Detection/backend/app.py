from flask import Flask, request, jsonify
from main import detect_from_image  # Import function from main.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for communication with frontend

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]

    # Run detection from main.py
    result = detect_from_image(file)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
    