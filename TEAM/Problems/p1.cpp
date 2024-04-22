/*
1
5 6
2 3 4

When n = 3


1
14 15
2 3 4
10 11 12 13
5 6 7 8 9 

when n = 5
*/

#include<iostream>

using namespace std;

int sum(int n){
	return n*(n+1)/2;
}

int main(){
	int n;
	cin >> n;

	int max = sum(n);

	bool front = true;

	int start = 1, end = max;
	int upto;


	for (int l=1; l<=n;l++){
		if(front){
			upto = start + l;
			for(; start<upto; start++){
				cout <<"\t"<< start;
			}
			cout << endl;
		} else {
			upto = end - l+1;
			for(int i=upto; i<=end; i++){
				cout <<"\t"<< i;
			}
			end = upto-1;
			cout << endl;
		}

		front = !front;
	}
}