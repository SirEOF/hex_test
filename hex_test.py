#!/usr/bin/env python
import quizzer

import sys

DOMAINS = [
        range(16),
        range(16) + [(i+1) * 10 for i in range(25)] + [256],
        range(256),
        range(65536),
        ]


def help_and_exit():
    print "./%s DIFFICULTY" % (sys.argv[0])
    print "This game tests your conversions of decimal to hex and back"
    print "Difficulties include quizzing on the following sets:"
    print "\t0 => range(16)"
    print "\t1 => range(16) + [(i+1) * 10 for i in range(25)] + [256]"
    print "\t2 => range(256)"
    print "\t3 => range(65536)"
    sys.exit(1)

def play(difficulty):
    domain = DOMAINS[difficulty]
    translations = []
    for decimal_value in domain:
        str_value = str(decimal_value).strip()
        hex_value = hex(decimal_value).strip()
        translations.append((str_value, hex_value))

    quizzer.play_loop(translations)

def main():
    if len(sys.argv) != 2:
        help_and_exit()
    difficulty = int(sys.argv[1])
    play(difficulty)

if __name__ == "__main__":
    main()
