#Retorna os dados para o CTK Text com a formatação
import datetime as dt
import re

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
    def conf_doencas(self):
        doencas = self._model_db.consulta_doencas()
        largura = [5, 40, 10, 20]
        cabecalho = ["ID", "DESCRIÇÃO", "CID", "PACIENTES"]
        conf_cabecalho = "".join(text.ljust(w) for text, w in zip(cabecalho, largura))
        formatacao = conf_cabecalho + "\n"
        formatacao += "-" * sum(largura) + "\n"

        for doenca in doencas:
            linha = "".join(str(item).ljust(w) for item, w in zip(doenca, largura))
            formatacao += linha + "\n"
        return formatacao
    def conf_especialidades(self):
        especialidades = self._model_db.consulta_especialidades()
        largura = [5, 40, 20]
        cabecalho = ["ID", "DESCRIÇÃO", "MÉDICOS"]
        conf_cabecalho = "".join(text.ljust(w) for text, w in zip(cabecalho, largura))
        formatacao = conf_cabecalho + "\n"
        formatacao += "-" * sum(largura) + "\n"

        for especialidade in especialidades:
            linha = "".join(str(item).ljust(w) for item, w in zip(especialidade, largura))
            formatacao += linha + "\n"
        return formatacao
    def conf_pacientes_doencas(self):
        pacientes_doencas = self._model_db.consulta_pacientes_doencas()
        largura = [35, 20, 30, 20, 25, 15]
        #p.nome, pd.data_diagnostico, d.nome, plan.nome, pp.numero_carteirinha, pp.validade
        cabecalho = ["PACIENTE", "DATA DIAGNÓSTICO", "OCORRÊNCIA", "PLANO", "CARTEIRINHA", "VÁLIDO ATÉ"]
        conf_cabecalho = "".join(text.ljust(w) for text, w in zip(cabecalho, largura))
        formatacao = conf_cabecalho + "\n"
        formatacao += "-" * sum(largura) + "\n"

        for paciente_doenca in pacientes_doencas:
            linha = "".join(str(item).ljust(w) for item, w in zip(paciente_doenca, largura))
            formatacao += linha + "\n"
        return formatacao

# Retorna os dados para os combo box
class Consultas_Controller:
    def __init__(self, model_db):
        self._model_db = model_db
    def buscarCidadesBD(self):
        return self._model_db.combo_box.buscarCidades()
    def buscarEspecialidadesBD(self):
        return self._model_db.combo_box.buscarEspecialidades()
    def buscarMedicosBD(self):
        return self._model_db.combo_box.buscarMedicos()
    def buscarPacientesBD(self):
        return self._model_db.combo_box.buscarPacientes()
    def buscarStatusBD(self):
        return self._model_db.combo_box.buscarStatus()
    def buscarPlanosBD(self):
        return self._model_db.combo_box.buscarPlanos()
    def buscarDoencasBD(self):
        return self._model_db.combo_box.buscarDoencas()

class Validacoes:
    def __init__(self, controller_instance):
        self.controller = controller_instance
        pass
    
    def validarHorario(self, hora):
        erro = self.controller.mostrar_erro
        
        if not hora:
            erro("Informe o horário do agendamento!")
            return False
        
        if len(hora) != 5 or hora[2] != ':':
            erro("Formato inválido! Use HH:MM")
            return False
        
        try:
            h, m = map(int, hora.split(':'))
            if 0 <= h <= 23 and 0 <= m <= 59:
                return True
            else:
                erro("Horário inválido!")
                return False
            
        except ValueError as v:
            erro(f"Erro: {v}\nHorário com caracteres inválidos!")
            return False
    def validarDatas(self, data):
        erro = self.controller.mostrar_erro
        data = data.strip()
        formato_us = "%Y-%m-%d"
        try:
            if len(data) == 0:
                erro("Nenhuma data informada!")
            elif len(data) == 10:
                formato_br_1 = "%d/%m/%Y"
                validacao = dt.datetime.strptime(data, formato_br_1)
                data = validacao.strftime(formato_us)
                return data
            elif len(data) == 8:
                formato_br_2 = "%d/%m/%y"
                validacao = dt.datetime.strptime(data, formato_br_2)
                data = validacao.strftime(formato_us)
                return data
            else:
                erro(f"A Data digitada não é um valor válido!")
                return False

        except ValueError as v:
            erro(f"A data digitada '{data} é inválida! {v}'")
            return False
    def validarCPF(self, cpf):
        erro = self.controller.mostrar_erro
        conf_cpf = cpf.replace(".", "").replace("-", "")

        if not cpf:
            erro("Informe o CPF!")
            return False
        
        if len(conf_cpf) != 11 or not conf_cpf.isdigit():
            erro("CPF Inválido, verifique os dígitos!")
            return False

        if len(set(conf_cpf)) == 1:
            erro("CPF Inválido!")
            return False
        
        cpf = conf_cpf
        return True
    def validarSalario(self, valor):
        erro = self.controller.mostrar_erro
        try:
            valor = int(valor.replace('.', ''))
            if valor > 0:
                return True
            else:
                erro("O valor de renda/salário deve ser um valor positivo!")
                return False
            
        except ValueError:
            erro("Valor de renda/salário incorreto!")
            return False
    def validarEmail(self, email):
        erro = self.controller.mostrar_erro
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not email:
            erro("Informe o endereço do e-mail!")
            return False
        if re.match(padrao, email):
            return True
        else:
            erro("Formato de e-mail inválido!")
            return False
    def validarTelefone(self, telefone):
        erro = self.controller.mostrar_erro
        numeros = re.sub(r'\D', '', telefone)

        if len(numeros) in [10, 11]:
            return True
        else:
            erro("Telefone inválido! Digite novamente com o DDD")
            return False
    def validarRua(self, rua, numero):
        erro = self.controller.mostrar_erro
        if not numero:
            erro("Informe o número da residência!")
            return False
        if not numero.isdigit():
            erro("Número do endereço não é numérico!")
            return False
        if not rua:
            erro("Informe o endereço da rua")
            return False
        if rua.isdigit():
            erro("Nome de rua inválida!")
            return False
        if len(rua.strip()) < 10:
            erro("Nome de rua muito curta, digite corretamente!")
            return False
        
        return True
        
    def validacaoAgendamento(self, data, hora, status, medico, paciente):
        lista_s = self.controller.consultas.buscarStatusBD()
        lista_m = self.controller.consultas.buscarMedicosBD()
        lista_p = self.controller.consultas.buscarPacientesBD()
        erro = self.controller.mostrar_erro

        if not data and not hora:
            erro("Insira as informações de data / horário!")
            return False
        
        if status not in lista_s or status == "Selecione o Status":
            erro("O status selecionado não é válido!")
            return False

        if medico not in lista_m or medico == "Selecione o Médico":
            erro("O médico selecionado não é válido!")
            return False

        if paciente not in lista_p or paciente == "Selecione o Paciente":
            erro("O paciente selecionado não é válido!")
            return False
        
        if not self.validarDatas(data):
            return False
        
        if not self.validarHorario(hora):
            return False

        return True
    def validacaoMedico(self, nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
        lista_e = self.controller.consultas.buscarEspecialidadesBD()
        lista_c = self.controller.consultas.buscarCidadesBD()
        erro = self.controller.mostrar_erro

        if especialidade not in lista_e or especialidade == "Selecione a Especialidade":
            erro("A especialidade selecionada não é válida!")
            return False
        if cidade not in lista_c or cidade == "Selecione a Cidade":
            erro("A cidade selecionada não é válida")
            return False
        if not self.validarRua(rua, numero):
            return False
        if not nome:
            erro("Digite o nome do Médico")
            return False
        if not self.validarDatas(nasc):
            return False
        if not self.validarCPF(cpf):
            return False
        if not self.validarSalario(salario):
            return False
        
        return True
    def validacaoPaciente(self, nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
        lista_c = self.controller.consultas.buscarCidadesBD()
        erro = self.controller.mostrar_erro

        if not nome:
            erro("Informe o nome do Paciente!")
            return False
        
        if cidade not in lista_c or cidade == "Selecione a Cidade":
            erro("A cidade selecionada não é válida")
            return False
        
        if not self.validarDatas(nasc):
            return False
        
        if not self.validarCPF(cpf):
            return False
        
        if not self.validarSalario(renda):
            return False
        
        if not self.validarEmail(email):
            return False
        
        if not self.validarTelefone(telefone):
            return False

        if not self.validarRua(rua, numero):
            return False
        
        return True

    def validacaoPlanoPaciente(self, paciente, plano, numero_carteirinha, validade):
        erro = self.controller.mostrar_erro
        lista_pp = self.controller.consultas.buscarPlanosBD()
        lista_p = self.controller.consultas.buscarPacientesBD()

        if plano not in lista_pp or plano == "Selecione o Plano de Saúde":
            erro("O Plano selecionado não é válido!")
            return False

        if paciente not in lista_p or paciente == "Selecione o Paciente":
            erro("O paciente selecionado não é válido!")
            return False
        
        if not self.validarDatas(validade):
            return False
        
        if not numero_carteirinha:
            erro("Informe o nº da carteirinha")
            return False
        
        if not numero_carteirinha.isdigit():
            erro("Número da carteirinha não é válido!")
            return False
        
        return True
    def validacaoPacienteDoenca(self, paciente, doencas, observacao, data):
        erro = self.controller.mostrar_erro
        lista_p = self.controller.consultas.buscarPacientesBD()
        lista_d = self.controller.consultas.buscarDoencasBD()

        if paciente not in lista_p or paciente == "Selecione o Paciente":
            erro("O paciente selecionado não é válido!")
            return False
        
        if doencas not in lista_d or doencas == "Selecione a Doença":
            erro("A doença selecionada não é válida!")
            return False
        
        if not self.validarDatas(data):
            return False
        
        return True
        
class Controller:
    def __init__(self, model_db):
        self._model_db = model_db
        self.consultas = Consultas_Controller(model_db)
        self.validacoes = Validacoes(self)
        self.app = None
    def set_app(self, app):
        self.app = app

    def mostrar_erro(self, mensagem: str):
        if self.app:
            self.app.exibir_mensagem_erro(mensagem)
    def mostrar_sucesso(self, mensagem: str):
        if self.app:
            self.app.exibir_mensagem_sucesso(mensagem)

    def cadastrarMedico(self, nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
        if not self.validacoes.validacaoMedico(nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
            return False

        id_espec = self._model_db.buscarIdEspecialidade(especialidade)
        id_city = self._model_db.buscarIdCidade(cidade)

        cidade = id_city
        especialidade = id_espec

        #Conversão do CPF
        cpf = cpf.replace(".", "").replace("-", "")
        conf_cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        cpf = conf_cpf

        #Conversão da Data
        formato_br = "%d/%m/%Y"
        conf_nasc1 = dt.datetime.strptime(nasc, formato_br)
        conf_nasc2 = conf_nasc1.strftime("%Y-%m-%d")
        nasc = conf_nasc2

        if self._model_db.salvar.salvarMedico(nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
            return True
        else:
            return False
    def cadastrarPaciente(self, nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
        if not self.validacoes.validacaoPaciente(nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
            return False

        id_city = self._model_db.buscarIdCidade(cidade)
        # if id_city:
        #     print(f"Controller: ID encontrado: {id_city}")
        # else:
        #     print("Controller: Cidade não encontrada.")
        cidade = id_city
        
        #Conversão do CPF
        cpf = cpf.replace(".", "").replace("-", "")
        conf_cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        cpf = conf_cpf

        #Conversão da Data
        formato_br = "%d/%m/%Y"
        conf_nasc1 = dt.datetime.strptime(nasc, formato_br)
        conf_nasc2 = conf_nasc1.strftime("%Y-%m-%d")
        nasc = conf_nasc2

        if self._model_db.salvar.salvarPaciente(nome, nasc, email, telefone, cpf, renda, cidade, rua, numero, complemento):
            return True
        else:
            return False
    def cadastrarPlanoPaciente(self, plano, paciente, numero_carteirinha, validade):
        if not self.validacoes.validacaoPlanoPaciente(paciente, plano, numero_carteirinha, validade):
            return False
        
        id_plano = self._model_db.buscarIdPlanos(plano)
        id_paciente = self._model_db.buscarIdPacientes(paciente)

        # if id_plano:
        #     print(f"Controller: ID encontrado: {id_plano}")
        # else:
        #     print("Controller: Especialidade não encontrada.")
        
        # if id_paciente:
        #     print(f"Controller: ID encontrado: {id_paciente}")
        # else:
        #     print("Controller: Especialidade não encontrada.")

        plano = id_plano
        paciente = id_paciente

        #Conversão da Data
        formato_br = "%d/%m/%Y"
        conf_val1 = dt.datetime.strptime(validade, formato_br)
        conf_val2 = conf_val1.strftime("%Y-%m-%d")
        validade = conf_val2
        
        if self._model_db.salvar.salvarPlanoPaciente(numero_carteirinha, validade, paciente, plano):
            return True
    def cadastrarPacientesDoencas(self, paciente, doencas, observacao, data):
        if not self.validacoes.validacaoPacienteDoenca(paciente, doencas, observacao, data):
            return False
        
        id_paciente = self._model_db.buscarIdPacientes(paciente)
        id_doenca = self._model_db.buscarIdDoencas(doencas)

        # if id_paciente:
        #     print(f"Controller: ID encontrado: {id_paciente}")
        # else:
        #     print("Controller: Especialidade não encontrada.")
        # if id_doenca:
        #     print(id_doenca)
        # else:
        #     print("Erro")
        
        doencas = id_doenca
        paciente = id_paciente

        #Conversão da Data
        formato_br = "%d/%m/%Y"
        conf_val1 = dt.datetime.strptime(data, formato_br)
        conf_val2 = conf_val1.strftime("%Y-%m-%d")
        data = conf_val2

        if self._model_db.salvar.salvarPacienteDoenca(paciente, doencas, observacao, data):
            return True
        
    def cadastrarAgendamento(self, data, hora, status, paciente, medico):
        if not self.validacoes.validacaoAgendamento(data, hora, status, medico, paciente):
            return False
        
        id_medico = self._model_db.buscarIdMedicos(medico)
        id_paciente = self._model_db.buscarIdPacientes(paciente)
        #id_agendamento = self._model_db.buscarIdAgendamentos(status)

        # if id_medico:
        #     continue
        # else:
        #     erro("Controller: Especialidade não encontrada.")
        # if id_paciente:
        #     pass
        # else:
        #     erro("Controller: Especialidade não encontrada.")
        # if id_agendamento:
        #     pass
        # else:
            # erro("Controller: Especialidade não encontrada.")
            
        medico = id_medico
        paciente = id_paciente
        data = self.validacoes.validarDatas(data)
        horario = f"{hora}:00"
        hora = horario

        if self._model_db.salvar.salvarAgendamento(data, hora, status, paciente, medico):
            return True
        else:
            return False