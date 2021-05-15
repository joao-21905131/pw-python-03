
from exercicio_2.analise_pasta import *
def main():
    pasta = pede_pasta()
    dadosFicheiros = faz_calculos(pasta)
    guarda_resultados(pasta)
    faz_grafico_barras(dadosFicheiros)
    faz_grafico_queijos(dadosFicheiros)


if __name__ == "__main__":
    main()