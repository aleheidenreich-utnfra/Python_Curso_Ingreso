# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import warnings

import customtkinter

'''
################# INTRODUCCION #################
#? El profesor OAK de pueblo paleta quiere que construyas un primer modelo prototipico 
#? de pokedex con 10 pokemones de prueba.
'''
NOMBRE = '' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)

B) Al presionar el boton "Mostrar Informe 1" se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) Al presionar el boton "Mostrar Informe 2"
    #! 0) - Cantidad de pokemones de tipo Fuego
    #! 1) - Cantidad de pokemones de tipo Electrico
    #! 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    #! 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    #! 4) - Cantidad de pokemones, con mas de 100 de poder.
    #! 5) - Cantidad de pokemones, con menos de 100 de poder
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea 
    #! 8) - el promedio de poder de todos los ingresados
    #! 9) - el promedio de poder de todos los pokemones de Electrico
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Pokedex de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Pokedex de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./2_modelos_examenes/pokedex_v1/UTN_Pokedex_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para boton mostrar
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = [
            "Charmander", "Charizard", "Pikachu", "Zapdos", "Mewtwo",
            "Moltres", "Mew", "Blastoise", "Raichu", "Digglet"
        ]
        self.lista_poder_pokemones = [
            60, 120, 51, 190, 194,
            190, 195, 120, 95, 51
        ]
        self.lista_tipo_pokemones = [
            "Fuego", "Fuego", "Electrico", "Electrico", "Psiquico",
            "Fuego", "Psiquico", "Agua", "Electrico", "Tierra"
        ]


    def btn_cargar_pokedex_on_click(self):
        pass
        

    def btn_mostrar_informe_1_on_click(self):
        pass

    
    def btn_mostrar_informe_2_on_click(self):
        pass

    
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()

            

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()