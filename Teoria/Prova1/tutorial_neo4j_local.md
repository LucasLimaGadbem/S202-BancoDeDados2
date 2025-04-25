### **Baixar e Executar um Container Neo4j**

1. **Baixar a imagem do Neo4j:**
   - No **Prompt de Comando** ou no **PowerShell**, execute:
     ```bash
     docker pull neo4j
     ```

2. **Executar o container Neo4j:**
   - Execute o seguinte comando para iniciar o Neo4j em um container:
     ```bash
     docker run -d --name neo4j-container -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/neo4jtest neo4j
     ```
     - **`-d`**: Executa o container em segundo plano.
     - **`--name neo4j-container`**: Dá o nome "neo4j-container" ao container.
     - **`-p 7474:7474`**: Mapeia a porta 7474 do container para a porta 7474 do host (interface web).
     - **`-p 7687:7687`**: Mapeia a porta 7687 do container para a porta 7687 do host (conexão Bolt para aplicações).
     - **`-e NEO4J_AUTH=neo4j/neo4jtest`**: Define as credenciais do Neo4j. Aqui, o usuário é `neo4j` e a senha é `neo4jtest`.

3. **Verificar se o Neo4j está rodando:**
   - Execute:
     ```bash
     docker ps
     ```
   - O Neo4j deve aparecer na lista de containers ativos.

4. **Acessar a interface web do Neo4j:**
   - Abra um navegador e acesse [http://localhost:7474](http://localhost:7474).
   - Faça login com as credenciais configuradas (`neo4j` e `neo4jtest`).

---

### **Acessar o Neo4j com um Script Python**

1. **Instalar a biblioteca `neo4j` no Python:**
   - Certifique-se de que você tem o Python instalado (recomenda-se usar o Python 3).
   - No terminal, execute:
     ```bash
     pip install neo4j
     ```

2. **Criar um script Python para se conectar ao Neo4j:**
   - Crie um arquivo chamado `neo4j_test.py` e insira o seguinte código:
     ```python
     from neo4j import GraphDatabase

     # Configurar conexão
     uri = "bolt://localhost:7687"  # URL do Neo4j
     username = "neo4j"  # Nome de usuário
     password = "neo4jtest"   # Senha

     # Criar driver
     driver = GraphDatabase.driver(uri, auth=(username, password))

     def test_connection():
         try:
             with driver.session() as session:
                 greeting = session.write_transaction(lambda tx: tx.run("RETURN 'Conexão com Neo4j bem-sucedida!'").single()[0])
                 print(greeting)
         except Exception as e:
             print(f"Erro ao conectar ao Neo4j: {e}")

     def insert_and_query():
         with driver.session() as session:
             # Inserir dados
             session.write_transaction(lambda tx: tx.run("CREATE (p:Person {name: 'Alice'})"))
             # Consultar dados
             result = session.read_transaction(lambda tx: tx.run("MATCH (p:Person {name: 'Alice'}) RETURN p.name").single())
             print("Nome recuperado:", result[0])

     # Testar conexão e executar operações
     test_connection()
     insert_and_query()

     # Fechar o driver
     driver.close()
     ```

3. **Executar o script:**
   - No terminal, execute:
     ```bash
     python neo4j_test.py
     ```
   - Se tudo estiver configurado corretamente, você verá a mensagem de conexão bem-sucedida e o nome recuperado do banco de dados Neo4j.