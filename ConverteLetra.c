/*Para rodar esse arquivo .c no cmd é preciso rodar ele pelo menos uma vez no visual studio
ou qualquer programa similar para gerar um .exe, assim é só abrir o diretório na qual o programa 
e os arquivos de teste foram salvos no prompt de comando e digitar 
"ConverteLetra ArquivoTextoEntrada.txt ArquivoTextoSaida.txt" para rodar. 
Os arquivos para teste .txt poderão ser criados pelo usuário para rodar com esse programa.

Aluno= Pedro Lunardelli Antunes*/

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