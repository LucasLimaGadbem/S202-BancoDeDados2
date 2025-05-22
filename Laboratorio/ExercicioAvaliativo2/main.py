from database import Database
from teacher_crud import TeacherCRUD
from cli import TeacherCLI
from query import TeacherDatabase

db = Database('bolt://34.200.239.66', 'neo4j', 'searches-hunks-police')

teacherDB = TeacherDatabase(db)
teacherCRUD = TeacherCRUD(db)
teacherCLI = TeacherCLI(teacherCRUD)

print("=== Questao 1 ===")
teacherDB.nome_professor()
teacherDB.inicial_professor()
teacherDB.cidade()
teacherDB.escola()

print("=== Questao 2 ===")
teacherDB.idade_professor()
teacherDB.media_populacao()
teacherDB.cep_cidade()
teacherDB.terceira_letra()

print("=== Questao 3 ===")
teacherCRUD.create('Chris Lima', 1956, '189.052.396-66')
chris = teacherCRUD.read("Chris Lima")
print(f"    Ano de Nascimento: {chris[0][0]}    CPF: {chris[0][1]}")
teacherCRUD.update("Chris Lima", "162.052.777-77")
chris = teacherCRUD.read("Chris Lima")
print(f"    Ano de Nascimento: {chris[0][0]}    CPF: {chris[0][1]}")
teacherCLI.run()


db.close()