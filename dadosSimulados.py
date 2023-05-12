import sqlite3
import random

# Conecta com o banco de dados
conn = sqlite3.connect('cientistas.db')
c = conn.cursor()

# Simula dados para a tabela localProjetos
projetos = ['P001', 'P002', 'P003', 'P004', 'P005']
locais = ['Local A', 'Local B', 'Local C', 'Local D', 'Local E']
for projeto in projetos:
    local = random.choice(locais)
    c.execute("INSERT INTO localProjetos (projeto, local) VALUES (?, ?)", (projeto, local))
    
# Simula dados para a tabela financiamento
fontes = ['Financiador A', 'Financiador B', 'Financiador C', 'Financiador D', 'Financiador E']
for projeto in projetos:
    fonte_projeto = random.choice(fontes)
    verba = random.uniform(1000, 50000)
    c.execute("INSERT INTO financiamento (projeto, fonteProjeto, verba) VALUES (?, ?, ?)", (projeto, fonte_projeto, verba))
    
# Simula dados para a tabela habilidades
habilidades = ['Habilidade 1', 'Habilidade 2', 'Habilidade 3', 'Habilidade 4', 'Habilidade 5']
for i, habilidade in enumerate(habilidades):
    c.execute("INSERT INTO habilidades (habilidadeID, nomeHabilidade) VALUES (?, ?)", (i+1, habilidade))
    
# Simula dados para a tabela habilidadesCientistas
cientistas = [123456, 234567, 345678, 456789, 567890]
for cientista in cientistas:
    habilidade = random.choice(range(1, len(habilidades)+1))
    c.execute("INSERT INTO habilidadesCientistas (cientista, habilidade) VALUES (?, ?)", (cientista, habilidade))

# Salva as alterações e fecha a conexão com o banco de dados
conn.commit()
conn.close()
