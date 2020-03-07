from TournamentResults import TournamentResults
import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as tkst
from tkinter import *
import ref
import copy

class GUI:

    def __init__(self):
        self.bracket_data = {}
        self.bracket_data_original = {}
        self.top_eight = {}
        self.top_eight_original = {}
        self.divisions_window_active = False

    def fileDialog(self, edit_area):
        filename = filedialog.askopenfilename(initialdir = "/Home/personal_projects/archery_elimination_brackets",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.bracket_data = TournamentResults()
        self.bracket_data.load_csv(filename)
        self.top_eight = self.bracket_data.top_eight()
        for division in self.top_eight:
            edit_area.insert(tk.INSERT, "\ndivision: " + division + "\n")
            for archer in self.top_eight[division]:
                edit_area.insert(tk.INSERT, archer.name + ": " + str(archer.score) + "\n")

    def divisions(self, top, edit_area):
        if not self.divisions_window_active:
            divisions = []
            for division_name, data in self.bracket_data.divisions.items():
                divisions.append(division_name)
            divisions_list = StringVar(value=(divisions))
            division_box = Listbox(top, listvariable=divisions_list, width=60, selectmode=MULTIPLE)
            division_box.pack()
            self.divisions_window_active = True
            merge_button = tk.Button(top, text = "Merge Divisions", command = lambda: self.merge_division(edit_area, division_box, divisions))
            merge_button.pack()
    
    def merge_division(self, edit_area, listbox, selections):
        selected_items = listbox.curselection()
        bracket_data_copy = copy.deepcopy(self.bracket_data)
        for item in selected_items:
            print(selections[item])


    def main(self):
        
        top = tk.Tk()
        
        frame1 = tk.Frame(
            master = top,
            bg = '#808000'
        )
        frame1.pack(fill='both',expand='yes')
        edit_area = tkst.ScrolledText(
            master = frame1,
            wrap = tk.WORD,
            width = 20,
            height = 10
        )

        edit_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        edit_area.insert(tk.INSERT, "\nScores Summary:\n")


        upload_button = tk.Button(top, text ="Upload File", command = lambda: self.fileDialog(edit_area))
        upload_button.pack()

        divisions_button = tk.Button(top, text = "Divisions", command = lambda: self.divisions(top, edit_area))
        divisions_button.pack()

        top.mainloop()

gui = GUI()
gui.main()