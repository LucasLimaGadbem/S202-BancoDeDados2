import threading
import time
import numpy as np
from pymongo import MongoClient

def simulacao1(i, intervalo):
    while True:
        if collection.find_one({"nomeSensor": "Temp1"})["sensorAlarmado"] == False:
            newTemp = np.random.randint(30, 40)
            collection.update_one({"nomeSensor": "Temp1"}, {"$set": {"valorSensor": newTemp}})
            print({f"Temperatura do sensor {i} = {newTemp}"})
            if newTemp > 38:
                collection.update_one({"nomeSensor": "Temp1"}, {"$set": {"sensorAlarmado": True}})
                print(f"Atencao! Temperatura muito alta! Verificar sensor {i}")
                flag = False
        else:
            print(f"Atencao! Temperatura muito alta! Verificar sensor {i}")
        time.sleep(intervalo)

def simulacao2(i, intervalo):
    while True:
        if collection.find_one({"nomeSensor": "Temp2"})["sensorAlarmado"] == False:
            newTemp = np.random.randint(30, 40)
            collection.update_one({"nomeSensor": "Temp2"}, {"$set": {"valorSensor": newTemp}})
            print({f"Temperatura do sensor {i} = {newTemp}"})
            if newTemp > 38:
                collection.update_one({"nomeSensor": "Temp2"}, {"$set": {"sensorAlarmado": True}})
                print(f"Atencao! Temperatura muito alta! Verificar sensor {i}")
                flag = False
        else:
            print(f"Atencao! Temperatura muito alta! Verificar sensor {i}")
        time.sleep(intervalo)

def simulacao3(i, intervalo):
    while True:
        if collection.find_one({"nomeSensor": "Temp3"})["sensorAlarmado"] == False:
            newTemp = np.random.randint(30, 40)
            collection.update_one({"nomeSensor": "Temp3"}, {"$set": {"valorSensor": newTemp}})
            print({f"Temperatura do sensor {i} = {newTemp}"})
            if newTemp > 38:
                collection.update_one({"nomeSensor": "Temp3"}, {"$set": {"sensorAlarmado": True}})
                print(f"Atencao! Temperatura muito alta! Verificar sensor {i}")
                flag = False
        else:
            print(f"Atencao! Temperatura muito alta! Verificar sensor {i}")
        time.sleep(intervalo)


# Configurar conexão
client = MongoClient("mongodb://localhost:27017/")  # URL do MongoDB

# Acessar um banco de dados e coleção
db = client["bancoiot"]  # Nome do banco de dados
collection = db["sensores"]  # Nome da coleção

# Inserir dados
document = [{
    "nomeSensor": "Temp1",
    "valorSensor": np.random.randint(30, 40),
    "unidadeMedida": "C°",
    "sensorAlarmado" : False
    },
    {
    "nomeSensor": "Temp2",
    "valorSensor": np.random.randint(30, 40),
    "unidadeMedida": "C°",
    "sensorAlarmado" : False
    },
    {
    "nomeSensor": "Temp3",
    "valorSensor": np.random.randint(30, 40),
    "unidadeMedida": "C°",
    "sensorAlarmado" : False
    }
]
     
result = collection.insert_many(document)

sen1 = threading.Thread(target=simulacao1, args=(1, 5))
sen2 = threading.Thread(target=simulacao2, args=(2, 5))
sen3 = threading.Thread(target=simulacao3, args=(3, 5))
sen1.start()
sen2.start()
sen3.start()