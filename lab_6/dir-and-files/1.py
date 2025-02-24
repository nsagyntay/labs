#Write a Python program to list only 
# directories, files and all directories,
#  files in a specified path.
import os
def list_contents():
    path = input("path:")
    if os.path.exists(path):
        print("Dir:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
        print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    else:
        print("Invalid path.")
list_contents()