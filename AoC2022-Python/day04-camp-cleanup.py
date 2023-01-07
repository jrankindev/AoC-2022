### ADVENT OF CODE 2022 DAY 4 CAMP CLEANUP ###


import helper.helper as helper


# * puzzle part 1
def puzzle_part_1(puzzle_input):
    # var to track overlapping elf work
    overlaps = 0

    # loop through each pair of elves
    for pairs in puzzle_input:
        # split into each elf
        elves = pairs.split(",")

        # create a set from the first elf range
        range_values = elves[0].split("-")
        first_elf = set(range(int(range_values[0]), int(range_values[1]) + 1))

        # create a set from the second elf range
        range_values = elves[1].split("-")
        second_elf = set(range(int(range_values[0]), int(range_values[1]) + 1))

        # find intersection between both elves
        elf_intersect = first_elf.intersection(second_elf)

        # if either of the elves' ranges are the intersect, then there is a full overlap
        if elf_intersect == first_elf or elf_intersect == second_elf:
            overlaps += 1

    return overlaps


# * puzzle part 2
def puzzle_part_2(puzzle_input):
    # var to track overlapping elf work
    overlaps = 0

    # loop through each pair of elves
    for pairs in puzzle_input:
        # split into each elf
        elves = pairs.split(",")

        # create a set from the first elf range
        range_values = elves[0].split("-")
        first_elf = set(range(int(range_values[0]), int(range_values[1]) + 1))

        # create a set from the second elf range
        range_values = elves[1].split("-")
        second_elf = set(range(int(range_values[0]), int(range_values[1]) + 1))

        # find intersection between both elves
        elf_intersect = first_elf.intersection(second_elf)

        # if any intersect was found at all, then there is overlap
        if len(elf_intersect) != 0:
            overlaps += 1

    return overlaps


# * main function
def main():
    # print title
    helper.print_title("2022", "4", "Camp Cleanup")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day04/pi.txt")

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "In how many assignment pairs does one range fully contain the other? ", answer,
    )

    # solve part 2 & print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "In how many assignment pairs do the ranges overlap? ",
        answer,
    )


if __name__ == "__main__":
    main()
