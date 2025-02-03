#Write a program able to play the 
#"Guess the number" - game, where 
#the number to be guessed is randomly 
#chosen between 1 and 20. This is how 
#it should work when run in a terminal:
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    count = 0
    while True:
        print("\nTake a guess.")
        guess = int(input())
        count += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break
guess_the_number()