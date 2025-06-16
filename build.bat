@echo off
set working_name=working
set working_iso=Belzerion_Working.iso

echo Clearing out the old files and creating a clean workspace...
rmdir /s /q cd\%working_name% 1>nul
rmdir /s /q generated_images 1>nul
rmdir /s /q generated_cels 1>nul
rmdir /s /q generated_anim_images 1>nul
rmdir /s /q generated_anim_cels 1>nul
Xcopy /E /q cd\orig\ cd\%working_name%\ 1>nul
echo:

echo Converting dialogue boxes to PNGs...
python tools\DokuToPNGs.py "tl:belzerion:msg0" "generated_images" "generated_anim_images"
python tools\DokuToPNGs.py "tl:belzerion:msg1" "generated_images" "generated_anim_images"
python tools\DokuToPNGs.py "tl:belzerion:msg2" "generated_images" "generated_anim_images"
python tools\DokuToPNGs.py "tl:belzerion:msg3" "generated_images" "generated_anim_images"
python tools\DokuToPNGs.py "tl:belzerion:msg4" "generated_images" "generated_anim_images"
python tools\DokuToPNGs.py "tl:belzerion:msg5" "generated_images" "generated_anim_images"
python tools\DokuToPNGs.py "tl:belzerion:msg6" "generated_images" "generated_anim_images"
python tools\DokuToPNGs.py "tl:belzerion:msg7" "generated_images" "generated_anim_images"
python tools\DokuToPNGs.py "tl:belzerion:msg8" "generated_images" "generated_anim_images"
echo:

echo Copying manual images into build folder...
Xcopy /E /q manual_images\ generated_images\ 1>nul
Xcopy /E /q manual_anim_images\ generated_anim_images\ 1>nul
echo:

echo Converting images to CELs...
python tools\DialogueBoxesToCELs.py "generated_images" "generated_cels" "raw_cels" "cd\orig"
python tools\DialogueBoxesToCELs.py "generated_anim_images" "generated_anim_cels" "raw_cels" "cd\orig"
echo:

echo Please take a minute to look for any errors, then press any button to continue.
echo:
pause

echo Copying over non-ANIM dialogue boxes...
Xcopy /E /q /Y generated_cels\ cd\%working_name%\
echo:

:: Folder names are the ANIM names
echo Converting dialogue box CELs to ANIM...
python tools\HexAppender.py "cd\working" "generated_anim_cels" "cd\working"
echo:

echo Copying over the opening video...
Xcopy /E /q /Y videos\Opening\complete\OpenM cd\%working_name%\BERU-MOV\
echo:

echo Copying over the banner image...
Xcopy /E /q /Y banner\BannerScreen cd\%working_name%\
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
echo Press any button to launch 4DO, otherwise close the window to cancel.

pause

start "" "D:\Games\3DO\4DO_1.3.2.4\4DO.exe"
