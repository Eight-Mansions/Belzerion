import shutil
import subprocess
import os
import sys
import json
from pathlib import Path
from CELArgumentParser import CELArgumentParser

# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 5:
    print("Usage: <input_directory> <output_directory> <raw_cel_directory> <original_directory>")
    exit()

input_directory = Path(sys.argv[1])
output_directory = Path(sys.argv[2])
raw_cel_directory = Path(sys.argv[3])
original_directory = Path(sys.argv[4])

IMAGE_TOOL_EXE = "tools\\3it-x64-windows.exe"
parser = CELArgumentParser(IMAGE_TOOL_EXE)

# Create the output folder if it doesn't exist
output_directory.mkdir(parents=True, exist_ok=True)

# Load the override file if it exists
override = {}
override_file = input_directory / "image_overrides.json"
if override_file.exists():
    with open(override_file) as file:
        override = json.load(file)


def check_override(path):
    for key, value in override.items():
        if key in path:
            return value
    return {}


png_folders = set()

# Find all folders that contain PNGs
for png_path in input_directory.rglob("*.png"):
    png_folders.add(png_path.parent)

for png_folder in png_folders:
    output_folder = os.path.relpath(png_folder, input_directory)
    Path(os.path.join(output_directory, output_folder)).mkdir(parents=True, exist_ok=True)

    for png in png_folder.glob("*.png"):
        # Check if this is a raw cel on the disc
        cel_path = Path(os.path.join(original_directory, output_folder, png.name.replace(".png", "")))

        if not cel_path.exists():
            # If it does not exist, then it's an extracted anim file. Use the raw cel directory instead
            cel_path = Path(os.path.join(raw_cel_directory, output_folder, png.name.replace(".png", ".cel")))

        if not cel_path.exists():
            # If it does not exist, then it's an extracted anim file. Use the raw cel directory instead
            cel_path = Path(os.path.join(raw_cel_directory, output_folder, png.name.replace(".png", "")))

        # arguments = parser.parse_cel(cel_path)

        # Load any image creation overrides here
        relative_path = os.path.join(output_folder, png.name)
        image_override = check_override(relative_path)

        bpp = 16
        if "bpp" in image_override:
            bpp = image_override["bpp"]

        command_builder = [f'{IMAGE_TOOL_EXE} to-cel --output-path',
                           f'"{os.path.join(output_directory, output_folder, png.name.replace(".png", ""))}"',
                           f'--bpp {bpp}',
                           f'--transparent 0xFFFFFF00',
                           f'--packed true']

        if "commands" in image_override:
            command_builder.extend(image_override["commands"])

        command_builder.append(f'"{png}"')

        command = " ".join(command_builder)
        process_info = subprocess.run(command, stdout=subprocess.PIPE)

        print(f"{process_info.stdout.decode('utf-8')}")
