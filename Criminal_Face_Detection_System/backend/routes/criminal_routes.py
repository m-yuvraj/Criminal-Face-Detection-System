from flask import Blueprint, request, jsonify
import os
from database import save_criminal, get_criminal_details

bp = Blueprint('criminal', __name__)

@bp.route('/register_criminal', methods=['POST'])
def register_criminal():
    data = request.form
    image = request.files['image']
    save_path = os.path.join('images', image.filename)
    image.save(save_path)
    save_criminal(data, save_path)
    return jsonify({"message": "Criminal registered successfully."})

@bp.route('/get_criminal_details/<string:criminal_id>', methods=['GET'])
def get_details(criminal_id):
    details = get_criminal_details(criminal_id)
    return jsonify(details)
