from random import randrange

hangman={0:'''
        ____________
         |''',
        1:'''
        ____________
         |
         O''',
        2:'''
        ____________
         |
         O
        /''',
        3:'''
        ____________
         |
         O
        / \\''',
        4:'''
        ____________
         |
         O
        / \\
         |''',
        5:'''
        ____________
         |
         O
        / \\
         |
        /''',
        6:'''
        ____________
         |
         O
        / \\
         |
        / \\ '''}


while True:
    list_of_words = ['LEARNING', 'PYTHON', 'CREATING', 'GAME', 'HIPPOPOTAMUS', 'AGE', 'SUMMER', 'WEIGHTLIFTING']
    word = list_of_words[randrange(len(list_of_words))]
    hidden_word = "x" * len(word)
    print(f'Hidden word is: {hidden_word}')

    mistake_count = 6
    hangman_count = 0
    used_letters = []

    while mistake_count > 0:
        letter_count = 0
        index_count = 0

        print('Pick a letter:')
        picked_letter = input().upper()

        if picked_letter in used_letters:
            print('You have already entered this letter. Please try another one!')
            continue

        used_letters.append(picked_letter)

        for letter in word:
            if letter == picked_letter:
                hidden_word = hidden_word[:index_count] + picked_letter + hidden_word[index_count+1:]
                letter_count += 1
            index_count += 1

        if len(picked_letter) > 0 and picked_letter in word:
            print(f'CORRECT! The word contains the letter {picked_letter}')
            print(hidden_word)
            print('==============================================')
        elif len(picked_letter) > 1:
            print('Invalid input. Please only enter one letter at a time!')
        elif not picked_letter.isalpha():
            print('Invalid input. Please only enter letters')
        else:
            mistake_count -= 1
            hangman_count += 1
            print(f'WRONG! Number of mistakes left: {mistake_count}')
            print(hangman[0 + hangman_count])
            print('==============================================')

        if hidden_word == word:
            print('CONGRATULATIONS! You won!')
            break

    if mistake_count == 0:
        print(f'HANGED! You were looking for {word}')

    restart = input('Do you want to play again? Yes or No? ')
    if not restart.lower().startswith('y'):
        print('Thanks for playing Hangman with me! See you next time!')
        break
    else:
        print('============================================== \n NEW GAME!')