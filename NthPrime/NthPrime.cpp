// Justin Ventura
// 01/11/20
// NthPrime.cpp
// Gull Code 2019

#include <iostream>
#include <math.h> // for sqrt

bool isPrime(int N) {

	if (N % 2 == 0) return false;
	int buffer = int(sqrt(N));

	for (int i = 3; i <= buffer; i+=2)
		if (N % i == 0) return false;

	return true;

}

int main() {

	int N;

	std::cout << "Enter N: ";
	std::cin >> N;

	if (N == 1)
		std::cout << "2\n";
	else if (N == 2)
		std::cout << "3\n";
	else if (N == 3)
		std::cout << "5\n";

	int curr = 3;
	int val = 7;
	while(curr <= N) {

		if (isPrime(val)) 
			curr++;
		if (curr == N) 
			std::cout << val << "\n";
		else
			val += 2;
	}

	return 0;

}
