import os
import sys

def calcula_linhas(nomeFicheiro):
    tamanho = 0
    f = open(nomeFicheiro,"r")
    lista = f.read()
    f.close()
    for i in lista.split("\n"):
        tamanho += 1

    return tamanho

def calcula_caracteres(nomeFicheiro):
    tamanho = 0
    f = open(nomeFicheiro)
    lista = f.read()
    f.close()
    for i in lista.split():
        tamanho += len(i)

    return tamanho

def calcula_palavra_comprida(nomeFicheiro):
    tamanhoMaior = 0
    f = open(nomeFicheiro)
    lista = f.read()
    f.close()
    for i in lista.split():
        if len(i)>tamanhoMaior:
            tamanhoMaior = len(i)
            palavra = i

    return palavra

def calcula_ocorrencia_de_letras(nomeFicheiro):
    f = open(nomeFicheiro)
    lista = f.read()
    f.close()
    list = {}
    for i in set (lista):
        list[i] = lista.count(i)
    return list