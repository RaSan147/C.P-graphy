// https://lightoj.com/problem/dimik-divisible-2
#pragma GCC optimize("Ofast")
#include <stdio.h>

int main(){
	unsigned long long int T, a, b, x, H, L, n, M;

	scanf("%llu", &T);

	for (unsigned long long int t=0; t<T; t++){
		scanf("%llu %llu %llu", &a, &b, &x);

		if (a>b){
			H = a; L = b;
		} else {
			L = a; H = b;
		}

		n = L;
		while (1) {
			M = H*n;
			if(M > x){
				break;
			}

			printf("%llu\n", M);
			n += L;
		}

		printf("\n");
	}
}