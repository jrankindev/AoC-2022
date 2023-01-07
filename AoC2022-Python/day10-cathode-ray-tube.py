### ADVENT OF CODE 2022 DAY 10 CATHODE RAY TUBE  ###


import helper.helper as helper


# * solve part 1 & 2
def solve_puzzle(puzzle_input):
    # tracking vars
    curr_cycle = 1
    x_reg = {}
    x = 1

    # screen list
    screen = ['.'] * (40 * 6)
    
    # loop over every instruction
    for line in puzzle_input:
        # if instruction is noop, do not change x (cycle length = 1)
        if line == "noop":
            x_reg[curr_cycle] = x
            curr_cycle += 1
        # else run 2 cycles then add value to x (cycle length = 2)
        else:
            _, value = line.split()
            x_reg[curr_cycle] = x
            curr_cycle += 1
            x_reg[curr_cycle] = x
            curr_cycle += 1
            x += int(value)

    # loop on x_reg dict to draw pixels
    row_count = 1
    for key, value in x_reg.items():
        # check if starting a new row on the display
        if row_count > 40:
            row_count = 1
        # if value is +- 1 of row count then draw lit pixel on screen
        if abs(value + 1 - row_count) <= 1:
            screen[key - 1] = '#'
        row_count += 1

    # find signal strengths of target cycles
    targets = [20, 60, 100, 140, 180, 220]
    target_signal_strengths = []
    for target in targets:
        target_signal_strengths.append(x_reg[target] * target)

    # return part 1 and 2 answers
    answer = [sum(target_signal_strengths), screen]
    return answer


# * main function
def main():
    # print title
    helper.print_title("2022", "10", "Cathode-Ray Tube")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day10/pi.txt")

    # solve part 1 and 2 print QA
    answer = solve_puzzle(puzzle_input)

    # print part 1 QA
    helper.print_question_answer(
        "Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths? ", answer[0],
    )

    # print part 2 QA
    helper.print_question_answer(
        "Render the image given by your program. What eight capital letters appear on your CRT? ",
        "",
    )

    # print out screen
    pixel_counter = 0
    for pixel in answer[1]:
        if pixel_counter == 40:
            print("\r")
            pixel_counter = 0
        print(pixel, end="")
        pixel_counter += 1
    print('\n')


if __name__ == "__main__":
    main()
