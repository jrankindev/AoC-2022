// ADVENT OF CODE HELPER

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

class helper {
   public:
    // * input loader int vector
    static std::vector<int> loadPuzzleInputVec(std::string puzzleInputFile) {
        // open puzzle file and store lines in vector
        std::vector<int> puzzleVector;
        std::ifstream file(puzzleInputFile);
        if (file.is_open()) {
            std::string line;
            while (getline(file, line)) {
                puzzleVector.push_back(stoi(line));
            }
        }
        file.close();

        return puzzleVector;
    }

    // * input loader string vector
    static std::vector<std::string> loadPuzzleInputStringVec(std::string puzzleInputFile) {
        // open puzzle file and store lines in vector
        std::vector<std::string> puzzleVector;
        std::ifstream file(puzzleInputFile);
        if (file.is_open()) {
            std::string line;
            while (getline(file, line))
                puzzleVector.push_back(line);
        }
        file.close();

        return puzzleVector;
    }

    // * input loader string
    static std::string loadPuzzleInputString(std::string puzzleInputFile) {
        // open puzzle file and store in string
        std::ifstream file(puzzleInputFile);
        std::stringstream buffer;
        buffer << file.rdbuf();
        std::string puzzleString = buffer.str();

        return puzzleString;
    }

    // * title printer
    static void printTitle(std::string year, std::string day, std::string title) {
        const std::string COLOR_TITLE = "\033[1;95m";
        const std::string COLOR_CLEAR = "\033[0m";

        // clear screen for readability
        system("clear");

        // print title
        std::cout << COLOR_TITLE << "\n     Advent of Code " << year << std::endl;
        std::cout << "     Day " << day << " - " << title << COLOR_CLEAR << std::endl;
    }

    // * question and answer printer
    static void printQuestionAnswer(std::string question, std::string answer) {
        const std::string COLOR_QUESTION = "\033[1;34m";
        const std::string COLOR_ANSWER = "\033[1;32m";
        const std::string COLOR_CLEAR = "\033[0m";

        std::cout << COLOR_QUESTION << question << COLOR_CLEAR;
        std::cout << COLOR_ANSWER << answer << "\n"
                  << COLOR_CLEAR << std::endl;
    }
};