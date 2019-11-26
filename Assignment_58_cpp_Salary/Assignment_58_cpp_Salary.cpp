//Name: Joey Fong
//Email: joey.fong39@myhunter.cuny.edu
//Date: November 25, 2019
//This C++ program that asks the user for their weekly salary, and continue asking until the number entered is positive (that is, greater than 0).

#include <iostream>
using namespace std;

int main()
{
  double salary;
    while (salary > 0)
    {
    cout << "Please enter your salary: ";
    cin >> salary;
    cout << "Your weekly salary is $" << salary << endl;
      if (salary < 0)
      {
      cout << "You entered a negative number." << endl;
      cout << "Please enter your salary: ";
      }
    }
return 0;
}
