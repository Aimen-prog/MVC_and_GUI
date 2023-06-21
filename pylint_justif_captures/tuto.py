To accomplish this task in Python, you can use the shutil module to copy the files and the os module to manipulate the file names. Here's an example script that achieves what you described:

python

import os
import shutil

# Source directory containing the folders with files
source_directory = "path/to/source/directory"

# Destination directory to store the copied files
destination_directory = "path/to/destination/directory"

# Iterate over each folder in the source directory
for folder_name in os.listdir(source_directory):
    folder_path = os.path.join(source_directory, folder_name)

    # Ensure that the item is a directory
    if os.path.isdir(folder_path):
        # Iterate over each file in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Copy the file to the destination directory
            shutil.copy2(file_path, destination_directory)

            # Rename the file using a new name
            new_file_name = folder_name + "_" + file_name
            new_file_path = os.path.join(destination_directory, new_file_name)

            # Rename the copied file
            os.rename(
                os.path.join(destination_directory, file_name),
                new_file_path
            )
