# Write a Python program to test 
# whether a given path exists or not.
# If the path exist find the filename
# and directory portion of the given 
# path.
import os
def get_path_info():
    path = input("path: ")
    if os.path.exists(path):
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Invalid path.")
get_path_info()