/**
 * @file insultgenerator_20dmrm.cpp
 * @author Daniel Mitchell: 20239030
 * @date 2022-10-02
 */
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <time.h>
#include <algorithm>
#include <random>

#include "insultgenerator_20dmrm.h"

using namespace std;

static const string filename = "InsultsSource.txt";
static vector<string> column1;
static vector<string> column2;
static vector<string> column3;

NumInsultsOutOfBounds::NumInsultsOutOfBounds(const string& message) : message(message) {}
string& NumInsultsOutOfBounds::what() { return message; }

FileException::FileException(const string& message) : message(message) {}
string& FileException::what() { return message; }

void InsultGenerator::initialize() const {
    ifstream fileIn(filename);
    string word;
    int count = 0;

    if (fileIn.fail()) {
        throw FileException("Could not read file.");
    }

    // seperatate insult source file into its columns
    while (fileIn >> word) {
        if (count % 3 == 0) {
            column1.push_back(word);
        }
        else if (count % 3 == 1) {
            column2.push_back(word);
        }
        else {
            column3.push_back(word);
        }
        count++;
    }
    fileIn.close();
}

string InsultGenerator::talkToMe() const {
    srand(time(0));
    int index1 = 0, index2 = 0, index3 = 0;

    // generate three random numbers for each respective column
    index1 = rand() % 50;
    index2 = rand() % 50;
    index3 = rand() % 50;
    string insult = column1.at(index1) + " " + column2.at(index2) + " " + column3.at(index3);

    return insult;
}

vector<string> InsultGenerator::generate(const int bounds) const {
    if (bounds < 0 || bounds > 10000) {
        throw NumInsultsOutOfBounds("Number of insults out of bounds.");
    }

    srand(time(0));     // create unique seed on each run for random generator 
    int index1 = 0, index2 = 0, index3 = 0, num_added = 0;
    string insult;
    vector<string> insults;
    while(num_added < bounds) {
        // generate three random indices for the 3 columns I will be choosing from
        index1 = rand() % 50;
        index2 = rand() % 50;
        index3 = rand() % 50;

        insult = column1.at(index1) + " " + column2.at(index2) + " " + column3.at(index3);
        if (find(insults.begin(), insults.end(), insult) != insults.end()) {}
        else {
            insults.push_back(insult);
            num_added++;
        }
    }
    sort(insults.begin(), insults.end());
    return insults;
}

void InsultGenerator::generateAndSave(const string& filename, const int bounds) const {
    ofstream fileOut(filename);
    if (fileOut.fail()) {
        throw FileException("Could not write to file." + filename);
    }

    vector<string> insults = InsultGenerator::generate(bounds);
    for (string line: insults) {
        fileOut << line << endl;
    }
    fileOut.close();
}

int main() {
    InsultGenerator ig;
    ig.initialize();
    cout << ig.talkToMe() << endl;
}