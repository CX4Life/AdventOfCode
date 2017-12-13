"""Day four of the 2017 Advent of Code challenge!"""
__author__ = 'Tim Woods'

INPUT_FILENAME = 'advent4-input.txt'

opened_file = open(INPUT_FILENAME, 'r')


def ensure_all_unique(line):
    """Make sure every word in the phrase occurs no more than once."""
    for word in line:
        if line.count(word) > 1:
            return False
    return True


def line_contains_anagrams(line):
    made_easy = [''.join(sorted(x)) for x in line]
    for word in made_easy:
        if made_easy.count(word) > 1:
            return True
    return False

total = 0

for line in opened_file:
    each_word = line.rstrip().split(' ')
    if not line_contains_anagrams(each_word):
        total += 1

print(total)

