CREATE DATABASE alunos;

USE alunos;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    curso VARCHAR(100) NOT NULL,
);

-- INSERT INTO alunos (nome, idade, curso) VALUES ('Aluno A', 18, 'Direito');
-- INSERT INTO alunos (nome, idade, curso) VALUES ('Aluno B', 21, 'ADS');