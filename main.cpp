//	Lab 5-11 : Problem Definition
//	Make a program that find the prime numbers in the given range.
//		example) find the prime numbers in the range [1..100]
//		2, 3, 5, 7, ... , 97

#include <iostream>
using namespace std;

int main()
{
	int begin, end;

	do
	{
		cout << "Enter your range [from, to] \n";
		cin >> begin >> end;
	} while (begin >= end || begin < 2 || end < 0);

	// TODO: iterate through each number in the range [begin..end]
	for (int n = begin; n <= end; n++)
	{
		// TODO: check if n is prime by testing divisibility from 2 up to n-1
		bool isPrime = true;
		for (int i = 2; i < n; i++)
		{
			// TODO: if n is divisible by i, it is not prime
			if (n % i == 0)
			{
				isPrime = false;
				break;
			}
		}
		// TODO: if n is prime, print it
		if (isPrime)
		{
			cout << n << " ";
		}
	}
	cout << endl;

	return 0;
}
