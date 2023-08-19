# Belzerion

## 1st time setup
You'll need to extract your copy of the original game to compile. To get live subtitle updates, you'll also need to supply a dokuwiki login.

### Setup Dokuwiki
1. Open the `tools` folder.
2. Copy `parameters_template.txt` to `parameters.txt`.
3. Open the file and next to `DOKU_WIKI_USERNAME` and `DOKU_WIKI_PASSWORD`, put your login information.
4. DO NOT COMMIT THIS FILE!

### Setup original game files
1. Open the `cd` folder and create an `orig` folder.
2. Under `tools`, open `OperaFS [De]Compiler [EN].exe`.
3. Select `De-Compile`, then select your `ISO` image.
4. Copy the extracted files into `cd\orig`.

## Compiling
1. Run `1-build.bat`. This will compile all the edited game assets into `cd\working`.
2. Open `OperaFS [De]Compiler [EN].exe`, then select `Compile`. Select the `cd\working` folder, then save as `cd\Belzerion_Working.iso`.
3. Run `3-sign.bat` to sign the game for playing.