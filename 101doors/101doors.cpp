// Justin Ventura
// 01/11/20
// 101doors.cpp
// Gull Code 2019

#include <iostream>

int main() {
	int n;
	int arr[101];
	for (int i = 0; i < 101; i++)
		arr[i] = 1;

	int pass = 2;
	while (pass <= 101) {
		for (int i = pass - 1; i < 101; i += pass) {
			if (arr[i] == 0)
				arr[i] = 1;
			else
				arr[i] = 0;
		}
		pass++;
	}

	std::cin >> n;

	if (n == 0) {
		for (int i = 0; i < 101; i++) {
			std::cout << (i+1) << " " << arr[i] << "\n";
		}
	}
	else if (n == 1) {
		for (int i = 0; i < 101; i++) {
			if (arr[i] == 1) {
				std::cout << (i+1) << " " << arr[i] << "\n";
			}
		}
	}
	else if (n == 2) {
		for (int i = 0; i < 101; i++) {
			if (arr[i] == 0) {
				std::cout << (i+1) << " " << arr[i] << "\n";
			}
		}
	}
	return 0;
}