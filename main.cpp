//	Lab 5-11 : Problem Definition
//	Make a program that find the prime nbers in the given range.
//		example) find the prime nbers in the range [1..100]
//		2, 3, 5, 7, ... , 97

#include <iostream>
using namespace std;

int main()
{
	int begin, end, n, i;

	do
	{
		cout << "Enter your range [from, to] \n";
		cin >> begin >> end;
	} while (begin >= end || begin < 2 || end < 0);
	
	for(n = begin; n <= end; n++){
		for (i=2; i<n; i++){
		if (n%i == 0)
			break;
		}
	if (i == n)
	cout << n << " ";
  }
	cout << endl;

	return 0;
}
