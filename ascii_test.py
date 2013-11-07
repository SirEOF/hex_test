#!/usr/bin/env python

import quizzer

import string
import sys

DECIMAL_MODE = "decimal"
HEX_MODE = "hex"

SPECIAL_CASES = {
    "\n": "\\n",
    "\t": "\\t",
    " ": "space",
}
CHARACTERS = ("0123456789abcdefghijklmnopqrstuvwxyz"
              "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
              "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\t\n")

def help_and_exit():
    print "./%s MODE" % (sys.argv[0])
    print "This game tests your conversions of ascii to decimal/hex and back"
    print "There are possible modes depending on what you want your quiz to include:"
    print "\t* decimal"
    print "\t* hex"
    sys.exit(1)

def play(mode):
    translations = []
    for character in CHARACTERS:
        if mode == DECIMAL_MODE:
            translation = str(ord(character))
        elif mode == HEX_MODE:
            translation = hex(ord(character))
        else:
            help_and_exit()
        if character in SPECIAL_CASES:
            character = SPECIAL_CASES[character]
        translations.append((character, translation))

    quizzer.play_loop(translations)

def main():
    if len(sys.argv) != 2:
        help_and_exit()
    mode = sys.argv[1]
    play(mode)

if __name__ == "__main__":
    main()
