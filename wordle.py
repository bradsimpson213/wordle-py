import random
from colorama import Fore, Back, Style
from logo import logo
import os


class Wordle:
    def __init__(self, logo):
        self._logo = logo
        self._words = self.get_all_words()
        self._game_word = self.chose_game_word()
        self._guess = ''
        self._guesses = [[] for x in range(6)]
        self._game_playing = True 
        self._tries = 0
        self.play_game()
    
    def get_all_words(self):
        f = open("words-med.txt", "r")
        words = [ x.rstrip() for x in f]
        wordle_words = [ x for x in words if len(x) == 5 ]
        return wordle_words

    def chose_game_word(self):
        return random.choice(self._words)
    

    def guess(self):
        bad_guess = True
        while bad_guess:
            user_guess = input("Guess a word: ").lower()
            if len(user_guess) != 5:
                print("Words must be 5 letters, try again!")
                continue
            elif user_guess in self._guesses:
                print(f"You already guessed {user_guess}, try again!")
                continue
            else:
                bad_guess = False
                self._guess = user_guess
                self._guesses[self._tries] = self._guess
                self._tries += 1
                
    
    def play_game(self):
        print(self._logo)
        print('Welcome to Wordle!')
        while self._tries < 6:
            self.guess()
            self.update_display()
            if self._guess == self._game_word:
                print(f"YOU WIN! {self._tries}/6 THE WORD WAS '{self._game_word.upper()}'! ")
                return
        
        print(f"Sorry you are out of tries, the word was {self._game_word}")
        

    def update_display(self):
        os.system('clear')
        for word in self._guesses:
            if len(word) > 1:
                display = []
                for index, letter in enumerate(word):
                    if letter == self._game_word[index]:
                        display.append((Back.GREEN, letter.upper()))
                    elif letter in self._game_word and letter != self._game_word[index]:
                        display.append((Back.YELLOW, letter.upper()))
                    else:
                        display.append((Style.RESET_ALL, letter.upper()))
                print(display[0][0] + display[0][1] + Style.RESET_ALL + ' ' + 
                        display[1][0] + display[1][1] + Style.RESET_ALL + ' ' + 
                        display[2][0] + display[2][1] + Style.RESET_ALL + ' ' + 
                        display[3][0] + display[3][1] + Style.RESET_ALL + ' ' + 
                        display[4][0] + display[4][1] + Style.RESET_ALL)
            else:
                display = [ "_" for x in range(len(self._game_word))]
                print(' '.join(display))


Wordle(logo)