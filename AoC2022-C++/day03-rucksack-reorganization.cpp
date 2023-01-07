// * ADVENT OF CODE 2022 - DAY 3 - RUCKSACK REORGANIZATION *

#include "helper/helper.h"

// * puzzle part 1
int puzzlePart1(std::vector<std::string> puzzleVector) {
    for (std::string line : puzzleVector) {
        std::cout << line << std::endl;
    }

    int answer = 0;
    return answer;
}

// * puzzle part 2
int puzzlePart2(std::vector<std::string> puzzleVector) {
    int answer = 0;
    return answer;
}

// * main function
int main() {
    // print title
    helper::printTitle("2022", "3", "Rucksack Reorganization");

    // load puzzle input
    std::vector<std::string> puzzleVector = helper::loadPuzzleInputStringVec("inputs/day03/pie.txt");

    // solve part 1
    int answer = puzzlePart1(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("\nFind the item type that appears in both compartments of each rucksack.\nWhat is the sum of the priorities of those item types? ", std::to_string(answer));

    // solve part 2
    answer = puzzlePart2(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("Find the item type that corresponds to the badges of each three-Elf group.\nWhat is the sum of the priorities of those item types? ", std::to_string(answer));

    return 0;
}