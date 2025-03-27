from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import BookCLI

db = Database(database = "relatorio_05", collection = "Livros")
bookModel = BookModel(database=db)
db.resetDatabase()
#01 - create
#personModel.create_person("Lucas", 21)

#02 - read
#personModel.read_person_by_id('67e55facc63d9785dda4afc5')

#03 - update
#personModel.update_person('67e55facc63d9785dda4afc5', 'Virginia', 20)

#04 - delete
#personModel.delete_person('67e55facc63d9785dda4afc5')

bookCLI = BookCLI(bookModel)
bookCLI.run()