import mysql.connector
import random

# Define as credenciais do banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="senha",
    database="Analytech Projet Ciencistas"
)

# Define uma lista de nomes e sobrenomes para serem usados como nomes de cientistas
nomes = ["Lucas", "Julia", "Pedro", "Amanda", "Mariana", "Fernando"]
sobrenomes = ["Silva", "Souza", "Pereira", "Costa", "Alves", "Oliveira"]

# Insere dados aleatórios na tabela cientistas
cursor = mydb.cursor()
for i in range(10):
    nome = random.choice(nomes) + " " + random.choice(sobrenomes)
    ssn = random.randint(100000000, 999999999)
    sql = "INSERT INTO cientistas (SSN, nome) VALUES (%s, %s)"
    val = (ssn, nome)
    cursor.execute(sql, val)
mydb.commit()

# Insere dados aleatórios na tabela projetos
cursor = mydb.cursor()
projetos = ["P001", "P002", "P003", "P004", "P005"]
for i in range(5):
    nome = "Projeto " + str(i+1)
    horas = random.randint(100, 1000)
    code = projetos[i]
    sql = "INSERT INTO projetos (Code, nome, horas) VALUES (%s, %s, %s)"
    val = (code, nome, horas)
    cursor.execute(sql, val)
mydb.commit()

# Insere dados aleatórios na tabela atribuicao
cursor = mydb.cursor()
sql = "SELECT SSN FROM cientistas"
cursor.execute(sql)
cientistas = cursor.fetchall()
for i in range(20):
    cientista = random.choice(cientistas)[0]
    projeto = random.choice(projetos)
    sql = "INSERT INTO atribuicao (cientista, projeto) VALUES (%s, %s)"
    val = (cientista, projeto)
    cursor.execute(sql, val)
mydb.commit()

# Insere dados aleatórios na tabela locais
cursor = mydb.cursor()
locais = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]
for i in range(5):
    localID = i+1
    localNome = locais[i]
    sql = "INSERT INTO locais (localID, localNome) VALUES (%s, %s)"
    val = (localID, localNome)
    cursor.execute(sql, val)
mydb.commit()

# Insere dados aleatórios na tabela localCientistas
cursor = mydb.cursor()
sql = "SELECT SSN FROM cientistas"
cursor.execute(sql)
cientistas = cursor.fetchall()
for i in range(10):
    cientista = random.choice(cientistas)[0]
    local = random.randint(1, 5)
    sql = "INSERT INTO localCientistas (cientista, local) VALUES (%s, %s)"
    val = (cientista, local)
    cursor.execute(sql, val)
mydb.commit()

# Insere dados aleatórios na tabela localProjetos
cursor = mydb.cursor()
for i in range(5):
    projeto = projetos[i]
    local = locais
