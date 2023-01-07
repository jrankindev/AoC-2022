### ADVENT OF CODE 2022 DAY 7 NO SPACE LEFT ON DEVICE ###


import helper.helper as helper


# * puzzle part 1 & 2
def puzzle_part_1_and_2(puzzle_input):
    # list for answers
    answer = []

    # var for tracking current path
    current_path = "root"

    # var for tracking file info
    file_info = []

    # var for tracking the unique directories
    directories = set()

    # add root path to directories list
    directories.add(current_path)

    # loop through puzzle input skipping first line
    for i in range(1, len(puzzle_input)):
        # split out portions of the input for command parsing
        cmd = puzzle_input[i].split()
        
        # parse commands
        if cmd[0] == "dir":
            directories.add(current_path + "/" + cmd[1])
        elif cmd[1] == "ls": continue
        elif cmd[1] == "cd":
            # check for cd direction
            if cmd[2] != "..":
                # add directory to current path
                current_path = current_path + "/" + cmd[2]
            else:
                # remove last directory from current path
                slash_position = current_path.rindex("/")
                current_path = current_path[:slash_position]
        else:
            current_file = [cmd[1], cmd[0], current_path]
            file_info.append(current_file)

    # loop through directories and add up all file values to get directory total size
    # store all directory sizes in a list that are at most 100,000 in size
    # also store all sizes in a list for part 2
    sizes_under_100k = []
    all_sizes = []
    for dir in directories:
        size_counter = 0
        for files in file_info:
            if files[2] == dir or (files[2].startswith(dir) and files[2] != dir):
                size_counter = size_counter + int(files[1])
        if size_counter <= 100000:
            sizes_under_100k.append(size_counter)
        all_sizes.append(size_counter)

    # sum of all sizes under 100k is answer to part 1
    answer.append(sum(sizes_under_100k))

    # * solve part 2
    # sort size values
    all_sizes.sort(reverse=True)

    # find minimum size needed to delete
    total_filesystem_size = 70000000
    unused_space_needed = 30000000
    current_used_space = all_sizes[0]
    available_space = total_filesystem_size - current_used_space
    minimum_amount_to_delete = unused_space_needed - available_space

    # loop through all sizes until finding the smallest value that meets min to delete
    for i in range(len(all_sizes)):
        if all_sizes[i] < minimum_amount_to_delete:
            # previous element is answer to part 2
            answer.append(all_sizes[i - 1])
            break

    return answer


# * main function
def main():
    # print title
    helper.print_title("2022", "7", "No Space Left On Device")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day07/pi.txt")

    # solve part 1 & 2
    answer = puzzle_part_1_and_2(puzzle_input)

    # part 1 print QA
    helper.print_question_answer(
        "Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories? ",
        answer[0],
    )

    # part 2 print QA
    helper.print_question_answer(
        "Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory? ",
        answer[1],
    )


if __name__ == "__main__":
    main()
