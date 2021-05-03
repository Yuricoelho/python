
def jogar():
    print("********************************")
    print("Bem-vindo ao jogo da forca!")
    print("********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou  = False

    while(not enforcou and not acertou):

        chute = input("Escolha uma letra para tentar ganhar adivinhas a palavra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Econtrei a letra {} na posição {} ".format(letra, index))
            index += 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()