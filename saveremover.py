
# DO NOT USE IF YOU HAVE ANY SAVES YOU DON'T WANT TO BE DELETED IN YOUR SAVES DIRECTORY
# All .sav files will be deleted from the saves directory when run
# Set achievement_reset to true to reset achievements for certain categories (All achievements, 30 achievements, etc.)
# Requires python, use AutoHotkey script to run after pressing a hotkey (Windows only)

import os

USER = os.path.expanduser('~')
dir = USER + "\\AppData\\LocalLow\\Monomi Park\\Slime Rancher" # Change if not using windows
list = os.listdir(dir)
achievement_reset = False

for item in list:
    if item.endswith(".sav"):
        os.remove(os.path.join(dir, item))
    if achievement_reset:
        if item.endswith(".prf"):
            os.remove(os.path.join(dir, item))

