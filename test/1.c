#include<stdio.h>
void event_time(int dia1,int dia2,int hora1,int hora2,int minuto1,int minuto2,int segundo1,int segundo2)
{
    int dia,hora,minuto,segundo;
    segundo=(segundo2-segundo1);
    minuto=(minuto2-minuto1);
    hora=(hora2-hora1);
    dia=(dia2-dia1);
    if(segundo<0)
    {
        segundo=segundo+60;
        minuto--;
    }
    if(minuto<0)
    {
        minuto=minuto+60;
        hora--;
    }
    if(hora<0)
    {
        hora=hora+24;
        dia--;
    }

    printf("%d dia(s)\n",dia);
    printf("%d hora(s)\n",hora);
    printf("%d minuto(s)\n",minuto);
    printf("%d segundo(s)\n",segundo);
}
int main()
{
    int dia1,dia2,hora1,hora2,minuto1,minuto2,segundo1,segundo2,dia,hora,minuto,segundo;
    scanf("Dia %d\n",&dia1);
    scanf("%d : %d : %d\n",&hora1,&minuto1,&segundo1);
    scanf("Dia %d\n",&dia2);
    scanf("%d : %d : %d",&hora2,&minuto2,&segundo2);

	// printf("%d %d %d %d - %d %d %d %d\n", dia1,dia2,hora1,hora2,minuto1,minuto2,segundo1,segundo2);

    event_time(dia1,dia2,hora1,hora2,minuto1,minuto2,segundo1,segundo2);
    return 0;
}