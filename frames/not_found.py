import customtkinter as ctk
import tkinter as tk
import config
from PIL import Image

class NotFoundFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(
            0,
            weight=1
        )
        self.grid_rowconfigure(
            [0,1],
            weight=1
        )
        
        self.proximity_icon = ctk.CTkImage(
            light_image=Image.open('images/denied.png'),
            size=(200, 200)
        )
        
        self.main_icon = ctk.CTkLabel(
            self,
            text='',
            image=self.proximity_icon,
            fg_color=config.blue_grey,
            anchor='center',
            justify='center'
        )
        self.main_icon.grid(
            row=0,
            columnspan=2,
            padx=10,
            pady=15,
            sticky='nsew'
        )


        self.instruction = ctk.CTkLabel(
            self,
            text='USUARIO NO REGISTRADO',
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.h1_title,
                weight='bold'
                ),
            text_color=config.warning,
            anchor='center',
            justify='center'
        )
        self.instruction.grid(
            row=1,
            columnspan=2,
            padx=30,
            pady=20,
            sticky='nsew'
        )

    def show(self):
        self.lift()

    def hide(self):
        self.forget()