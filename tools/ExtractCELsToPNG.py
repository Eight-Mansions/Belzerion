import shutil
import subprocess
import os
import sys
from pathlib import Path

# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 3:
    print("Usage: <game_files> <output_directory>")
    exit()

game_files = sys.argv[1]
output_directory = sys.argv[2]

IMAGE_TOOL_EXE = "C:\\Users\\yagen\\OneDrive\\Games\\Translations\\Inactive\\Belzerion\\tools\\3it_win64.exe"

print("Scanning for potential CEL files...")
#for path in Path(game_files).rglob("*"):
#    if not path.is_file():
#        continue

#    path = str(path)

    # Be careful not to pick up pngs and export them as pngs
#    if path.lower().endswith(".png"):
#        continue

#    command = f'{IMAGE_TOOL_EXE} to-png "{path}"'
#    print(command)
#    subprocess.run(command, stdout=subprocess.PIPE)

print("Copying PNGs over...")
for path in Path(game_files).rglob("*.png"):
    # Create a relative path to preserve the disc structure of the game
    output_path = os.path.join(output_directory, os.path.relpath(path, game_files))
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    shutil.move(path, output_path)
