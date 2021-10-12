import shutil
import os
import tkinter as tk
from tkinter import filedialog as fd



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File_Sorter")
        self.geometry('350x200')

        self.ext_image=[".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff"]
        self.ext_video=[".mp4", ".avi", ".mpg", ".mpeg", ".wmv", ".mov", "ogv"]
        self.ext_audio=[".mp3", ".cda", ".ogg", ".wav"]
        self.ext_doc=[".pdf", ".doc", ".odt", ".docx", ".odp", ".ppt", "ods", "xls", "xlsx"]
        self.ext_comp=[".zip", ".rar", ".gz", ".gzip", ".tar", ".tgz"]
        self.Folders=["Images", "Videos", "Music", "Documents", "Compressed_files", "Others"]
        self.Ext=[self.ext_image, self.ext_video, self.ext_audio, self.ext_doc, self.ext_comp, [""]]
        self.path=""

        self.CF_label=tk.Label(self, text="Chose a folder")
        self.CF_label.grid(column=0, row=0)
        self.CF_button=tk.Button(self, text="Chose", command=self.chose_folder)
        self.CF_button.grid(column=1, row=0)

        self.F_label=tk.Label(self, text="Folder")
        self.F_label.grid(column=0, row=1)
        self.Folder_var=tk.StringVar(self)
        self.Folder_var.set(self.Folders[0])
        self.index=0
        self.Ext_var=tk.StringVar(self)
        self.Ext_var.set(' '.join([str(elem)+", " for elem in self.Ext[self.index]]))
        self.Folder_menu=tk.OptionMenu(self, self.Folder_var, *self.Folders, command=self.option_change)
        self.Folder_menu.grid(column=1, row=1)
        self.Add_F_button=tk.Button(self, text="Add Folder", command=self.add_folder)
        self.Add_F_button.grid(column=2, row=1)

        self.F_I_label=tk.Label(self, text="Folder Information")
        self.F_I_label.grid(column=0, row=2)
        self.F_N_label=tk.Label(self, text="Folder Name")
        self.F_N_label.grid(column=0, row=3)
        self.F_N_entry=tk.Entry(self, textvariable=self.Folder_var)
        self.F_N_entry.grid(column=1,row=3)
        self.F_ext_label=tk.Label(self, text="Folder extentions")
        self.F_ext_label.grid(column=0, row=4)
        self.F_ext_entry=tk.Entry(self, textvariable=self.Ext_var)
        self.F_ext_entry.grid(column=1,row=4)
        self.F_U_button=tk.Button(self, text="Update", command=self.update_folder_info)
        self.F_U_button.grid(column=1, row=5)
        self.S_button=tk.Button(text="Sort", command=self.sort_init)
        self.S_button.grid(column=2, row=6)
        


    def chose_folder(self):
        self.path=fd.askdirectory()+"/"

    def add_folder(self):
        self.Folders.append("New Folder")
        self.Ext.append([])
        self.update_menu()

    def update_menu(self):
        menu=self.Folder_menu["menu"]
        menu.delete(0, "end")
        for string in self.Folders:
            menu.add_command(label=string, command=self.option_change)
        self.Folder_var.set(self.Folders[-1])

    def update_folder_info(self):
        self.Folders[self.index]=str(self.F_N_entry.get())
        self.Ext[self.index]=list(str(self.F_ext_entry.get()).split(", "))
        self.update_menu()

    def option_change(self, *args):
        self.index=self.Folders.index(str(self.F_N_entry.get()))
        print(str(self.Folder_var))
        self.Ext_var.set(' '.join([str(elem)+", " for elem in self.Ext[self.index]]))

        print(self.index)

    def sort(self,file_name, ext):
        for i in range(len(self.Ext)):
            for j in self.Ext[i]:
                try:
                    os.mkdir(self.path + self.Folders[i])
                except:
                    pass
                if ext == j:
                    try:
                        shutil.move(self.path + file_name, self.path + self.Folders[i])
                    except:
                        pass

        if ext != "":
            try:
                shutil.move(self.path + file_name, self.path + "Others")
            except:
                pass

    def sort_init(self):
        for file in os.listdir(self.path):
            file_name, ext =os.path.splitext(file)
            self.sort(file,ext)

if __name__ == "__main__":
    app=App()
    app.mainloop()
