//Name: Joey Fong
//Email: joey.fong39@myhunter.cuny.edu
//Date: November 25, 2019
//This C++ program asks the user for an initial dollar amount. It then repeatedly asks for the amount spent and reports on the remaining amount, until it runs out of money. 

#include <iostream>
using namespace std;

int main()
{
  double amount_left;
  double spent;
  cout<<"Please enter the initial dollar amount: ";
  cin>> amount_left;

     while (amount_left > 0)
     {
     cout<<"Please enter the amount you spent: ";
     cin>> spent;
     amount_left = amount_left - spent;
     cout<<"You now have $" << amount_left << " remaining" << endl;
       if (amount_left <= 0)
       {
       cout<<"Your initial amount has been entirely spent";
       }
     }
return 0;
}
