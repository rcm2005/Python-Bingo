import random



def sortear_cartelas(numero_participantes):
    contador = 0
    conjunto_matrizes = []
    while contador != numero_participantes:
        matriz = []
        for i in range(0,5):
            linha = []
            for j in range(0,5):
                if j == 0:
                    item = random.randint(1, 15)
                elif j == 1:
                    item = random.randint(16, 30)
                elif j == 2:
                    item = random.randint(31, 45)
                elif j == 3:
                    item = random.randint(46, 60)
                elif j == 4:
                    item = random.randint(61, 75)
                linha.append(item)
            matriz.append(linha)
        conjunto_matrizes.append(matriz)
        contador +=1
    return conjunto_matrizes

def bingo():
    global numero_jogadores, matrizes
    #introduzindo o jogo
    print('******************************')
    print("Seja bem vindo ao Bingo Online")
    print('******************************')
    #coletando informações para o jogo
    numero_jogadores = int(input("Quantos jogadores vão participar do jogo (minimo 1, maximo 5)")) 
    


    matrizes = sortear_cartelas(numero_jogadores)


    
    

    for i in range(len(matrizes)):

        print("\n")
        ii = i + 1
        ii = str(ii)
        print("jogador  " + ii)

        for o in range(0,5):
              
            print(matrizes[i][o], end='\n')
            
        


    print("Número de cartelas geradas:", len(matrizes))

def mostrar_cartelas():
    global matrizes
    for i in range(len(matrizes)):

        print("\n")
        ii = i + 1
        ii = str(ii)
        print("jogador  " + ii)

        for o in range(0,5):
              
            print(matrizes[i][o], end='\n')





bingo()