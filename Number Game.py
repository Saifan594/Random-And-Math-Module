print("\033c")

import random

playing = True

number = random.randint(1, 10)

print("Guess a number between 1 to 10!")

while playing:
    guess = int(input("Give me your best guess : "))
    
    if guess > number:
        print("NO! Your guessed number is greater than the correct number.")
        print("Please try again!")
    
    elif guess < number:
        print("NO! Your guessed number is smaller than the correct number.")
        print("Please try again!")
    
    else:
        print("You win the game!")
        print(f"The number was {guess}")
        break