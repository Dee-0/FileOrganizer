import tkinter
import customtkinter as ct
import Organizer
import OrganizerVariables as vars

# System Settings
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

# App frame values
app = ct.CTk()
app.geometry("{}x{}".format(vars.WIDTH,vars.HEIGHT))
app.title("File Organizer")

# UI Elements
title = ct.CTkLabel(app, text="Choose a folder to organize").pack(padx=10,pady=10)

txt = ct.CTkEntry(app)

def set_text():
    txt.delete(0,"end")
    txt.insert(0,"zzz")

# Path label
path_choice = ct.CTkEntry(app, width=350, height=20, placeholder_text="Choose a folder").pack(padx=10,pady=5)

# Browse Button
browse_files = ct.CTkButton(app, text="Browse", command=Organizer.browse_files).pack()

# Organize Button
organize_files = ct.CTkButton(app, text="Organize", command=Organizer.organize_files).pack(padx=30,pady=70)

# Run GUI
def run_gui():
    app.mainloop()