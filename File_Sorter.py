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
        self.Ext=[self.ext_image, self.ext_video, self.ext_audio, self.ext_doc, self.ext_comp]

        self.CF_label=tk.Label(self, text="Chose a folder")
        self.CF_label.grid(column=0, row=0)
        self.CF_button=tk.Button(self, text="Chose", command=self.chose_folder)
        self.CF_button.grid(column=1, row=0)

        self.F_label=tk.Label(self, text="Folder")
        self.F_label.grid(column=0, row=1)
        self.Folder_var=tk.StringVar(self)
        self.Folder_var.set(self.Folders[0])
        self.Ext_var=tk.StringVar(self)
        self.Ext_var.set(' '.join([str(elem)+", " for elem in self.Ext[0]]))
        self.Folder_menu=tk.OptionMenu(self, self.Folder_var, *self.Folders)
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
        


    def chose_folder(self):
        path=fd.askdirectory()

    def add_folder(self):
        self.Folders.append("New Folder")
        self.update_menu()

    def update_menu(self):
        menu=self.Folder_menu["menu"]
        menu.delete(0, "end")
        for string in self.Folders:
            menu.add_command(label=string, command=lambda value=string: self.Folder_var.set(value))

    def update_folder_info(self):
        self.Folders[0]=str(self.F_N_entry.get())
        self.Ext[0]=list(str(self.F_ext_entry.get()).split(", "))
        self.update_menu()

if __name__ == "__main__":
    app=App()
    app.mainloop()
