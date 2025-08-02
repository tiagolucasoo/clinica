import customtkinter as ctk
import os
from tkinter import Menu, messagebox

from controller.controller import Controller

from model.model import Model
from model.setup import INICIAR_BANCO
from model.seed_data import INCLUIR_REGISTROS

from view.pag_inicial import view_inicial

from view.cadastros.cad_agendamentos import Cad_Agendamentos
from view.cadastros.cad_medicos import Cad_Medicos
from view.cadastros.cad_pacientes import Cad_Pacientes
from view.cadastros.cad_pacientes_planos import Cad_Paciente_plano
from view.cadastros.cad_pacientes_doencas import Cad_Paciente_doenca

from view.consultas.con_agendamentos import Con_Agendamentos
from view.consultas.con_medicos import Con_Medicos
from view.consultas.con_pacientes import Con_Pacientes
from view.consultas.con_doencas import Con_Doencas
from view.consultas.con_especialidades import Con_Especialidades
from view.consultas.con_pacientes_doencas import Con_Pacientes_doencas

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.minsize(1200, 700)
        self.title("TLG ADMIN - Sistema de Clínica")

        os.system('cls')
        self.model = Model()
        
        INICIAR_BANCO()
        INCLUIR_REGISTROS()

        self.controller = Controller(model_db=self.model)
        self.controller.set_app(self)
        self.telas = {}

        container = ctk.CTkFrame(master=self, fg_color="transparent")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for tela in (Cad_Agendamentos, Cad_Paciente_plano, Cad_Paciente_doenca, Cad_Medicos, Cad_Pacientes,  view_inicial,
                     Con_Pacientes_doencas, Con_Agendamentos, Con_Medicos, Con_Pacientes, Con_Doencas, Con_Especialidades):
            nome = tela.__name__
            frame = tela(parent=container, controller_instance=self.controller)
            self.telas[nome] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.exibir_tela("view_inicial")
        self.criar_menu()

    def criar_menu(self):
        barra_menu = Menu(self)

        menu_inicio = Menu(barra_menu, tearoff=0)
        menu_inicio.add_command(label="Página Inicial", command=lambda: self.exibir_tela("view_inicial"))
        menu_inicio.add_separator()
        menu_inicio.add_command(label="Sair", command=self.quit)
        barra_menu.add_cascade(label="Página Inicial", menu=menu_inicio)

        menu_cadastro = Menu(barra_menu, tearoff=0)
        menu_cadastro.add_command(label="Agendamentos", command=lambda: self.exibir_tela("Cad_Agendamentos"))
        menu_cadastro.add_command(label="Médicos", command=lambda: self.exibir_tela("Cad_Medicos"))
        menu_cadastro.add_command(label="Pacientes", command=lambda: self.exibir_tela("Cad_Pacientes"))
        menu_cadastro.add_command(label="Planos Pacientes", command=lambda: self.exibir_tela("Cad_Paciente_plano"))
        menu_cadastro.add_command(label="Pacientes Doenças", command=lambda: self.exibir_tela("Cad_Paciente_doenca"))
        barra_menu.add_cascade(label="Cadastro", menu=menu_cadastro)

        menu_consulta = Menu(barra_menu, tearoff=0)
        menu_consulta.add_command(label="Agendamentos", command=lambda: self.exibir_tela("Con_Agendamentos"))
        menu_consulta.add_command(label="Médicos", command=lambda: self.exibir_tela("Con_Medicos"))
        menu_consulta.add_command(label="Pacientes", command=lambda: self.exibir_tela("Con_Pacientes"))
        menu_consulta.add_command(label="Doenças", command=lambda: self.exibir_tela("Con_Doencas"))
        menu_consulta.add_command(label="Especialidades", command=lambda: self.exibir_tela("Con_Especialidades"))
        menu_consulta.add_command(label="Pacientes (Situação)", command=lambda: self.exibir_tela("Con_Pacientes_doencas"))
        barra_menu.add_cascade(label="Consultas", menu=menu_consulta)

        menu_aparencia = Menu(barra_menu, tearoff=0)
        menu_aparencia.add_command(label="Modo Escuro", command=lambda: ctk.set_appearance_mode("dark"))
        menu_aparencia.add_command(label="Modo Claro", command=lambda: ctk.set_appearance_mode("light"))
        barra_menu.add_cascade(label="Aparência", menu=menu_aparencia)

        self.configure(menu=barra_menu)

    def exibir_tela(self, nome_tela):
        frame = self.telas[nome_tela]
        frame.tkraise()

    def exibir_mensagem_sucesso(self, mensagem):
        messagebox.showinfo("Sucesso", mensagem, parent=self)

    def exibir_mensagem_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem, parent=self)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    app = App()
    app.mainloop()