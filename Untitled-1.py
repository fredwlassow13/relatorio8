from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.214.15.20:7687", "neo4j", "fight-eights-night")
db.drop_all()

# Criando uma instância da classe GameDatabase para interagir com o banco de dados
Game = GameDatabase(db)

# Criando alguns Players
Game.create_Player("João")
Game.create_Player("Maria")
Game.create_Player("José")

# Criando alguns alunos
Game.create_Match("Volei")
Game.create_Match("Futebol")
Game.create_Match("Rugbi")

# Atualizando o nome de uma Match
Game.update_Match("Volei", "Basquete")

Game.insert_Player_Match("Joao", "Volei")
Game.insert_Player_Match("Maria", "Rugbi")
Game.insert_Player_Match("Joao", "Rugbi")
Game.insert_Player_Match("Jose", "Futebol")

# Deletando um player e uma match
Game.delete_Player("Joao")
Game.delete_Match("Volei")

# Imprimindo todas as informações do banco de dados
print("MATCH:")
print(Game.get_Match())
print("PLAYERS:")
print(Game.get_Match())
print("Aulas:")
print(Game.get_Match())

# Fechando a conexão com o banco de dados
db.close()