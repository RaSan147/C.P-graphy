#include <stdio.h>
#include <string.h>



int main()
{
    char c[5];
    char ch;
    for(int i=0;i<5;i++)
    {
        ch=getchar();
        c[i]=ch;
        printf("*");

        
    }
    for (int i = 0; i < 5; i++)
    {
        printf("%c",c[i]);
    }
    
  
    

   

    return 0;
}