# filesDetect.py: Skyflow detect PDF file    Version: 1.2
# Author: Priyanta Dharmasena
# Modified: July 2024
import tkinter as tk
import os
from tkinter import filedialog

def file_selector(file_type, starting_directory):
    if  file_type:
        windowTitle = 'Select ' + file_type + ' file: '
     
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    root.attributes('-topmost', True)  # Make the file dialog stays on top!
    root.after(0, root.lift)  # Lift the root window
    root.after(0, lambda: root.focus_force())  # Force focus

    root.grab_set()  # Set grab to make it modal    

    # Open a file dialog for selecting a file
    file_path = filedialog.askopenfilename(initialdir=starting_directory, title= windowTitle)

    root.grab_release() # Dialog is closed, release the grab

    # Return the file name and file path as a tuple
    if file_path:
        root.destroy()  # Destroy the root window after use
        return os.path.basename(file_path), file_path
    else:
        root.destroy()  # Destroy the root window after use
        return None, None


if __name__ == "__main__":
    # Example usage - standalone testing stuff
    selected_file_name, selected_file_path = file_selector('Test', os.getcwd())

    if selected_file_name and selected_file_path:
        # Retrieve directory and file name
        selected_directory = os.path.dirname(selected_file_path)
        selected_filename = os.path.basename(selected_file_path)

        # Print the retrieved values
        print("---> Selected directory:", selected_directory)
        print("---> Selected filename:", selected_filename)
        exit()

        # Use the selected file name and file path for further processing
    else:
        print("---> No file selected.")
        exit()
