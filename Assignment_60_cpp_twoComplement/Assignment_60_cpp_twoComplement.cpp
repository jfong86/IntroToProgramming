//Name: Joey Fong
//Email: joey.fong39@myhunter.cuny.edu
//Date: November 26, 2019
//C++ program that asks the user for a whole number between -31 and 31 and prints out the number in "two's complement" notation, using the following algorithm: 
/*
   1. Ask the user for a number, n.
   2. If the number is negative, print a 1 and let x = 32 + n.
   3. If the number is not negative, print a 0 and let x = n.
   4. Let b = 16.
   5.  While b > 0.5:
        If x >= b then print 1, otherwise print 0
        Let x be the remainder of dividing x by b.
        Let b be b/2. 
   6. Print a new line ('\n'). 
*/

#include <iostream>
using namespace std;

int main()
{
  int n, x, b;
  cout << "Enter a number: ";
  cin >> n;

    if (n < 0)
    {
    cout << 1;
    x = 32 + n;
    }
    else
    {
    cout << 0;
    x = n;
    }

  b = 16;

    while (b > 0.5)
    {
      if (x >= b)
      {
      cout << 1;
      }
      else
      {
      cout << 0;
      }
    x = x % b;
    b = b/2;
    }

cout << "\n";

return 0;
}
