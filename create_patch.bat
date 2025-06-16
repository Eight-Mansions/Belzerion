@echo off
set original_disc=Belzerion.iso
set working_disc=Belzerion_Working.iso

:: Check that the files exist
if not exist cd\%original_disc_1% (
	echo Could not find the original bin
	echo Please verify a file named %original_disc% exists in the cd folder
	echo and try again.
	goto :EXIT
)

if not exist cd\%working_disc_1% (
	echo Could not find the translated bin
	echo Please verify a file named %working_disc% exists in the cd folder
	echo and try again.
	goto :EXIT
)

:: Create a patch with the two bins
echo Creating patch, please wait...
release\patch_data\xdelta.exe -9 -S none -B 1812725760 -e -vfs "cd\%original_disc%" "cd\%working_disc%" release\patch_data\Belzerion-patch.xdelta

echo Patch created successfully in the release\patch_data folder!

:EXIT
echo Press any key to close this window
pause >nul
exit