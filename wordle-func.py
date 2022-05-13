import random
from colorama import Fore, Back, Style
from logo import logo
import os

'''Terminal version of Wordle'''

def get_word ():
    ''' reads the words file, strips away new lines,
    turns it to a list, then filters the list for 5 character 
    words and returns them '''
    f = open("words.txt", "r")
    words = [ x.rstrip() for x in f]
    wordle_words = [ x for x in words if len(x) == 5 ]
    word = random.choice(wordle_words)
    return word


def display(game_word, guesses):
    os.system('clear')
    for word in guesses:
        if len(word) > 1:
            display = []
            for index, letter in enumerate(word):
                if letter == game_word[index]:
                    display.append((Back.GREEN, letter.upper()))
                elif letter in game_word and letter != game_word[index]:
                    display.append((Back.YELLOW, letter.upper()))
                else:
                    display.append((Style.RESET_ALL, letter.upper()))
            print(display[0][0] + display[0][1] + Style.RESET_ALL + ' ' + 
                    display[1][0] + display[1][1] + Style.RESET_ALL + ' ' + 
                    display[2][0] + display[2][1] + Style.RESET_ALL + ' ' + 
                    display[3][0] + display[3][1] + Style.RESET_ALL + ' ' + 
                    display[4][0] + display[4][1] + Style.RESET_ALL)
        else:
            display = [ "_" for x in range(len(game_word))]
            print(' '.join(display))


def wordle ():
    print(logo)
    print('Welcome to Wordle!')
    game_word = get_word()
    tries = 0
    guesses = [[] for x in range(6)]

    while tries < 6:
        guess = input("Guess a word: ").lower()
        if guess == game_word:
            guesses[tries] = guess 
            display(game_word, guesses)
            print(f"YOU WIN! {tries + 1}/6 THE WORD WAS {game_word.upper()}! ")
            return
        elif len(guess) < 5:
            print("Words must be 5 letters, try again!")
            continue
        elif guess in guesses:
            print(f"You already guessed {guess}, try again!")
            continue
        guesses[tries] = guess 
        display(game_word, guesses)
        tries += 1
    
    print(f"Sorry you are out of tries, the word was {game_word}")

wordle()