#!/usr/bin/env python
import random
import sys

DOMAINS = [
        range(16),
        range(16) + [(i+1) * 10 for i in range(25)] + [256],
        range(256),
        range(65536),
        ]


def help_and_exit():
    print "./%s DIFFICULTY [TIMEOUT]" % (sys.argv[0])
    print "This game tests your conversions of decimal to hex and back"
    print "Difficulties include quizzing on the following sets:"
    print "\t0 => range(16)"
    print "\t1 => range(16) + [(i+1) * 10 for i in range(25)] + [256]"
    print "\t2 => range(256)"
    print "\t3 => range(65536)"
    print "Timeout corresponds to how much time you get per question."
    print "This is optional, and by default you are given infinite time."
    sys.exit(1)

def play_loop(difficulty):
    domain = DOMAINS[difficulty]
    correctness_table = {}
    for decimal_value in domain:
        str_value = str(decimal_value).strip()
        hex_value = hex(decimal_value).strip()
        correctness_table[hex_value] = str_value
        correctness_table[str_value] = hex_value

    possibilities = correctness_table.keys()

    # Start the game out with only three possibilities
    random.shuffle(possibilities)
    current_pointer = 3
    current_set = possibilities[0:current_pointer]

    # TODO: Implement timeout
    # TODO: Some sort of weighted random
    # print correctness_table
    score = 0
    weight = 5
    correctness = []
    force_option = None
    while True:
        # print current_set
        if force_option:
            quiz = force_option
            force_option = None
        else:
            quiz = random.choice(current_set)

        sys.stdout.write("Convert %s=" % quiz)
        answer = raw_input().strip()
        if correctness_table[quiz] == answer:
            print "Correct!"
            correctness.append(True)
        else:
            print "Wrong. Answer=%s" % correctness_table[quiz]
            correctness.append(False)
        print ""

        score += correctness[-1]
        if len(correctness) > weight:
            score -= correctness[0]
            correctness = correctness[1:]

        if (score > weight * 0.8) and (len(current_set) < len(possibilities)):
            current_pointer += 1
            current_set.append(possibilities[current_pointer])
            score = 0
            correctness = []

def main():
    if len(sys.argv) != 2:
        help_and_exit()
    difficulty = int(sys.argv[1])
    play_loop(difficulty)

if __name__ == "__main__":
    main()
