from Database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI


db = Database(database = "ExercicioAvaliativo1", collection = "Motoristas")
db.resetDatabase()

motoristaDAO = MotoristaDAO(db)

MotoristaCLI = MotoristaCLI(motoristaDAO)
MotoristaCLI.run()