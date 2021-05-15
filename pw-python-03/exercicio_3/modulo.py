import os
import math
def pede_pasta():
    while(True):
        try:
            nomeFicheiro = input("nome do ficheiro:")
            if os.path.isdir(nomeFicheiro):
                return nomeFicheiro

        except OSError:
            print("Não conseguiu abrir o ficheiro: ",nomeFicheiro)




def calcula_tamanho_pasta(pasta):
    soma=0
    for nome in os.listdir(pasta):
        junta = os.path.join(pasta,nome)
        if os.path.isfile(junta):
            soma += os.path.getsize(junta) / (1024*1024)
        if os.path.isdir(junta):
            soma += calcula_tamanho(junta)
    return soma

def main():
    fich = pede_pasta()
    tamanho = calcula_tamanho_pasta(fich)
    print(f"O tamanho é:{tamanho}")

if __name__ == "__main__":
    main()