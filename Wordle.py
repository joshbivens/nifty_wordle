# File: Wordle.py
# Programmer: Josh Bivens
# Email: the joshbivens@gmail.com

"""

"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import (
    WordleGWindow, 
    N_COLS, N_ROWS, 
    MISSING_COLOR, 
    CORRECT_COLOR, 
    PRESENT_COLOR
)

def wordle():
    target = random.choice(FIVE_LETTER_WORDS).upper()
    current_row = 0
    
    def get_char(index):
        return gw.get_square_letter(current_row, index)
    
    def build_word():
        word = ""
        for i in range(N_COLS):
            char = gw.get_square_letter(current_row, i)
            word += char
        return word
    
    def word_in_list():
        word = build_word()
        return word.lower() in FIVE_LETTER_WORDS 

    def enter_action(s):
        nonlocal current_row

        if word_in_list():
            for i in range(N_COLS):
                char = get_char(i) 

                if char in target:
                    if target[i] == char:
                        gw.set_square_color(current_row, i, CORRECT_COLOR)
                    else:
                        gw.set_square_color(current_row, i, PRESENT_COLOR)  
                else:
                    gw.set_square_color(current_row, i, MISSING_COLOR)
        else:
           gw.show_message("Word not in list!") 
        
        current_row += 1

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    gw.show_message(target)

# Startup code
if __name__ == "__main__":
    wordle()
