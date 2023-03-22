import os
import tkinter
import shutil
from PIL import Image
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

# pick folders
input("Press Enter key to pick the folder you want to search through.")
folder_path = filedialog.askdirectory()
input("press Enter key and pick the output where the duplicate images will go.")
output_path = filedialog.askdirectory()

def find_duplicate_images(folder_path):
  # create a dictionary to store the checksums of the images
  checksums = {}
  dupes = []
  
  # traverse the folder and compute the checksum for each image
  for root, dirs, files in os.walk(folder_path):
    for file in files:
    
        # skip non-image files
        if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        try:
            file_path = os.path.join(root, file)
            with Image.open(file_path) as img:
                checksum = hash(img.tobytes())
            
            # add the checksum to the dictionary
            if checksum in checksums:
            
                # this is a duplicate image and add it to list
                print(f'Found duplicate image: {file_path}')
                dupes.append(file_path)
                # this is the original image and add it to list
                print(f'The original image---: {checksums[checksum]}')
                dupes.append(checksums[checksum])
            else:
                checksums[checksum] = file_path
        
        # Ingore errors        
        except OSError:
            continue

  # move images from source to output
  for image in dupes:
    shutil.move(image, output_path)
  
    if not dupes:
        print("Found no duplicate images")
    else:
        print(f"The dupes are: {dupes}\n They have been move successfully")
  
  input("Finished. Press Enter key to close")  
  
# run the function
find_duplicate_images(folder_path)
