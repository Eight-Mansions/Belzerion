@echo off
set working_name=working

echo Clearing out the old files and creating a clean workspace...
rmdir /s /q cd\%working_name% 1>nul
Xcopy /E /q cd\orig\ cd\%working_name%\ 1>nul
echo:

echo Converting dialogue boxes to PNGs...
python tools\DokuToPNGs.py "tl:belzerion:msg0-1-01" "generated_images\msg0-1-01"
echo:

echo Converting dialogue box images to CELs...
python tools\DialogueBoxesToCELs.py "generated_images\msg0-1-01" "generated_cels\msg0-1-01"
echo:

echo Converting dialogue box CELs to ANIM...
::rename "cd\working\BELZERION_ART\MSG0-1-01.C6" MSG0-1-01.C6.ANIM
tools\3DO-ANIM.exe -origanim "cd\working\BELZERION_ART\MSG0-1-01.C6.ANIM" -inputceldir "generated_cels\msg0-1-01" -includeplut FALSE -overwrite TRUE
::rename "cd\working\BELZERION_ART\MSG0-1-01.C6.ANIM" MSG0-1-01.C6
echo:

pause