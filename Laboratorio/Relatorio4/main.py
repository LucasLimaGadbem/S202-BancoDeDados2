from database import Database
from helper.writeAJson import writeAJson
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="produtos")
db.resetDatabase()

verificador = ProductAnalyzer(db)

vendas_por_dia = verificador.Total_vendas_dia()

mais_vendido = verificador.Produto_mais_vendido()

maior_compra = verificador.Cliente_maior_compra()

comprado_maior_que_1 = verificador.Produtos_vendidos_mais_1()