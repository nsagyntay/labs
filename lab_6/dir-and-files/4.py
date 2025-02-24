# Write a Python program to count the 
# number of lines in a text file.
import os
def count_lines():
    file_path = input("path:")
    if os.path.exists(file_path):
        file = open(file_path)
        print("Line count:", sum(1 for _ in file))
        file.close()
    else:
        print("File not found.")
count_lines()