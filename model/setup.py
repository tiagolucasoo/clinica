import sqlite3
import os

#Criação das Tabelas e do Banco

def ROTA_BANCO():
    caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'clinica.db'))
    conn = sqlite3.connect(caminho_banco)
    return conn

'''
Tabelas para criar:
    Paises, Cidades, Especialidades,
    Medicos, Pacientes, Planos_Saude,
    Pacientes_Planos, Doencas, Pacientes_Doencas
    Agendamentos
'''

def BD_TABELA_PAISES():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paises(
            id_pais INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50) NOT NULL UNIQUE
        )
    ''')
    print("Tabela Paises conectada")
    conn.commit()
    conn.close()

def BD_TABELA_CIDADES():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cidades(
            id_cidade INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pais INTEGER NOT NULL,
            nome VARCHAR(50) NOT NULL UNIQUE,
            uf CHAR(2),
            FOREIGN KEY (id_pais) REFERENCES paises(id_pais)
        )
    ''')
    print("Tabela Cidades conectada")
    conn.commit()
    conn.close()

def BD_TABELA_ESPECIALIDADES():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS especialidades(
            id_especialidade INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50) NOT NULL UNIQUE
        )
    ''')
    print("Tabela Especialidades conectada")
    conn.commit()
    conn.close()

def BD_TABELA_MEDICOS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicos(
            id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50) NOT NULL,
            data_nas DATE NOT NULL,
            cpf VARCHAR(14) NOT NULL,
            salario DECIMAL(8,2) NOT NULL,
            rua VARCHAR(30) NOT NULL,
            numero VARCHAR(20) NOT NULL,
            complemento VARCHAR(20),
            especialidade VARCHAR(40),
            
            id_cidade INTEGER NOT NULL,
            id_especialidade INTEGER NOT NULL,
            
            FOREIGN KEY (id_cidade) REFERENCES cidades(id_cidade),
            FOREIGN KEY (id_especialidade) REFERENCES especialidades(id_especialidade)
        )
    ''')
    print("Tabela Médicos conectada")
    conn.commit()
    conn.close()

def BD_TABELA_PACIENTES():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes(
            id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(30) NOT NULL,
            data_nasc DATE NOT NULL,
            cpf VARCHAR(14) NOT NULL,
            telefone VARCHAR(15) NOT NULL,
            rua VARCHAR(30) NOT NULL,
            numero VARCHAR(5) NOT NULL,
            complemento VARCHAR(20),
            email VARCHAR(35),
            renda_familiar DECIMAL(8,2) NOT NULL,
            
            id_cidade INTEGER NOT NULL,
            FOREIGN KEY (id_cidade) REFERENCES cidades(id_cidade)
        )
    ''')
    print("Tabela Pacientes conectada")
    conn.commit()
    conn.close()

def BD_TABELA_PLANOS_SAUDE():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS planos_saude(
            id_plano INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50) NOT NULL,
            cobertura VARCHAR(50) NOT NULL
        )
    ''')
    print("Tabela Planos Saúde conectada")
    conn.commit()
    conn.close()

def BD_TABELA_PACIENTES_PLANOS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes_planos(
            id_paciente_plano INTEGER PRIMARY KEY AUTOINCREMENT,
            
            numero_carteirinha VARCHAR(50) NOT NULL,
            validade DATE NOT NULL,
            id_paciente INTEGER NOT NULL,
            id_plano INTEGER NOT NULL,
            
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
            FOREIGN KEY (id_plano) REFERENCES planos_saude(id_plano)
        )
    ''')
    print("Tabela Pacientes Planos conectada")
    conn.commit()
    conn.close()

def BD_TABELA_DOENCAS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doencas(
            id_doenca INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50) NOT NULL,
            CID VARCHAR(10) NOT NULL
        )
    ''')
    print("Tabela Doenças conectada")
    conn.commit()
    conn.close()

def BD_TABELA_PACIENTES_DOENCAS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes_doencas(
            id_paciente_doenca INTEGER PRIMARY KEY AUTOINCREMENT,
            data_diagnostico DATE NOT NULL,
            
            id_paciente INTEGER NOT NULL,
            id_doenca INTEGER NOT NULL,
            
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
            FOREIGN KEY (id_doenca) REFERENCES doencas(id_doenca)
        )
    ''')
    print("Tabela Pacientes Doenças conectada")
    conn.commit()
    conn.close()

def BD_TABELA_AGENDAMENTOS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos(
            id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
            data_agendamento DATE NOT NULL,
            hora_agendamento TIME NOT NULL,
            status VARCHAR(20) NOT NULL,
            
            id_paciente INTEGER NOT NULL,
            id_medico INTEGER NOT NULL,
            
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
            FOREIGN KEY (id_medico) REFERENCES medicos(id_medico)
        )
    ''')
    print("Tabela Agendamentos conectada\n")
    conn.commit()
    conn.close()

def INICIAR_BANCO():
    print("Acessando o Banco de Dados...\n")
    BD_TABELA_PAISES()
    BD_TABELA_CIDADES()
    BD_TABELA_ESPECIALIDADES()
    BD_TABELA_MEDICOS()
    BD_TABELA_PACIENTES()
    BD_TABELA_PLANOS_SAUDE()
    BD_TABELA_PACIENTES_PLANOS()
    BD_TABELA_DOENCAS()
    BD_TABELA_PACIENTES_DOENCAS()
    BD_TABELA_AGENDAMENTOS()
    print("Banco de Dados carregado com sucesso!\n")

INICIAR_BANCO()
