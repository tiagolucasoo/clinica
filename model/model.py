import sqlite3
import os

def ROTA_BANCO():
        caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'clinica.db'))
        conn = sqlite3.connect(caminho_banco)
        return conn

class Validacoes:
    pass

class Registros:
    def salvarMedico(self, nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO medicos (nome, data_nas, id_especialidade, cpf, salario, rua, numero, complemento, id_cidade)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (nome, nasc, especialidade, cpf, salario, rua, numero, complemento, cidade))
            conn.commit()
            print("Model: Médico salvo com sucesso no banco de dados.")
            return True
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao salvar médico: {e}")
            return False
        except Exception as e:
            print(f"Erro geral ao salvar médico: {e}")
            return False
        finally:
            conn.close()
    
    def salvarAgendamento(self, data, hora, status, paciente, medico):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO agendamentos (data_agendamento, hora_agendamento, status, id_paciente, id_medico)
                VALUES (?, ?, ?, ?, ?)""",
                (data, hora, status, paciente, medico))
            conn.commit()
            print("Model: Médico salvo com sucesso no banco de dados.")
            return True
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao salvar médico: {e}")
            return False
        except Exception as e:
            print(f"Erro geral ao salvar médico: {e}")
            return False
        finally:
            conn.close()

    def salvarPaciente(self, nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
        conn = ROTA_BANCO()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO pacientes (nome, email, telefone, data_nasc, cpf, renda_familiar, rua, numero, complemento, id_cidade)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento))
            conn.commit()
            print("Model: Paciente salvo com sucesso no banco de dados.")
            return True
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao salvar Paciente: {e}")
            return False
        except Exception as e:
            print(f"Erro geral ao salvar Paciente: {e}")
            return False
        finally:
            conn.close()

class Combo_box:
    def buscarCidades(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        
        cursor.execute("SELECT nome FROM cidades")
        cidades_lista = [row[0] for row in cursor.fetchall()]
        conn.close()
        return cidades_lista
    def buscarEspecialidades(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        
        cursor.execute("SELECT nome FROM especialidades")
        especialidades_lista = [row[0] for row in cursor.fetchall()]
        conn.close()
        return especialidades_lista
    def buscarMedicos(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        
        cursor.execute("SELECT nome FROM medicos")
        medicos_lista = [row[0] for row in cursor.fetchall()]
        conn.close()
        return medicos_lista
    def buscarPacientes(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        
        cursor.execute("SELECT nome FROM pacientes")
        pacientes_lista = [row[0] for row in cursor.fetchall()]
        conn.close()
        return pacientes_lista
    def buscarStatus(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        
        cursor.execute("SELECT DISTINCT status FROM agendamentos")
        status_lista = [row[0] for row in cursor.fetchall()]
        conn.close()
        return status_lista
    def buscarPlanos(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        
        cursor.execute("SELECT DISTINCT nome FROM planos_saude")
        planos = [row[0] for row in cursor.fetchall()]
        conn.close()
        return planos
    def buscarDoencas(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        
        cursor.execute("SELECT DISTINCT nome FROM doencas")
        doencas = [row[0] for row in cursor.fetchall()]
        conn.close()
        return doencas
    def listarEspecialidades():
        conn = ROTA_BANCO()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT nome FROM especialidades")
            especialidades = [row[0] for row in cursor.fetchall()]
            return especialidades
        finally:
            conn.close()

class Consultas:
    def consulta_agendamentos(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id_agendamento, m.nome, a.status, a.data_agendamento, a.hora_agendamento, p.nome
                       FROM agendamentos a
                       INNER JOIN pacientes p ON (p.id_paciente = a.id_paciente)
                       INNER JOIN medicos m ON (m.id_medico = a.id_medico)
                       """)
        dados = cursor.fetchall()
        conn.close()
        return dados
    def consulta_pacientes(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id_paciente, p.nome, p.cpf,
                       --CAST((strftime('%Y', 'now') - strftime('%Y', p.data_nasc)) AS INTEGER) AS Idade,
                       CAST((julianday('now') - julianday(p.data_nasc)) / 365.25 AS INTEGER) AS Idade,
                       p.email, p.telefone, c.nome, p.rua, p.numero
                       FROM pacientes p
                       INNER JOIN cidades c ON (c.id_cidade = p.id_cidade)
                       """)
        dados = cursor.fetchall()
        conn.close()
        return dados
    def consulta_medicos(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT m.id_medico, m.nome, m.cpf,
                       CAST((julianday('now') - julianday(m.data_nas)) / 365.25 AS INTEGER) AS Idade,
                       e.nome, m.salario, c.nome, m.rua, m.numero
                       FROM medicos m
                       INNER JOIN cidades c ON (c.id_cidade = m.id_cidade)
                       INNER JOIN especialidades e ON (e.id_especialidade = m.id_especialidade)
                       """)
        dados = cursor.fetchall()
        conn.close()
        return dados
    def consulta_doencas(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        cursor.execute("""
                        SELECT d.id_doenca, d.nome, d.CID,
                            (SELECT count(pd.id_paciente) FROM pacientes_doencas pd, pacientes p WHERE (pd.id_paciente = p.id_paciente) AND (pd.id_doenca = d.id_doenca)) 'Pacientes diagnosticados'
                        FROM doencas d
        """)
        dados = cursor.fetchall()
        conn.close()
        return dados
    def consulta_especialidades(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        cursor.execute("""
                        SELECT e.id_especialidade, e.nome,
                            (SELECT count(m.id_medico) FROM medicos m WHERE (m.id_especialidade = e.id_especialidade)) 'Médicos'
                        FROM especialidades e
        """)
        dados = cursor.fetchall()
        conn.close()
        return dados
    def consulta_pacientes_doencas(self):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT p.nome, pd.data_diagnostico, d.nome, plan.nome, pp.numero_carteirinha, pp.validade
                    FROM pacientes p
                        INNER JOIN pacientes_doencas pd ON (pd.id_paciente = p.id_paciente)
                        INNER JOIN doencas d ON (d.id_doenca = pd.id_doenca)
                        INNER JOIN pacientes_planos pp ON (pp.id_paciente = p.id_paciente)
                        INNER JOIN planos_saude plan ON (plan.id_plano = pp.id_plano)
                    --WHERE (pd.id_doenca = d.id_doenca) AND (p.id_paciente = pd.id_paciente)
                    --AND (pp.id_paciente = p.id_paciente)
                    """)
        dados = cursor.fetchall()
        conn.close()
        return dados
    
class Model:
    def __init__(self):
        self.combo_box = Combo_box()
        self.salvar = Registros()
    def buscarIdEspecialidade(self, nome_especialidade):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        resultado = None
        try:
            cursor.execute("""SELECT id_especialidade FROM especialidades WHERE nome = ?""", (nome_especialidade,))
            resultado = cursor.fetchone() 
            
        except Exception as e:
            print(f"Erro ao buscar especialidade: {e}")
        finally:
            conn.close()
            
        return resultado[0] if resultado else None
    def buscarIdCidade(self, nome_cidade):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        resultado = None
        try:
            cursor.execute("""SELECT id_cidade FROM cidades WHERE nome = ?""", (nome_cidade,))
            resultado = cursor.fetchone() 
            
        except Exception as e:
            print(f"Erro ao buscar cidade: {e}")
        finally:
            conn.close()
        return resultado[0] if resultado else None
    def buscarIdAgendamentos(self, status):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        resultado = None
        try:
            cursor.execute("""SELECT id_agendamento FROM agendamentos WHERE status = ?""", (status,))
            resultado = cursor.fetchone() 
            
        except Exception as e:
            print(f"Erro ao buscar cidade: {e}")
        finally:
            conn.close()
        return resultado[0] if resultado else None
    def buscarIdMedicos(self, medico):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        resultado = None
        try:
            cursor.execute("""SELECT id_medico FROM medicos WHERE nome = ?""", (medico,))
            resultado = cursor.fetchone() 
            
        except Exception as e:
            print(f"Erro ao buscar cidade: {e}")
        finally:
            conn.close()
        return resultado[0] if resultado else None
    def buscarIdPacientes(self, paciente):
        conn = ROTA_BANCO()
        cursor = conn.cursor()
        resultado = None
        try:
            cursor.execute("""SELECT id_paciente FROM pacientes WHERE nome = ?""", (paciente,))
            resultado = cursor.fetchone() 
            
        except Exception as e:
            print(f"Erro ao buscar cidade: {e}")
        finally:
            conn.close()
        return resultado[0] if resultado else None