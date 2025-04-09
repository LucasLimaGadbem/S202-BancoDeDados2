from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def clean(tx):
    try:
        tx.run("MATCH(n) DETACH DELETE n;")
    except:
        print("Erro ao excluir...")
        raise

def get_cachorro(tx):
    query = """
        MATCH (n {caracteristica: 'Cachorro'}) 
        RETURN n.nome AS nome;
    """
    try:
        result = tx.run(query)
        return [{
            'nome': row['nome']
        } for row in result]

    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise

def get_feminino(tx):
    query = """
        MATCH (n {sexo: 'Feminino'}) 
        RETURN DISTINCT n.nome AS nome;
    """
    try:
        result = tx.run(query)
        return [{
            'nome': row['nome']
        } for row in result]

    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise

def get_masculino(tx):
    query = """
        MATCH (n {sexo: 'Masculino'}) 
        RETURN DISTINCT n.nome AS nome;
    """
    try:
        result = tx.run(query)
        return [{
            'nome': row['nome']
        } for row in result]

    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise


def get_engenheiro(tx):
    query = """
        MATCH (n {caracteristica: 'Engenheiro'}) 
        RETURN DISTINCT n.nome AS nome;
    """
    try:
        result = tx.run(query)
        return [{
            'nome': row['nome']
        } for row in result]

    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise


def create_database(tx, par_ser, par_caracteristica, par_nome, par_sexo, par_idade):
    labels = par_ser + ":" + par_caracteristica
    query = f"""
        CREATE (n:{labels} {{
            nome: $nome_query,
            sexo: $sexo_query,
            idade: $idade_query,
            caracteristica: $caracteristica_query
        }})
        RETURN 
            n.nome AS nome,
            n.sexo AS sexo,
            n.idade AS idade;
    """
    try:
        result = tx.run(
            query,
            nome_query = par_nome,
            sexo_query = par_sexo,
            idade_query = par_idade,
            caracteristica_query = par_caracteristica
        )
        return [{
            'nome':row['nome'],
            'sexo':row['sexo'],
            'idade':row['idade']
        } for row in result]

    except ServiceUnavailable as exception:

        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise


def main():
    uri = "neo4j://localhost:7687"
    user = "neo4j"
    password = "neo4jneo4j"

    driver = GraphDatabase.driver(uri, auth=(user, password))

    print("Limpando dados...")
    with driver.session() as session:
        session.execute_write(clean)

    print("Criando o banco de dados...")
    with driver.session() as session:

        result = session.execute_write(create_database, "Humano", "Professora", "Suelen", "Feminino", 56)
        result = session.execute_write(create_database, "Humano", "Medica", "Anaile", "Feminino", 26)
        result = session.execute_write(create_database, "Humano", "Quimica", "Cristiane", "Feminino", 26)
        result = session.execute_write(create_database, "Humano", "Engenheiro", "Luiz", "Masculino", 31)
        result = session.execute_write(create_database, "Humano", "Secretaria", "Mariana", "Feminino", 76)
        result = session.execute_write(create_database, "Humano", "Economista", "Suzi", "Feminino", 48)
        result = session.execute_write(create_database, "Humano", "Empreendedor", "Adriano", "Masculino", 52)
        result = session.execute_write(create_database, "Animal", "Cachorro", "Athena", "Feminino", 10)
        result = session.execute_write(create_database, "Animal", "Cachorro", "Pipoca", "Feminino", 6)
        result = session.execute_write(create_database, "Animal", "Cachorro", "Esmeralda", "Feminino", 4)
        session.run("Match (s:Humano{nome: 'Skelen'}),(b:Animal{nome:'Bela'}),(a:Humano{nome: 'Ana'})" \
        ",(c:Humano{nome: 'Clara'}),(l:Humano{nome: 'Lucas'}), (p:Animal{nome: 'Pituca'}), "\
        "(lun:Animal{nome: 'Luna'}), (chr:Humano{nome: 'Christina'}), (skel:Humano{nome: 'Skelsen'})," \
        "(adr:Humano{nome: 'Adriano'})"\
        "CREATE (l)-[:DONO]->(b)"\
        "CREATE (a)-[:DONO]->(p)"\
        "CREATE (c)-[:DONO]->(lun)"\
        "CREATE (s)-[:MAE]->(a)"\
        "CREATE (s)-[:MAE]->(c)"\
        "CREATE (s)-[:MAE]->(l)"\
        "CREATE (b)-[:MAE]->(p)"\
        "CREATE (a)-[:FILHA]->(s)"\
        "CREATE (c)-[:FILHA]->(s)"\
        "CREATE (l)-[:FILHO]->(s)"\
        "CREATE (p)-[:FILHA]->(b)"\
        "CREATE (a)-[:IRMA]->(c)"\
        "CREATE (c)-[:IRMA]->(a)"\
        "CREATE (l)-[:IRMAO]->(a)"\
        "CREATE (a)-[:IRMA]->(l)"\
        "CREATE (l)-[:IRMAO]->(c)"\
        "CREATE (c)-[:IRMA]->(l)"\
        "CREATE (b)-[:IRMA]->(lun)"\
        "CREATE (p)-[:IRMA]->(lun)"\
        "CREATE (lun)-[:IRMA]->(b)"\
        "CREATE (lun)-[:IRMA]->(p)"\
        "CREATE (skel)-[:IRMA]->(s)"\
        "CREATE (s)-[:IRMA]->(skel)"\
        "CREATE (adr)-[:MARIDO]->(skel)"\
        "CREATE (skel)-[:ESPOSA]->(adr)"\
        "CREATE (s)-[:TIA]->(a)"\
        "CREATE (s)-[:TIA]->(c)"\
        "CREATE (s)-[:TIA]->(l)"\
        "CREATE (adr)-[:TIO]->(a)"\
        "CREATE (adr)-[:TIO]->(c)"\
        "CREATE (adr)-[:TIO]->(l)"\
        "CREATE (chr)-[:MAE]->(s)"\
        "CREATE (chr)-[:MAE]->(skel)"\
        "CREATE (chr)-[:VO]->(a)"\
        "CREATE (chr)-[:VO]->(c)"\
        "CREATE (chr)-[:VO]->(l)"\
        "CREATE (a)-[:NETA]->(chr)"\
        "CREATE (c)-[:NETA]->(chr)"\
        "CREATE (l)-[:NETO]->(chr)"\
        "CREATE (a)-[:SOBRINHA]->(skel)"\
        "CREATE (c)-[:SOBRINHA]->(skel)"\
        "CREATE (l)-[:SOBRINHO{desde: 2003}]->(skel)"\
        "CREATE (a)-[:SOBRINHA]->(adr)"\
        "CREATE (c)-[:SOBRINHA]->(adr)"\
        "CREATE (l)-[:SOBRINHO]->(adr)"
        )
        
    flag = True
    while flag:
        print("Escolha uma opção:")
        print("1 - Listar todos os cachorros")
        print("2 - Listar todos as mulheres e cachorras")
        print("3 - Listar todos os engenheiros")
        print("4 - Listar todos os homens")
        print("5 - Sair")
        op = input("Digite a opcao desejada: ")
        with driver.session() as session:
            if op == "1":
                cachorros = session.execute_read(get_cachorro)
                print("Cachorros:")
                for c in cachorros:
                    print(c['nome'])
            elif op == "2":
                femininos = session.execute_read(get_feminino)
                print("Femininos:")
                for f in femininos:
                    print(f['nome'])
            elif op == "3":
                engs = session.execute_read(get_engenheiro)
                print("Engenheiro:")
                for a in engs:
                    print(a['nome'])
            elif op == "4":
                masculino = session.execute_read(get_masculino)
                print("Masculino:")
                for f in masculino:
                    print(f['nome'])
            elif op == "5":
                print("Saindo...")
                flag = False
            else:
                print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()