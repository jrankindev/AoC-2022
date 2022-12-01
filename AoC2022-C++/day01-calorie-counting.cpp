// * ADVENT OF CODE 2022 - DAY 1 - CALORIE COUNTING *

#include <bits/stdc++.h>

#include "helper/helper.h"

// * puzzle part 1 and 2 function
std::vector<int> puzzlePart1and2(std::vector<std::string> puzzleVector) {
    // vector to track total calories per elf
    std::vector<int> totals;

    // loop through all of the strings in the puzzle vector tracking totals along the way
    // everytime there is a blank line, push back current total to totals vector
    // check if last line, if so, push total
    int currentTotal = 0;
    for (int i = 0; i < puzzleVector.size(); i++) {
        if (puzzleVector[i] == "\r") {
            totals.push_back(currentTotal);
            currentTotal = 0;
        } else if (i == puzzleVector.size() - 1) {
            currentTotal += stoi(puzzleVector[i]);
            totals.push_back(currentTotal);
        } else {
            currentTotal += stoi(puzzleVector[i]);
        }
    }

    // sort totals
    sort(totals.begin(), totals.end(), std::greater<int>());

    // setup answer vector
    std::vector<int> answer(2);
    answer[0] = totals[0];
    answer[1] = totals[0] + totals[1] + totals[2];

    return answer;
}

// * main function
int main() {
    // print title
    helper::printTitle("2022", "1", "Calorie Counting");

    // load puzzle input
    std::vector<std::string> puzzleVector = helper::loadPuzzleInputStringVec("inputs/day01/pi.txt");

    // solve part 1
    std::vector<int> answer = puzzlePart1and2(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("\nFind the Elf carrying the most Calories. How many total Calories is that Elf carrying? ", std::to_string(answer[0]));

    // print question and answer
    helper::printQuestionAnswer("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total? ", std::to_string(answer[1]));

    return 0;
}