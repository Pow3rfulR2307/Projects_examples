/*Para rodar esse arquivo .c no cmd é preciso rodar ele pelo menos uma vez no visual studio
ou qualquer programa similar para gerar um .exe, assim é só abrir o diretório na qual o programa e o arquivo de teste 
foram salvos no prompt de comando e digitar "ContagemLetra ArquivoTextoEntrada.txt" para rodar. 
O arquivo de teste pode ser criado pelo usuário para rodar com esse programa.

Aluno= Pedro lunardelli Antunes*/

#include <stdio.h>
int main(int argc, char**argv){
    FILE* txtfile;
    int c;
    int ca=0, cb=0, cc=0, cd=0, ce=0, cf=0, cg=0, ch=0, ci=0, cj=0, ck=0, cl=0, cm=0, cn=0, 
    co=0, cp=0, cq=0, cr=0, cs=0, ct=0, cu=0, cv=0, cw=0, cx=0, cy=0, cz=0;
    txtfile= fopen(argv[1], "r");
    while ((c=fgetc(txtfile))!=EOF){
        if ((c>=65 && c<=90) || (c>=97 && c<=122)){
            if (c==65 || c==97){
                ca+=1;
            }
            else if (c==66 || c==98){
                cb+=1;
            }
            else if (c==67 || c==99){
                cc+=1;
            }
            else if (c==68 || c==100){
                cd+=1;
            }
            else if (c==69 || c==101){
                ce+=1;
            }
            else if (c==70 || c==102){
                cf+=1;
            }
            else if (c==71 || c==103){
                cg+=1;
            }
            else if (c==72 || c==104){
                ch+=1;
            }
           else if (c==73 || c==105){
                ci+=1;
            }
            else if (c==74 || c==106){
                cj+=1;
            }
            else if (c==75 || c==107){
                ck+=1;
            }
            else if (c==76 || c==108){
                cl+=1;
            }
            else if (c==77 || c==109){
                cm+=1;
            }
            else if (c==78 || c==110){
                cn+=1;
            }
            else if (c==79 || c==111){
                co+=1;
            }
            else if (c==80 || c==112){
                cp+=1;
            }
            else if (c==81 || c==113){
                cq+=1;
            }
            else if (c==82 || c==114){
                cr+=1;
            }
            else if (c==83 || c==115){
                cs+=1;
            }
            else if (c==84 || c==116){
                ct+=1;
            }
            else if (c==85 || c==117){
                cu+=1;
            }
            else if (c==86 || c==118){
                cv+=1;
            }
            else if (c==87 || c==119){
                cw+=1;
            }
            else if (c==88 || c==120){
                cx+=1;
            }
            else if (c==89 || c==121){
                cy+=1;
            }
            else if (c==90 || c==122){
                cz+=1;
            }
        }
    }
    printf("(A): %d\n", ca);
    printf("(B): %d\n", cb);
    printf("(C): %d\n", cc);
    printf("(D): %d\n", cd);
    printf("(E): %d\n", ce);
    printf("(F): %d\n", cf);
    printf("(G): %d\n", cg);
    printf("(H): %d\n", ch);
    printf("(I): %d\n", ci);
    printf("(J): %d\n", cj);
    printf("(K): %d\n", ck);
    printf("(L): %d\n", cl);
    printf("(M): %d\n", cm);
    printf("(N): %d\n", cn);
    printf("(O): %d\n", co);
    printf("(P): %d\n", cp);
    printf("(Q): %d\n", cq);
    printf("(R): %d\n", cr);
    printf("(S): %d\n", cs);
    printf("(T): %d\n", ct);
    printf("(U): %d\n", cu);
    printf("(V): %d\n", cv);
    printf("(W): %d\n", cw);
    printf("(X): %d\n", cx);
    printf("(Y): %d\n", cy);
    printf("(Z): %d\n", cz);
    return 0;
}