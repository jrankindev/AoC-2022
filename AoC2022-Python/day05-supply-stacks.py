### ADVENT OF CODE 2022 DAY 5 SUPPLY STACKS ###


import helper.helper as helper
import copy


# * puzzle part 1
def puzzle_part_1(stacks, instructions):
    # parse out command from instructions
    for command in instructions:
        command = command.split()
        total_move, original_stack, destination_stack = int(
            command[1]), int(command[3]) - 1, int(command[5]) - 1

        # loop through total number of moves
        for i in range(0, total_move):
            # get item to move
            item = stacks[original_stack][-1]
            # pop item off original stack
            stacks[original_stack].pop()
            # add item to destination stack
            stacks[destination_stack].append(item)

    # setup answer (last box on each stack)
    answer = ""
    for stack in stacks:
        answer += stack[-1]

    return answer


# * puzzle part 2
def puzzle_part_2(stacks, instructions):
    # parse out command from instructions
    for command in instructions:
        command = command.split()
        total_move, original_stack, destination_stack = int(
            command[1]), int(command[3]) - 1, int(command[5]) - 1

        # get items to move
        items = stacks[original_stack][- total_move:]
        # move items off original stack
        stacks[original_stack] = stacks[original_stack][:- total_move]
        # add items to destination stack
        stacks[destination_stack] = stacks[destination_stack] + items

    # setup answer (last box on each stack)
    answer = ""
    for stack in stacks:
        answer += stack[-1]

    return answer


# * get instructions
def get_instructions(puzzle_input):
    # find where instructions start by looking for blank line
    for i, line in enumerate(puzzle_input):
        if line == "":
            instruction_start = i + 1

    # set instructions
    instructions = puzzle_input[instruction_start:]

    return instructions


# * main function
def main():
    # print title
    helper.print_title("2022", "5", "Supply Stacks")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day05/pi.txt")

    # get puzzle instructions
    instructions = get_instructions(puzzle_input)

    # set stacks
    stacks = [
        ["D", "L", "J", "R", "V", "G", "F"],
        ["T", "P", "M", "B", "V", "H", "J", "S"],
        ["V", "H", "M", "F", "D", "G", "P", "C"],
        ["M", "D", "P", "N", "G", "Q"],
        ["J", "L", "H", "N", "F"],
        ["N", "F", "V", "Q", "D", "G", "T", "Z"],
        ["F", "D", "B", "L"],
        ["M", "J", "B", "S", "V", "D", "N"],
        ["G", "L", "D"],
    ]

    # solve part 1 and print QA
    answer = puzzle_part_1(copy.deepcopy(stacks), instructions)
    helper.print_question_answer(
        "After the rearrangement procedure completes, what crate ends up on top of each stack? ", answer,
    )

    # solve part 2 & print QA
    answer = puzzle_part_2(copy.deepcopy(stacks), instructions)
    helper.print_question_answer(
        "After the rearrangement procedure completes, what crate ends up on top of each stack? ",
        answer,
    )


if __name__ == "__main__":
    main()
