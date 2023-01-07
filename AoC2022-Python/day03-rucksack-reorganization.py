### ADVENT OF CODE 2022 DAY 3 RUCKSACK REORGANIZATION ###


import helper.helper as helper


# * puzzle part 1
def puzzle_part_1(puzzle_input):
    # var to track sum of all priority values
    priority_sum = 0

    # loop through each rucksack contents
    for contents in puzzle_input:

        # get first and second compartments of rucksack
        first = contents[:len(contents)//2]
        second = contents[len(contents)//2:]

        # check if item is in both compartments, if so, set it in priority
        for item in first:
            if item in second:
                priority = item

        # find ascii subtraction value needed based on case
        subtract = 38 if priority.isupper() else 96
        # calculate the priority value
        priority_value = ord(priority) - subtract
        # add current item priority to sum
        priority_sum += priority_value

    return priority_sum


# * puzzle part 2
def puzzle_part_2(puzzle_input):
    # var to track sum of all priority values
    priority_sum = 0

    # divide rucksacks into 3 elves per group
    elf_group = []
    for i, line in enumerate(puzzle_input):
        if i % 3 == 0:
            elf_group.append(puzzle_input[i:i+3])

    # loop through each group
    for group in elf_group:
        # create a set of each group member, this finds common badge item
        badge = set(group[0]) & set(group[1]) & set(group[2])
        # convert badge to string
        badge = str(badge)
        # find ascii subtraction value needed based on case
        subtract = 38 if badge.isupper() else 96
        # calculate the priority value
        priority_value = ord(badge[2]) - subtract
        # add current item priority to sum
        priority_sum += priority_value

    return priority_sum


# * main function
def main():
    # print title
    helper.print_title("2022", "3", "Rucksack Reorganization")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day03/pi.txt")

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types? ", answer,
    )

    # solve part 2 & print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types? ",
        answer,
    )


if __name__ == "__main__":
    main()
