def pede_nome():
    while(True):
        try:
            nomeFicheiro = input("nome do ficheiro:")
            print(nomeFicheiro)
            f = open(nomeFicheiro)
            print("Ficheiro lido com sucesso")
            f.close()
            return nomeFicheiro
        except OSError:
            print("Não conseguiu abrir o ficheiro: ",nomeFicheiro)


def gera_nome(nome,listaDados):
    # troca a parte final por json
    parte = nome.split(".")[0] + ".json"
    # abre o novo ficheiro
    p1 = open(parte,"w")
    #escreve os dados
    p1.write(str(listaDados))
    #fecha o ficheiro
    p1.close()
