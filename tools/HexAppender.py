import sys
import os
from pathlib import Path

if len(sys.argv) < 4:
    print("Usage: <original_anims> <directory_of_cels> <output_anims>")
    exit()

orig_anim_base_path = Path(sys.argv[1])
cel_folder_base_path = Path(sys.argv[2])
output_anim_base_path = Path(sys.argv[3])

processed_anims = set()

# Find all image groups
for generated_cel_file in cel_folder_base_path.rglob("*"):
    if generated_cel_file.is_dir():
        continue

    anim_name = generated_cel_file.parent.name

    if anim_name in processed_anims:
        continue

    # Keep track that we've looked at this one
    processed_anims.add(anim_name)

    relative_path = generated_cel_file.parent.relative_to(cel_folder_base_path)
    orig_anim_path = orig_anim_base_path / relative_path
    output_anim_path = output_anim_base_path / relative_path
    cel_folder_path = generated_cel_file.parent

    # Open the original anim and obtain the PLUT
    with open(orig_anim_path, "rb") as input_file:
        raw_hex = input_file.read().hex()
        ccb_start = raw_hex.index('CCB'.encode('utf-8').hex())
        header = raw_hex[0:ccb_start]

    with open(output_anim_path, "wb") as output_file:
        # Write out the header
        output_file.write(bytes.fromhex(header))

        ccb_added = False

        # Iterate through the CELs and add them to the output anim
        for cel in sorted(cel_folder_path.glob("*"), key=os.path.getmtime):

            with open(cel, "rb") as cel_file:
                raw_hex = cel_file.read().hex()

                if not ccb_added:
                    start = 0
                    ccb_added = True
                elif "PLUT" in raw_hex:
                    start = raw_hex.index('PLUT'.encode('utf-8').hex())
                else:
                    start = raw_hex.index('PDAT'.encode('utf-8').hex())
                cel_data = raw_hex[start:]
                output_file.write(bytes.fromhex(cel_data))

    print(f"Successfully wrote to ANIM {output_file.name}")
