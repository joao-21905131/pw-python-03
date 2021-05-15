
from exercicio_1.analisa_ficheiro import *
from exercicio_1.analisa_ficheiro.calculos import *
import json

def main():
    ficheiro = pede_nome()
    #guardar os valores
    listaDados = {}
    listaDados["Numero de linhas"] = calcula_linhas(ficheiro)
    listaDados["Numero de caracteres no ficheiro"] = calcula_caracteres(ficheiro)
    listaDados["Palavra mais comprida"] = calcula_palavra_comprida(ficheiro)
    listaDados["Numero de ocorrencias"] = calcula_ocorrencia_de_letras(ficheiro)
    #vai gerir um ficheiro .json com os dados calculados anteriormente
    gera_nome(ficheiro,listaDados)

if __name__ == '__main__':
    main()