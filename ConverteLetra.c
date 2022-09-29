
/*PROGRAMA QUE RECEBE DOIS ARQUIVOS .TXT, UM DE ENTRADA E OUTRO DE SAÍDA POR MEIO DE ARGUMENTOS NO CMD. 
O PROGRAMA ENTÃO CONVERTE TODAS AS LETRAS MINÚSCULAS DO ARQUIVO .TXT DE ENTRADA PARA MAIÚSCULAS NO ARQUIVO .TXT SAÍDA */
   
#include <stdio.h>
int main(int argc, char**argv){
    int ch;
    FILE* file1;
    file1=fopen(argv[1], "r+");
    FILE* file2;
    file2=fopen(argv[2], "w");
    printf("Texto convertido:\n\n");
    while((ch=fgetc(file1))!=EOF){
        if ((ch>=97) && (ch<=122)){
            ch-=32;
        }
        fputc(ch, file2);
        printf("%c",ch);
    }
    return 0;
    }
