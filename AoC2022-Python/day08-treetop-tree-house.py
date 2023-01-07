### ADVENT OF CODE 2022 DAY 8 TREETOP TREE HOUSE ###


import helper.helper as helper


# * puzzle part 1
def puzzle_part_1(puzzle_input):
    # var to track visible trees
    visible = 0

    # first count total number of trees on perimeter
    perimeter = (len(puzzle_input) * 2) + (len(puzzle_input[0]) * 2) - 4
    visible = perimeter

    # loop through each line and compare tree heights in cardinal directions
    # do not compare perimeter trees as we already know those are visible
    for i, line in enumerate(puzzle_input):
        if i != 0 and i != len(puzzle_input) - 1:
            for x, tree in enumerate(line):
                if x != 0 and x != len(line) - 1:
                    # get tallest tree in cardinal directions as integers
                    up = []
                    above_lines = puzzle_input[:i]
                    for current_line in above_lines:
                        up.append(int(current_line[x]))

                    down = []
                    below_lines = puzzle_input[i + 1:]
                    for current_line in below_lines:
                        down.append(int(current_line[x]))

                    left = [int(n) for n in line[:x]]

                    right = [int(n) for n in line[x + 1:]]

                    # list of all trees to compare against
                    comparison_trees = [int(max(up)),
                                        int(max(down)),
                                        int(max(left)),
                                        int(max(right))]

                    for c_tree in comparison_trees:
                        if int(tree) > c_tree:
                            visible += 1
                            break

    return visible


# * puzzle part 2
def puzzle_part_2(puzzle_input):
    # list for all scenic scores
    scenic_scores = []

    # loop through each line and compare tree heights in cardinal directions
    # find total trees we can see from a given internal tree (not perimeter)
    for i, line in enumerate(puzzle_input):
        if i != 0 and i != len(puzzle_input) - 1:
            for x, tree in enumerate(line):
                if x != 0 and x != len(line) - 1:
                    # get lists of trees in cardinal directions
                    up = []
                    above_lines = puzzle_input[:i]
                    for current_line in above_lines:
                        up.append(int(current_line[x]))
                    up.reverse()

                    down = []
                    below_lines = puzzle_input[i + 1:]
                    for current_line in below_lines:
                        down.append(int(current_line[x]))

                    left = [int(n) for n in line[:x]]
                    left.reverse()

                    right = [int(n) for n in line[x + 1:]]

                    # count visible trees for each cardinal direction
                    up_visible = 0
                    for up_tree in up:
                        if up_tree >= int(tree):
                            up_visible += 1
                            break
                        else:
                            up_visible += 1

                    down_visible = 0
                    for down_tree in down:
                        if down_tree >= int(tree):
                            down_visible += 1
                            break
                        else:
                            down_visible += 1

                    left_visible = 0
                    for left_tree in left:
                        if left_tree >= int(tree):
                            left_visible += 1
                            break
                        else:
                            left_visible += 1

                    right_visible = 0
                    for right_tree in right:
                        if right_tree >= int(tree):
                            right_visible += 1
                            break
                        else:
                            right_visible += 1

                    # calculate scenic score
                    tree_scenic_score = up_visible * down_visible * left_visible * right_visible
                    scenic_scores.append(tree_scenic_score)

    return max(scenic_scores)


# * main function
def main():
    # print title
    helper.print_title("2022", "8", "Treetop Tree House")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day08/pi.txt")

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "Consider your map; how many trees are visible from outside the grid? ",
        answer,
    )

    # solve part 2 & print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "Consider each tree on your map. What is the highest scenic score possible for any tree? ",
        answer,
    )


if __name__ == "__main__":
    main()
