# This script helps you delete "unused" raw files which have no .jpg match.

**Here is an outline of the algorithm:**
 1. Copy JPGs and RAWs from camera memory card to your coputer into a an empty folder.
 2. Move the script in this folder.
 3. Create here a new folder called: *cr3*.
 4. Copy all RAW files (with extension .CR3) to this new folder.
 5. Delete the useless JPGs.
 6. Run the script.

**How the script works:**
  1. Itterate through all JPGs and CR3s to save the names of them.
  2. Create a list of CR3s which have no .jpg match.
  3. Move all CR3 above identified into a new folder called *0trash*.

**After runnign the script:**
  1. All useless CR3s can be found in new folder named *0trash*.
  2. All files can be deleted because have no coresponding JPG.
