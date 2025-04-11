from Corrida import Corrida

class Motorista:
    def __init__(self, corridas: list[Corrida], nota: int):
        self.corridas = corridas
        self.nota = nota

    def get_info(self):
        return {
            "corridas": [corrida.get_info() for corrida in self.corridas],
            "nota": self.nota
        }