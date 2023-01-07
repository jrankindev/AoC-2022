### ADVENT OF CODE 2022 DAY 2 ROCK PAPER SCISSORS ###


import helper.helper as helper


# * puzzle part 1
def puzzle_part_1(puzzle_input):
    # var for tracking score across all rounds
    score = 0

    # loop through each round and add to score
    for round in puzzle_input:
        # split round into both parts
        round_choices = round.split()

        # take the ascii value for the choice characters
        # subtract base ascii value to get choices on same 1-3 scale
        opponent_choice_value = ord(round_choices[0]) - 64
        my_choice_value = ord(round_choices[1]) - 87

        # calculate the delta of the round
        outcome = (3 + my_choice_value - opponent_choice_value) % 3

        # 0 = draw, 1 = win, 2 = loss
        match outcome:
            case 0:
                score += my_choice_value + 3
            case 1:
                score += my_choice_value + 6
            case 2:
                score += my_choice_value

    return score


# * puzzle part 2
def puzzle_part_2(puzzle_input):
    # var for tracking score across all rounds
    score = 0

    # loop through each round and add to score
    for round in puzzle_input:
        # split round into both parts
        round_choices = round.split()

        # take the ascii value for the choice characters
        # subtract base ascii value to get choices on 1-3 or 0-2 scale
        opponent_choice_val = ord(round_choices[0]) - 64
        needed_outcome = ord(round_choices[1]) - 88

        # 0 = loss, 1 = draw, 2 = win
        match needed_outcome:
            case 0:
                if opponent_choice_val == 1:
                    score += 3
                else:
                    score += (opponent_choice_val + 2) % 3
            case 1:
                score += opponent_choice_val + 3
            case 2:
                score += (opponent_choice_val % 3) + (needed_outcome * 3) + 1

    return score


# * main function
def main():
    # print title
    helper.print_title("2022", "2", "Rock Paper Scissors")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day02/pi.txt")

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "What would your total score be if everything goes exactly according to your strategy guide? ", answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide? ",
        answer,
    )


if __name__ == "__main__":
    main()
