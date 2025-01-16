print("\033c")

import random

options = ["Rock", "Paper", "Scissors"]

score = 0

while True:
    user_choice = input("Choose Rock, Paper or Scissors : ")
    
    computer_choice = random.choice(options)
    
    print(f"You chose : {user_choice}")
    print(f"Computer chose : {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!\n\n")
    
    elif user_choice == "Rock" and computer_choice == "Scissors":
        score += 1
        print(f"Rock smashes scissors! You win!\nScore : {score}\n\n")
    
    elif user_choice == "Paper" and computer_choice == "Rock":
        score += 1
        print(f"Paper covers rock! You win!\nScore : {score}\n\n")
    
    elif user_choice == "Scissors" and computer_choice == "Paper":
        score += 1
        print(f"Scissors cut paper! You win!\nScore : {score}\n\n")
    
    else:
        score -= 1
        print(f"You lose! Computer wins!\nScore : {score}\n\n")