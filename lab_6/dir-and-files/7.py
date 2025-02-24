# Write a Python program to copy the
# contents of a file to another file
import os
import shutil
def copy_file():
    s = input("source file: ")
    des = input("destination file: ")
    if os.path.exists(s):
        shutil.copy(s, des)
        print("File copied.")
    else:
        print("Source file not found.")
copy_file()