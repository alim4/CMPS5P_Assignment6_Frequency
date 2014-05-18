__author__ = 'anthonylim'

from collections import Counter
from collections import defaultdict

import operator
import re

alphabet = "abcdefghijklmnopqrstuvwxyz"


def main():
    # input = raw_input("What file would you like to read?\n")
    # print ("Jekyll and Hyde")
    # word_count, letter_count = process_book('stevenson')
    # top_thirty(word_count)
    # top_letters(letter_count)
    #
    # print ("War of the Worlds")
    # word_count, letter_count = process_book('wells')
    # top_thirty(word_count)
    # top_letters(letter_count)
    #
    # print ("Great Expectations")
    # word_count, letter_count = process_book('dickens')
    # top_thirty(word_count)
    # top_letters(letter_count)

    word_count_list = []
    letter_count_list = []

    word_count, letter_count = process_book('stevenson')
    word_count_list.append(word_count)
    letter_count_list.append(letter_count)

    word_count, letter_count = process_book('wells')
    word_count_list.append(word_count)
    letter_count_list.append(letter_count)

    word_count, letter_count = process_book('dickens')
    word_count_list.append(word_count)
    letter_count_list.append(letter_count)

    combined_top_thirty(word_count_list, letter_count_list)


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
        book1_str[idx] = re.sub(r'\W+', '', item).lower()

    for i in range(len(book1_str)):
        word_count[book1_str[i]] += 1

    #print sorted_book
    # endregion

    # ///

    # region begin letter count
    for i in read_data:
        if i in alphabet:
            letter_count[i] += 1
    # endregion

    return word_count, letter_count


def top_letters(letter_count):
    print ("")
    print "{0: <9} {1}".format("letter", "frequency")
    for letter in letter_count.items():
        print "{0: <10} {1}".format(letter[0], letter[1])


def top_thirty(word_count):
    # Sort the dictionary based on value
    sorted_book = sorted(word_count.iteritems(), key=operator.itemgetter(1), reverse=True)

    print "{0: <12} {1}".format("word", "frequency")
    for i in range(30):
        print "{0: <3}: {1: <8} {2:.4}".format(i + 1,
                                               sorted_book[i][0],
                                               float(sorted_book[i][1]) / len(sorted_book))


def combined_top_thirty(books, letters):
    sorted_list = []
    total_len = 0
    for book in books:
        total_len += len(book)
        sorted_list.append(book)

    # Sum the dictionaries together
    dictsum = sum(
        (Counter(dict(x)) for x in sorted_list),
        Counter()
    )

    result = sorted(dict(dictsum).iteritems(), key=operator.itemgetter(1), reverse=True)

    print "{0: <12} {1}".format("word", "frequency")
    for i in range(30):
        print "{0: <3}: {1: <8} {2:.4}".format(i + 1,
                                               result[i][0],
                                               float(result[i][1]) / total_len)

    # For letters
    letter_list = []
    letter_len = 0

    for letter in letters:
        letter_list.append(letter)
        for i in letter.values():
            letter_len += i

    # Sum the letter dictionaries together
    letterdictsum = sum(
        (Counter(dict(x)) for x in letter_list),
        Counter()
    )

    letterresult = sorted(dict(letterdictsum).iteritems(), key=operator.itemgetter(1), reverse=True)

    print "{0: <12} {1}".format("letter", "frequency")
    for i in range(26):
        print "{0: <3}: {1: <8} {2:.4}".format(i + 1,
                                               letterresult[i][0],
                                               float(letterresult[i][1]) / letter_len)


main()