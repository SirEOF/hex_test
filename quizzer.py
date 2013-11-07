"""
quizzer.py

Logic to run quiz games independently of the actual quiz content.
"""
import random
import sys

def play_loop(translations, start_set_size=6):
    """Plays a quiz game.

    Arguments:
        translations: A list of pairs, where items in a pair correspond to each
            other as each other's quiz answer.

    Does not return.
    """
    correctness_table = {}
    for (item_one, item_two) in translations:
        correctness_table[item_one] = item_two
        correctness_table[item_two] = item_one

    # Start the game out with only three possibilities
    random.shuffle(translations)
    possibilities = [item for pair in translations for item in pair]
    current_set = possibilities[0:start_set_size]

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

        if ((score > weight * 0.8)
           and (len(current_set) < len(possibilities) - 1)):
            current_pointer += 1
            current_set.append(possibilities[current_pointer])
            score = 0
            correctness = []
