#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
import sys
__author__ = "Michael Trepanier"
"Had help from Greg Spurgeon and Joseph Hafed"


def create_word_dict(filename):
    word_dict = {}
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


"""Returns a word/count dict for the given file."""


def print_words(filename):
    d = create_word_dict(filename)
    for key, value in sorted(d.items()):
        print(key, ":", value,)
    """Prints one per line '<word> : <count>', sorted
                # word : count alphabetical order
                by word for the given file."""


def print_top(filename):
    d = create_word_dict(filename)
    sorted_d = sorted(d.items(), key=lambda a: a[1], reverse=True)
    for i in sorted_d[0:20]:
        print(i[0], ":", i[1])


"""Prints the top count listing for the given file."""
# show top 20 sorted by the highest count
# Your code here


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
