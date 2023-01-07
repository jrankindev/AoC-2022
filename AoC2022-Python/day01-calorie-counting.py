### ADVENT OF CODE 2022 DAY 1 CALORIE COUNTING ###


import helper.helper as helper


# * puzzle part 1 & 2
def puzzle_part_1_and_2(puzzle_input):
    # append empty line
    puzzle_input.append("")

    # list of elf totals
    totals = []
    # var to track counting per elf
    current_count = 0

    # loop through each line and add current calories to current_count
    # append to totals if blank line (signifies end of specific elf)
    for calorie in puzzle_input:
        if calorie != "":
            current_count += int(calorie)
        else:
            totals.append(current_count)
            current_count = 0

    # sort totals in reverse order
    totals.sort(reverse=True)

    return totals


# * main function
def main():
    # print title
    helper.print_title("2022", "1", "Calorie Counting")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day01/pi.txt")

    # solve part 1 & 2 and print QA
    answer = puzzle_part_1_and_2(puzzle_input)
    helper.print_question_answer(
        "Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? ", answer[
            0],
    )

    # part 2print QA
    helper.print_question_answer(
        "Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total? ",
        sum(answer[:3]),
    )


if __name__ == "__main__":
    main()
