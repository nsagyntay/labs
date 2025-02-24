# Write a Python program to write a
#  list to a file.
def write_list_to_file():
    file_path = input("name:")
    items = input("words:").split()
    file = open(file_path, 'w')
    for item in items:
        file.write(item + '\n')
    file.close()
write_list_to_file()