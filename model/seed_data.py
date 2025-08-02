import os
import sqlite3

def ROTA_BANCO():
    caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'clinica.db'))
    conn = sqlite3.connect(caminho_banco)
    return conn

def DADOS_PAISES():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
        ('Brasil',), ('Argentina',), ('Paraguai',), ('Uruguai',),
        ('Chile',), ('Portugal',), ('Espanha',), ('Alemanha',),
        ('Estados Unidos',), ('Canadá',), ('Suiça',), ('Finlândia',),
        ('Rússia',), ('Ucrânia',), ('México',), ('Venezuela',),
        ('Japão',), ('China',), ('Coreia do Sul',), ('Bolivia',),
        ('Camarões',), ('Albânia',), ('Argelia',), ('Egito',)]
    
    cursor.executemany('INSERT OR IGNORE INTO paises (nome) VALUES (?)', dados)
    conn.commit()
    print('Dados de Países Inseridos!')
    conn.close()

def DADOS_CIDADES():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
        ('Londrina', 'PR', 1,), ('Cambé', 'PR', 1,), ('São Paulo', 'SP', 1,), ('Campinas', 'SP', 1,),
        ('Xique-Xique', 'BH', 1,), ('Curitiba', 'PR', 1,), ('Maringá', 'PR', 1,), ('Cascavel', 'PR', 1,),
        ('Barracão', 'PR', 1,), ('Dionísio Cerqueira', 'SC', 1,), ('Buenos Aires', None, 2,), ('Ivaiporã', 'PR', 1,),
        ('Campinas', 'SP', 1,), ('Cabo Frio', 'RJ', 1,), ('Umuarama', 'PR', 1,), ('Arraial do Cabo', 'RJ', 1,),
        ('Cascavel', 'CE', 1,), ('Arapuã', 'PR', 1,), ('New Jersey', None, 9,),
        ('New York', None, 9,), ('Jardim Alegre', 'PR', 1,), ('Rolândia', 'PR', 1,)]

    cursor.executemany('INSERT OR IGNORE INTO cidades (nome, uf, id_pais) VALUES (?, ?, ?)', dados)
    conn.commit()
    print('Dados de Cidades Inseridos!')
    conn.close()

def DADOS_ESPECIALIDADES():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
        ('Cardiologia',), ('Dermatologia',), ('Endocrinologia',),
        ('Gastroenterologia',), ('Ginecologia',), ('Neurologia',),
        ('Oftalmologia',), ('Ortopedia',), ('Otorrinolarigonlogia',),
        ('Pediatria',), ('Psiquiatria',), ('Radiologia',),
        ('Urologia',), ('Anestesiologia',), ('Cirurgia Geral',),
        ('Cirurgia Plástica',), ('Neurocirurgia',), ('Oncologia',),
        ('Pneumologia',), ('Reumatologia',)]

    cursor.executemany('INSERT OR IGNORE INTO especialidades (nome) VALUES (?)', dados)
    conn.commit()
    print('Dados de Especialidades Inseridas!')
    conn.close()

def DADOS_MEDICOS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
        ('João Gabriel da Silva', '1980-03-22', '123.456.789-00', 8000.00, 'Rua Rio de Janeiro', '100', 'ap 801', 1,1,),
        ('Maria Eduarda dos Santos', '1975-03-29', '987.654.321-00', 8500.00, 'Avenida Castelo Branco', '1200', None , 1,2,),
        ('Pedro Henrique de Oliveira', '1988-04-05', '111.222.333-44', 7500.00, 'Avenida Esperança', '300', 'Apto 101', 2, 3,),
        ('Ana Maria Costa', '1990-04-12', '555.666.777-88', 12000.00, 'Rua Augusta', '400', None, 3, 1,),
        ('Nathalia Duarte', '2001-04-12', '124.789.145-44', 3000.00, 'Rua Mercúrio', '124', None, 1, 3,),
        ('Tiago Lucas', '2001-09-18', '122.004.845-10', 4000.00, 'Rua Cabo Frio', '85', None, 1, 2,),
        ('Gregório Oliveira', '1997-12-14', '568.124.010-50', 2500.00, 'Rua Bandeirantes', '120', None, 2, 4,),
        ('Tom Hanks', '1989-10-10', '414.010.125-55', 6000.00, 'Avenida Paraná', '10B', None, 3, 5,),
        ('Jorge Sakamoto', '2004-04-16', '956.010.454-20', 8000.00, 'Avenida São João', '17C', None, 5, 8,),
        ('Hiro Nakaruma', '1978-04-26', '865.010.441-14', 1172.05, 'Rua Brigadeiro Correia de Melo', '1024', None, 5, 20,),
        ("Guilherme Ricardo", "1990-05-05", "099.105.051-00", 3000.00, "Rua Fernando de Souza", "20", "Centro comercial", 4, 5,),
        ("Maria Teles Fraga", "1985-05-20", "020.185.011-10", 3890.00, "Rua Jataizinho", "200", "Centro comercial", 2, 1,),
        ("Ana Liduário", "1970-05-20", "070.197.002-99", 4600.00, "Avenida da Liberdade", "1990", "Esquina", 6, 3,)]

    cursor.executemany('INSERT OR IGNORE INTO medicos (nome, data_nas, cpf, salario, rua, numero, complemento, id_cidade, id_especialidade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', dados)
    conn.commit()
    print('Dados de Médicos Inseridos!')
    conn.close()

def DADOS_PACIENTES():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
    ("José Ricardo", "2000-12-30", "656.599.965-10", "4399965-6565", "Rua José Noronha", "1", "5480", 1, "josericardo@gmail.com", "casa",),
    ("Ana Luiza", "2000-10-20", "441.298.745-11", "4398745-4412", "Avenida Celso Garcia", "5", "6100", 1, "Analuiza01@gmail.com", "casa",),
    ("Ana Maria", "1980-07-18", "112.598.411-12", "4398441-1125", "Avenida Paraná", "10", "3500", 13, "anamaria02@gmail.com", "ap 1, bloco 3",),
    ("Carlos Henrique", "1970-12-25", "202.011.988-13", "1198865-2020", "Rua Curitiba", "15", "11650", 3, "carloshenr1010@outlook.com", None,),
    ("Isadora Fernandes", "2005-05-16", "201.011.988-64", "1198864-2010", "Rua Coronel", "20", "14500", 3, "isafernandez18@gmail.com", "ap 2, bloco 2",),
    ("Marcelo Teles", "1980-10-20", "101.441.987-10", "4198710-1014", "Rua Padre Kelman", "20", "7400", 6, "marceloteleslu@gmail.com", "casa",),
    ("Priscila Lima", "1995-04-11", "228.943.984-72", "4398472-2289", "Rua Xique-Xique", "8", "3000", 13, None, "ap 5, bloco 18",),
    ("Maria Fernandes", "2006-10-10", "171.122.998-88", "2299988-1711", "Rua Mercúrio", "1145", "7200", 17, "mariafernandez10@outlook.com", "Casa de fundos",),
    ("Mariana Torres", "2012-12-12", "111.722.998-89", "2299889-1117", "Rua Ruy Virmond Carnascialli", "562A", "5900", 17, "mariana.t.torres@gmail.com", None,),
    ("Celso Silva Souza", "2011-11-11", "180.942.896-22", "4298622-1809", "Rua Heron Domingues", "562B", "2890", 7, None, "Casa de esquina",),
    ("Santiago Fernandes", "2002-05-27", "100.264.955-14", "4395564-2001", "Rua José Noronha", "57", "50", 1, "santiagofernandes7@gmail.com", "casa",),
    ("Maria Fernandes", "2016-05-10", "010.244.598-10", "4398544-2010", "Rua José Noronha", "57", "50", 1, "mariafernandes10@gmail.com", "casa",),
    ("Guilherme Fernandes", "2002-05-27", "020.244.569-34", "4396544-2020", "Rua José Noronha", "57", "50", 1, "guilhermefernandes05@gmail.com", "casa",)]

    cursor.executemany('INSERT OR IGNORE INTO pacientes (nome, data_nasc, cpf, telefone, rua, numero, renda_familiar, id_cidade, email, complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', dados)
    conn.commit()
    print('Dados de Pacientes Inseridos')
    conn.close()

def DADOS_PLANOS_SAUDE():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
    ('Plano Básico', 'Consultas, Exames Simples',),
    ('Plano Bronze', 'Consultas, Exames Simples, Exames Laboratoriais',),
    ('Plano Prata', 'Consultas, Exames Simples, Exames Laboratoriais, Internações',),
    ('Plano Ouro', 'Consultas, Exames Simples, Exames Laboratoriais, Internações, Cirurgias',),
    ('Plano Diamante', 'Consultas, Exames Simples, Exames Laboratoriais, Internações, Cirurgias, Emergência 24h',),
    ('Plano Familiar', 'Consultas, Exames Simples, Exames Laboratoriais, Internações, Cirurgias, Emergência 24h, Plano Odontologico',),
    ('Plano Empresarial', 'Consultas, Exames Simples, Exames Laboratoriais, Internações, Cirurgias, Emergência 24h, Assistência Médica Empresarial',),
    ('Plano Executivo', 'Consultas, Exames Simples, Exames Laboratoriais, Internações, Cirurgias, Emergência 24h, Check-up Anual',),
    ('Plano Senior', 'Consultas, Exames Simples, Exames Laboratoriais, Internações, Cirurgias, Emergência 24h, Cuidado Geriátrico',),
    ('Plano Estudantial', 'Consultas, Exames Simples, Exames Laboratoriais, Emergência 24h',)]

    cursor.executemany('INSERT OR IGNORE INTO planos_saude (nome, cobertura) VALUES (?, ?)', dados)
    conn.commit()
    print('Dados de Planos de Saúde Inseridos!')
    conn.close()

def DADOS_PACIENTES_PLANOS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
    (1, 3, '1234567890', '2024-01-01'), (2, 5, '2345678901', '2024-02-15',),
    (3, 6, '3456789012', '2024-03-20'), (4, 6, '4567890123', '2024-04-10',),
    (5, 7, '5678901234', '2023-05-01'), (6, 7, '6789012345', '2024-06-05',),
    (7, 10, '7890123456', '2024-07-25'), (8, 10, '8901234567', '2024-07-30',),
    (9, 6, '9012345678', '2024-09-12'), (10, 7, '0123456789', '2024-10-01',),
    (1, 3, '1234567890', '2025-01-01'), (2, 5, '2345678901', '2025-02-15',),
    (3, 6, '3456789012', '2025-03-20'), (4, 6, '4567890123', '2025-04-10',),
    (5, 7, '5678901234', '2025-05-01'), (6, 7, '6789012345', '2025-06-05',),
    (7, 10, '7890123456', '2025-07-25'), (8, 10, '8901234567', '2025-07-30',),
    (9, 6, '9012345678', '2025-09-12'), (10, 7, '0123456789', '2025-10-01',)]

    cursor.executemany('INSERT OR IGNORE INTO pacientes_planos (id_paciente, id_plano, numero_carteirinha, validade) VALUES (?, ?, ?, ?)', dados)
    conn.commit()
    print('Dados de Planos de Pacientes Inseridos!')
    conn.close()

def DADOS_DOENCAS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
    ('Gripe', 'J10',), ('Diabetes Mellitus', 'E14',), ('Hipertensão Essencial', 'I10',),
    ('Asma', 'J45',), ('Pneumonia', 'J18',), ('Infarto Agudo do Miocárdio', 'I21',),
    ('Insuficiência Renal Crônica', 'N18',), ('Tuberculose Pulmonar', 'B19',), ('Hepatite Viral', 'B19',),
    ('Depressão', 'F32',), ('Câncer de Mama', 'C50',), ('Acidente Vascular Cerebral', 'I63',),
    ('Gastrite', 'K29',), ('HIV/AIDS', 'B24',), ('Artrite Reumatoide', 'M06',),
    ('Esquizofrenia', 'F20',), ('Doença de Alzheimer', 'G30',), ('Lombalgia', 'M54',),
    ('Malária', 'B50',), ('Cistite', 'N30',)]

    cursor.executemany('INSERT OR IGNORE INTO doencas (nome, CID) VALUES (?, ?)', dados)
    conn.commit()
    print('Dados de Doenças Inseridos!')
    conn.close()

def DADOS_PACIENTES_DOENCAS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()

    dados = [
    (1, 1, '2023-12-15',), (3, 2, '2023-12-20',), (3, 3, '2023-12-27',),
    (2, 4, '2024-02-02',), (4, 10, '2024-02-05',), (3, 14, '2024-03-15',),
    (3, 13, '2024-03-20',), (5, 9, '2024-04-25',), (11, 5, '2024-06-03',),
    (4, 5, '2024-06-03',), (6, 10, '2024-06-04',), (2, 1, '2024-06-06',),
    (5, 1, '2024-07-25',), (7, 1, '2024-08-10',), (5, 1, '2024-09-02',),
    (6, 5, '2024-09-02',), (8, 10, '2024-11-19',), (1, 1, '2025-02-02',),
    (7, 5, '2025-02-11',), (9, 10, '2025-03-17',), (13, 5, '2025-03-23',),
    (8, 10, '2025-04-29',), (10, 5, '2025-05-02',), (10, 10, '2025-05-17',),
    (9, 1, '2024-07-25',), (9, 2, '2024-08-10',), (12, 2, '2024-09-02',),
    (10, 4, '2024-10-05',), (8, 4, '2024-11-19',), (5, 1, '2025-02-02',),
    (1, 5, '2025-02-11',), (7, 10, '2025-03-17',), (5, 5, '2025-03-23',),
    (2, 10, '2025-04-29',), (6, 2, '2025-05-02',), (9, 4, '2025-05-17',)]

    cursor.executemany('INSERT OR IGNORE INTO pacientes_doencas (id_paciente, id_doenca, data_diagnostico) VALUES (?, ?, ?)', dados)
    conn.commit()
    print('Dados de Pacientes Doenças Inseridos!')
    conn.close()

def DADOS_AGENDAMENTOS():
    conn = ROTA_BANCO()
    cursor = conn.cursor()
    dados = [
    (1, 2, '2025-06-17', '08:30:00', 'Confirmado',), (2, 1,'2025-06-17', '09:00:00', 'Confirmado',),
    (3, 4, '2025-06-17', '10:00:00', 'Confirmado',), (4, 3, '2025-06-17', '11:30:00', 'Confirmado',),
    (5, 5, '2025-06-18', '08:00:00', 'Confirmado',), (6, 6, '2025-06-18', '14:00:00', 'Confirmado',),
    (7, 7, '2025-06-19', '15:30:00', 'Confirmado',), (8, 8, '2025-06-18', '16:00:00', 'Confirmado',),
    (9, 9, '2025-06-23', '10:30:00', 'Confirmado',), (10, 10, '2025-06-23', '11:00:00', 'Cancelado',),
    (1, 3, '2025-06-24', '08:30:00', 'Cancelado',), (2, 4,'2025-06-24', '09:00:00', 'Agendado',),
    (3, 2, '2025-06-24', '10:00:00', 'Agendado',), (4, 1, '2025-06-24', '11:30:00', 'Agendado',),
    (5, 1, '2025-06-25', '08:00:00', 'Agendado',), (6, 2, '2025-06-25', '14:00:00', 'Agendado',),
    (7, 3, '2025-06-25', '15:30:00', 'Agendado',), (8, 7, '2025-06-25', '16:00:00', 'Agendado',),
    (9, 9, '2025-06-26', '10:30:00', 'Agendado',), (10, 1, '2025-06-26', '11:00:00', 'Agendado',),
    (11, 3, '2025-06-27', '08:30:00', 'Cancelado',), (12, 4,'2025-06-27', '09:00:00', 'Agendado',),
    (13, 2, '2025-06-27', '10:00:00', 'Agendado',), (4, 11, '2025-06-27', '11:30:00', 'Agendado',),
    (5, 11, '2025-07-01', '08:00:00', 'Agendado',), (6, 12, '2025-07-01', '14:00:00', 'Agendado',),
    (7, 13, '2025-07-01', '15:30:00', 'Agendado',), (4, 13, '2025-07-01', '16:00:00', 'Agendado',),
    (2, 9, '2025-07-04', '10:30:00', 'Agendado',), (10, 1, '2025-07-04', '11:00:00', 'Agendado',)]

    cursor.executemany('INSERT OR IGNORE INTO agendamentos (id_paciente, id_medico, data_agendamento, hora_agendamento, status) VALUES (?, ?, ?, ?, ?)', dados)
    conn.commit()
    print('Dados de Agendamentos Inseridos!')
    conn.close()

def INCLUIR_REGISTROS():
    print('Acessando registros de inserção!\n')
    DADOS_PAISES()
    DADOS_CIDADES()
    DADOS_ESPECIALIDADES()
    DADOS_MEDICOS()
    DADOS_PACIENTES()
    DADOS_PLANOS_SAUDE()
    DADOS_PACIENTES_PLANOS()
    DADOS_DOENCAS()
    DADOS_PACIENTES_DOENCAS()
    DADOS_AGENDAMENTOS()
    print('\nRegistros Inseridos com Sucesso!\n')