from database import Database
from game import game

db = Database('bolt://13.218.187.4', 'neo4j', 'survivals-students-hood')
db.drop_all()

game_db = game(db)

game_db.create_player("Lucas")
game_db.create_player("Ana")
game_db.create_player("Clara")

game_db.create_match([("Lucas", 200), ("Ana", 100)])
game_db.create_match([("Ana", 200), ("Clara", 100)])
game_db.create_match([("Clara", 300), ("Lucas", 250)])

print(game_db.get_players())
print(game_db.get_match(2))
print(game_db.get_player_hist(1))

db.close()