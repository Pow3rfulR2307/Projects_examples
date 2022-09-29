
#JOQUEMPÔ PROGRAMADO EM PYTHON, COM POSSIBILIDADE DE JOGADA ENTRE JOGADORES, JOGADOR VS PC OU PC VS PC.

import random
from random import choice
vx=0
vy=0
start=str(input('DIGITE "S" PARA INICIAR OU "N" PARA SAIR: ')).upper().strip()
while start!='S' and start!='N':
    start=str(input('DIGITE APENAS "S" OU "N": ')).upper().strip()
if start=='S':
    lista=('PEDRA', 'PAPEL', 'TESOURA')
    tipo=str(input('digite 1 para (humano x pc), 2 para (humano x humano) e 3 para (pc x pc): ')).strip()
    while tipo!='1' and tipo!='2' and tipo!='3':
        tipo=str(input('Errado, digite 1 para (humano x pc), 2 para (humano x humano) e 3 para (pc x pc): ')).strip()
    while tipo=='1' or tipo=='2' or tipo=='3':
        if tipo=='1':
            a='JOGADOR'
            b='PC'
            x=str(input('digite pedra, papel ou tesoura: ')).upper().strip()
            y=random.choice(lista)
        elif tipo=='2':
            a='JOGADOR 1'
            b='JOGADOR 2'
            x=str(input('Jogador 1 digite pedra, papel ou tesoura: ')).upper().strip()
            y=str(input('Jogador 2 digite pedra, papel ou tesoura: ')).upper().strip()
        elif tipo=='3':
            a='PC 1'
            b='PC 2'
            x=random.choice(lista)
            y=random.choice(lista)
        if x=='PEDRA' and y=='TESOURA' or x=='TESOURA' and y=='PAPEL' or x=='PAPEL' and y=='PEDRA':
            print(a,'GANHOU POIS JOGOU',x,'ENQUANTO',b,'PERDEU POIS JOGOU',y)
            vx=vx+1
            print('O PLACAR ATUAL É (',a,':',vx,') VS (',b,':',vy,')')
        elif x=='PEDRA' and y=='PAPEL' or x=='TESOURA' and y=='PEDRA' or x=='PAPEL' and y=='TESOURA':
            print(a,'PERDEU POIS JOGOU',x,'ENQUANTO',b,'GANHOU POIS JOGOU',y)
            vy=vy+1
            print('O PLACAR ATUAL É (',a,':',vx,') VS (',b,':',vy,')')
        elif x==y:
            print('EMPATE,',a,'JOGOU',x,'E',b,'TAMBÉM JOGOU ',y)
            print('O PLACAR ATUAL É (',a,':',vx,') VS (',b,':',vy,')')
        else:
            print('SIGA AS INSTRUÇOES CORRETAMENTE')
        continuar=str(input('DIGITE QUALQUER COISA PARA TENTAR DE NOVO OU "N" PARA SAIR: ')).upper().strip()
        if continuar!='N':
            continue
        else:
            if vx>vy:
                print('ENCERRANDO JOGO, O PLACAR FINAL FOI (',a,':',vx,') VS (',b,':',vy,'), PORTANTO',a,'GANHOU!')
            elif vx<vy:
                print('ENCERRANDO JOGO, O PLACAR FINAL FOI (',a,':',vx,') VS (',b,':',vy,'), PORTANTO',b,'GANHOU!')
            else:
                print('ENCERRANDO JOGO, O PLACAR FINAL FOI (',a,':',vx,') VS (',b,':',vy,'), PORTANTO EMPATE!')
            print('OBRIGADO POR JOGAR! CÓDIGO DESENVOLVIDO POR PEDRO LUNARDELLI ANTUNES')
            break
if start=='N':
    print('SAINDO...O CÓDIGO NÃO EXECUTADO FOI DESENVOLVIDO POR PEDRO LUNARDELLI ANTUNES')
