import os
import sys
import dokuwiki
import textwrap
from PIL import Image, ImageDraw, ImageFont
from ConfigUtils import ConfigUtils
from pathlib import Path

if len(sys.argv) < 4:
    print("Usage: <page_id> <output_cel_folder> <output_anim_folder>")
    exit()

page_id = sys.argv[1]
output_cel_folder = sys.argv[2]
output_anim_folder = sys.argv[3]

names_to_colors = {
    "achilles": (160, 160, 176),
    "commander": (0, 152, 232),
    "dr. hisano": (128, 224, 24),
    "flare-112": (184, 240, 248),
    "flare-207": (208, 208, 0),
    "flare-386": (184, 240, 248),
    "gigant": (184, 240, 248),
    "hangman": (232, 0, 0),
    "leon": (255, 255, 255),
    "none": (184, 240, 248),
    "nurse": (184, 240, 248),
    "office robo": (184, 240, 248),
    "owner": (184, 240, 248),
    "police": (184, 240, 248),
    "question-blue": (0, 152, 232),
    "question-red": (232, 0, 0),
    "reporter": (184, 240, 248),
    "rina": (184, 240, 248),
    "rina-red": (232, 0, 0),
    "saeko": (255, 192, 216),
    "sp-robo": (184, 240, 248),
    "you": (255, 255, 255),
}

# Get the lines for this page
config = ConfigUtils()
wiki = dokuwiki.DokuWiki(config.get_doku_wiki_url(), config.get_doku_wiki_username(), config.get_doku_wiki_password())
script_raw = wiki.pages.get(page_id)

# Create the main output folder if it doesn't exist
Path(output_cel_folder).mkdir(parents=True, exist_ok=True)
Path(output_anim_folder).mkdir(parents=True, exist_ok=True)

# Default to CEL mode if not found
is_anim = False

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
        is_anim = "anim" in line.lower()
        continue

    _, file, translation, speaker, *_ = [x.strip() for x in line.split("|")]
    file = file.replace("{", "").replace("}", "").split(":")[-1]

    if is_anim:
        image_output_path = os.path.join(output_anim_folder, parent_folder)
    else:
        image_output_path = os.path.join(output_cel_folder, parent_folder)

    if is_anim:
        folder = file.split("_")[0]
        image_output_path = os.path.join(image_output_path, folder)

    # Create the batch output folder if it doesn't exist
    Path(image_output_path).mkdir(parents=True, exist_ok=True)

    speaker = speaker.lower()
    #print(f"File: {file}, Translation: {translation}, Speaker: {speaker}")

    # Create an image using this speaker's template
    # Some areas create archives too large that it doesn't fit, causing music to stop
    # Handle these special cases by using alternative templates with less colors
    if "msg5-2-0" in str(image_output_path):
        if "flare" in speaker:
            base_box = Image.open(os.path.join("templates", "template_blank.png"))
        else:
            base_box = Image.open(os.path.join("templates", "template_metal_box_gridless.png"))
    elif "msg8" in str(image_output_path) or "Speak" in image_output_path:
        base_box = Image.open(os.path.join("templates", "template_metal_box_gridless.png"))
    else:
        # Trying the boxes without the grids for lower file sizes
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

    #base_box = base_box.convert(mode="P", palette=1, colors=32)
    base_box.save(os.path.join(image_output_path, file))
