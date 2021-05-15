from automovel import automovel
def main():
    a1 = automovel(60, 10, 15)
    print("autonomia")
    print(a1.autonomia())
    print("abastecimento")
    print(a1.abastece(45))
    print("distancia")
    print(a1.percorre(150))
    print("distancia 2")
    print(a1.percorre(250))

if __name__ == "__main__":
        main()