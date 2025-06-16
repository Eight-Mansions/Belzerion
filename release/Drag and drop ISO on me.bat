@echo off
set filename=Belzerion - English v1.0
set file_type=ISO
set patch_file=Belzerion-patch.xdelta

set found_disc=

pushd %~dp0
if "%~1"=="" goto :NOISO

echo ################################################################################
echo                            Belzerion - English v1.0         
echo                          "You may have lost your past,
echo                   but you've got a future ahead of you yet."
echo ################################################################################
echo:
echo:
echo "The mother computer Vishnu will now check to see if your disc is ready to go..."
echo:

:: Iterate over all files that get dragged onto here
for %%A in (%*) do (
    echo Checking %%A...
    echo:

    if /I "%%~xA"==".bin" (
        :: If we got a bin, convert it to iso first, then patch that
        echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        echo BIN file detected. Activating Cybernizer to digitize the BIN to an ISO...
        echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        echo:
        3dt\3dt_win64.exe to-iso %%A "Belzerion (Original Japanese).iso"
        echo:

        echo "Transmitting converted ISO through the language processor..."
        echo:
        patch_data\xdelta.exe -d -f -s "Belzerion (Original Japanese).iso" "patch_data\%patch_file%" "%filename%.iso" 2>nul

        if not errorlevel 1 (
            set found_disc=true

        echo:
        echo ***
        echo:
        echo:
            echo "Perfect! Original disc for 'Belzerion' found!"
        )
        if not defined found_disc goto :NOPATCHFOUND

        echo "Removing Cybernized conversion of base file..."
        echo:
        del "Belzerion (Original Japanese).iso"

        goto :COMPLETE
    )

    patch_data\xdelta.exe -d -f -s %%A "patch_data\%patch_file%" "%filename%.iso" 2>nul
    if not errorlevel 1 (
        set found_disc=true

	echo ***
	echo:
        echo "Perfect! Original disc for 'Belzerion' found!"
    )

)

if not defined found_disc goto :NOPATCHFOUND

:COMPLETE
echo "You're ready to go!"
echo:
echo -----------------------------------------------------------------------------
echo The following %file_type% file should have been created next to the bat file:
echo * %filename%.iso
echo -----------------------------------------------------------------------------
echo:
echo "Now just load up this .iso file on your favorite device and enjoy!"
echo:
goto :EXIT

:NOISO
echo To patch %file_type% don't run this bat file.
echo Simply drag and drop %file_type% on it and the patch process will start.
goto :EXIT

:NOPATCHFOUND
echo "Uh oh, no patch found suitable for any of the supplied files.
echo  Please make sure to drag in a clean ISO or BIN file of the original 'Belzerion'."
echo:
echo "If the problem persists, go throw a sad puppy at SnowyAria ; _;,
echo  I'm sure she did something again..."

:EXIT
popd
echo:
echo Press any key to close this window
pause >nul
exit
