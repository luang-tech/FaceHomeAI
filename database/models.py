TABELA_MORADORES = """
CREATE TABLE IF NOT EXISTS moradores (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    residencia_id INTEGER NOT NULL,

    nome TEXT NOT NULL,

    email TEXT,

    telefone TEXT,

    cor_led TEXT NOT NULL,

    ativo INTEGER DEFAULT 1,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
"""
TABELA_RESIDENCIAS = """
CREATE TABLE IF NOT EXISTS residencias (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome TEXT NOT NULL,

    endereco TEXT,

    cidade TEXT,

    estado TEXT,

    telefone TEXT,

    email TEXT,

    plano TEXT DEFAULT 'Basic',

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
"""
TABELA_VISITANTES = """
CREATE TABLE IF NOT EXISTS visitantes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    residencia_id INTEGER NOT NULL,

    nome TEXT NOT NULL,

    telefone TEXT,

    validade DATETIME,

    cor_led TEXT,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
"""
TABELA_DISPOSITIVOS = """
CREATE TABLE IF NOT EXISTS dispositivos (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    residencia_id INTEGER NOT NULL,

    nome TEXT NOT NULL,

    tipo TEXT NOT NULL,

    local TEXT,

    ip TEXT,

    status TEXT DEFAULT 'Desligado',

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
"""
TABELA_AUTOMACOES = """
CREATE TABLE IF NOT EXISTS automacoes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    residencia_id INTEGER NOT NULL,

    morador_id INTEGER NOT NULL,

    evento TEXT NOT NULL,

    dispositivo TEXT NOT NULL,

    acao TEXT NOT NULL,

    valor TEXT,

    ativo INTEGER DEFAULT 1,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
"""