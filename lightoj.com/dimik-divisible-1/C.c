// https://lightoj.com/problem/dimik-divisible-2
#pragma GCC optimize("Ofast")
#include <stdio.h>




int main(){
    short int T;
	unsigned long int a, b, x, n, start;

	scanf("%hd", &T);

	for (short int t=0; t<T; t++){
		scanf("%lu %lu %lu", &a, &b, &x);

        n = a % x;
		start = n ? a + x - n : a;


		for (; start<=b; start+=x){
			printf("%lu\n", start);
		}
		printf("\n");
	}
}