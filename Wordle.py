# File: Wordle.py
# Programmer: Josh Bivens
# Email: the joshbivens@gmail.com

"""

"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # MILESTONE 1
    for i, letter in enumerate(random.choice(FIVE_LETTER_WORDS)):
        gw.set_square_letter(0, i, letter)

# Startup code

if __name__ == "__main__":
    wordle()
