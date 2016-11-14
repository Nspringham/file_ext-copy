# ext_copy_dest.py - Find all files in directory tree 
# Find all specific file extension in directory tree
# Print the files
# Copy files to designated folder


import os
import shutil


def move_all_ext(extension, source_root, dest_dir):
    # Recursively walk source_root
    for (dirpath, dirnames, filenames) in os.walk(source_root):
        # Loop through the files in current dirpath
        for filename in filenames:
            # Check file extension
            if os.path.splitext(filename)[-1] == extension:
                try:
                    print("copying file: %s" % filename)
                    # Move file
                    shutil.copy(os.path.join(dirpath, filename), os.path.join(dest_dir, filename))
                except PermissionError:
                    print('Could not copy file: %s' % filename)
                except shutil.SameFileError:
                    print('Could not copy duplicate file: %s' % filename)



print('Welcome to the file find/copy module\n')
print('You will be asked to enter a directory name and the file type that you want to copy\n')
# Prompt new folder name
print('Enter new directory name:')
newDir = input()
print('Enter the file extension (.pdf, .txt, etc..)')
fileExt = input()

# File directory path
os.makedirs(os.path.join('C:\\Users\\<user>\\Documents\\', newDir))

# Move all pdf files from C:\ to C:\Users\<user>\Documents\
move_all_ext('.' + fileExt, "C:\\", os.path.join('C:\\Users\\<user>\\Documents\\', newDir))

