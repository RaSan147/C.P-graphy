/*
1
0 1
1 0 1
0 1 0 1
*/

#include<bits/stdc++.h>

using namespace std;

int main(){
	int r, c;
	r = 1;

	int rows;
	cin >> rows;

	

	for (int i=1;i<=rows;i++){
		c = r;  // 0  // 1
		for (int n=0; n<i; n++){ // ..
			cout << c << ' '; // 0 1 // 1 0 1
			c = !c; // 1 0 // 0 1
		}
		r = !r; // 1 0
		cout << endl;
	}
}

