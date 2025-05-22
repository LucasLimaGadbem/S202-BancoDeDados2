class TeacherCRUD():
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        result = self.db.execute_query(query, {'name': name, 'ano_nasc': ano_nasc, 'cpf': cpf})
        if result is not None:
            print(f'O professor {name} foi criado no banco de dados')
    
    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["ano_nasc"], result["cpf"]) for result in results]

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        result = self.db.execute_query(query, {'name': name})
        if result is not None:
            print(f'O professor {name} foi deletado do banco de dados')

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        result = self.db.execute_query(query, {'name': name, 'newCpf': newCpf})
        if result is not None:
            print(f'O professor {name} foi alterado, novo cpf: {newCpf}')