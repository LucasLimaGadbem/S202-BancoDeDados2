from MotoristaDAO import MotoristaDAO
from Passageiro import Passageiro
from Motorista import Motorista
from Corrida import Corrida

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input('Enter a command: ')
            if command == 'quit':
                print('Goodbye!')
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print('Invalid command. Try again.')

class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO: MotoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command('create', self.create_motorista)
        self.add_command('read', self.read_motorista)
        self.add_command('update', self.update_motorista)
        self.add_command('delete', self.delete_motorista)

    def create_motorista(self):
        corridas = []

        while True:
            nota = int(input('Nota da corrida: '))
            distancia = float(input('Distância percorrida: '))
            valor = float(input('Valor da corrida: '))

            nome_passageiro = input('Nome do passageiro: ')
            documento_passageiro = input('Documento do passageiro: ')

            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)

            if input('Deseja adicionar outra corrida? (S/N): ').strip().lower() != 's':
                break

        nota_media = sum(corrida.nota for corrida in corridas) // len(corridas)
        motorista = Motorista(corridas, nota)

        self.motoristaDAO.create_motorista(motorista)

    def read_motorista(self):
        motorista_id = input("ID do motorista: ")
        motorista = self.motoristaDAO.read_motorista_by_id(motorista_id)

        if motorista:
            print(f'Nota média: {motorista["nota"]}')
            print('Corridas: ')
            for corrida in motorista["corridas"]:
                passageiro = corrida["passageiro"]

                print(f'\tNota: {corrida["nota"]}')
                print(f'\tDistância: {corrida["distancia"]}')
                print(f'\tValor: {corrida["valor"]}')

                print('\tPassageiro: ')
                print(f'\t\tNome: {passageiro["nome"]}')
                print(f'\t\tDocumento: {passageiro["documento"]}')
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        
        motorista_id = input("ID do motorista: ")
        motorista = self.motoristaDAO.read_motorista_by_id(motorista_id)

        if motorista:
            corridas = []

            while True:
                nota = int(input('Nota da corrida: '))
                distancia = float(input('Distância percorrida: '))
                valor = float(input('Valor da corrida: '))

                nome_passageiro = input('Nome do passageiro: ')
                documento_passageiro = input('Documento do passageiro: ')

                passageiro = Passageiro(nome_passageiro, documento_passageiro)
                corrida = Corrida(nota, distancia, valor, passageiro)

                corridas.append(corrida)

                if input('Deseja adicionar outra corrida? (S/N): ').strip().lower() != 's':
                    break

            nota_media = sum(corrida.nota for corrida in corridas) // len(corridas)
            novo_motorista = Motorista(corridas, nota_media)

            self.motoristaDAO.update_motorista_by_id(motorista_id, novo_motorista)
        else:
            print("Motorista não encontrado.")


    def delete_motorista(self):
        id = input('Entre com o id: ')
        self.motoristaDAO.delete_motorista(id)

    def run(self):
        print('Bem vindo ao motorista CLI!')
        print('Comandos: create, read, update, delete, quit')
        super().run()