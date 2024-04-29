#IDEIA: Fazer um programa para comprar materiais recicláveis

import random
#função para gerar numeros aleatórios para a quantidade de itens
def random_generator():
    return random.randint(1, 10)

#função para gerar numeros aleatórios para o preço dos itens
def random_generator2():
    return random.randint(0, 3)

#funçaõ para gerar numeros aleatórios para o preço dos itens, nesse caso, gera preços mais caros para os itens "Madeira" e "Metal"
def random_generator5():
    return random.randint(2, 5)

#funçaõ para gerar numeros aleatórios para a quantidade de itens, nesse caso, gera quantidades menores para os itens "Madeira" e "Metal"
def random_generator4():
    return random.randint(1, 15)

#função para gerar os nomes das ruas
def random_generator3():
    ruas = ["Centro", "15 de Julho", "Bom Jesus", "Camacuã", "Ametista", "Gralha Azul"]
    return random.choice(ruas)




#"banco de dados" do app
#primeiro item é o tipo de material, segunto item é a quantidade, terceiro item é o preço, ultimo item é a rua
produtos={1:["Plástico", (random_generator()),  (random_generator2()), (random_generator3())],
        2:["Vidro", (random_generator()),  (random_generator2()), (random_generator3())],
        3:["Papelão", (random_generator()),  (random_generator2()), (random_generator3())],
        4:["Isopor", (random_generator()),  (random_generator2()), (random_generator3())],
        5:["Latinha", (random_generator()),  (random_generator2()), (random_generator3())],
        6:["Madeira", (random_generator4()),  (random_generator5()), (random_generator3())],
        7:["Metal", (random_generator4()),  (random_generator5()), (random_generator3())],
        8:["Tecido", (random_generator()),  (random_generator2()), (random_generator3())],
}
#lista para carrinho de compras
carrinho=[]

#variável para manter o while rodando até o usuário decidir parar
fim="CONTINUAR"





#programa para realizar as compras, usando estrutura de repetição while para o usuário poder adicionar vários itens ao carrinho
while fim!="FINALIZAR":
    #variável para o usuário informar o produto que busca
    r=str(input("Digite um dos materias que procura: latinhas, papelão, vidro, madeira, isopor, plástico, metal, tecido\n"))
    #se o usuário procurar por plástico, rodará este pedaço do código
    if r=="plástico" or r=="PLÁSTICO" or r=="plastico" or r=="PLASTICO":
        #print para separar o código, para poder entender melhor no console
        print("-"*20)
        print("Temos os seguintes anúncios:\n")
        #o programa printa os elementos presentes no dicionário, referentes à busca do usuário, nesse caso, referente plástico (1), e pega cada item dentro dessa categoria
        print("Produto:", produtos[1][0], "/ Quantidade:", produtos[1][1], "/ Preço por unidade:", produtos[1][2], "/ Rua:", produtos[1][3])
        print("-"*20)
        #variável para o usuário informar se quer adicionar os itens ao carrinho
        r1=str(input("Deseja os itens desse anúncio? Digite SIM ou NÃO: "))
        print("-"*20)
        #se o usuário quiser os itens o programa rodará este pedaço
        if r1=="SIM" or r1=="sim" or r1=="s" or r1=="ss":
            #o programa os adiciona no carrinho (lista)
            carrinho.append(produtos[1])
            print("-"*20)
            print("Os itens foram adicionados ao seu carriho!\n")
            #o usuário decide se vai continuar as compras ou parar por aqui
            fim=str(input("CONTINUAR as compras ou FINALIZAR?: "))
        else:
            continue
    #se o usuário procurar por vidro, rodará este pedaço do código
    #o código funciona no mesmo esquema que foi citado acima, apenas troca a busca pela respectiva posiçao do material procrado
    elif r=="vidro" or r=="VIDRO":
        print("-"*20)
        print("Temos os seguintes anúncios:\n")
        print("Produto:", produtos[2][0], "/ Quantidade:", produtos[2][1], "/ Preço por unidade:", produtos[2][2], "/ Rua:", produtos[2][3])
        print("-"*20)
        r1=str(input("Deseja os itens desse anúncio? Digite SIM ou NÃO: "))
        if r1=="SIM" or r1=="sim" or r1=="s" or r1=="ss":
            carrinho.append(produtos[2])
            print("Os itens foram adicionados ao seu carriho!\n")
            fim=str(input("CONTINUAR as compras ou FINALIZAR?: "))
        else:
            continue
    #se o usuário procurar por papelão, rodará este pedaço do código
    elif r=="papelão" or r=="PAPELÃO" or r=="papelao" or r=="PAPELAO":
        print("-"*20)
        print("Temos os seguintes anúncios:\n")
        print("Produto:", produtos[3][0], "/ Quantidade:", produtos[3][1], "/ Preço por unidade:", produtos[3][2], "/ Rua:", produtos[3][3])
        print("-"*20)
        r1=str(input("Deseja os itens desse anúncio? Digite SIM ou NÃO: "))
        if r1=="SIM" or r1=="sim" or r1=="s" or r1=="ss":
            carrinho.append(produtos[3])
            print("Os itens foram adicionados ao seu carriho!\n")
            fim=str(input("CONTINUAR as compras ou FINALIZAR?: "))
        else:
            continue
    #se o usuário procurar por isopor, rodará este pedaço do código
    elif r=="isopor" or r=="ISOPOR":
        print("-"*20)
        print("Temos os seguintes anúncios:\n")
        print("Produto:", produtos[4][0], "/ Quantidade:", produtos[4][1], "/ Preço por unidade:", produtos[4][2], "/ Rua:", produtos[4][3])
        print("-"*20)
        r1=str(input("Deseja os itens desse anúncio? Digite SIM ou NÃO: "))
        if r1=="SIM" or r1=="sim" or r1=="s" or r1=="ss":
            carrinho.append(produtos[4])
            print("Os itens foram adicionados ao seu carriho!\n")
            fim=str(input("CONTINUAR as compras ou FINALIZAR?: "))
        else:
            continue
    #se o usuário procurar por latinha, rodará este pedaço do código
    elif r=="latinha" or r=="LATINHA":
        print("-"*20)
        print("Temos os seguintes anúncios:\n")
        print("Produto:", produtos[5][0], "/ Quantidade:", produtos[5][1], "/ Preço por unidade:", produtos[5][2], "/ Rua:", produtos[5][3])
        print("-"*20)
        r1=str(input("Deseja os itens desse anúncio? Digite SIM ou NÃO: "))
        if r1=="SIM" or r1=="sim" or r1=="s" or r1=="ss":
            carrinho.append(produtos[5])
            print("Os itens foram adicionados ao seu carriho!\n")
            fim=str(input("CONTINUAR as compras ou FINALIZAR?: "))
        else:
            continue
    #se o usuário procurar por madeira, rodará este pedaço do código
    elif r=="madeira" or r=="MADEIRA":
        print("-"*20)
        print("Temos os seguintes anúncios:\n")
        print("Produto:", produtos[6][0], "/ Quantidade:", produtos[6][1], "/ Preço por unidade:", produtos[6][2], "/ Rua:", produtos[6][3])
        print("-"*20)
        r1=str(input("Deseja os itens desse anúncio? Digite SIM ou NÃO: "))
        if r1=="SIM" or r1=="sim" or r1=="s" or r1=="ss":
            carrinho.append(produtos[6])
            print("Os itens foram adicionados ao seu carriho!\n")
            fim=str(input("CONTINUAR as compras ou FINALIZAR?: "))
        else:
            continue
    #se o usuário procurar por metal, rodará este pedaço do código
    elif r=="metal" or r=="METAL":
        print("-"*20)
        print("Temos os seguintes anúncios:\n")
        print("Produto:", produtos[7][0], "/ Quantidade:", produtos[7][1], "/ Preço por unidade:", produtos[7][2], "/ Rua:", produtos[7][3])
        print("-"*20)
        r1=str(input("Deseja os itens desse anúncio? Digite SIM ou NÃO: "))
        if r1=="SIM" or r1=="sim" or r1=="s" or r1=="ss":
            carrinho.append(produtos[7])
            print("Os itens foram adicionados ao seu carriho!\n")
            fim=str(input("CONTINUAR as compras ou FINALIZAR?: "))
        else:
            continue
    #se o usuário procurar por tecido, rodará este pedaço do código
    elif r=="tecido" or r=="TECIDO":
        print("-"*20)
        print("Temos os seguintes anúncios:\n")
        print("Produto:", produtos[8][0], "/ Quantidade:", produtos[8][1], "/ Preço por unidade:", produtos[8][2], "/ Rua:", produtos[8][3])
        print("-"*20)
        r1=str(input("Deseja os itens desse anúncio? Digite SIM ou NÃO: "))
        if r1=="SIM" or r1=="sim" or r1=="s" or r1=="ss":
            carrinho.append(produtos[8])
            print("Os itens foram adicionados ao seu carriho!\n")
            fim=str(input("CONTINUAR as compras ou FINALIZAR?: "))
        else:
            continue






#parte final para realizar a soma dos itens no carrinho
#variável para definir a soma inicial em 0
soma=0
#condição usada para linkar o final da repetição While à esta parte final
if fim=="FINALIZAR":
    print("-"*20)
    print("-"*20)
    print("Este é seu carrinho de compras:\n")
    print("-"*20)
    #o programa procura pelos itens do carri nho
    for i in carrinho:
        #o programa printa os itens do carrinho
        print("Produto:", i[0], "/ Quantidade:", i[1], "/ Preço:", i[2], "/ Rua:", i[3])
        print("-"*20)
        #calculo do preço dos itens do carrinho
        calculo=i[1]*i[2]
        soma=soma+calculo
    print("-"*20)
    #o programa printa o preço final
    print(f"O preço final da sua compra é {soma} reais")
    #o usuario decide se vai continuar a compra
    r2=str(input("Finalizar compra? "))
    print("-"*20)


    if r2=="SIM"or r2=="sim" or r2=="s" or r2=="ss" or r2=="FINALIZAR" or r2=="finalizar":
        print("-"*20)
        r3=int(input("Qual a forma de pagamento?\n PIX [1]  Cartão de crédito [2]  Cartão de débito [3] \n"))
        print("-"*20)
        if r3==1:
            print("Chave PIX: 40238917409823\n")
            print("Aguardando pagemento...\n")
            print("Aguardando pagemento...\n")
            print("Aguardando pagemento...\n")
            print("Pagamento recebido, retire seus produtos nas ruas: ")
            for i in carrinho:
                print("Rua:", i[3])
                print("-"*20)
            print("Finalizado.")
        if r3==2 or r3==3:
            cartao=str(input("Nome: "))
            cartao1=int(input("Digite o CPF: "))
            cartao2=int(input("Digite a data de vencimento no formato XX.XX.XX: "))
            cartao3=int(input("Digite o CVV: "))
            print("Aguardando pagemento...")
            print("Aguardando pagemento...")
            print("Aguardando pagemento...")
            print("Pagamento recebido, retire seus produtos nas ruas: ")
            for i in carrinho:
                print("Rua:", i[3])
                print("-"*20)
            print("Finalizado.")
    else:
        print("Compra cancelada. Programa finalizado.")