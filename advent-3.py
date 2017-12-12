def m(to_move):
    return int(to_move / 2)

class pos:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y


all_spots = {}

origin = pos(1, 0, 0)

all_spots[origin.val] = origin
to_move = 2


def move_left(spaces, starting_pos):
    start_val = starting_pos.val
    start_x = starting_pos.x
    start_y = starting_pos.y
    for i in range(spaces):
        start_val += 1
        start_x -= 1
        temp = pos(start_val, start_x, start_y)
        all_spots[start_val] = temp


def move_right(spaces, starting_pos):
    start_val = starting_pos.val
    start_x = starting_pos.x
    start_y = starting_pos.y
    for i in range(spaces):
        start_val += 1
        start_x += 1
        temp = pos(start_val, start_x, start_y)
        all_spots[start_val] = temp


def move_up(spaces, starting_pos):
    start_val = starting_pos.val
    start_x = starting_pos.x
    start_y = starting_pos.y
    for i in range(spaces):
        start_val += 1
        start_y += 1
        temp = pos(start_val, start_x, start_y)
        all_spots[start_val] = temp


def move_down(spaces, starting_pos):
    start_val = starting_pos.val
    start_x = starting_pos.x
    start_y = starting_pos.y
    for i in range(spaces):
        start_val += 1
        start_y -= 1
        temp = pos(start_val, start_x, start_y)
        all_spots[start_val] = temp

def main():
    """Make a big old thing of numbers"""
    i = 1
    while(max(all_spots.keys()) < 277678):
        move_right(i, all_spots[max(all_spots.keys())])
        move_up(i, all_spots[max(all_spots.keys())])
        move_left(i+1, all_spots[max(all_spots.keys())])
        move_down(i+1, all_spots[max(all_spots.keys())])
        i += 2

    print(all_spots[277678].x, all_spots[277678].y)

if __name__ == '__main__':
    main()
