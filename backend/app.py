from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess
from flask_cors import CORS
from flask import send_from_directory

app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["CONVERTED_FOLDER"] = "converted"

# Ensure directories exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["CONVERTED_FOLDER"], exist_ok=True)


@app.route("/")
def home():
    return jsonify({"message": "Flask server is running!"})


@app.route("/upload", methods=["POST"])
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filename = file.filename
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    
    print(f"📁 Saving file to: {file_path}")  # ✅ Debug log

    try:
        file.save(file_path)
        print(f"✅ File saved successfully: {file_path}")  # ✅ Success log
    except Exception as e:
        print(f"❌ Error saving file: {e}")  # ❌ Error log
        return jsonify({"error": "File upload failed"}), 500

    file_url = f"http://127.0.0.1:5001/uploads/{filename}"
    return jsonify({"message": "File uploaded successfully", "file_url": file_url})



from flask import send_from_directory

@app.route("/uploads/<path:filename>")
def serve_uploaded_file(filename):
    directory = os.path.abspath(app.config["UPLOAD_FOLDER"])  # Absolute path fix
    print(f"📤 Serving file from: {directory}/{filename}")  # ✅ Debug log
    return send_from_directory(directory, filename)


@app.route("/convert", methods=["POST"])
def convert_model():
    data = request.json
    input_url = data.get("input_path")  # Get the file URL from frontend

    if not input_url:
        return jsonify({"error": "No input file provided"}), 400

    filename = os.path.basename(input_url)
    input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    if not os.path.exists(input_path):
        return jsonify({"error": f"Input file does not exist: {input_path}"}), 400

    output_filename = os.path.splitext(filename)[0] + ".obj"
    output_path = os.path.join(app.config["CONVERTED_FOLDER"], output_filename)

    try:
        print(f"🔄 Converting: {input_path} → {output_path}")

        # ✅ Run the subprocess with detailed logging
        command = f"assimp export \"{input_path}\" \"{output_path}\""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        print(f"🔹 Command Output: {result.stdout}")
        print(f"🔹 Command Error: {result.stderr}")

        if result.returncode != 0:
            return jsonify({"error": f"Conversion failed: {result.stderr}"}), 500

        output_url = f"http://127.0.0.1:5001/converted/{output_filename}"
        return jsonify({"message": "Conversion successful!", "output_path": output_url})
    except Exception as e:
        print(f"🔹 Exception: {str(e)}")  # Debug log
        return jsonify({"error": str(e)}), 500



@app.route("/converted/<filename>")
def serve_converted_file(filename):
    return send_from_directory(app.config["CONVERTED_FOLDER"], filename)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
