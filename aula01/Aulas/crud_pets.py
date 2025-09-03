import sqlite3
# crud_pets.py
def conectar_banco():
    # Cria ou conecta ao arquivo de banco de dados
    conn = sqlite3.connect('pets.db')
    return conn

def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            raca TEXT NOT NULL,
            adotado BOOLEAN NOT NULL
        )
    ''')
    conn.commit()

# Função para cadastrar um novo pet
def cadastrar_pet_db():
    conn = conectar_banco()
    cursor = conn.cursor()
    nome = input("Nome do pet: ")
    idade = int(input("Idade do pet: "))
    raca = input("Raça do pet: ")
    adotado = 0

    try:
        cursor.execute('''
            INSERT INTO pets (nome, idade, raca, adotado)
            VALUES (?, ?, ?, ?)
        ''', (nome, idade, raca, adotado))
        conn.commit()
        print(f"\nPet '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o pet: {e}")
    finally:
        conn.close()


# Função para listar todos os pets
def listar_pets():
    """Lista todos os pets cadastrados no banco de dados."""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nome, idade, raca, adotado FROM pets")
    pets = cursor.fetchall()
    
    if not pets:
        print("Nenhum pet cadastrado.")
    else:
        for pet in pets:
            status = "Adotado" if pet[4] == 1 else "Disponível"
            print(f"\nID: {pet[0]}")
            print(f"Nome: {pet[1]}")
            print(f"Idade: {pet[2]} ano(s)")
            print(f"Raça: {pet[3]}")
            print(f"Status: {status}")
    
    conn.close()
# Função para buscar pet por nome
def buscar_pet():
    """Busca pets por nome no banco de dados."""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    nome = input("Digite o nome do pet para buscar: ").lower()
    
    cursor.execute("SELECT id, nome, idade, raca, adotado FROM pets WHERE lower(nome) LIKE ?", ('%' + nome + '%',))
    encontrados = cursor.fetchall()

    if not encontrados:
        print("Nenhum pet com esse nome foi encontrado.")
    else:
        for pet in encontrados:
            status = "Adotado" if pet[4] == 1 else "Disponível"
            print(f"\nID: {pet[0]} | Nome: {pet[1]} | Idade: {pet[2]} | Raça: {pet[3]} | Status: {status}")
    
    conn.close()
# Função para atualizar dados de um pet
def atualizar_pet():
    """Atualiza os dados de um pet no banco de dados."""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    try:
        id_pet = int(input("Digite o ID do pet para atualizar: "))
        
        cursor.execute("SELECT * FROM pets WHERE id = ?", (id_pet,))
        pet_existente = cursor.fetchone()

        if pet_existente:
            nome = input("Novo nome (ou Enter para manter o atual): ") or pet_existente[1]
            idade = input("Nova idade (ou Enter para manter a atual): ") or pet_existente[2]
            raca = input("Nova raça (ou Enter para manter a atual): ") or pet_existente[3]
            
            # Converte a idade para inteiro, se foi digitada
            if isinstance(idade, str):
                idade = int(idade)

            cursor.execute('''
                UPDATE pets
                SET nome = ?, idade = ?, raca = ?
                WHERE id = ?
            ''', (nome, idade, raca, id_pet))
            conn.commit()
            print("Informações atualizadas com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número para o ID e a idade.")
    finally:
        conn.close()

# Função para marcar um pet como adotado
def marcar_como_adotado():
    """Marca um pet como adotado no banco de dados."""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    try:
        id_pet = int(input("Digite o ID do pet para marcar como adotado: "))

        cursor.execute("SELECT nome FROM pets WHERE id = ?", (id_pet,))
        pet_nome = cursor.fetchone()
        
        if pet_nome:
            cursor.execute("UPDATE pets SET adotado = 1 WHERE id = ?", (id_pet,))
            conn.commit()
            print(f"Pet '{pet_nome[0]}' marcado como adotado!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o ID.")
    finally:
        conn.close()
# Função para remover um pet do sistema
def remover_pet():
    """Remove um pet do banco de dados."""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    try:
        id_pet = int(input("Digite o ID do pet para remover: "))

        cursor.execute("SELECT nome FROM pets WHERE id = ?", (id_pet,))
        pet_nome = cursor.fetchone()
        
        if pet_nome:
            cursor.execute("DELETE FROM pets WHERE id = ?", (id_pet,))
            conn.commit()
            print(f"Pet '{pet_nome[0]}' removido com sucesso.")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o ID.")
    finally:
        conn.close()

# Função para exibir o menu
def menu():
    print("\n--- SISTEMA DE ADOÇÃO DE PETS ---")
    print("1. Cadastrar pet")
    print("2. Listar pets")
    print("3. Buscar pet por nome")
    print("4. Atualizar pet")
    print("5. Marcar como adotado")
    print("6. Remover pet")
    print("0. Sair")

# --- Função principal (adaptada) ---
# Você vai chamar a nova função de cadastro no seu programa principal
def main():
    conn = conectar_banco()
    criar_tabela(conn)
    conn.close()

# Programa principal
while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pet_db()
        elif opcao == '2':
            listar_pets()
        elif opcao == '3':
            buscar_pet()
        elif opcao == '4':
            atualizar_pet()
        elif opcao == '5':
            marcar_como_adotado()
        elif opcao == '6':
            remover_pet()
        elif opcao == '0':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()