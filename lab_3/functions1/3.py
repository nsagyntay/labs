'''Write a program to solve a classic
puzzle: We count 35 heads and 94 
legs among the chickens and rabbits
in a farm. How many rabbits and how
many chickens do we have? create 
function: solve(numheads, numlegs):'''
def solve(numheads, numlegs):
    R = (numlegs - (2 * numheads)) // 2
    C = numheads - R
    return C, R
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
