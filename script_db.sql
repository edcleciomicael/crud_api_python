-- Criar tabela

CREATE TABLE IF NOT EXISTS pessoa(
	id_pessoa SERIAL PRIMARY KEY NOT NULL,
	nome VARCHAR(100) NOT NULL,
	data_nascimento DATE,
	salario VARCHAR(100) NOT NULL,
	observacoes TEXT
);

--Aterando a tabela

ALTER TABLE pessoa 
ADD COLUMN nome_mae VARCHAR(100) NOT NULL, 
ADD COLUMN nome_pai VARCHAR(100) NOT NULL,
ADD COLUMN cpf VARCHAR(20) NOT NULL;

-- Indice para multicolunas

CREATE INDEX pessoa_multi_idx 
	ON pessoa (nome, data_nascimento);

-- Indice para coluna

CREATE INDEX pessoa_multi_idx 
	ON pessoa (cpf)


-- Inserir valores

INSERT INTO 
	pessoa (nome, data_nascimento, salario, observacoes, nome_mae, nome_pai, cpf)
	VALUES ('EDCLECIO MICAEL', '31-03-1995', 'R$3000', 'Analista de sistema nas horas vagas', 'JANAÍNA BATISTA', 'EDNO ALEXANDRE', '082.659.164-03'),
		   ('ROBERTO DA SILVA', '20-06-2000', 'R$4500', 'Prestativo', 'MARIA DO CEU', 'JOÃO MARIA DA SILVA', '100.750.185-10'),
		   ('BEATRIZ GOMES PAIVA', '01-08-1998', 'R$2700', 'Dedicada', 'JULIANA GOMES FONSECA', 'REINALDO PAIVA', '090.641.254-15');


-- Atualizar dados 

UPDATE pessoa
	SET salario = 'R$2500'
	WHERE id_pessoa = 3

-- Deletar dados

DELETE FROM pessoa
	WHERE id_pessoa = 3


-- Obter um registro

SELECT * FROM pessoa
	WHERE id_pessoa = 2


--DADOS DE EXEMPLO PARA INSERIR NO POSTAMAN 

	{
  "nome": "EDCARLA CAWANE",
  "data_nascimento": "2000-12-25",
  "salario": "3000",
  "observacoes": "NADA",
  "nome_mae": "EDUARDA ROCHA",
  "nome_pai": "RICARDO MOREIRA",
  "cpf": "085.155.632.09"
}