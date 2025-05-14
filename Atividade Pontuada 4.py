import os
import time

os.system("cls || clear")

# Função para verificar se a lista está vazia.
def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
        print("\nA lista está vazia.")
        return True
    return False

# Função para adicionar.
def adicionar_funcionario(lista_funcionarios):
    nome = input("Nome: ").lower()
    cpf = input("CPF: ")
    cargo = input("Cargo: ").lower()
    salario = input("Salário: ")
    funcionario = {
        "nome": nome,
        "cpf": cpf,
        "cargo": cargo,
        "salario": salario
    }
    lista_funcionarios.append(funcionario)
    print(f"\n{nome} adicionado com sucesso.")

# Função para mostrar todos os funcionários.
def mostrar_funcionarios(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return
    print("\n - Lista de funcionários - ")
    for f in lista_funcionarios:
        print(f"- Nome: {f['nome']}, Data de Nascimento: {f['salario']}, CPF: {f['cpf']}, Função: {f['cargo']}")

# Função para atualizar.
def atualizar_funcionario(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return
    mostrar_funcionarios(lista_funcionarios)
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ").lower()
    for funcionario in lista_funcionarios:
        if funcionario["nome"] == nome_antigo:
            funcionario["nome"] = input(f"Novo nome para {nome_antigo} (ou ENTER para manter): ").lower() or funcionario["nome"]
            funcionario["salario"] = input(f"Novo salário (ou ENTER para manter): ") or funcionario["salario"]
            funcionario["cpf"] = input(f"Novo CPF (ou ENTER para manter): ") or funcionario["cpf"]
            funcionario["cargo"] = input(f"Novo cargo (ou ENTER para manter): ").lower() or funcionario["cargo"]
            print(f"{nome_antigo} foi atualizado.")
            return
    print(f"\nO nome {nome_antigo} não foi encontrado.")

# Função para atualizar arquivo.
def atualizar_funcionario_arquivo(nome_arquivo):
    # Lê todos os funcionários do arquivo
    funcionarios = []
    with open(nome_arquivo, "r") as f:
        for linha in f:
            nome, cpf, cargo, salario = linha.strip().split(", ")
            funcionarios.append({
                "nome": nome,
                "cpf": cpf,
                "cargo": cargo,
                "salario": salario
            })

    # Mostra funcionários e pede qual atualizar
    print("\n - Lista de funcionários - ")
    for f in funcionarios:
        print(f"- Nome: {f['nome']}, CPF: {f['cpf']}, Cargo: {f['cargo']}, Salário: {f['salario']}")
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ").lower()

    atualizado = False
    for funcionario in funcionarios:
        if funcionario["nome"] == nome_antigo:
            funcionario["nome"] = input(f"Novo nome para {nome_antigo} (ou ENTER para manter): ").lower() or funcionario["nome"]
            funcionario["salario"] = input(f"Novo salário (ou ENTER para manter): ") or funcionario["salario"]
            funcionario["cpf"] = input(f"Novo CPF (ou ENTER para manter): ") or funcionario["cpf"]
            funcionario["cargo"] = input(f"Novo cargo (ou ENTER para manter): ").lower() or funcionario["cargo"]
            atualizado = True
            print(f"{nome_antigo} foi atualizado.")
            break
    if not atualizado:
        print(f"\nO nome {nome_antigo} não foi encontrado.")
        return

    # Sobrescreve o arquivo com a lista atualizada
    with open(nome_arquivo, "w") as f:
        for funcionario in funcionarios:
            f.write(f"{funcionario['nome']}, {funcionario['cpf']}, {funcionario['cargo']}, {funcionario['salario']}\n")

# Função para excluir.
def excluir_funcionario(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return
    mostrar_funcionarios(lista_funcionarios)
    nome_remover = input("Digite o nome do funcionário que deseja remover: ").lower()
    for funcionario in lista_funcionarios:
        if funcionario["nome"] == nome_remover:
            lista_funcionarios.remove(funcionario)
            print(f"{nome_remover} foi removido com sucesso.")
            return
    print(f"O nome {nome_remover} não foi encontrado.")

# Lista de funcionários.
funcionarios = []

# Mostrando menu.
while True:
    print("""
    ===Bem vindo ao cadastro de funcionários DENDÊ TECH===
    1 - Adicionar funcionário
    2 - Listar funcionários
    3 - Atualizar funcionário
    4 - Remover funcionário
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_funcionario(funcionarios)

            nome_arquivo = "Cadastro de funcionarios.csv"
            with open(nome_arquivo, "a") as cadastro_funcionarios:
                for funcionario in funcionarios:
                    cadastro_funcionarios.write(
                        f"{funcionario['nome']}, {funcionario['cpf']}, {funcionario['cargo']}, {funcionario['salario']}\n"
                    )
        case 2:
            os.system("cls || clear")
            mostrar_funcionarios(funcionarios)
            decisao = input("Digite (s) para voltar ao menu ou (n) para encerrar o programa: ").lower()
            if decisao == "s":
                os.system("cls || clear")
                continue
            else:
                break
        case 3:
            nome_arquivo = "Cadastro de funcionarios.csv"
            atualizar_funcionario_arquivo(nome_arquivo)
        case 4:
            excluir_funcionario(funcionarios)
        case 5:
            print("\nPrograma sendo encerrado", end="", flush=True)
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(1)
            os.system("cls || clear")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    if opcao != 1:
        time.sleep(2)
    os.system("cls || clear")