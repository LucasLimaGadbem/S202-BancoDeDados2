### **Baixar e Executar um Container MongoDB**

1. **Baixar a imagem do MongoDB:**
   - No **Prompt de Comando** ou no **PowerShell**, execute:
     ```bash
     docker pull mongo
     ```

2. **Executar o container MongoDB:**
   - Execute o seguinte comando para iniciar o MongoDB em um container:
     ```bash
     docker run -d --name mongo-container -p 27017:27017 mongo
     ```
     - **`-d`**: Executa o container em segundo plano.
     - **`--name mongo-container`**: Dá o nome "mongo-container" ao container.
     - **`-p 27017:27017`**: Mapeia a porta 27017 do container para a porta 27017 do host (porta padrão do MongoDB).

3. **Verificar se o MongoDB está rodando:**
   - Execute:
     ```bash
     docker ps
     ```
   - O MongoDB deve aparecer na lista de containers ativos.

---

### **Acessar o MongoDB com um Script Python**

1. **Instalar a biblioteca `pymongo` no Python:**
   - Certifique-se de que você tem o Python instalado (recomenda-se usar o Python 3).
   - No terminal, execute:
     ```bash
     pip install pymongo
     ```

2. **Criar um script Python para se conectar ao MongoDB:**
   - Crie um arquivo chamado `mongo_test.py` e insira o seguinte código:
     ```python
     from pymongo import MongoClient

     # Configurar conexão
     client = MongoClient("mongodb://localhost:27017/")  # URL do MongoDB

     # Acessar um banco de dados e coleção
     db = client["test_database"]  # Nome do banco de dados
     collection = db["test_collection"]  # Nome da coleção

     # Inserir dados
     document = {"name": "Alice", "age": 25, "city": "Wonderland"}
     result = collection.insert_one(document)
     print("Documento inserido com ID:", result.inserted_id)

     # Recuperar dados
     retrieved_document = collection.find_one({"name": "Alice"})
     print("Documento recuperado:", retrieved_document)

     # Fechar conexão
     client.close()
     ```

3. **Executar o script:**
   - No terminal, execute:
     ```bash
     python mongo_test.py
     ```
   - Se tudo estiver configurado corretamente, você verá a mensagem com o ID do documento inserido e os dados recuperados do MongoDB.