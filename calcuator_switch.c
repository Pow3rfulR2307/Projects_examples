//Calculador feita em C

#include <stdio.h>
int main(){
    float num1, num2;
    int operation;
    printf("type in the first number:\n");
    scanf("%f", &num1);
    printf("type in the second number:\n");
    scanf("%f", &num2);
    printf("Type; in the operation: 1(+), 2(-), 3(*), 4(/): \n");
    scanf("%d", &operation);
    switch (operation)
    {
    case (1):
        printf("The anwser is %.2f", (num1+num2));
        break;
    case(2):
        printf("The anwser is %.2f", (num1-num2));
        break;
    case(3):
        printf("The anwser is %.2f", (num1*num2));
        break;
    case(4):
        if (num2!=0){
        printf("The anwser is %.2f", (num1/num2));
        }
        else{
            printf("no");
        }
        break;
    default:
        printf("operator invalid");
        break;
    }
    return 0;
}
