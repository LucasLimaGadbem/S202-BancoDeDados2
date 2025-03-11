from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self._database = database

    #pesquisa por id
    def getById(self, id: int):
        pokemon = self._database.collection.find_one({"id": id})
        nome = "pokemon"+str(id)
        writeAJson(pokemon, nome)

    #pesquisa por nome
    def getByName(self, name: str):
        pokemon = self._database.collection.find_one({"name": name})
        writeAJson(pokemon, name)

    #pesquisa por numero
    def getByNum(self, num: int):
        pokemon = self._database.collection.find_one({"num": num})
        nome = "pokemon"+str(num)
        writeAJson(pokemon, nome)
    
    #pesquisa por evolução anterior
    def getByPrevEvolution(self, name: str):
        pokemon = self._database.collection.find({"prev_evolution.name": name})
        nome = "pokemons_anteriores_a_"+name
        writeAJson(pokemon, nome)
    
    #pesquisa por inicial ou final
    def getByInicialFinal(self, letra: str):
        pokemon = self._database.collection.find({"name":{"$regex":f"^{letra}|{letra}$", "$options": "i"}})
        nome = "pokemons_inicial_final_"+letra
        writeAJson(pokemon, nome)