"""Day 5 of the 2017 Advent of Code challenge!"""
__author__ = 'Tim Woods'

INPUT_FILENAME = 'advent5-input.txt'


def array_from_input():
    ret = []
    opened = open(INPUT_FILENAME, 'r')
    for line in opened:
        ret.append(int(line.rstrip()))
    return ret


def go_through_instructions(list_of_inst):
    index = 0
    hops = 0
    while 0 <= index < len(list_of_inst):
        add_to_current_index = list_of_inst[index]
        if add_to_current_index < 3:
            list_of_inst[index] += 1
        else:
            list_of_inst[index] -= 1
        index += add_to_current_index
        hops += 1
    return hops


def main():
    instructions = array_from_input()
    hops = go_through_instructions(instructions)
    print(hops)


if __name__ == '__main__':
    main()