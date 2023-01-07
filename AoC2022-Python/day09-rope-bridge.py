### ADVENT OF CODE 2022 DAY 9 ROPE BRIDGE ###


import helper.helper as helper
import copy
import numpy as np


# * class for knot objects to track coordinates
class Knot:
    def __init__(self, x, y):
       self.x = x
       self.y = y
    def __str__(self):
        return f"{self.x},{self.y}"
    visited_coords = []


# * solve puzzle part 1 & 2
def solve_puzzle(puzzle_input, num_knots):
    # create list of knots based on num_knots with overlapping 0,0 coordinates
    knot_list = []
    for _ in range(num_knots):
        knot_list.append(Knot(0,0))

    # clear visited coords list for each knot
    # append starter coords
    for knot in knot_list:
        knot.visited_coords.clear()
        knot.visited_coords.append([knot.x, knot.y])

    # loop through each instruction from puzzle input
    for instruction in puzzle_input:
        print(f"### Performing {instruction}")
        # split out instructions
        direction, distance = instruction.split()
        distance = int(distance)

        # step through each increment of distance
        for _ in range(distance):
            # move head knot according to instructions
            # tail must move with head if it would be further than 1 move away to next knot in any direction
            # print(f"-> HEAD Moving from {knot_list[0]}")
            og_head_pos = knot_list[0]

            match direction:
                case "U": knot_list[0].y += 1
                case "D": knot_list[0].y -= 1
                case "L": knot_list[0].x -= 1
                case "R": knot_list[0].x += 1

            # print(f"-> HEAD moved to {knot_list[0]}")
            new_head_pos = knot_list[0]

            print(f"HS = {og_head_pos} | HF = {new_head_pos}")

            # add new head coordinates to visited list
            # print(f"Appending to head visited list: {[knot_list[0].x, knot_list[0].y]}")
            knot_list[0].visited_coords.append([knot_list[0].x, knot_list[0].y])
            print(knot_list[0].visited_coords)
            # print(knot_list[0].visited_coords)
            # visited_coords_head.append([head.x, head.y])
            #print(knot_list[0].visited_coords)
            #print(len(knot_list[0].visited_coords))

            # loop through each knot in knot list and move each accordinly
            for i in range(1, len(knot_list)):
                # check if next knot needs to move
                move = check_knot_move(knot_list[0], knot_list[i])

                # print(f"-> Knot {i} needs to move: {move}\n")
                og_tail_pos = knot_list[i]


                # if move is True, then move to last head position
                if move:
                    # print(f"---> TAIL {i} Moving from {knot_list[i]}")
                    head_knot_visited_coords = copy.deepcopy(knot_list[0].visited_coords)
                    # knot_list[i].x = knot_list[0].visited_coords[-2][0]
                    knot_list[i].x = head_knot_visited_coords[-2][0]
                    # knot_list[i].y = knot_list[0].visited_coords[-2][1]
                    knot_list[i].x = head_knot_visited_coords[-2][1]
                    head_knot_visited_coords.clear()
                    knot_list[i].visited_coords.append([knot_list[i].x, knot_list[i].y])
                    # visited_coords_tail.append(f"{tail.x}, {tail.y}")
                    # print(f"---> TAIL {i} moved to {knot_list[i]}\n")
                #print(f"---> Knot {i} Visited Coords: {knot_list[i].visited_coords}")
                new_tail_pos = knot_list[i]
                print(f"Move = {move}\nTS = {og_tail_pos} | TF = {new_tail_pos}\n")
        print(f"### Done | F = {knot_list[0]} and {knot_list[1]}")
        print("\n\n")

    for i, knot in enumerate(knot_list):
        print(f"Knot({i}) Visited List:\n{knot.visited_coords}")

    unique_tail_coords = set()

    return len(unique_tail_coords)


# * calculate distance between two points
def check_knot_move(first_knot, second_knot):
    # get distance between both coordinates    √[(x₂ - x₁)² + (y₂ - y₁)²]
    distance = np.sqrt((np.square((second_knot.x - first_knot.x)) + np.square((second_knot.y - first_knot.y))))
    print(f"Dist = {round(distance, 1)}")

    # if the distance is 2 then tail must move on cardinal direction
    move = True if distance >= 2 else False

    return move


# * main function
def main():
    # print title
    helper.print_title("2022", "9", "Rope Bridge")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day09/pie.txt")

    # solve part 1 and print QA
    answer = solve_puzzle(puzzle_input, 2)
    helper.print_question_answer(
        "Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once? ",
        answer,
    )

    # solve part 2 & print QA
    # answer = solve_puzzle(puzzle_input, 10)
    helper.print_question_answer(
        "Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once? ",
        answer,
    )


if __name__ == "__main__":
    main()
