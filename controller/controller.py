class Consultas_Model:
    def __init__(self, model_db):
        self._model_db = model_db
    def conf_agendamentos(self):
        agendamentos = self._model_db.consulta_agendamentos()
        largura = [5, 30, 25, 20, 20, 30]
        cabecalho = ["ID", "MÉDICO", "STATUS DA CONSULTA", "DATA AGENDADA", "HORÁRIO MARCADO", "PACIENTE"]
        conf_cabecalho = "".join(text.ljust(w) for text, w in zip(cabecalho, largura))
        formatacao = conf_cabecalho + "\n"
        formatacao += "-" * sum(largura) + "\n"

        for agendamento in agendamentos:
            linha = "".join(str(item).ljust(w) for item, w in zip(agendamento, largura))
            formatacao += linha + "\n"
        return formatacao
    def conf_pacientes(self):
        pacientes = self._model_db.consulta_pacientes()
        largura = [4, 30, 20, 6, 35, 15, 20, 30, 5]
        cabecalho = ["ID", "NOME", "CPF", "IDADE", "EMAIL", "TELEFONE", "CIDADE", "RUA", "Nº"]
        conf_cabecalho = "".join(text.ljust(w) for text, w in zip(cabecalho, largura))
        formatacao = conf_cabecalho + "\n"
        formatacao += "-" * sum(largura) + "\n"

        for paciente in pacientes:
            linha = "".join(str(item).ljust(w) for item, w in zip(paciente, largura))
            formatacao += linha + "\n"
        return formatacao
    def conf_medicos(self):
        pacientes = self._model_db.consulta_medicos()
        largura = [4, 30, 20, 6, 35, 15, 20, 30, 5]
        cabecalho = ["ID", "NOME", "CPF", "IDADE", "ESPECIALIDADE", "SALÁRIO", "CIDADE", "RUA", "Nº"]
        conf_cabecalho = "".join(text.ljust(w) for text, w in zip(cabecalho, largura))
        formatacao = conf_cabecalho + "\n"
        formatacao += "-" * sum(largura) + "\n"

        for paciente in pacientes:
            linha = "".join(str(item).ljust(w) for item, w in zip(paciente, largura))
            formatacao += linha + "\n"
        return formatacao

class Controller:
    def __init__(self, model_db):
        self._model_db = model_db
    def set_app(self, app):
        self.app = app
    def buscarCidadesBD(self):
        return self._model_db.buscarCidades()
    def buscarEspecialidadesBD(self):
        return self._model_db.buscarEspecialidades()
    def buscarMedicosBD(self):
        return self._model_db.buscarMedicos()
    def buscarPacientesBD(self):
        return self._model_db.buscarPacientes()
    def buscarStatusBD(self):
        return self._model_db.buscarStatus()

    def cadastrarMedico(self, nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
        if not self.validacaoMedico(nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
            print("Controller: Dados do médico inválidos.")
            return False
        print(f"Controller: Consultando ID para a especialidade: {especialidade}")
        id_espec = self._model_db.buscarIdEspecialidade(especialidade)
        if id_espec:
            print(f"Controller: ID encontrado: {id_espec}")
        else:
            print("Controller: Especialidade não encontrada.")
        especialidade = id_espec

        print(f"Controller: Consultando ID para a cidade: {cidade}")
        id_city = self._model_db.buscarIdCidade(cidade)
        if id_city:
            print(f"Controller: ID encontrado: {id_city}")
        else:
            print("Controller: Cidade não encontrada.")
        cidade = id_city

        print(f"Controller: Tentando cadastrar o médico: {nome}")
        if self._model_db.salvarMedico(nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
            print("Controller: Médico salvo com sucesso via Model.")
            return True
        else:
            print("Controller: Falha ao salvar Médico via Model.")
            return False

    def validacaoMedico(self, nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
        if not nome or not cpf or not especialidade:
            print("Validação: Nome, CPF e Especialidade são campos obrigatórios.")
            return False
        
        return True

    def cadastrarPaciente(self, nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
        if not self.validacaoPaciente(nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
            print("Controller: Dados do médico inválidos.")
            return False

        print(f"Controller: Consultando ID para a cidade: {cidade}")
        id_city = self._model_db.buscarIdCidade(cidade)
        if id_city:
            print(f"Controller: ID encontrado: {id_city}")
        else:
            print("Controller: Cidade não encontrada.")
        cidade = id_city

        print(f"Controller: Tentando cadastrar o médico: {nome}")
        if self._model_db.salvarPaciente(nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
            print("Controller: Paciente salvo com sucesso via Model.")
            return True
        else:
            print("Controller: Falha ao salvar Paciente via Model.")
            return False

    def validacaoPaciente(self, nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
        if not nome or not cpf or not email:
            print("Validação: Nome, CPF e Email são campos obrigatórios.")
            return False
        
        return True
    
    def cadastrarAgendamento(self, data, hora, status, paciente, medico):
        
        print(f"Controller: Consultando ID para a especialidade: {medico}")
        id_medico = self._model_db.buscarIdMedicos(medico)
        if id_medico:
            print(f"Controller: ID encontrado: {id_medico}")
        else:

            print("Controller: Especialidade não encontrada.")
        medico = id_medico

        print(f"Controller: Consultando ID para a especialidade: {paciente}")
        id_paciente = self._model_db.buscarIdPacientes(paciente)
        if id_paciente:
            print(f"Controller: ID encontrado: {id_paciente}")
        else:

            print("Controller: Especialidade não encontrada.")
        paciente = id_paciente

        print(f"Controller: Consultando ID para a especialidade: {status}")
        id_agendamento = self._model_db.buscarIdAgendamentos(status)
        if id_agendamento:
            print(f"Controller: ID encontrado: {id_agendamento}")
        else:

            print("Controller: Especialidade não encontrada.")

        print(f"Controller: Tentando cadastrar o médico: {status}")
        if self._model_db.salvarAgendamento(data, hora, status, paciente, medico):
            print("Controller: Médico salvo com sucesso via Model.")
            return True
        else:
            print("Controller: Falha ao salvar Médico via Model.")
            return False