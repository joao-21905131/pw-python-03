import csv
import os
import math
from matplotlib import pyplot as plt

def pede_pasta():
    while(True):
        try:
            caminho = input("Indique o caminho da pasta:")
            if (os.listdir(caminho)):
                return caminho
        except IOError:
        print("Pasta não existente")

def faz_calculos(ficheiro):
    local = {}
    for i in os.listdir(ficheiro):
        i = os.path.splitext(i)

        if i[1]  in local:
            local[i[1]]['quantidade'] += 1
            local[i[1]]['volume'] += int(os.path.getsize(ficheiro + i[0] + i[1])/(1024))
        else:
            local[i[1]] = {'quantidade': 1, 'volume': int(os.path.getsize(ficheiro + i[0] + i[1])/(1024))}

    return local

def guarda_resultados(pasta,dados):
    nomeFicheiro = os.path.basename(pasta)
    with open(f"{nomeFicheiro}.csv","w",newline='') as f:
        dados=["Extensao", "Quantidade", "Tamanho[kByte]"]
        writer = csv.DictWriter(f,dados)
        writer.writeheader()
        for i in faz_calculos().keys():
            writer.writerow({'Extensao': i,
                             'Quantidade':faz_calculos().get(i)['quantidade'],
                             'Tamanho[kByte]':faz_calculos().get(i)['volume']})

def faz_grafico_queijos( dados):

    chave = [key for key in dados.keys()]
    valores_Quantidades = [dados[key]['quantidade'] for key in dados.keys()]
    plt.pie(valores_Quantidades, labels=chave, autopct='%1.0f%%')
    plt.title("Quantidades")
    plt.show()

    lista_valores_Tamanhos = [dados[key]['size'] for key in dados.keys()]
    plt.pie(lista_valores_Tamanhos, labels=chave, autopct='%1.0f%%')
    plt.title("Tamanhos")
    plt.show()

def faz_grafico_barras(dados):
    chave = [ key for key in dados.keys()]
    valores = [dados[key]["quantidade"]for key in dados.keys()]
    plt.bar(chave,valores)
    plt.title("Quantidades")
    plt.show()

    lista_valores_Tamanhos = [dados[key]['size'] for key in dados.keys()]
    plt.bar(chave, valores)
    plt.title("Tamanhos")
    plt.show()