import random

user_wins = 0
computer_wins = 0
draw = 0
options = ['rock', 'paper', 'scissor']

while True:
    user_input = input("Rock, Paper, Scissor or Q to quit: ").lower()
    if user_input == "q":
        break
    # computer_input = random.choice(["rock", "paper", "scissor"])
    if user_input not in options:
        print("Invalid input. Please input Rock, Paper, Scissor or Q to quit")
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissor: 2
    computer_pick = options[random_number]
    print("Computer picked: ", computer_pick)
    if user_input == 'rock' and computer_pick == 'scissor' or user_input == 'paper' and computer_pick == 'rock' or user_input == 'scissor' and computer_pick == 'paper':
        print("You win!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Draw!")
        draw += 1
    else:
        print("Computer wins!")
        computer_wins += 1
        
print('***********************///***********************')
print("You won: ", user_wins, " times.")
print('----------------------------------------------------------------')
print("Computer won: ", computer_wins, " times.")
print('----------------------------------------------------------------')
print("Draw: ", draw, " times.")
print('----------------------------------------------------------------')
print("Thank you for playing! Good bye!")
