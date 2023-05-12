from faker import Faker
import random

# Cria uma instância do Faker para gerar dados aleatórios
fake = Faker()

# Cria uma lista de nomes de instituições para serem utilizados na criação dos cientistas
instituicoes = ["Universidade de São Paulo", "Universidade Federal do Rio de Janeiro", "Universidade Federal de Minas Gerais", "Universidade Estadual de Campinas", "Universidade Federal de São Paulo"]

# Cria uma lista de nomes de projetos para serem utilizados na criação dos projetos
projetos = ["Projeto de Pesquisa em Inteligência Artificial", "Projeto de Desenvolvimento de Software para Gestão Empresarial", "Projeto de Estudo de Viabilidade Econômica de uma Nova Indústria", "Projeto de Desenvolvimento de Novos Materiais para Construção Civil", "Projeto de Estudo de Mudanças Climáticas na Região"]

# Cria uma lista de cidades para serem utilizadas na criação dos locais
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Campinas", "Curitiba", "Porto Alegre", "Brasília", "Salvador"]

# Cria uma lista de nomes de financiadores para serem utilizados na criação dos financiadores
financiadores = ["CNPq", "FAPESP", "CAPES", "FINEP", "BNDES", "Banco Mundial", "Fundação Lemann"]

# Cria uma lista de habilidades para serem utilizadas na criação das habilidades
habilidades = ["Programação em Python", "Estatística", "Análise de Dados", "Machine Learning", "Redes de Computadores", "Desenvolvimento Web"]

# Função para gerar um número aleatório de cientistas, projetos e locais
def gerar_quantidades():
    qtd_cientistas = random.randint(10, 20)
    qtd_projetos = random.randint(5, 10)
    qtd_locais = random.randint(3, 5)
    return qtd_cientistas, qtd_projetos, qtd_locais

# Função para gerar os dados dos cientistas
def gerar_cientistas(qtd_cientistas):
    cientistas = []
    for i in range(qtd_cientistas):
        ssn = fake.random_int(min=100000000, max=999999999)
        nome = fake.name()
        instituicao = random.choice(instituicoes)
        cientistas.append((ssn, nome, instituicao))
    return cientistas

# Função para gerar os dados dos projetos
def gerar_projetos(qtd_projetos):
    projetos = []
    for i in range(qtd_projetos):
        code = fake.random_int(min=1000, max=9999)
        nome = random.choice(projetos)
        horas = random.randint(100, 500)
        projetos.append((code, nome, horas))
    return projetos

# Função para gerar os dados das atribuições
def gerar_atribuicao(cientistas, projetos):
    atribuicoes = []
    for cientista in cientistas:
        projet
