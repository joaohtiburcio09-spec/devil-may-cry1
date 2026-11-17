CREATE DATABASE IF NOT EXISTS devil_may_cry;
USE devil_may_cry;

CREATE TABLE IF NOT EXISTS cacadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    rank_estilo VARCHAR(10) DEFAULT 'SSS'
);

CREATE TABLE IF NOT EXISTS demonios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    classe VARCHAR(50) NOT NULL,
    nivel_ameaca INT NOT NULL
);

CREATE TABLE IF NOT EXISTS missoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    recompensa DECIMAL(10, 2) NOT NULL,
    status VARCHAR(30) DEFAULT 'Pendente',
    cacador_id INT,
    FOREIGN KEY (cacador_id) REFERENCES cacadores(id) ON DELETE SET NULL
);

-- Dados iniciais de exemplo
INSERT INTO cacadores (nome, especialidade, rank_estilo) VALUES 
('Dante', 'Espadas e Armas de Fogo', 'SSS'),
('Vergil', 'Yamato / Corte Dimensional', 'SSS'),
('Nero', 'Red Queen e Devil Breakers', 'SS');