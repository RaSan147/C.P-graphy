// C++ code to demonstrate printing pattern of alphabets
#include <iostream>
using namespace std;

// Function to demonstrate printing pattern
void alphabet(int n)
{
	int i = 1, j = 0;

	// assigning ASCII value of A which is 65
	int num = 65;

	// converting ASCII value to character,
	// now our alpha variable is having
	// value A after typecasting.
	char alpha = char(num);
	while (i <= n) {

		// alpha is having A value and it
		// will change as soon as alpha
		// increased or decreased.
		while (j <= i - 1) {
			cout << alpha << " ";
			j++;
		}

		// incrementing alpha value so as it can
		// point to next character
		alpha++;

		// we have to reset j value so as it can
		// start from beginning and print * equal to
		// i.
		j = 0;
		i++;

		// Ending line after each row
		cout << endl;
	}
}

// Driver Code
int main()
{
	int n = 5;

	// Function Call
	alphabet(n);
	return 0;
}
