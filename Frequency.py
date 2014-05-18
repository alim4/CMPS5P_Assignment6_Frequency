__author__ = 'anthonylim'

from collections import Counter
from collections import defaultdict

import operator
import re

alphabet = "abcdefghijklmnopqrstuvwxyz"

def main():
    # input = raw_input("What file would you like to read?\n")
    process_book('greatexpectations')

def process_book(book_file):
    word_count = defaultdict(int)
    letter_count = defaultdict(int)

    with open("{0}.txt".format(book_file), 'r') as f:
        read_data = f.read()

    # region begin word count
    # Split words into individual elements
    book1_str = read_data.split()

    # Strip elements of non-alpha characters
    # Uses regular expressions
    for idx, item in enumerate(book1_str):
        book1_str[idx] = re.sub(r'\W+', '', item)

    for i in range(1000):
        word_count[book1_str[i]] += 1

    # Sort the dictionary based on value
    sorted_book = sorted(word_count.iteritems(), key=operator.itemgetter(1), reverse=True)

    #print sorted_book
    # endregion
    # ///
    # region begin letter count
    for i in read_data:
        if i in alphabet:
            letter_count[i] += 1

    for i in letter_count.items():
        print "{0}: {1}".format(i[0], i[1])
    print sorted_book
    # endregion

main()