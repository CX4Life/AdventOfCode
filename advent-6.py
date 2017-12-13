"""Day 6 of the 2017 Advent of Code challenge!"""
__author__ = 'Tim Woods'

test_input = [0, 2, 7, 0]
actual_input = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]


def count_until_pattern_recurs(memory_banks):
    seen_before = [tuple(memory_banks)]

    def index_of_max():
        return memory_banks.index(max(memory_banks))

    def distribute(index):
        blocks_to_distribute = memory_banks[index]
        memory_banks[index] = 0
        while blocks_to_distribute:
            index += 1
            where_to_add = index % len(memory_banks)
            memory_banks[where_to_add] += 1
            blocks_to_distribute -= 1
        seen_before.append(tuple(memory_banks))

    def all_unique():
        seen = set()
        for elem in seen_before:
            if elem in seen:
                return False
            seen.add(elem)
        return True

    while all_unique():
        starting_point = index_of_max()
        distribute(starting_point)

    return seen_before

def run_test_input():
    """Make sure that function works on the test input provided"""
    seen = count_until_pattern_recurs(test_input)
    print(find_gap(seen))


def find_gap(seen_vals):
    for elem in seen_vals:
        if seen_vals.count(elem) > 1:
            first_index = seen_vals.index(elem)
            seen_vals[first_index] = (0)
            second_index = seen_vals.index(elem)
            return second_index - first_index


def main():
    run_test_input()
    really_seen = count_until_pattern_recurs(actual_input)
    print(find_gap(really_seen))

if __name__ == '__main__':
    main()
