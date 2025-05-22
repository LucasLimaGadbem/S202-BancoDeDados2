class TeacherDatabase:
    def __init__(self, database):
        self.db = database
    
    def nome_professor(self):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": "Renzo"}
        results = self.db.execute_query(query, parameters)
        for record in results:
            print(f'Ano de nascimento: {record["ano_nasc"]} \nCPF: {record["cpf"]}')
    
    def inicial_professor(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        for record in results:
            print(f'Nome: {record["name"]} \nCPF: {record["cpf"]}')
    
    def cidade(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        results = self.db.execute_query(query)
        for record in results:
            print(f'Cidade: {record["name"]}')
    
    def escola(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address, s.number AS number"
        results = self.db.execute_query(query)
        for record in results:
            print(f'Escola: {record["name"]} \nEndereco: {record["address"]} \nNumero: {record["number"]}')    

    def idade_professor(self):
        query = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS jovem, MIN(t.ano_nasc) AS velho"
        results = self.db.execute_query(query)
        return (results[0]["jovem"], results[0]["velho"])

    def media_populacao(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS avg_population"
        results = self.db.execute_query(query)
        return results[0]["avg_population"]

    def cep_cidade(self):
        query = "MATCH (c:City) WHERE (c.cep = '37540-000') RETURN REPLACE(c.name, 'a', 'A') AS nome_a"
        results = self.db.execute_query(query)
        return results[0]["nome_a"]

    def terceira_letra(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS char"
        results = self.db.execute_query(query)
        for record in results:
            print(f'Terceira letra do nome: {record['char']}')