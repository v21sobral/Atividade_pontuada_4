import os
import time
from dataclasses import dataclass

@dataclass
class Funcionario:
    def __inicio__(self, nome, cpf, cargo, salario):
        self.nome = nome.lower()
        self.cpf = cpf
        self.cargo = cargo.lower()
        self.salario = salario

class CadastroFuncionarios:
    def __inicio__(self):
        self.funcionarios = []

    def verificar_lista_vazia(self):
        if not self.funcionarios:
            print("\nA lista está vazia.")
            return True
        return False

    def adicionar_funcionario(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        cargo = input("Cargo: ")
        salario = input("Salário: ")
        funcionario = Funcionario(nome, cpf, cargo, salario)
        self.funcionarios.append(funcionario)
        print(f"\n{nome} adicionado com sucesso.")

    def mostrar_funcionarios(self):
        if self.verificar_lista_vazia():
            return
        print("\n - Lista de funcionários - ")
        for f in self.funcionarios:
            print(f"- Nome: {f.nome}, Salário: {f.salario}, CPF: {f.cpf}, Função: {f.cargo}")

    def atualizar_funcionario(self):
        if self.verificar_lista_vazia():
            return
        self.mostrar_funcionarios()
        nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ").lower()
        for funcionario in self.funcionarios:
            if funcionario.nome == nome_antigo:
                funcionario.nome = input(f"Novo nome para {nome_antigo} (ou ENTER para manter): ").lower() or funcionario.nome
                funcionario.salario = input(f"Novo salário (ou ENTER para manter): ") or funcionario.salario
                funcionario.cpf = input(f"Novo CPF (ou ENTER para manter): ") or funcionario.cpf
                funcionario.cargo = input(f"Novo cargo (ou ENTER para manter): ").lower() or funcionario.cargo
                print(f"{nome_antigo} foi atualizado.")
                return
        print(f"\nO nome {nome_antigo} não foi encontrado.")

    def excluir_funcionario(self):
        if self.verificar_lista_vazia():
            return
        self.mostrar_funcionarios()
        nome_remover = input("Digite o nome do funcionário que deseja remover: ").lower()
        for funcionario in self.funcionarios:
            if funcionario.nome == nome_remover:
                self.funcionarios.remove(funcionario)
                print(f"{nome_remover} foi removido com sucesso.")
                return
        print(f"O nome {nome_remover} não foi encontrado.")

# Uso das classes no menu principal
cadastro = CadastroFuncionarios()

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
            cadastro.adicionar_funcionario()
        case 2:
            os.system("cls || clear")
            cadastro.mostrar_funcionarios()
            decisao = input("Digite (s) para voltar ao menu ou (n) para encerrar o programa: ").lower()
            if decisao == "s":
                os.system("cls || clear")
                continue
            else:
                break
        case 3:
            cadastro.atualizar_funcionario()
        case 4:
            cadastro.excluir_funcionario()
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