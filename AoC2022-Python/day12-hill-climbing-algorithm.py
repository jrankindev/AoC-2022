### ADVENT OF CODE 2022 DAY 12 HILL CLIMBING ALGORITHM ###


import helper.helper as helper
import numpy as np


# * puzzle part 1
def puzzle_part_1(height_map):
    # get coordinates of start and end points
    start_coords = np.where(height_map == 'S')
    end_coords = np.where(height_map == 'E')

    find_path(height_map, start_coords, end_coords)

    return 0


# * puzzle part 2
def puzzle_part_2(puzzle_input):
    return 0


# * convert character in height map to height integer value
def char_to_height(char):
    if char == 'S':
        return 0
    elif char == 'E':
        return 27
    else:
        return ord(char) -96


# * find path from start coord to end coords in height_map
def find_path(height_map, start_coords, end_coords):
    # break x and y variables out of passed coords
    start_x, start_y = start_coords[0][0], start_coords[1][0]
    end_x, end_y = end_coords[0][0], end_coords[1][0]

    # vars for tracking current coordinates on heightmap
    current_x, current_y = start_x, start_y

    print(height_map)
    print("\nstart =", start_x, start_y)
    print("end =", end_x, end_y)
    print("current =", current_x, current_y)
    print("")

    move_counter = 0
    while current_x != end_x or current_y != end_y:
        # get current coord height value
        current_height = char_to_height(height_map[current_x, current_y])
        print("current height =", current_height)

        # get directional height differences
        up = [[]]
        right = [char_to_height(height_map[current_x +1, current_y]), current_x +1, current_y]
        down = [char_to_height(height_map[current_x, current_y + 1]), current_x, current_y + 1]
        left = [[]]
        height_diff = [up, right, down, left]

        for direction in height_diff:
            if direction[0] == 1:
                print(direction)

        print(height_diff)
        
        current_x = end_x
        current_y = end_y




# * main function
def main():
    # print title
    helper.print_title("2022", "12", "Hill Climbing Algorithm")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day12/pie.txt")

    # store puzzle input in 2D list for heightmap then convert to numpy array
    height_map = []
    for row in puzzle_input:
        row_list = [char for char in row]
        height_map.append(row_list)
    height_map = np.array(height_map, dtype=str)

    # solve part 1 & print QA
    answer = puzzle_part_1(height_map)
    helper.print_question_answer(
        "What is the fewest steps required to move from your current position to the location that should get the best signal? ",
        answer,
    )

    # solve part 2 & print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "??? ",
        answer,
    )


if __name__ == "__main__":
    main()
