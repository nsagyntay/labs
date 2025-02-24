# Write a Python program to delete file
# by specified path. Before deleting
# check for access and whether a given
# path exists or not.
import os
def delete_file():
    file_path = input("file:")
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted.")
    else:
        print("File not found")
delete_file()