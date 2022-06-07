print('Welcome to my computer quiz !')

playing = input('Do you want to play ? (yes/no) \n').lower()

if playing in ['No', 'no', 'n']:
    quit()
elif playing in ['Yes', 'yes', 'y']:
    print('Oke ! Let\'s play')
    questions = {
        'What is the name of the computer language used to create the Python programming language ?': 'Python',
        'What is the name of the computer language used to create the C programming language ?': 'C',
        'What is the name of the computer language used to create the C++ programming language ?': 'C++',
        'What is the name of the computer language used to create the Java programming language ?': 'Java',
    }

    n = len(questions)
    score = 0
    num = 0

    for q in questions:
        a = input(q + '\n')
        if a.lower() == questions[q].lower():
            print('Correct !')
            score += 1
            num += 1
        else:
            print('Wrong !')
    s = 's' if num > 1 else ''
    print(f'{num} answer{s} correct .Your score is : {str(score)} - {str(score/n*100)}%')
else:
    print('Please answer yes or no !!')
