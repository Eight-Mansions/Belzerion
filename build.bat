@echo off
set working_name=working
set working_iso=Belzerion_Working.iso

echo Clearing out the old files and creating a clean workspace...
rmdir /s /q cd\%working_name% 1>nul
Xcopy /E /q cd\orig\ cd\%working_name%\ 1>nul
echo:

echo Converting dialogue boxes to PNGs...
python tools\DokuToPNGs.py "tl:belzerion:msg0" "generated_images"
python tools\DokuToPNGs.py "tl:belzerion:msg1" "generated_images"
echo:

echo Converting dialogue box images to CELs...
python tools\DialogueBoxesToCELs.py "generated_images" "generated_cels" "raw_cels" "cd\orig"
echo:

:: TODO: Either make this part more intelligent, or hardcode the other ANIM creation steps
:: Folder names are the ANIM names
:: Currently, they all go in BELZERION_ART, but if others don't, we'll have to account for that structure
echo Converting dialogue box CELs to ANIM...
rename "cd\working\BELZERION_ART\MSG0-1-01.C6" MSG0-1-01.C6.ANIM
tools\3DO-ANIM.exe -origanim "cd\working\BELZERION_ART\MSG0-1-01.C6.ANIM" -inputceldir "generated_cels\BELZERION_ART\msg0-1-01.c6" -includeplut TRUE -overwrite TRUE
rename "cd\working\BELZERION_ART\MSG0-1-01.C6.ANIM" MSG0-1-01.C6
echo:

echo Creating final iso...
tools\3doiso.exe -in cd\working -out "cd\%working_iso%"
echo:

echo Signing release...
tools\3DOHomebrewSigning.exe genromtags "cd\%working_iso%"
echo:

echo Complete!
echo:
echo:

pause