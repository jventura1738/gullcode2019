// Justin Ventura
// 01/11/20
// outofboxadd.cpp
// Gull Code 2019

#include <iostream>

int main() {
	int a, b;
	std::cin >> a >> b;

	if (a >= 0) {
		if (b >= 0) {
			for (int i = 0; i < b; i++)
				a++;
			std::cout << a;
		}
		else {
			for (int i = 0; i > b; i--)
				a--;
			std::cout << a;
		}
	}
	else if (a < 0) {
		if (b >= 0) {
			for (int i = 0; i < b; i++)
				a++;
			std::cout << a;
		}
		else {
			for (int i = 0; i > b; i--)
				a--;
			std::cout << a;
		}
	}
	return 0;
}