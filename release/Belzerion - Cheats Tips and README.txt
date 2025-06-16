########################################################################
               Belzerion - English Patch v1.0 (June 2025)
########################################################################

## Intro ##
"You may have lost your past, but you've got a future ahead of you yet."

In a world devestated by war, only a highly-advanced AI can keep mankind
safe in an artifical utopia, Shangri-la. But what secrets does the
mother computer Vishnu hold, and can they be trusted?

Punch your way through robot crime in this cyperpunk adventure game,
blending both adventure exploration and real-time combat with flips and
fists!

----------------------------------------------------------------------

*************************
## COMPATIBILITY ISSUE ##
*************************
4DO has a massive slowdown during the Chapter 3 battles. This isn't an
issue on console or Phoenix. I haven't tested RetroArch's core.

----------------------------------------------------------------------

## Patch Instructions ##
* The patcher expects the ISO or BIN version of the game. If a BIN is
  supplied, the tool will convert it to an ISO automatically.

### Windows ###
1. Drag and drop your original Japanese ISO or BIN image onto the file
   called "Drag and drop ISO on me.bat"
2. If a valid disc image is found, the patched ISO will be created in
   this folder.

### Other OS ###
This release uses a basic .xdelta patch, so any web-based patching tool
or OS-specific .xdelta patcher should work okay. We've switched from
xdelta3 to xdelta to help with compatibility. The .xdelta file is located
in the "patch_data" folder. Apply the patch to your disc.

For this, you will need an ISO and not a BIN. You can use 3dt to convert
from a BIN to an ISO here - https://github.com/trapexit/3dt

 3dt_win64.exe to-iso <your BIN here> "Belzerion (Original Japanese).iso"

## Combat Controls ##
There are two main modes: energy rifle and fists. The game will
automatically switch to fists when any enemy is in melee range.

Rifle:
  - Hold A to shoot.
  - To lock on, let the cursor turn red by hovering over an enemy,
    then hold A.
  - Press L or R to side-flip and dodge projectiles.
  - Press B to use your shield.
    - You have limited uses, but the shield lasts a long while.
    - Later in the game, this will upgrade to deal massive damage in
      retaliation.
      It's extremely good for lowering boss health if you use it while
      they're on screen!
    - Don't hold it down; a single use uses less energy and lasts quite
      a while.

Fists:
  - Press A to punch. Press multiple times for a combo that ends with
    sending the foe flying back.
  - Press Left or Right with A for a hook.
    - Alternate left and right for a devestating hook combo.
    - This hook becomes even stronger after the blade upgrade. 
  - Press L or R to dash left and right.
    - Press A during a dash for a boosted punch. This often sends
      enemies flying to the back wall.
  - Press B to use your shield (see above for more info).

## Tips ##
- Dying will restart the current fight with refreshed shields and health,
  so don't stress too much about it!

- The true ending requires that you beat the game with less than 5 game
  overs, HOWEVER: if you use the chapter select code (normally given by
  clearing the true end), you can start at the final chapter with zero
  deaths for an easy clear. See Cheat section below for the code.

- Chapter 7 pit maze (O = walkable, X = pit):
    O
  O O X
  O X X
  O O X
  X O X
  X O X

- Boss: A.S.L.A.
  - This is a gimmick fight, but also has a bit of a problem.
    AVOID USING YOUR SHIELDS! Shields prevent the gimmick from happening.
  - You can't damage the boss normally, so your goal is to survive until
    you're grabbed. It'll start out far way, so dodge any projectiles
    coming your way. You can return fire, but it's unknown if this speeds
    up the fight or not. Easy enough to stay to the side, never let it
    be in front of you.
  - Once it comes up close, avoid standing right in front of it! It'll
    use a powerful melee combo that'll shred your health. Use L and R to
    dash, then use a flying punch by punching during a dash. If you can
    land a single hit, the boss will retreat. It may retreat if you
    survive long enough.
  - NOW the boss should lunge forward again and grab you in the process.
    Once the head opens up, punch to deal 1/3rd damage to the boss. Now
    repeat 3 times!
  - WARNING: If you use shields during the close-range phase, it can skip
    the gimmick grab, resulting in an unwinnable fight (or at least
    wasted time!).
  - For a visual reference, here's the fight from my playthrough:
    https://youtu.be/iMQyGIv0eBE?si=ieF_DDNeZ0o4nu5I&t=4261

## Cheats ##
All cheats end with P to confirm, which is the start button.

Chapter Select:
  Up, B, A, C, A, Down, B, A, C, A, P

Sound Mode:
  Hold L, then Up, Down, Left, Right, B, A, P

Battle Mode (boss rush):
  Up, C, R, A, B, P

## Credits ##
SnowyAria - Translation, Hacking
NicheTopic - Image Edits

## Special Thanks ##
trapexit - 3it 3DO Image Tool, which was invaluable to make this happen!
         - 3dt for adding BIN to ISO support to the patcher.
fixel - ODE saves so many blank CDs testing translations like this and
        others, especially as this game had issues that only broke on
        console.
Cargodin - Editing pass on opening video
Emi, Fia, Telephone_Ghost, Shentok - Playtesting!

## Contact ##
Have any issues or run into any problems? Feel free to drop by our
discord here:
*  https://discord.gg/bewGNtm

Alternatively, you can message SnowyAria/ArcaneAria on ROMhacking.net
or on Bluesky at @snowyaria.bsky.social
