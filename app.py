from flask import Flask, jsonify
import subprocess
import os
import sys

app = Flask(__name__)

@app.route('/run-python-script')
def run_script():
    try:
        # Path to the .blend file
        file_path = '/Users/nicschl/Japanese Architecture.blend'

        # Ensure the file exists
        if not os.path.exists(file_path):
            return "Error: The file does not exist.", 400

        # Path to the Blender executable (assuming it's in your PATH)
        blender_executable = "blender"

        # Launch Blender with the specific file
        subprocess.run([blender_executable, file_path], check=True)
        return "Blender is now open with your file.", 200
    except subprocess.CalledProcessError as e:
        return f"Error opening Blender: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
