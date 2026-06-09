import os
import shutil

"""
cmd='pyinstaller'
  +' --clean' # Removes previous compilation
  +' --onedir' # Puts the executable and libs in one directory
  #+' --onefile' # Puts the executable and libs in a single file
  +' --windowed' # Windowed application
  +' --icon="./fig/guiduino.ico"' # Adds the application icon
  +' --add-data "./fig/*.png;fig/"' # Adds the figures to the executable
  +' --name guiduino' # Names the executable
  +' main.py' # Start file

  """

shutil.copytree('bin', 'dist/bin', dirs_exist_ok=True) 

cmd='pyinstaller --clean --onefile --windowed --icon="./fig/bar.png" --add-data "./fig/*.png;fig/" --add-data "./fig/*;fig/" --name AltBAR-UI main.py'

os.system(cmd)

