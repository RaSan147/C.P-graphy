/*
1
14 15
2 3 4
10 11 12 13 
5 6 7 8 9
*/ 

/*
1
5 6
2 3 4*/

#include <bits/stdc++.h>
using namespace std;


int main() {
  int n,sum=0;
  cin>>n;
  
int a=1;  
  
for(int i=1; i<=n; i++){
sum+=i;}  
  for(int i= 1; i<=n;i++){
	if (i%2 != 0){
	for(int  j=0; j<i;j++){
	cout<<a<<" ";
	a++;
	}
	}
	
	else {
	for(int j=0 ; j<i;j++){
	 cout<<sum<<" ";
	 sum --;
	}
	}
	cout<<endl;
	
	
  }
}
  
