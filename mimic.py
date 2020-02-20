#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string "" is what comes before
the first word in the file.  This will be the seed string.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

# import random
import sys
import random

__author__ = """https: // thispointer.com/
                python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
                https://stackoverflow.com/questions/27155819/delete-a-key-and-value-from-an-ordereddict
                Asked my bro for help on adding to the value list for each key
                Asked Jake Hershey for help on print_mimic"""

time_comment = 'Assessment took around 1-3 hours to complete'


def create_mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    with open(filename, "r") as file:
        data = file.read()
        words_data = data.split()
        mimic_dict = {}
        for index, word in enumerate(words_data):
            if index == 0:
                mimic_dict.update({"": [word]})
                mimic_dict[word] = [words_data[index+1]]
            elif word in mimic_dict:
                mimic_dict[word].append(words_data[index+1])
            else:
                mimic_dict.update(
                    {words_data[index]: words_data[index+1:index+2]})
    return mimic_dict


def print_mimic(mimic_dict, start_word):
    """Given a previously compiled mimic_dict and start_word, prints
        200 random words:
        - Print the start_word
        - Lookup the start_word in your mimic_dict and get it's next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    count = 200
    while count:
        print(start_word)
        next_word = mimic_dict.get(start_word)
        if not next_word:
            next_word = mimic_dict[""]
        start_word = random.choice(next_word)
        count -= 1


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
