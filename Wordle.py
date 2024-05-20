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
        # Build word from board
        i = 0
        word = ""
        while i < N_COLS:
            word += gw.get_square_letter(0, i)
            i += 1

        # MILESTONE 2
        if word.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Word Found!")
        else:
            gw.show_message("Word not in list!")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # MILESTONE 1
    # for i, letter in enumerate(random.choice(FIVE_LETTER_WORDS)):
    #     gw.set_square_letter(0, i, letter)

# Startup code

if __name__ == "__main__":
    wordle()
