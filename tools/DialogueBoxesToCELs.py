import shutil
import subprocess
import os
import sys
from pathlib import Path

# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 3:
    print("Usage: <input_directory> <output_directory>")
    exit()

input_directory = Path(sys.argv[1])
output_directory = Path(sys.argv[2])

IMAGE_TOOL_EXE = "tools\\3it_win64.exe"

# Create the output folder if it doesn't exist
output_directory.mkdir(parents=True, exist_ok=True)

png_folders = set()

# Find all folders that contain PNGs
for png_path in input_directory.rglob("*.png"):
    png_folders.add(png_path.parent)

for png_folder in png_folders:
    output_folder = os.path.relpath(png_folder, input_directory)
    Path(os.path.join(output_directory, output_folder)).mkdir(parents=True, exist_ok=True)
    for png in png_folder.glob("*.png"):
        command = f'{IMAGE_TOOL_EXE} to-cel --output-path ' \
                  f'"{os.path.join(output_directory, output_folder, png.name.replace(".png", ".cel"))}" ' \
                  f'--transparent 0xFFFFFF00 ' \
                  f'--packed true ' \
                  f'"{png}"'

        subprocess.run(command, stdout=subprocess.PIPE)
