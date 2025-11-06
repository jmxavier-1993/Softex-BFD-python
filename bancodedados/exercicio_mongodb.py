import pymongo
import os
from dotenv import load_dotenv

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

# 2. Acessa a variável de ambiente
MONGO_URI = os.getenv("MONGO_URI")

# Verifica se a URI foi carregada
if MONGO_URI is None:
    print("ERRO: Variável MONGO_URI não encontrada no ambiente ou .env!")
else:
    # 3. Usa a variável para criar a conexão
    try:
        conn = pymongo.MongoClient(MONGO_URI)
        
        # O comando 'server_info()' tenta realmente se conectar
        conn.admin.command('ping') 
        print("Conexão com o MongoDB estabelecida com sucesso!")
        print(conn)
        conn.close()
        
    except pymongo.errors.ConnectionFailure as e:
        print(f"Falha ao conectar ao MongoDB: {e}")


    
    