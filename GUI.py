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
path_label = ct.CTkLabel(app, text="Path")
path_label.pack(padx=5,pady=5)

# Browse Button
browse_files = ct.CTkButton(app, text="Browse", command=Organizer.browse_files).pack()

# Organize Button
organize_files = ct.CTkButton(app, text="Organize", command=Organizer.organize_files).pack(padx=20,pady=30)

# State Label
st_label = ct.CTkLabel(app, text="")
st_label.pack(padx=5,pady=5)

# Print when completed
def update_path_gui():
    path_label.configure(text="{}".format(vars.PATH_TO_ORGANIZE))

def path_empty():
    path_label.configure(text="Path is empty!")

def state_label():
    st_label.configure(text="{}".format(vars.CURRENT_STATE))


def on_closing():
    app.destroy()
# Run GUI
def run_gui():
    app.protocol("Close Window", on_closing)
    app.mainloop()