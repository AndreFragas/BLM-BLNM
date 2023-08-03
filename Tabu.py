class Tabu:
    def __init__(self, indexMaquina, interacoes_saida):
        self.maquina = indexMaquina
        self.cont = 0
        self.interacoes_saida = interacoes_saida

    def incrementar_contador(self):
        self.cont += 1