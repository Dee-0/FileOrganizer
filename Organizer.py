import tkinter
from tkinter import filedialog
import os
from os import listdir
from os.path import isfile, join
import shutil
import OrganizerVariables as vars
import GUI

def browse_files():
    tkinter.Tk().withdraw()
    vars.PATH_TO_ORGANIZE = filedialog.askdirectory()
    GUI.update_path_gui()

def organize_files():
    if vars.PATH_TO_ORGANIZE == "":
        vars.PATH_TO_ORGANIZE = "Path is empty!"
        GUI.update_path_gui()
    else:
        directories = next(os.walk(vars.PATH_TO_ORGANIZE))[1]
        for f in listdir(vars.PATH_TO_ORGANIZE):
            if isfile(join(vars.PATH_TO_ORGANIZE, f)):
                filename, file_extension = os.path.splitext("{}/{}".format(vars.PATH_TO_ORGANIZE,f))
                if (file_extension[1:] not in directories):
                    create_folder(file_extension[1:])
                move_file(f,file_extension[1:])
        vars.CURRENT_STATE = "Complete!"
        GUI.state_label()

def move_file(file_to_move,extension):
    shutil.move("{}/{}".format(vars.PATH_TO_ORGANIZE,file_to_move), "{}/{}/{}".format(vars.PATH_TO_ORGANIZE,extension,file_to_move))

def create_folder(extension):
    path = os.path.join(vars.PATH_TO_ORGANIZE, extension)
    if not os.path.exists("{}/{}".format(vars.PATH_TO_ORGANIZE, extension)):
        os.mkdir(path)
