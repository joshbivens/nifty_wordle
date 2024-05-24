# File: Wordle.py
# Programmer: Josh Bivens
# Email: the joshbivens@gmail.com

"""

"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, MISSING_COLOR, CORRECT_COLOR, PRESENT_COLOR

def wordle():
    target = random.choice(FIVE_LETTER_WORDS)
    
    def get_char(index):
        return gw.get_square_letter(0, index)
    
    def build_word():
        i = 0
        word = ""
        for i in range(N_COLS):
            char = gw.get_square_letter(0, i)
            word += char
        return word.lower()
    
    def word_in_list():
        word = build_word
        if word in FIVE_LETTER_WORDS:
            return True
        return False

    def enter_action(s):
        if word_in_list():
            i = 0
            for i in range(N_COLS):

                char = get_char(i) 

                if char in target:

                    if i == target.index(char):
                        gw.set_square_color(0, i, CORRECT_COLOR)
                    else:
                        gw.set_square_color(0, i, PRESENT_COLOR)
                        
                else:
                    gw.set_square_color(0, i, MISSING_COLOR)

                i += 1
        else:
           gw.show_message("Word not in list!") 
        
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    gw.show_message(target)
    # MILESTONE 1
    # for i, letter in enumerate(random.choice(FIVE_LETTER_WORDS)):
    #     gw.set_square_letter(0, i, letter)

# Startup code

if __name__ == "__main__":
    wordle()
