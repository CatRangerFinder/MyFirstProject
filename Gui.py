import tkinter as tk
import customtkinter


#system settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Power calculator")
#todo make window non resizable
#tk.Tk().resizable(width=False, height=False)

# UI elements
title = customtkinter.CTkLabel(app, text='Input')
title.pack(padx=10, pady=10)

#input for calculator
input1_input = tk.StringVar()
input1 = customtkinter.CTkEntry(app, width=350, height= 40, textvariable=input1_input)
input1.pack(padx=10, pady=10)
input2_input = tk.StringVar()
input2 = customtkinter.CTkEntry(app, width=350, height= 40, textvariable=input2_input)
input2.pack(padx=10, pady=10)

#buttons todo fix this/make it useful
calculate_button = customtkinter.CTkButton(app, text='Calculate',) #command=calculate)
calculate_button.pack(padx=10, pady=10)


# run app
app.mainloop()