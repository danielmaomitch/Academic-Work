#include <iostream>
#include <string>
#include <vector>
#include <time.h>
#include "insultgenerator_20dmrm.h"

using namespace std;

int main() {

	InsultGenerator ig;
	vector<string> insults;
	clock_t start=0, finish=0;

	try {
		ig.initialize();
	} catch (FileException& e) {
		cerr << e.what() << endl;
		return 1;
	}

	cout << "A single insult:" << endl;
	cout << ig.talkToMe() << endl;

	try {
		insults = ig.generate(-100);
	} catch (NumInsultsOutOfBounds& e) {
		cerr << e.what() << endl;
	}
	try {
		insults = ig.generate(40000);
	} catch (NumInsultsOutOfBounds& e) {
		cerr << e.what() << endl;
	}

	cout << "\n100 insults, all different:" << endl;
	insults = ig.generate(100);
	if (insults.size() > 0)
		for (int i = 0; i < 100; i++)
			cout << insults[i] << endl;
	else
		cerr << "Insults could not be generated!" << endl;

	try {
		ig.generateAndSave("Nothing.txt", 40000);
	} catch (NumInsultsOutOfBounds& e) {
		cerr << e.what() << endl;
	}
	cout << "\nSaving 1000 unique insults to a file...";
	try {
		ig.generateAndSave("SavedInsults.txt", 1000);
	} catch (FileException& e) {
		cerr << e.what() << endl;
		return 1;
	}
	cout << "done." << endl;

	try {
		start = clock();
		insults = ig.generate(10000);
		finish = clock();
	} catch (NumInsultsOutOfBounds& e) {
		cerr << e.what() << endl;
	}
	cout << "\n" << insults.size() << " insults generated." << endl;
	cout << (1e3 * (finish - start)/CLOCKS_PER_SEC) << " msec to complete." << endl;

	return 0;

}
