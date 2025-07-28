import customtkinter as ctk
from controller.controller import Controller
from model.model import Model
from tkinter import messagebox

class Cad_Medicos(ctk.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance

        # Altura Y entre containers Principais = 20
        # Label e Input (Padrão)
        # Width Input = 40px
        # Width Button = 60px

        # CONTAINER - Nome
        container_nome = ctk.CTkFrame(self, fg_color="transparent")
        container_nome.pack(side='top', pady=20)

        ctk.CTkLabel(container_nome, text="Nome Completo").pack()
        self.input_nome = ctk.CTkEntry(container_nome, placeholder_text="Dr. João da Silva", width=780, height=40, border_width=0)
        self.input_nome.pack()



        # CONTAINER - Especialidade
        container_especialidade = ctk.CTkFrame(self, fg_color="transparent")
        container_especialidade.pack(side='top', pady=20)
        ctk.CTkLabel(container_especialidade, text="Especialidade").pack()

        self.lista_especialidades = self.controller.buscarEspecialidadesBD()
        self.input_especialidades = ctk.CTkComboBox(container_especialidade, values=self.lista_especialidades, width=780, height=40, border_width=0)
        self.input_especialidades.set("Selecione a Especialidade")
        self.input_especialidades.pack(side='left')
        #self.input_especialidade = ctk.CTkEntry(container_especialidade, placeholder_text="Cardiologia", width=780, height=40, border_width=0)
        #self.input_especialidade.pack()
        


        # CONTAINER - Nascimento e CPF
        container_dados = ctk.CTkFrame(self, fg_color="transparent")
        container_dados.pack(side='top', pady=20)

        container_nasc = ctk.CTkFrame(container_dados, fg_color="transparent")
        container_nasc.pack(side='left', padx=10)

        ctk.CTkLabel(container_nasc, text="Data de Nascimento").pack()
        self.input_nasc = ctk.CTkEntry(container_nasc, placeholder_text="DD/MM/AAAA", width=380, height=40, border_width=0)
        self.input_nasc.pack()

        container_cpf = ctk.CTkFrame(container_dados, fg_color="transparent")
        container_cpf.pack(side='left', padx=10)

        ctk.CTkLabel(container_cpf, text="CPF").pack()
        self.input_cpf = ctk.CTkEntry(container_cpf, placeholder_text="000.000.000-00", width=380, height=40, border_width=0)
        self.input_cpf.pack()



        # CONTAINER - Salário e Cidade
        container_dados2 = ctk.CTkFrame(self, fg_color="transparent")
        container_dados2.pack(side='top', pady=20)

        container_salario = ctk.CTkFrame(container_dados2, fg_color="transparent")
        container_salario.pack(side='left', padx=10)
        ctk.CTkLabel(container_salario, text="Salário (R$)").pack()
        self.input_salario = ctk.CTkEntry(container_salario, placeholder_text="Ex: 8500.50", width=380, height=40, border_width=0)
        self.input_salario.pack()

        # self.input_cidade = ctk.CTkEntry(container_cidade, placeholder_text="São Paulo", width=380, height=40, border_width=0)
        # self.input_cidade.pack(side='left')

        container_cidade = ctk.CTkFrame(container_dados2, fg_color="transparent")
        container_cidade.pack(side='left', padx=10)
        ctk.CTkLabel(container_cidade, text="Cidade").pack(side='top')

        self.lista_cidades = self.controller.buscarCidadesBD()
        self.input_cidades = ctk.CTkComboBox(container_cidade, values=self.lista_cidades, width=380, height=40, border_width=0)
        self.input_cidades.set("Selecione a Cidade")
        self.input_cidades.pack(side='left')

        # CONTAINER - Rua, Número e Complemento
        container_endereco = ctk.CTkFrame(self, fg_color="transparent")
        container_endereco.pack(side='top', pady=20)

        container_rua = ctk.CTkFrame(container_endereco, fg_color="transparent")
        container_rua.pack(side='left', padx=10)
        ctk.CTkLabel(container_rua, text="Rua").pack()
        self.input_rua = ctk.CTkEntry(container_rua, placeholder_text="Av. Brasil", width=380, height=40, border_width=0)
        self.input_rua.pack(side='left')

        container_numero = ctk.CTkFrame(container_endereco, fg_color="transparent")
        container_numero.pack(side='left', padx=10)
        ctk.CTkLabel(container_numero, text="Número").pack()
        self.input_numero = ctk.CTkEntry(container_numero, placeholder_text="123", width=80, height=40, border_width=0)
        self.input_numero.pack(side='left')

        container_complemento = ctk.CTkFrame(container_endereco, fg_color="transparent")
        container_complemento.pack(side='left', padx=10)
        ctk.CTkLabel(container_complemento, text="Complemento").pack()
        self.input_complemento = ctk.CTkEntry(container_complemento, placeholder_text="Apto 4B", width=280, height=40, border_width=0)
        self.input_complemento.pack(side='left')



        # CONTAINER, BOTÕES
        container_button = ctk.CTkFrame(self, fg_color="transparent")
        container_button.pack(side='top', pady=20)

        salvar = ctk.CTkButton(container_button, text="Salvar", command=self.salvar_dados_medico, width=380, height=60)
        salvar.pack(side='left', padx=10)
        
        limpar = ctk.CTkButton(container_button, text="Limpar Campos", command=self.limpar_campos, fg_color="gray", width=380, height=60)
        limpar.pack(side='right', padx=10)

    def salvar_dados_medico(self):
        nome = self.input_nome.get()
        nasc = self.input_nasc.get()
        especialidade = self.input_especialidades.get()
        cpf = self.input_cpf.get()
        salario = self.input_salario.get()
        cidade = self.input_cidades.get()
        rua = self.input_rua.get()
        numero = self.input_numero.get()
        complemento = self.input_complemento.get()

        if self.controller.cadastrarMedico(nome, nasc, especialidade, cpf, salario, cidade, rua, numero, complemento):
            messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Falha ao cadastrar o médico. Verifique os dados e tente novamente.")
    
    def limpar_campos(self):
        self.input_nome.delete(0, 'end')
        self.input_nasc.delete(0, 'end')
        self.input_cpf.delete(0, 'end')
        self.input_salario.delete(0, 'end')
        self.input_cidades.set("Selecione a Cidade")
        self.input_especialidades.set("Selecione a Especialidade")
        self.input_rua.delete(0, 'end')
        self.input_numero.delete(0, 'end')
        self.input_complemento.delete(0, 'end')