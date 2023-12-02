#include <stdio.h>
#include <string.h>

int main(){
	int T;
	scanf("%d", &T);

	int cp, vp, tp;
	char c;

	for(int i=0;i<T;i++){
		char txt[1000];
		char V[1000];
		char C[1000];

		gets(txt);

		cp = vp = tp =  0;

		c = txt[tp];

		while(c!='\0'){
			c = txt[tp];

			printf("%c", c);
			if(c==' '){
				continue;
			}
			if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u'){
				V[vp] = c;
				vp++;
			} else {
				C[cp] = c;
				cp++;
			}
			tp++;
		}
		C[cp] = '\0';
		V[vp] = '\0';
		printf("%s\n%s\n", V, C);
	}
}