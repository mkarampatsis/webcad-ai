from flask import Flask, jsonify, make_response

from flask_cors import CORS

# from flask_swagger_ui import get_swaggerui_blueprint
# from mongoengine import connect
from datetime import timedelta

from src.blueprints.ai import ai

app = Flask(__name__)


@app.errorhandler(413)
def too_large(e):
    return make_response(jsonify(message="File is too large"), 413)


# CORS configuration
cors = CORS(
    app,
    resources={
        r"*": {
            "origins": [
                "http://localhost:4200"
            ]
        }
    },
)

# Register blueprints
app.register_blueprint(ai, url_prefix="/ai")
