import customtkinter as ctk
from tkinter import messagebox

from model.model import Consultas
from controller.controller import Consultas_Model, Controller

class Con_Agendamentos(ctk.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance
        model = Consultas()
        consultas_controller = Consultas_Model(model)

        fonte = ("Consolas", 12)
        lista = consultas_controller.conf_agendamentos()

        self.listagem = ctk.CTkTextbox(self, width=1200, height=700, font=fonte)
        self.listagem.pack()

        self.listagem.insert("1.0", lista)
        self.listagem.configure(state="disabled")
        print(lista)
        