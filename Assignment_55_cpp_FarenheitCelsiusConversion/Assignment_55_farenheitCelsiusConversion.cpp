//Name: Joey Fong
//Email: joey.fong39@myhunter.cuny.edu
//Date: Nov. 21, 2019
//This program prompt the user for the degrees in farenheit and then print out the temperature in celsius.

#include <iostream>
using namespace std;

int main()

{
	float farenheit;
	float celsius;
	cout<<"Enter a degree in farenheit:";
	cin>>farenheit;
	//celsius = (farenheit - 32.0) * (5.0/9.0)
	celsius = (farenheit - 32.0) * (5.0/9.0);
	cout << fixed << celsius << endl;
	return 0;
}
