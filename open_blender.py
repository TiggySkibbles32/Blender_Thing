import subprocess

# Path to the Blender executable (for macOS)
blender_path = "/Applications/Blender.app/Contents/MacOS/Blender"  # Adjust if necessary
# Path to your .blend file
blend_file_path = "/Users/nicschl/Japanese Architecture.blend"  # Adjust the path to your file

# Run Blender with the .blend file
try:
    subprocess.Popen([blender_path, blend_file_path])
    print("Blender is opening...")
except Exception as e:
    print(f"Error: {e}")
