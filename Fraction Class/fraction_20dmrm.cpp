/**
 * @file fraction_20dmrm.h
 * @author Daniel Mitchell
 * @date 2022-10-23
 */
#include <iostream>
#include <cmath>
#include <string>

#include "fraction_20dmrm.h"
using namespace std;

Fraction::Fraction() : num(0), denom(1) {}
Fraction::Fraction(int numerator) : num(numerator), denom(1) {}
Fraction::Fraction(int numerator, int denominator) : num(numerator), denom(denominator) {
    if (denom == 0) {
        throw FractionException("Denominator cannot be zero!");
    }

    // if both the num and denom are negative, make the fraction positive, noramlize after
    else if (denom < 0 && num < 0) {
        num *= -1;
        denom *= -1;
        this->normalize();
    }
    //if only the numerator is negative, normalize as a positive fraction, then make the numerator negative
    else if (num < 0) {
        num *= -1;
        this->normalize();
        num *= -1;
    }
    //if only the denominator is negative, normalize as a positive fraction, then make the numerator negative
    else if (denom < 0) {
        denom *= -1;
        this->normalize();
        num *= -1;
    }
    // if both numerator and denominator are positive, just normalize 
    else{
        this->normalize();
    }
}

FractionException::FractionException(const string& message) : message(message) {}
string& FractionException::what() { return message; }

int Fraction::numerator() const { return num; }
int Fraction::denominator() const { return denom; }

// divide both sides by the Greatest Common Denominator to put into lowest form
Fraction& Fraction::normalize() {
    int gcd = GCD(num, denom);
    num = num / gcd;    
    denom = denom / gcd;
    return *this;
}

// use a given formula to find the GCD
int Fraction::GCD(int n, int m) {
    if (m <= n && n%m == 0) { return m; }
    else if (n < m) { return GCD(m, n); }
    else { return GCD(m, n%m); }
}

// The following are all operator overloads 
Fraction& Fraction::operator++() {
	num += denom;
	return *this;
}

Fraction Fraction::operator++(int unused) {
    Fraction clone(num, denom);
    num+=denom;
    return clone;
}

Fraction& Fraction::operator-() {
    num = 0 - num;
    return *this;
}

// addition performed by converting both fractions into the same denominator using common multiples 
Fraction operator+(const Fraction& left, const Fraction& right) {
    return Fraction((left.num * right.denom) + (right.num * left.denom), left.denom * right.denom);
}

// subtraction performed in the same fashion as addition
Fraction operator-(const Fraction& left, const Fraction& right) {
    return Fraction((left.num * right.denom) - (right.num * left.denom), left.denom * right.denom);
}

Fraction operator*(const Fraction& left, const Fraction& right) {
    return Fraction(left.num * right.num, left.denom * right.denom);
}

Fraction operator/(const Fraction& left, const Fraction& right) {
    return Fraction(left.num * right.denom, left.denom * right.num);
}

Fraction& Fraction::operator+=(const Fraction& right) {
    num = (num * right.denom) + (right.num * denom);
    denom = denom * right.denom;
    return *this;
}

// convert fractions to the same denominator, the higher numerator is then greater 
// all compare operators are designed in a similar fashion
bool operator<(const Fraction& left, const Fraction& right) {
    return left.numerator() * right.denominator() < right.numerator() * left.denominator();
}

bool operator>(const Fraction& left, const Fraction& right) {
    return left.numerator() * right.denominator() > right.numerator() * left.denominator();
}

bool operator<=(const Fraction& left, const Fraction& right) {
    return (left.numerator() * right.denominator() < right.numerator() * left.denominator()) || (left.numerator() == right.numerator() && left.denominator() == right.denominator());
}

bool operator>=(const Fraction& left, const Fraction& right) {
    return (left.numerator() * right.denominator() > right.numerator() * left.denominator()) || (left.numerator() == right.numerator() && left.denominator() == right.denominator());
}

// == is defined as both fractions having the same numerator and denominator 
bool operator==(const Fraction& left, const Fraction& right) {
    return left.numerator() == right.numerator() && left.denominator() == right.denominator();
}

bool operator!=(const Fraction& left, const Fraction& right) {
    return !(left.numerator() == right.numerator() && left.denominator() == right.denominator());
}

// fractions are printed in the form "x/y"
ostream& operator<<(ostream& out, const Fraction& frac) {
    out << frac.numerator() << "/" << frac.denominator();
    return out;
}

// split the string in half "/" as the delimiter 
istream& operator>>(istream& in, Fraction& fraction) {
    string input;
    in >> input;

    // split the string into the numerator on the LHS of the "/" and the denominator on the RHS 
    if (input.find("/") != -1) {
        int index = input.find("/");
        int num = stoi(input.substr(0, index)); // LHS
        int denom = stoi(input.substr(index + 1));  // RHS
        fraction = Fraction(num, denom);
    }
    // if the string does not have a "/" then it is just an integer
    else {
        int num = stoi(input);
        fraction = Fraction(num);
    }
    
    return in;
}

