// Justin Ventura
// 01/11/20
// bullcow.cpp
// Gull Code 2019

#include <iostream>

int main() {

	int num1, num2, temp1, temp2, bull = 0, cow = 0;
	int arr1[4];
	int arr2[4];
	std::cout << "Enter num1: ";
	std::cin >> num1;
	std::cout << "Enter num2: ";
	std::cin >> num2;

	for (int i = 0; i <= 3; i++) {
		temp1 = num1 % 10;
		temp2 = num2 % 10;
		num1 /= 10;
		num2 /= 10;
		arr1[i] = temp1;
		arr2[i] = temp2;
		if (temp1 == temp2) bull++;
	}

	for (int i = 0; i <= 3; i++) {

		for (int j = 0; j <= 3; j++) {

			if (arr1[i] == arr2[j])
				cow++;

		}

	}
	cow -= bull;

	std::cout << bull << " bulls and " << cow << " cows.\n";

	return 0;

}