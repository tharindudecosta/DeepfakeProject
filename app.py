from flask import Flask
from routes.video_analysis import video_analysis_blueprint 
import os
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(video_analysis_blueprint)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
CORS(app)

if __name__ == "__main__":
    app.run(debug=True,port=8000)