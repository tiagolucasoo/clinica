import customtkinter as ctk
from controller.controller import Controller
from model.model import Model
from tkinter import messagebox

class Cad_Paciente_doenca(ctk.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance

        # CONTAINER - Paciente e Doença
        container_dados = ctk.CTkFrame(self, fg_color="transparent")
        container_dados.pack(side='top', pady=20)
        
        container_paciente = ctk.CTkFrame(container_dados, fg_color="transparent")
        container_paciente.pack(side='left', padx=10)

        ctk.CTkLabel(container_paciente, text="Paciente").pack()
        self.lista_pacientes = self.controller.consultas.buscarPacientesBD()
        self.input_pacientes = ctk.CTkComboBox(container_paciente, values=self.lista_pacientes, width=380, height=40, border_width=0)
        self.input_pacientes.set("Selecione o Paciente")
        self.input_pacientes.pack(side='left')

        container_medico = ctk.CTkFrame(container_dados, fg_color="transparent")
        container_medico.pack(side='left', padx=10)

        ctk.CTkLabel(container_medico, text="Médico").pack()
        self.lista_doencas = self.controller.consultas.buscarDoencasBD()
        self.input_doencas = ctk.CTkComboBox(container_medico, values=self.lista_doencas, width=380, height=40, border_width=0)
        self.input_doencas.set("Selecione o Médico")
        self.input_doencas.pack(side='left')



        # CONTAINER - Data, Hora e Status
        container_date = ctk.CTkFrame(self, fg_color="transparent")
        container_date.pack(side='top', pady=20)

        container_data = ctk.CTkFrame(container_date, fg_color="transparent")
        container_data.pack(side='left', padx=10)
        ctk.CTkLabel(container_data, text="Data do Diagnóstico").pack()
        self.input_data = ctk.CTkEntry(container_data, placeholder_text="Dr. João da Silva", width=380, height=40, border_width=0)
        self.input_data.pack(side='left')
        
        container_hora = ctk.CTkFrame(container_date, fg_color="transparent")
        container_hora.pack(side='left', padx=10)
        ctk.CTkLabel(container_hora, text="Observação").pack()
        self.input_hora = ctk.CTkEntry(container_hora, placeholder_text="Dr. João da Silva", width=380, height=40, border_width=0)
        self.input_hora.pack(side='left')



        # CONTAINER, BOTÕES
        container_button = ctk.CTkFrame(self, fg_color="transparent")
        container_button.pack(side='top', pady=20)

        salvar = ctk.CTkButton(container_button, text="Salvar", command=self.salvar_dados_paciente, width=380, height=60)
        salvar.pack(side='left', padx=10)
        
        limpar = ctk.CTkButton(container_button, text="Limpar Campos", command=self.limpar_campos, fg_color="gray", width=380, height=60)
        limpar.pack(side='right', padx=10)

    def salvar_dados_paciente(self):
        data = self.input_data.get()
        hora = self.input_hora.get()
        status = self.input_status.get()
        paciente = self.input_pacientes.get()

        # Envia os dados para o controller e verifica o resultado
        if self.controller.cadastrarAgendamento(data, hora, status, paciente):
            messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Falha ao cadastrar o paciente. Verifique os dados e tente novamente.")
    
    def limpar_campos(self):
        data = self.input_data.delete(0, 'end')
        hora = self.input_hora.delete(0, 'end')
        status = self.input_status.set("Selecione o Status")
        paciente = self.input_pacientes.set("Selecione o Paciente")