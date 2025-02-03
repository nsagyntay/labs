#Write a Python function that takes
# a list and returns a new list with
# unique elements of the first list. 
# Note: don't use collection set.
def unique_elements(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
user_input = input("input elements of list:")
user_list = list(map(int, user_input.split()))
print("Unique elements:", unique_elements(user_list))