import customtkinter as ctk
from tkinter.filedialog import askopenfilename
import tkinter as tk
from PIL import Image
import datetime

import os
import sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class view_inicial(ctk.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance

        fundo = ctk.CTkFrame(master=self, fg_color="transparent")
        fundo.pack()

        imagem_light = resource_path("img/logo_color.png")
        imagem_dark = resource_path("img/logo_branca.png")

        logo_ssec = ctk.CTkImage(light_image=Image.open(imagem_light),
                                  dark_image=Image.open(imagem_dark),
                                  size=(475, 420))
        logo = ctk.CTkLabel(self, image=logo_ssec, text="")
        logo.pack()

        # Rodapé
        info_ssec = ctk.CTkLabel(self, text="Desenvolvido por Tiago Lucas (GitHub: Tiagolucasoo)", fg_color="transparent")
        info_ssec.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

        self.info_hora = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.info_hora.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        self.atualizar_data()

    def atualizar_data(self):
        agora = datetime.datetime.now().strftime("%d/%m/%Y  -  %H:%M:%S")
        self.info_hora.configure(text=agora)
        self.after(1000, self.atualizar_data)