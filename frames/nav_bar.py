import customtkinter as ctk
import tkinter as tk
import config

class NavigationBar(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(
            [0,1,2],
            weight=1
        )
        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.company_name = ctk.CTkLabel(
            self,
            text='UAEH',
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.h5_title,
                weight='bold'
                ),
            text_color=config.wine,
            anchor='w',
            justify='left'
        )
        self.company_name.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky='w'
        )

        self.app_name = ctk.CTkLabel(
            self,
            text='Sistema de Autenticación',
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.h5_title,
                weight='bold'
                ),
            text_color=config.second_color,
            anchor='center',
            justify='center'
        )
        self.app_name.grid(
            row=0,
            column=1,
            padx=20,
            pady=20,
            sticky='nsew'
        )

        self.menu = ctk.CTkLabel(
            self,
            text='menu',
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.h5_title,
                weight='normal'
                ),
            text_color=config.third_color,
            anchor='e',
            justify='right'
        )
        self.menu.grid(
            row=0,
            column=2,
            padx=20,
            pady=20,
            sticky='e'
        )