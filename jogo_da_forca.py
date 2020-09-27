# jogo da forca
# algoritmo implementado com interface em linha de comando

import sys

palavra = ""   # palavra a ser digitada no começo do jogo, para os jogadores adivinharem
dica1 = ""   # dica relacionada à palavra
dica2 = ""   # dica relacionada à palavra
letras = []  # lista de letras da palavra
chances = 6   # quantidade de chances que o jogador possui

# função que indica os passos iniciais do jogo
def inicio():
    palavra = input("Digite a palavra para começar o jogo:")
    dica1 = input("Digita a dica 1 para o jogador:")
    dica2 = input("Digite a dica 2 para o jogador:")

    # separa as letras da palavra, colocando cada uma como um índice de uma lista
    for char in range(len(palavra)):
        letras.append(palavra[char])

    # identifica a quantidade de letras da palavras
    numero_letras = len(letras)

    for i in range(100):
        print("\n")

    print("\n" "A palavra possui", numero_letras, "letras:")

    # mostra a quantidade de espaços correspondentes às letras da palavra
    for i in range(numero_letras):
        print(" __ ", end = '')

    print("\n" "Dica 1:", dica1,
          "\n" "Dica 2:", dica2)


# função que diminui o número de chances do usuário de acordo com certas circunstâncias
def diminuir_chances(chances):
    # se ainda restarem chances para o usuário e se a resposta for considerada falsa uma chance é diminuída
    if chances != 0:
        chances -= 1
        return chances
    else:
        return 0


# função que desenha os bonecos de acordo com a quantidade de chances restantes
def desenha_boneco(chances):
    # o boneco possui 6 partes, que são correspondentes à quantidade de chances totais
    # partes do boneco: cabeça, tronco, braço direito, braço esquerdo, perna direita, perna esquerda

    if chances == 1:
        print(" O ")

    elif chances == 2:
        print(" O " "\n",
              " |")

    elif chances == 3:
        print("  O " "\n",
              "/|")

    elif chances == 4:
        print("  O " "\n",
              "/|" "\\")

    elif chances == 5:
        print("  O " "\n",
              "/|" "\\" "\n",
              "/")
    elif chances == 6:
        print("  O " "\n",
          "/|" "\\" "\n",
          "/" "\\")



def comparar_resposta(letras, resposta):
    for i in range(len(letras)):
        if letras[i] == resposta:   # se a letra da palavra for igual a resposta dada pelo usuário
            return True   # retorna que a resposta está certa

    return False   # retorna que a resposta está errada, caso a resposta não corresponda com uma letra existente na palavra

    '''
    nas linhas seguintes tem outra possível implmentação do código acima com 'for each':
    
    cont = 0   # contador da posição da letra
    for i in letras:
        if i == resposta:   # se a letra da palavra for igual a resposta dada pelo usuário
            return (True, cont)   # retorna que a resposta está certa e a posição da letra
            cont += 1

    return False    # retorna que a resposta está errada, caso a resposta não corresponda com uma letra existente na palavra
    '''


# main
inicio()

espacos_vazios = []
for x in range(len(letras)):   # cria um lista com os espaços vazios correspondetes às letras para mostrar ao jogador
    espacos_vazios.append(" __ ")

while chances != 0:
    print("\n")
    desenha_boneco(chances)
    resposta = input("digite uma letra:")

    bool_resposta = comparar_resposta(letras, resposta)

    if bool_resposta == False:
        print("Resposta errada.")
        chances = diminuir_chances(chances)

        if chances != 0:
            print("Você perdeu uma chance. Você possui", chances, " chances.")
        else:
            print("Game Over")
            sys.exit()

    elif bool_resposta == True:
        print("Resposta certa.")

        for y in range((len(letras))):
            if letras[y] == resposta:   # se a letra estiver certa, ela é substituída no respectivo espaço vazio
                espacos_vazios[y] = resposta

    print("Palavra:", espacos_vazios)

    if espacos_vazios == letras:   # caso toda a palavra seja descoberta
        break

print("Você ganhou o jogo.")