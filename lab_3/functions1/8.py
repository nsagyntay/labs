'''Write a function that takes
in a list of integers and returns
True if it contains 007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False'''
def spy_game(nums):
    sequence = [0, 0, 7]
    i = 0
    for num in nums:
        if num == sequence[i]:
            i += 1
            if i == len(sequence):
                return True
    return False
print("1,2,4,0,0,7,5 ->",spy_game([1,2,4,0,0,7,5]))
print("1,0,2,4,0,5,7 ->",spy_game([1,0,2,4,0,5,7]))
print("1,7,2,0,4,5,0 ->",spy_game([1,7,2,0,4,5,0]))
