### ADVENT OF CODE 2022 DAY 6 TUNING TROUBLE ###


import helper.helper as helper
from collections import Counter


# * solve puzzle
def solve_puzzle(puzzle_input, preamble_length):
    # position tracking var
    position = 0

    # loop through puzzle input searching for a unique string of preamble_length
    while position < len(puzzle_input) - (preamble_length - 1):
        # if Counter sees preamble length of unique chars, then break, else keep going
        if len(Counter(puzzle_input[0 + position:preamble_length + position])) == preamble_length:
            break
        else:
            position += 1

    # return is position offset by preamble length
    return position + preamble_length


# * main function
def main():
    # print title
    helper.print_title("2022", "6", "Tuning Trouble")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day06/pi.txt", 0)

    # solve part 1 and print QA
    answer = solve_puzzle(puzzle_input, 4)
    helper.print_question_answer(
        "How many characters need to be processed before the first start-of-packet marker is detected? ",
        answer,
    )

    # solve part 2 & print QA
    answer = solve_puzzle(puzzle_input, 14)
    helper.print_question_answer(
        "How many characters need to be processed before the first start-of-message marker is detected? ",
        answer,
    )


if __name__ == "__main__":
    main()
