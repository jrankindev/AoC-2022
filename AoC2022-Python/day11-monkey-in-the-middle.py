### ADVENT OF CODE 2022 DAY 11 MONKEY IN THE MIDDLE ###


import helper.helper as helper
import re
import math
import copy


# * class for monkey objects
class Monkey:
    def __init__(self, monkey_id, items, operation, divisible_by, true_throw_id, false_throw_id) -> None:
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.true_throw_id = true_throw_id
        self.false_throw_id = false_throw_id

    def __str__(self) -> str:
        return f"monkey_id = {self.monkey_id}, items = {self.items}, operation = {self.operation}, divisible_by = {self.divisible_by}, true_throw_id = {self.true_throw_id}, false_throw_id = {self.false_throw_id}, total inspections = {self.total_inspections}"

    total_inspections = 0


# * puzzle part 1
def puzzle_part_1(puzzle_input, rounds, manage_worry):
    # list to store monkey objects in
    monkey_objs = []

    # parse each monkey from the puzzle input into a monkey object
    monkeys = puzzle_input.split("\n\n")
    for monkey in monkeys:
        monkey_list = monkey.split("\n")
        monkey_id = int(re.findall(r'\d+', monkey_list[0])[0])
        str_items = re.findall(r'\d+', monkey_list[1])
        items = list(map(int, str_items))
        operation = monkey_list[2][23:]
        divisible_by = int(re.findall(r'\d+', monkey_list[3])[0])
        true_throw_id = int(re.findall(r'\d+', monkey_list[4])[0])
        false_throw_id = int(re.findall(r'\d+', monkey_list[5])[0])

        new_monkey = Monkey(monkey_id, items, operation, divisible_by, true_throw_id, false_throw_id)
        monkey_objs.append(new_monkey)

    for monkey in monkey_objs:
        print(monkey)

    # loop through rounds
    for round_num in range(1, rounds + 1):
        print("Round =", round_num)
        for monkey in monkey_objs:
            # print("\nRound =", round_num, "Monkey =", monkey.monkey_id)

            # create a items list copy
            new_items_list = copy.deepcopy(monkey.items)
            
            # update total inspections
            monkey.total_inspections += len(monkey.items)

            #for i, item in enumerate(new_items_list):
            for i in range(0, len(monkey.items)):

                # print("-> CHECKING ITEM =", new_items_list[i], ", ID =", i)

                # perform operation to get new worry value
                operation = monkey.operation.split()
                # print(operation, new_items_list[i], end="")
                if operation[0] == "*":
                    if operation[1] == "old":
                        new_items_list[i] = new_items_list[i] * new_items_list[i]
                    else:
                        new_items_list[i] = new_items_list[i] * int(operation[1])
                else:
                    if operation[1] == "old":
                        new_items_list[i] = new_items_list[i] + new_items_list[i]
                    else:
                        new_items_list[i] = new_items_list[i] + int(operation[1])
                # print(", NEW VAL =", new_items_list[i])

                # after item inspection, if managing worry levels, drop worry level
                if manage_worry:
                    new_items_list[i] = math.floor(new_items_list[i] // 3)
                    # print("FINAL ITEM VAL =", new_items_list[i])

                # perform test
                divisible = True if new_items_list[i] % monkey.divisible_by == 0 else False
                # print("DIVISIBLE =", divisible, ", monkey.divisible_by =", monkey.divisible_by, ", new_items_list[i] =", new_items_list[i], ", TEST_VAL =")

                # throw item to other monkey based on divisible test
                if divisible:
                    # print("TRUE THROW TO =", monkey_objs[monkey.true_throw_id].monkey_id)
                    monkey_objs[monkey.true_throw_id].items.append(new_items_list[i])
                else:
                    # print("FALSE THROW TO =", monkey_objs[monkey.false_throw_id].monkey_id)
                    monkey_objs[monkey.false_throw_id].items.append(new_items_list[i])

            # clear item list for current monkey
            # print("ITEMS BEFORE CLEAR =", monkey.items)
            monkey.items.clear()
            # print("ITEMS AFTER CLEAR =", monkey.items)

        # print(f"\n### STATS AFTER ROUND {round_num}###")
        # for monkey in monkey_objs:
            # print(monkey)

        # print("\n")

    total_inspections = []
    for monkey in monkey_objs:
        total_inspections.append(monkey.total_inspections)
        print(monkey.total_inspections)

    total_inspections.sort(reverse=True)

    print(total_inspections)

    return total_inspections[0] * total_inspections[1]


# * puzzle part 2
def puzzle_part_2(puzzle_input):
    answer = 0
    return answer


# * main function
def main():
    # print title
    helper.print_title("2022", "11", "Monkey in the Middle")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day11/pie.txt", 0)

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input, 1000, False)
    helper.print_question_answer(
        "Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. " +
        "What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans? ",
        answer,
    )

    # solve part 2 & print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "??? ",
        answer,
    )


if __name__ == "__main__":
    main()
