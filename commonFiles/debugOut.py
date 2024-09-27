import os
import sys
import base64
import time
from datetime import datetime
from pathlib import Path

def debug(debugOutStr, directory_out, scriptname):
    #full path to current script
    #script_path = Path(__file__).resolve()
    #current script dir
    #script_directory = script_path.parent
    #script_name = script_path.name    # Remove  script file name from dir-path
    #script_directory = str(script_directory).replace(script_name, '')
    #current_directory =  script_directory
    now = datetime.now()
    dateTimeStr = now.strftime("%d-%b-%Y %H:%M:%S")
    debugOutFile = f'{directory_out}/debugOut-{scriptname}.txt'

    with open(debugOutFile, "a") as file:           # output to debug file
         print("*" * 46, file=file)
         print(f"\nDebug Output at: *** {dateTimeStr}  ***\n", file=file)
         print("*" * 46, file=file)
         print(debugOutStr, file=file)
