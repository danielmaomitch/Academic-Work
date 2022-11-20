/**
 * @file insultgenerator_20dmrm.cpp
 * @author Daniel Mitchell: 20239030
 * @date 2022-10-02
 */
#include <string>
#include <vector>

using namespace std;

class InsultGenerator {
    public:
        void initialize() const;        // read all insults from the insult source file and store in attributes 
        void generateAndSave(const string& filename, const int num) const;        // store a given number of unique insults into a given file name and type
        string talkToMe() const;        // generate a single unique insult
        vector<string> generate(const int bounds) const;        // generate a given number of unique insults
};

class FileException {
    public:
        FileException(const string& message);       // file exception handling
        string& what();     // error message
    private:
        string message;
};

class NumInsultsOutOfBounds {
    public:
        NumInsultsOutOfBounds(const string& message);       // out of bounds exception handling
        string& what();     // error message
    private:
        string message;
};

