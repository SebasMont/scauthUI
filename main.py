#Scauth GUI
import customtkinter as ctk
import tkinter as tk
import config as col_set
from frames import place_id
from frames import nav_bar
from frames import not_found
from frames import user_data

"""
class Json:

    def __init__(
        self,
        username,
        role,
        account_number,
        institute,
        career
    ):
        self.username = username
        self.role = role
        self.account_number = account_number
        self.institute = institute
        self.career = career

request = Json(
    "Rey Sebastian Monter Fragoso",
    "Estudiante",
    419115,
    "Instituto de Ciencias Básicas e Ingeniería",
    'Lic. en Ingeniería en Electrónica'
)
"""

# Main App class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Main window settings
        self.geometry('800x500')
        self.title('Scauth')
        self.configure(fg_color = col_set.pearl)
        self.grid_columnconfigure(
            0,
            weight=1
        )
        self.grid_rowconfigure(
            [0,1,2],
            weight=1
        )

        #Not Found Frame
        self.not_found_frame = not_found.NotFoundFrame(
            master=self,
            width=780,
            corner_radius=20,
            fg_color = col_set.blue_grey
            )

        #Place Id Frame call
        self.place_id_frame = place_id.PlaceIdFrame(
            master=self,
            width=780,
            corner_radius=20,
            fg_color = col_set.blue_grey
            )
        
        #User data frame
        self.user_data_frame = user_data.UserDataFrame(
            master=self,
            width=780,
            corner_radius=20,
            fg_color = col_set.blue_grey,
            #user=request
        )
        
        #Navigation Bar call
        self.nav_bar = nav_bar.NavigationBar(
            master=self,
            width=800,
            height=80,
            corner_radius=0,
            fg_color = col_set.blue_grey,
        )
        self.nav_bar.grid(
            column=0,
            row=0,
            padx = 0,
            pady = 0,
            sticky='nwe'
        )

        #Contaniner for multiple frames
        self.main_container = ctk.CTkFrame(
            self,
            width=780,
            corner_radius=20,
            fg_color = col_set.pearl
        )
        self.main_container.grid(
            column=0,
            row=1,
            padx = 0,
            pady = 0,
            sticky='nsew'
        )

        #Button bar for navigation among pages
        self.button_bar = ctk.CTkFrame(
            self,
            fg_color = col_set.pearl
            )
        self.button_bar.grid(
            column=0,
            row=2,
            padx = 5,
            pady = 5,
            sticky='nsew'
        )

        b1 = tk.Button(self.button_bar, text="Page 1", command=self.show_start_page)
        b2 = tk.Button(self.button_bar, text="Page 2", command=self.show_not_found_page)
        b3 = tk.Button(self.button_bar, text="Page 3", command=self.show_user_data_page)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        self.show_user_data_page()

    #Functions for showing and changing pages
    def show_start_page(self):
        self.not_found_frame.grid_forget()
        self.user_data_frame.grid_forget()
        self.place_id_frame.grid(
            column=0,
            row=1,
            padx = 5,
            pady = 5,
            sticky='ns'
        )
        self.place_id_frame.show()
        
    def show_not_found_page(self):
        self.place_id_frame.grid_forget()
        self.user_data_frame.grid_forget()
        self.not_found_frame.grid(
            column=0,
            row=1,
            padx = 5,
            pady = 5,
            sticky='ns'
        )
        self.not_found_frame.show()

    def show_user_data_page(self):
        self.place_id_frame.grid_forget()
        self.not_found_frame.grid_forget()
        self.user_data_frame.grid(
            column=0,
            row=1,
            padx = 5,
            pady = 5,
            sticky='ns'
        )
        self.user_data_frame.show()



if __name__ == '__main__':
    app = App()
    app.mainloop()
