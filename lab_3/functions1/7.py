'''Given a list of ints, return True 
if the array contains a 3 next to a 3
somewhere.

def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False'''
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print("1, 3, 3 -> ",has_33([1, 3, 3]))
print("1, 3, 1, 3 -> ",has_33([1, 3, 1, 3]))
print("3, 1, 3 -> ",has_33([3, 1, 3]))

