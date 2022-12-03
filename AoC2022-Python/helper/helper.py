### ADVENT OF CODE HELPER LIB ###

import os

## * input loader
# return_type 1 is to load into list, otherwise load in variable
# line_type 1 is to load each line as an string, otherwise load as int
def load_puzzle_input(puzzle_file_input: str, return_type=1, line_type=1):
    if return_type:
        puzzle_input = []
        with open(puzzle_file_input, encoding="UTF-8") as file:
            for line in file:
                if line_type:
                    line = line.strip()
                else:
                    line = int(line.strip())
                puzzle_input.append(line)
        return puzzle_input
    else:
        with open(puzzle_file_input, encoding="UTF-8") as file:
            puzzle_input = file.read()
        return puzzle_input


## * title printer
def print_title(year: str, day: str, title: str):

    # clear screen for readability (check to see if windows - nt)
    os.system("cls" if os.name == "nt" else "clear")

    color_header = "\033[95m" + "\033[1m"
    color_clear = "\033[0m"
    print(f"{color_header} Advent of Code {year} ")
    print(f" Day {day} - {title} \n{color_clear}")


## * question and answer printer
def print_question_answer(question: str, answer: str):
    color_question = "\033[94m"
    color_answer = "\033[92m"
    color_clear = "\033[0m"
    print(
        f"{color_question}{question}", end="",
    )
    print(f"{color_answer} {str(answer)} \n {color_clear}")
