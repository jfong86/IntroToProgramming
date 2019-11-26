//Name: Joey Fong
//Email: joey.fong39@myhunter.cuny.edu
//Date: November 25, 2019
//This C++ program that asks the user for their average grade and prints
/*
    "Your letter grade is F" if it is strictly less than 60,
    "Your letter grade is C or D" if it is 60 or greater, but strictly less than 80,
    "Your letter grade is B" if it is 80 or greater, but strictly less than 90, and
    "Your letter grade is A" otherwise.
*/

#include <iostream>
#include <array>
using namespace std;

int main()
{
  float grade [3] = {60, 80, 90};
  float x;
  cout<<"Enter your average grade: ";
  cin>> x;

    if (x < grade[0])
    {
    cout<<"Your letter grade is F";
    }
    else if (x >= grade[0] && x < grade[1])
    {
    cout<<"Your letter grade is C or D";
    }
    else if (x >= grade[1] && x < grade[2])
    {
    cout<<"Your letter grade is B";
    }
    else
    {cout<<"Your letter grade is A";
    }
return 0;
}
