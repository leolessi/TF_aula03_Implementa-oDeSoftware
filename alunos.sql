CREATE DATABASE alunos;

USE alunos;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    curso VARCHAR(100) NOT NULL,
);

-- INSERT INTO alunos (nome, curso) VALUES ('Aluno A', 'Direito');
-- INSERT INTO alunos (nome, curso) VALUES ('Aluno B', 'ADS');