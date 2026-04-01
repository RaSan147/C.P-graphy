// http://vjudge.net/problem/SPOJ-PRIME1

#include<stdio.h>
#include <stdlib.h>
// #define LIMIT 1000000000



int main(){
	const int LIMIT = 1000000000;
	char *allN = (char *)calloc(LIMIT, sizeof(char));
	if (allN == NULL) {
		fprintf(stderr, "Memory allocation failed\n");
		return 1;
	}


	int j;

	j = 2;
	while(j<LIMIT/j){
		allN[2*j]=1;
		j++;
	}

	for(int i=3;i*i<LIMIT+1;i+=2){
		if(allN[i]){
			continue;
		}
		j = 2;
		while(j<LIMIT/j){
			allN[i*j]=1;
			j++;
		}
	}

	int T;
	scanf("%d", &T);

	// for(int i=1; i<10;i++){
	// 	printf("%d %d|", i, allN[i]);
	// }

	int m, n;
	while(T--){
		scanf("%d %d", &m, &n);
		
		if(m<2){
			m=2;
		}
		for(int i=m;i<=n;i++){
			if(!allN[i]){
				printf("%d\n", i);
			}
		}

		printf("\n");
	}

	free(allN);
}