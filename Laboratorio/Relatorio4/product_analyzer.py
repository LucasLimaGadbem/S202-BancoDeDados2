from database import Database
from helper.writeAJson import writeAJson


class ProductAnalyzer:
    def __init__(self, database: Database):
        self._database = database

    def Total_vendas_dia(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": None, "total": {"$sum": "$total"}}}
        ])

        writeAJson(result, "total_vendas_por_dia")

    def Produto_mais_vendido(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])

        writeAJson(result, "produto_mais_vendido")

    def Cliente_maior_compra(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])

        writeAJson(result, "cliente_maior_compra")

    def Produtos_vendidos_mais_1(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match":{"produtos.quantidade":{"$gt": 1}}},
            {"$group": {"_id": "$produtos.descricao", "totalVendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"totalVendido": -1}},
            {"$project": {"_id":1, "totalVendido": 1}},
        ])
        
        writeAJson(result, "produtos_vendidos_mais_que_1")