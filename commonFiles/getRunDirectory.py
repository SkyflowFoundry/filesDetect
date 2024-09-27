# getRunDirectory.py: Utility script
# Author: Priyanta Dharmasena
# Modified: August 2024
from pathlib import Path

def getDirectory():
    script_path = Path(__file__).resolve()
    script_directory = script_path.parent
    script_name = script_path.name
    script_directory = str(script_directory).replace(script_name, '')
    return script_directory

if __name__ == "__main__":
    current_directory = getDirectory()
    print(f"### Current directory: {current_directory}")
