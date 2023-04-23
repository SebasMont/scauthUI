import customtkinter as ctk
import tkinter as tk
import config
from PIL import Image

class UserDataFrame(ctk.CTkFrame):
    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(
            [0,1],
            weight=1
        )
        self.grid_rowconfigure(
            [0,1,2,3],
            weight=1
        )

        self.role = ctk.CTkLabel(
            self,
            text=user.role,
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.h3_title,
                weight='bold'
                ),
            text_color=config.pearl,
            fg_color=config.success,
            corner_radius=25,
            anchor='center',
            justify='center'
        )
        self.role.grid(
            row=0,
            column=0,
            padx=5,
            pady=2,
            sticky='nsew'
        )
        
        self.avatar_pic = ctk.CTkImage(
            light_image=Image.open('images/default_avatar.png'),
            size=(100, 100)
        )
        
        self.avatar = ctk.CTkLabel(
            self,
            text='',
            image=self.avatar_pic,
            fg_color=config.blue_grey,
            anchor='center',
            justify='center'
        )
        self.avatar.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky='nsew'
        )


        self.name = ctk.CTkLabel(
            self,
            text=user.username,
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.p_text,
                weight='bold'
                ),
            text_color=config.third_color,
            anchor='center',
            justify='center'
        )
        self.name.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky='nsew'
        )

        self.account_number = ctk.CTkLabel(
            self,
            text=user.account_number,
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.p_text,
                weight='bold'
                ),
            text_color=config.third_color,
            anchor='center',
            justify='center'
        )
        self.account_number.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky='nsew'
        )

        self.institute = ctk.CTkLabel(
            self,
            text=user.institute,
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.p_text,
                weight='normal'
                ),
            text_color=config.third_color,
            anchor='center',
            justify='center'
        )
        self.institute.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky='nsew'
        )

        self.career = ctk.CTkLabel(
            self,
            text='Lic. En Ingeniería en Electrónica',
            font=ctk.CTkFont(
                family=config.font_family,
                size=config.p_text,
                weight='normal'
                ),
            text_color=config.third_color,
            anchor='center',
            justify='center'
        )
        self.career.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky='nsew'
        )

    def show(self):
        self.lift()
    
    def hide(self):
        self.forget()