import time
print('PROJETO MÁQUINA\n')
#definindo os produtos na máquina
counter=0
matriz=[[counter,'COCA-COLA',3.75,2],
        [counter,'PEPSI',3.67,5],
        [counter,'MONSTER',9.96,1],
        [counter,'CAFÉ',1.25,100],
        [counter,'REDBULL',13.99,2]]
for i in range (len(matriz)):
    counter += 1
    matriz[i][0]=counter
for a in matriz:
    print(a)
#função que pega o pedido do usuário
def getUserSelection():
    user_selection = int(input('DIGITE CORRETAMENTE O ID DA BEBIDA QUE DESEJA COMPRAR: '))
    while user_selection <1 or user_selection>counter:
        user_selection = int(input('DIGITE NOVAMENTE O ID DA BEBIDA, ALGO DEU ERRADO: '))
    return user_selection-1
#função que verifica
def avaiable(user_selection):
    if matriz[user_selection][3]> 0:
        return True
    else:
        return False
#função que calcula o troco
def troco(valor):
    possible=[200,100,50,20,10,5,2,1,0.5,0.25,0.1,0.5,0.01]
    for elemento in possible:
        amount=int((valor/elemento))
        if valor>elemento:
            print('CONFIRA SEU TROCO:\n')
            if elemento>=1:
                print(amount,'x',elemento,'REAIS')
            else:
                print(amount,'x', elemento, 'CENTAVOS')
            valor = valor - (elemento*amount)
while True:
    administrator=int(input('1 PARA MODO ADMINISTRADOR OU 2 PARA USUÁRIO: '))
    while administrator!=1 and administrator!=2:
        administrator = int(input('1 PARA MODO ADMINISTRADOR OU 2 PARA USUÁRIO: '))
    if administrator==1:
        action=int(input('1:REMOVER\n2:ADICIONAR\n3:EDITAR: '))
        while action not in range (1,4):
            action = int(input('1:REMOVER\n2:ADICIONAR\n3:EDITAR: '))
        #OPÇÃO PARA REMOVER UM ITEM DA MATRIZ POR MEIO DO ID
        if action==1:
            remove=int(input('DIGITE UM ID PARA REMOVER: '))
            while remove not in range(1,len(matriz)+1):
                remove = int(input('DIGITE UM ID VÁLIDO: '))
            matriz.remove(matriz[remove-1])
            counter=0
            for i in range(len(matriz)):
                counter += 1
                matriz[i][0] = counter
            for i in matriz:
                print(i)
        #OPÇÃO PARA ADICIONAR UM NOVO PRODUTO, SEU PREÇO E SEU ESTOQUE
        elif action==2:
            counter+=1
            new_product=[counter]
            add_p=str(input('DIGITE O NOME DO PRODUTO  PARA ADICIONAR:\n')).upper().strip()
            new_product.append(add_p)
            add_v=float(input('DIGITE O PREÇO DO PRODUTO NOVO:\n'))
            while add_v<=0:
                add_v = float(input('PREÇO INVÁLIDO:\n'))
            if add_v>0:
                new_product.append(add_v)
            add_s=int(input('DIGITE A QUANTIDADE DIPONÍVEL DESSE NOVO PRODUTO:\n'))
            new_product.append(add_s)
            matriz.append(new_product)
            print(new_product,'\n')
            for i in matriz:
                print(i)
        #OPÇÃO PARA EDITAR UM PRODUTO JÁ NA MATRIZ, SEJA O ESTOQUE, PREÇO OU NOME
        elif action==3:
            edit=int(input('1:EDITAR UM NOME\n2:EDITAR UM PREÇO\n3:EDITAR UM ESTOQUE: '))
            while edit not in range (1,4):
                edit = int(input('1:EDITAR UM NOME\n2:EDITAR UM PREÇO\n3:EDITAR UM ESTOQUE: '))
            if edit==1:
                x=int(input('DIGITE O NUMERO DO ID DA COLUNA QUE VOCÊ DESEJAR MUDAR O NOME DO PRODUTO:\n '))
                while x not in range(1,len(matriz)+1):
                    x = int(input('DIGITE UM ID VÁLIDO: '))
                if x in range(1,len(matriz)+1):
                    new_name=input('DIGITE O NOME DO PRODUTO QUE VOCÊ QUER:\n').upper().strip()
                    matriz[x-1][1]=new_name
            elif edit==2:
                x = int(input('DIGITE O NUMERO DO ID QUE VOCÊ DESEJAR MUDAR O PREÇO DO PRODUTO:\n'))
                while x not in range(1,len(matriz)+1):
                    x = int(input('DIGITE UM ID VÁLIDO: '))
                if x in range(1,len(matriz)+1):
                    new_price=float(input('DIGITE O NOVO PREÇO:\n'))
                    while new_price<=0:
                        new_price = float(input('PREÇO INVÁLIDO:\n'))
                    if new_price>0:
                        matriz[x - 1][2] = new_price
            elif edit==3:
                x = int(input('DIGITE O NUMERO DO ID QUE VOCÊ DESEJAR MUDAR O ESTOQUE DO PRODUTO:\n'))
                while x not in range(1,len(matriz)+1):
                    x = int(input('DIGITE UM ID VÁLIDO: '))
                if x in range(1,len(matriz)+1):
                    new_amount=int(input('DIGITE O NOVO ESTOQUE:\n'))
                    matriz[x - 1][3] = new_amount
                for i in matriz:
                    print(i)
        continue
    if administrator==2:
        #começo do programa com repetição que atualiza o estoque
        print('AS BEBIDAS DISPONÍVEIS SÃO:\n')
        for i in matriz:
            print(i,'\n')
        userSelection = getUserSelection()
        #caso o produto esteja em estoque
        if avaiable(userSelection):
            productValue = matriz[userSelection][2]
            print('O ESTOQUE DO PRODUTO', matriz[userSelection] [1], 'ESTÁ DISPONÍVEL\n')
            print('O VALOR A SER PAGO SERÁ DE',productValue,'\n')
            #pedindo o valor
            valor=float(input('DIGITE O VALOR A SER PAGO: '))
            while valor<productValue:
                valor=float(input('VALOR INSUFICIENTE, DIGITE NOVAMENTE OU DIGITE "0" PARA SAIR: '))
                if valor==0:
                    exit()
                    time.sleep(2)
            if valor==productValue:
                #aceitando a compra e subtraindo 1 do estoque
                matriz[userSelection] [3] = ((matriz[userSelection][3]) - 1)
                print('COMPRA ACEITA')
                time.sleep(2)
            elif valor>productValue:
                #calcula o troco e subtraindo 1 do estoque
                b = troco(valor-productValue)
                matriz[userSelection][3] = ((matriz[userSelection][3]) - 1)
                time.sleep(3)
        else:
            #caso não haja estoque
            print('PRODUTO FORA DE ESTOQUE')
            time.sleep(2)
