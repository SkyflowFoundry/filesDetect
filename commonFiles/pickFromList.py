# pickFromList.py: Pick a file type to process
# Author: Priyanta Dharmasena
# Created: August 2024
def pick_list_values(values=None, items_per_line=4):
    values = ["mp3", "wav", "pdf", "txt", "csv", "json", "jpg", "jpeg", "tif", "tiff", "png", "bmp"]
    print("Please pick your required file-type from this list:")
    for idx, value in enumerate(values, 1):
        print(f"{idx}. {value}", end="\t")
        if idx % items_per_line == 0:
            print()  #throw newline

    if len(values) % items_per_line != 0:
        print()

    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= choice <= len(values):
                selected_value = values[choice - 1]
                print(f"You have selected: {selected_value}")
                return selected_value
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(values)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#selected_value = pick_list_values()
