from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokedex = Pokedex(db)

#pesquisando o pokemon de id 7
pokedex.getById(7)

#pesquisando o pokemon de numero 106
pokedex.getByNum("106")

#pesquisando os pokemons que evoluem de Bulbasaur
pokedex.getByPrevEvolution("Bulbasaur")

#pesquisando o pokemon Charmander
pokedex.getByName("Charmander")

#pesquisando os pokemons que começam ou terminam com a letra S
pokedex.getByInicialFinal('R')