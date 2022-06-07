import random

top_of_range = input('Type a number : ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number greater than 0')
        quit()
else:
    print('Please type a number')
    quit()

r = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess : ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            print('Please type a number greater than 0')
    else:
        print('Please type a number')
        continue
    if user_guess == r:
        print('Your guess is correct')
        break
    elif user_guess > r:
        print('Your guess is too high')
    else:
        print('Your guess is too low')

print('***********************///***********************')
print('You got it in', guesses, 'guesses')
print('----------------------------------------------------------------')
print("Thank you for playing! Good bye!")
