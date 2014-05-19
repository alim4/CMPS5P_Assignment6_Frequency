__author__ = 'anthonylim'

## Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 4=6
#
# Frequency
# ##

from collections import Counter
from collections import defaultdict

import operator
import re

alphabet = "abcdefghijklmnopqrstuvwxyz"
text_file = open("Output.txt", "w")

def main():
    # input = raw_input("What file would you like to read?\n")
    text_file.write("Anthony Lim\nalim4@ucsc.edu\n\n")
    print ("==================\nJekyll and Hyde\n==================")
    text_file.write("==================\nJekyll and Hyde\n==================\n")
    word_count, letter_count = process_book('stevenson')
    top_thirty(word_count)
    top_letters(letter_count)

    print ("==================\nWar of the Worlds\n==================")
    text_file.write("==================\nWar of the Worlds\n==================")
    word_count, letter_count = process_book('wells')
    top_thirty(word_count)
    top_letters(letter_count)

    print ("==================\nGreat Expectations\n==================")
    text_file.write("==================\nGreat Expectations\n==================\n")
    word_count, letter_count = process_book('dickens')
    top_thirty(word_count)
    top_letters(letter_count)

    print ("###################\nStats for all books\n###################")
    text_file.write("###################\nStats for all books\n###################\n")

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

    text_file.write("\nEOF")
    text_file.close()


def process_book(book_file):
    """

    :param book_file: the name of the file to open
    :return: dictionaries of the words in the book and letters in the book
    """
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
    """
    prints out the most frequent letters and their frequency
    :param letter_count: dictionary of letters in book
    """
    letter_len = 0
    for letter in letter_count.items():
        letter_len += letter[1]

    print "The frequencies for each letter, ordered by frequency (most frequent first)."
    text_file.write("The frequencies for each letter, ordered by frequency (most frequent first).\n")
    print "{0: <9} {1}".format("letter", "frequency")
    text_file.write("{0: <9} {1}\n".format("letter", "frequency"))
    for letter in letter_count.items():
        print "{0: <10} {1:.4}".format(letter[0], float(letter[1]) / letter_len)
        text_file.write("{0: <10} {1:.4}\n".format(letter[0], float(letter[1]) / letter_len))


def top_thirty(word_count):
    # Sort the dictionary based on value
    """
    prints out the top 30 most frequent words and their frequency
    :param word_count: dictionary of words in book
    """
    sorted_book = sorted(word_count.iteritems(), key=operator.itemgetter(1), reverse=True)

    print "The top thirty most frequently used words, ordered by frequency (most frequent first)."
    text_file.write("The top thirty most frequently used words, ordered by frequency (most frequent first).\n")
    print "{0: <12} {1}".format("word", "frequency")
    text_file.write("{0: <12} {1}\n".format("word", "frequency"))
    for i in range(30):
        print "{0: <3}: {1: <8} {2:.4}".format(i + 1,
                                               sorted_book[i][0],
                                               float(sorted_book[i][1]) / len(sorted_book))
        text_file.write("{0: <3}: {1: <8} {2:.4}\n".format(i + 1,
                                               sorted_book[i][0],
                                               float(sorted_book[i][1]) / len(sorted_book)))


def combined_top_thirty(books, letters):
    """
    gets the top 30 words and frequent letters among all the
    books, and prints out the combined result
    :param books: list of books to go through
    :param letters: list of letters to go through
    """
    sorted_list = []
    total_len = 0
    for book in books:
        total_len += len(book)
        sorted_list.append(sorted(book.iteritems(), key=operator.itemgetter(1), reverse=True))

    wordlist = []
    tuplelist = []
    for i in sorted_list:
        for j in range(30):
            wordlist.append(i[j][0])
            tuplelist.append(i[j])

    temp = []
    for i in Counter(wordlist).items():
        # If word occurs in all three dicts
        if i[1] == 3:
            temp.append(i[0])

    # Sum the dictionaries together
    dictsum = sum(
        (Counter(dict(x)) for x in sorted_list),
        Counter()
    )


    result = sorted(dict(dictsum).iteritems(), key=operator.itemgetter(1), reverse=True)

    print "A list of the words in all three top-thirty lists, ordered by overall weighted frequency"
    text_file.write("A list of the words in all three top-thirty lists, ordered by overall weighted frequency\n")
    for i in range(30):
        if result[i][0] in temp:
            print "{0}: {1:<10} {2:.4}".format(i+1, result[i][0], float(result[i][1]) / total_len)
            text_file.write("{0}: {1:<10} {2:.4}\n".format(i+1, result[i][0], float(result[i][1]) / total_len))

    print "The top thirty words across all books, with each book weighted equally"
    text_file.write("The top thirty words across all books, with each book weighted equally\n")
    print "{0: <12} {1}".format("word", "frequency")
    text_file.write("{0: <12} {1}\n".format("word", "frequency"))
    for i in range(30):
        print "{0: <3}: {1: <8} {2:.4}".format(i + 1,
                                               result[i][0],
                                               float(result[i][1]) / total_len)
        text_file.write("{0: <3}: {1: <8} {2:.4}\n".format(i + 1,
                                               result[i][0],
                                               float(result[i][1]) / total_len))

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

    print "The letter frequencies across all books, with each book weighted equally."
    text_file.write("The letter frequencies across all books, with each book weighted equally.\n")
    print "{0: <12} {1}".format("letter", "frequency")
    text_file.write("{0: <12} {1}\n".format("letter", "frequency"))
    for i in range(26):
        print "{0: <3}: {1: <8} {2:.4}".format(i + 1,
                                               letterresult[i][0],
                                               float(letterresult[i][1]) / letter_len)
        text_file.write("{0: <3}: {1: <8} {2:.4}\n".format(i + 1,
                                               letterresult[i][0],
                                               float(letterresult[i][1]) / letter_len))

if __name__ == "__main__":
    main()