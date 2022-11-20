/**
 * @file fraction_20dmrm.h
 * @author Daniel Mitchell
 * @date 2022-10-23
 */

#include <iostream>

using namespace std;

class Fraction {
    public:
        Fraction(); // default constructor 
        Fraction(int);  // constructor/converter when given whoel number
        Fraction(int, int); // constructor when given numerator and denominator 

        int numerator() const;  // accessor 
        int denominator() const;    //accessor 

        // unary operators 
        Fraction& operator++();	// pre-increment overload 
        Fraction operator++(int unused); // Post-increment overload 
        Fraction& operator-(); // negation

        // member binary operators 
        Fraction& operator+=(const Fraction& right);    // += operator overload 

    private:
        Fraction& normalize();  // noramlizes a fraction into its form with the smallest numerator and denominator 
        int GCD(int n, int m);  // finds te Greatest Common Denominator between two integers n and m

        int num;    // numerator of a fraction
        int denom;  // denominator of a fraction

        

    // friendly binary operators
    friend Fraction operator+(const Fraction& left, const Fraction& right); // + operator overload
    friend Fraction operator-(const Fraction& left, const Fraction& right); // - operator overload
    friend Fraction operator*(const Fraction& left, const Fraction& right); // * operator overload
    friend Fraction operator/(const Fraction& left, const Fraction& right); // / operator overload
};

class FractionException {
    public:
        FractionException(const string& message);       // null denominator exception handling
        string& what();     // error message output
    private:
        string message; // error message
};

// non-member operator overloads
bool operator<(const Fraction& left, const Fraction& right); // < operator overload
bool operator>(const Fraction& left, const Fraction& right); // > operator overload
bool operator<=(const Fraction& left, const Fraction& right);    // <= operator overload
bool operator>=(const Fraction& left, const Fraction& right);    // >= operator overload
bool operator==(const Fraction& left, const Fraction& right);    // == operator overload
bool operator!=(const Fraction& left, const Fraction& right);    // != operator overload
ostream& operator<<(ostream& out, const Fraction& frac);    // << operator overload
istream& operator>>(istream& in, Fraction& fraction);   // >> operator overload