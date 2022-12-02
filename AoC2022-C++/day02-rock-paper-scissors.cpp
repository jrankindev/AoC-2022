// * ADVENT OF CODE 2022 - DAY 2 - ROCK PAPER SCISSORS *

#include "helper/helper.h"

// * puzzle part 1
int puzzlePart1(std::vector<std::string> puzzleVector) {
    // var for tracking score across all rounds
    int score = 0;

    // loop through each round and add to score
    for (std::string round : puzzleVector) {
        // take the ascii value for the choice characters
        // subtract base ascii value to get choices on same 1-3 scale
        int oppChoiceVal = round.at(0) - 64;
        int myChoiceVal = round.at(2) - 87;

        // calculate delta of round
        int outcome = (3 + myChoiceVal - oppChoiceVal) % 3;

        // 0 is draw, 1 is win, 2 is loss
        switch (outcome) {
            case 0:
                score += myChoiceVal + 3;
                break;
            case 1:
                score += myChoiceVal + 6;
                break;
            case 2:
                score += myChoiceVal;
                break;
        }
    }

    return score;
}

// * puzzle part 2
int puzzlePart2(std::vector<std::string> puzzleVector) {
    // var for tracking score across all rounds
    int score = 0;

    // loop through each round and add to score
    for (std::string round : puzzleVector) {
        // take the ascii value for the choice/needed outcome characters
        // subtract base ascii value to get choices on 1-3 or 0-2 scale
        int oppChoiceVal = round.at(0) - 64;
        int neededOutcome = round.at(2) - 88;

        // 0 is lose, 1 is draw, 2 is win
        switch (neededOutcome) {
            case 0:
                if (oppChoiceVal == 1) {
                    score += 3;
                } else {
                    score += (oppChoiceVal + 2) % 3;
                }
                break;
            case 1:
                score += oppChoiceVal + 3;
                break;
            case 2:
                score += (oppChoiceVal % 3) + (neededOutcome * 3) + 1;
                break;
        }
    }

    return score;
}

// * main function
int main() {
    // print title
    helper::printTitle("2022", "2", "Rock Paper Scissors");

    // load puzzle input
    std::vector<std::string> puzzleVector = helper::loadPuzzleInputStringVec("inputs/day02/pi.txt");

    // solve part 1
    int answer = puzzlePart1(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("\nWhat would your total score be if everything goes exactly according to your strategy guide? ", std::to_string(answer));

    // solve part 2
    answer = puzzlePart2(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide? ", std::to_string(answer));

    return 0;
}