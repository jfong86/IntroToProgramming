//Name: Joey Fong
//Email: joey.fong39@myhunter.cuny.edu
//Date: Nov. 21, 2019
//This program asks the user for two numbers x and y, and draws a grid of zeros and ones with x rows and y columns using 'character graphics'.

#include <iostream>  //The built-in library for input/output
using namespace std; //The names of standard definitions

int main()           //C++ programs all have a main() function

{
int i, j;

cout<<"Enter the number of rows: ";
cin>>i;
cout<<"Enter the number of columns: ";
cin>>j;

for (int x=0; x<i; x++)
	{
	for (int y=0; y<j; y++)
		{
		cout << ((x+y+1)%2);
		}
	cout << endl;
	}

return 0;
}
