from pathlib import Path
import os
import sys


# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 3:
    print("Usage: <input_folder> <doki_namespace>")
    exit()

input_folder = Path(sys.argv[1])
doki_namespace = sys.argv[2]

image_map = {}


def read_directory(directory, doki_namespace):
    """
    Scans the given directory recursively and parses any files within
    :param directory: Current directory to scan
    """
    for path in directory.rglob("*.png"):
        if path.is_file():
            add_image(path, doki_namespace)


def add_image(image_path, doki_namespace):
    relative_path = str(image_path.parent.relative_to(input_folder))
    if relative_path not in image_map:
        image_map[relative_path] = []

    image_name_lower = str(image_path.name).lower()

    image_code = "|{{ " + doki_namespace + image_name_lower.replace(" ", "_") \
                 + "|}}|" + " | | |"

    image_map[relative_path].append(image_code)


def output_map():
    result = ""
    for folder in image_map:
        result += "==== " + folder + " ====\n"
        #result += "^Images^Filename^Translation^Notes^\n"
        result += "^Image^Translation^Speaker^Notes^\n"
        result += "\n".join(image_map[folder]) + "\n"
        result += "\n"
    print(result)


read_directory(input_folder, doki_namespace)
output_map()
