import shutil
import subprocess
import os
import sys
from pathlib import Path

# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 3:
    print("Usage: <input_directory> <output_directory>")
    exit()

input_directory = sys.argv[1]
output_directory = sys.argv[2]

IMAGE_TOOL_EXE = "tools\\3it_win64.exe"

# Create the output folder if it doesn't exist
Path(output_directory).mkdir(parents=True, exist_ok=True)

for path in Path(input_directory).glob("*.png"):
    if not path.is_file():
        continue

    command = f'{IMAGE_TOOL_EXE} to-cel --output-path ' \
              f'"{os.path.join(output_directory, path.name.replace(".png", ".cel"))}" ' \
              f'--transparent 0xFFFFFF00 ' \
              f'--packed true ' \
              f'"{path}"'

    subprocess.run(command, stdout=subprocess.PIPE)
