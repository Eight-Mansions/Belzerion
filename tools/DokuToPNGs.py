import os
import sys
import dokuwiki
import textwrap
from PIL import Image, ImageDraw, ImageFont
from ConfigUtils import ConfigUtils
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage: <page_id> <output_folder>")
    exit()

page_id = sys.argv[1]
output_folder = sys.argv[2]

names_to_colors = {
    "commander": (0, 152, 232),
    "leon": (255, 255, 255),
    "you": (255, 255, 255),
    "flare-207": (208, 208, 0)
}

# Get the lines for this page
config = ConfigUtils()
wiki = dokuwiki.DokuWiki("https://snowy.coffee/doku", config.get_doku_wiki_username(), config.get_doku_wiki_password())
script_raw = wiki.pages.get(page_id)

# Create the main output folder if it doesn't exist
Path(output_folder).mkdir(parents=True, exist_ok=True)

# Parse the raw library records into a map
# ===== (5) represents a title, ignore this
# ==== (4) represents the parent folder, save this to preserve the disc structure for easy inserting
# === (3) represents the type, either "anim" or "cel" files. ANIMs will be grouped into a folder
for line in script_raw.split("\n"):
    if not line or "^" in line or "=====" in line:
        continue

    # If we have a parent folder header, keep track of it
    if "====" in line:
        parent_folder = line.replace("=", "").strip().replace("/", os.path.sep)
        continue

    # Record if this is a cel or anim file
    if "===" in line:
        is_anim = line.replace("=", "").strip().lower() == "anim"
        continue

    _, file, translation, speaker, *_ = [x.strip() for x in line.split("|")]
    file = file.replace("{", "").replace("}", "").split(":")[-1]

    image_output_path = os.path.join(output_folder, parent_folder)
    if is_anim:
        folder = file.split("_")[0]
        image_output_path = os.path.join(image_output_path, folder)

    # Create the batch output folder if it doesn't exist
    Path(image_output_path).mkdir(parents=True, exist_ok=True)

    speaker = speaker.lower()
    print(f"File: {file}, Translation: {translation}, Speaker: {speaker}")

    # Create an image using this speaker's template
    base_box = Image.open(os.path.join("templates", "template_metal_box.png"))
    template = Image.open(os.path.join("templates", f"template_{speaker}.png"))

    base_box.paste(template, (0, 0), template)

    text_image = ImageDraw.Draw(base_box)
    font = ImageFont.truetype("arial.ttf", 12)

    # Handle any manual breaks, otherwise split automatically
    if "\\n" in translation:
        wrapped_translations = translation.split("\\n")
    else:
        wrapped_translations = textwrap.wrap(translation, width=42)

    for index, wrapped_translation in enumerate(wrapped_translations):
        text_image.text((10, 20 + (13 * index)), wrapped_translation, font=font, fill=names_to_colors[speaker])

    base_box.save(os.path.join(image_output_path, file))
