-- Cria o banco de dados Analytech Projet Ciencistas
CREATE DATABASE `Analytech Projet Ciencistas`;

-- Seleciona o banco de dados recém-criado
USE `Analytech Projet Ciencistas`;


-- Tabelas-base do Projeto Cientistas --

-- Cria a tabela cientistas
CREATE TABLE cientistas (
  SSN BIGINT,
  nome VARCHAR(30) NOT NULL,
  sexo VARCHAR(10) NOT NULL,
  instituicao VARCHAR(50) NOT NULL,
  PRIMARY KEY (SSN) 
);

-- Cria a tabela projetos
CREATE TABLE projetos (
  Code VARCHAR(4),
  nome VARCHAR(50) NOT NULL,
  horas INT,
  dataInicio DATETIME NOT NULL,
  dataCerre DATETIME NULL,
  PRIMARY KEY (Code) 
);

-- Cria a tabela atribuicao
CREATE TABLE atribuicao (
  cientista BIGINT NOT NULL,
  projeto VARCHAR(4) NOT NULL,
  PRIMARY KEY (cientista, projeto),
  FOREIGN KEY (cientista) REFERENCES cientistas (SSN),
  FOREIGN KEY (projeto) REFERENCES projetos (Code)
);

-- Localização de Projetos e Cientistas --

-- Cria a tabela locais
CREATE TABLE locais (
  localID INT,
  localNome VARCHAR(50) NOT NULL,
  cidade VARCHAR(50) NOT NULL,
  PRIMARY KEY (localID) 
);

-- Cria a tabela localCientistas
CREATE TABLE localCientistas (
  cientista BIGINT NOT NULL,
  local INT NOT NULL,
  PRIMARY KEY (cientista, local),
  FOREIGN KEY (cientista) REFERENCES cientistas (SSN),
  FOREIGN KEY (local) REFERENCES locais (localID)
);

-- Cria a tabela localProjetos

CREATE TABLE localProjetos (
  projeto VARCHAR(4) NOT NULL,
  local INT NOT NULL,
  PRIMARY KEY (projeto, local),
  FOREIGN KEY (projeto) REFERENCES projetos (Code),
  FOREIGN KEY (local) REFERENCES locais (localID)
);

-- Financiamento --

-- Cria a tabela financiadores
CREATE TABLE financiadores (
  financiadorID BIGINT NOT NULL,
  nomeFinanciador VARCHAR(50) NOT NULL,
  PRIMARY KEY (financiadorID) 
);

-- Cria a tabela financiamento
CREATE TABLE financiamento (
  projeto VARCHAR(4) NOT NULL,
  financiador BIGINT NOT NULL,
  verba FLOAT,
  PRIMARY KEY (projeto, financiador),
  FOREIGN KEY (projeto) REFERENCES projetos (Code),
  FOREIGN KEY (financiador) REFERENCES financiadores (financiadorID)
);

-- Habilidades -- 

-- Cria a tabela habilidades
CREATE TABLE habilidades (
  habilidadeID INT,
  nomeHabilidade VARCHAR(30) NOT NULL,
  PRIMARY KEY (habilidadeID)
);

-- Cria a tabela habilidadesCientistas
CREATE TABLE habilidadesCientistas (
  cientista BIGINT NOT NULL,
  habilidade INT NOT NULL,
  PRIMARY KEY (cientista, habilidade),
  FOREIGN KEY (cientista) REFERENCES cientistas (SSN),
  FOREIGN KEY (habilidade) REFERENCES habilidades (habilidadeID)
);


