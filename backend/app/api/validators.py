from functools import wraps
from flask import request, jsonify

def validate_input():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            data = request.get_json()
            if not data or 'alt_text' not in data:
                return jsonify({"error": "Invalid input format"}), 400
            return f(*args, **kwargs)
        return decorated_function
    return decorator