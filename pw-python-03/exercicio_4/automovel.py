class automovel:
    def __init__(self, cap_dep, quant_comb, consumo):
        self.capacidade = cap_dep
        self.quantidade = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quantidade

    def abastece(self,combustivel):

        if combustivel + self.quantidade  <= self.capacidade:
            self.quantidade += combustivel
            return automovel.autonomia(self)
        else:
            return "Erro no abastecimengos"

    def percorre(self,distancia):
        if distancia <= automovel.autonomia(self):
            self.quantidade -= distancia*(self.consumo/100)
            return automovel.autonomia(self)
        else:
            return -1

    def autonomia(self):
        autono = (int)(self.quantidade / self.consumo * 100)
        return autono