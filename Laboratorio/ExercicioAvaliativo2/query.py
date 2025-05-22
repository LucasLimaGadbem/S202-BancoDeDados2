class TeacherDatabase:
    def __init__(self, database):
        self.db = database
    
    # Buscar professor pelo nome
    def get_teacher_name(self):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": "Renzo"}
        results = self.db.execute_query(query, parameters)
        for record in results:
            print(f'Ano de nascimento: {record["ano_nasc"]} \nCPF: {record["cpf"]}')
    
    # Buscar professor pela inicial
    def get_teacher_initial(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        for record in results:
            print(f'Nome: {record["name"]} \nCPF: {record["cpf"]}')
    
    # Buscar nome de todas as cidades
    def get_city(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        results = self.db.execute_query(query)
        for record in results:
            print(f'Cidade: {record["name"]}')
    
    # Buscar escola por uma faixa de valores do seu número
    def get_school(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address, s.number AS number"
        results = self.db.execute_query(query)
        for record in results:
            print(f'Escola: {record["name"]} \nEndereco: {record["address"]} \nNumero: {record["number"]}')    

    # Buscar professor mais jovem e mais velho
    def get_teacher_age(self):
        query = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS jovem, MIN(t.ano_nasc) AS velho"
        results = self.db.execute_query(query)
        return (results[0]["jovem"], results[0]["velho"])

    # Buscar média dos habitantes das cidades
    def get_avg_population(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS avg_population"
        results = self.db.execute_query(query)
        return results[0]["avg_population"]

    # Buscar cidade pelo CEP e substituir "a" por "A" no nome
    def get_city_cep(self):
        query = "MATCH (c:City) WHERE (c.cep = '37540-000') RETURN REPLACE(c.name, 'a', 'A') AS nome_a"
        results = self.db.execute_query(query)
        return results[0]["nome_a"]

    # Buscar 3ª letra do nome dos professores
    def get_teacher_char(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS char"
        results = self.db.execute_query(query)
        for record in results:
            print(f'Terceira letra do nome: {record['char']}')