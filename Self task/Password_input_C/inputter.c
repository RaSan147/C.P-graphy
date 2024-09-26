// Task

// Make a password input function in c
// Requirements:
// Getc/getch/getchar (read only 1 character) at a time

// Knowledge support:
// printf("\b"); 
// This deletes last printed character

// How password input work:
// You press a key, on the screen instead of the key a star * shows up

// Limitation:
// You can't use backspace when entering password (this is advance stuff)

// Extra marks: do some research to fix the limitation

#include <stdio.h>
#include <conio.h>

int type(char c){
	if (c == 13){ // Enter / Carriage return
		return 0;
	} else if (c == 8){ // Backspace
		return 1;
	} else if (c>31 && c<127){ // printable characters
		return 2;
	}

	return 3;
}


int main(){
	char password[64];
	char c=2;
	unsigned int pos = 0;
	while(c){
		c = getch();

		int c_type = type(c);

		if (c_type==0){
			printf("\n");
			password[pos] = 0;
			c = 0;
		} else if (c_type==1) {
			if (pos) { // has typed something
				printf("\b \b");
				pos -= 1;
			}
		} else if (c_type==2) {
			// printf("\b*");
			printf("*");
			password[pos] = c;
			pos +=1;
		} else {
			continue;
		}
	}

	printf("%s", password);
}