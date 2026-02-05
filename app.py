import webbrowser
import os

# Get the absolute path to your file
file_path = os.path.abspath("game.html")

# Open it in a new tab
webbrowser.open(f"file://{file_path}")

#def load():
#  print("working")
#  game.html

#load()
