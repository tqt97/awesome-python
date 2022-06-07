name = input('Type your name:')
print(f'Welcome {name} to this advanture!')


answer = input(
    'You are on a dirt road, it has come to an end and you can go left or right? Which way do you go? \n').lower()

if answer == 'left':
    answer = input(
        'You come to a river, you can walk around it or swim across the river? \n').lower()
    if answer == 'swim':
        print('You swam across and were eaten by an alligator.')
    elif answer == 'walk':
        print('You walk for many miles, ran out of water and you lost the game.')
    else:
        print('Not valid answer. You lose')
elif answer == 'right':
    answer = input(
        'You come to a bridge, it looks wobbly, do you want to cross it (cross/back) ? \n').lower()
    if answer == 'cross':
        answer = input(
            'You cross the bridge and meet a stranger, do you want to talk to him (yes/no)? \n').lower()
        if answer == 'yes':
            print(
                'You met a stranger and he asked you to go to a magical island, do you want to go (yes/no)?')
        elif answer == 'no':
            print(
                'You don\'t talk to a magical island and you lost the game.')
        else:
            print('Not valid answer. You lose')
    elif answer == 'back':
        print('You go back to the main road. Now you can decide what you want to cross')
    else:
        print('Not valid answer. You lose')
else:
    print('Not a valid answer. You lose !')

print('-------------------------****------------------------------')
print('The game is over. Thanks for playing.')