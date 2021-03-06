from TournamentResults import TournamentResults
import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as tkst
from tkinter import *
import copy

# GUI class which encapsualtes the functionality of the frontend
# Uploads, and edits data from the tournamentResults 
# class with buttons on the GUI, thanks to tkinter
class GUI:

    #Initalizes all the bracket data and GUI widgets used in the frontend
    def __init__(self):
        self.bracket_data = {}
        self.bracket_data_original = {}
        self.top_eight = {}
        self.top_eight_original = {}
        self.divisions_window_active = False

        self.top = None
        self.edit_area = None
        self.merge_button = None
        self.reset_button = None
        self.divisions_button = None
        self.division_box = None


    #Uploads file from user input, and uses it to generate bracket_data
    #Renders the results and necessary buttons in the window
    def file_dialog(self):
        filename = filedialog.askopenfilename(initialdir = "/Home/Desktop",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.bracket_data = TournamentResults()
        self.bracket_data.load_csv(filename)
        self.bracket_data_original = copy.deepcopy(self.bracket_data)

        self.top_eight = self.bracket_data.top_eight()
        self.top_eight_original = copy.deepcopy(self.top_eight)

        self.fill_brackets()

        self.conditionalRender()

    
    #Renders tk widgets if they are needed and have not yet been rendered
    #Deletes tk widgets that are no longer needed
    def conditionalRender(self):

        if self.divisions_button == None or not self.divisions_button.winfo_ismapped():
            self.divisions_button = tk.Button(self.top, text = "Divisions", command = lambda: self.divisions())
            self.divisions_button.pack()

        if self.reset_button == None or not self.reset_button.winfo_ismapped():
            self.reset_button = tk.Button(self.top, text ="Reset", command = lambda: self.reset())
            self.reset_button.pack()

        if self.division_box != None and self.division_box.winfo_ismapped():
            self.division_box.delete(0, tk.END)
            self.division_box.pack_forget()
            self.divisions_window_active = False

        if self.merge_button != None and self.merge_button.winfo_ismapped():
            self.merge_button.pack_forget()

    #On divisions button click, deletes the divisions button
    #and renders the selectable division box and merge division button
    def divisions(self):
        self.divisions_button.pack_forget()

        #Generate list of divisions
        divisions = []
        for division_name, data in self.bracket_data.divisions.items():
            divisions.append(division_name)
        divisions.sort(key=len) #sort by length for clearer selection
        divisions_list = StringVar(value=(divisions))

        self.division_label.pack()
        self.division_box = Listbox(self.top, listvariable=divisions_list, width=300, selectmode=MULTIPLE)
        self.division_box.pack()
        self.divisions_window_active = True

        self.merge_button = tk.Button(self.top, text = "Merge Divisions", command = lambda: self.merge_division(divisions))
        self.merge_button.pack()


    #Generates and returns a new division name and list for given
    #request to merge divisions by the user
    def create_new_division(self, selections, selected_items):
        bracket_data_copy = copy.deepcopy(self.bracket_data)
        merged_list = []
        division_count = 0
        new_division_name = ""
        for item in selected_items:
            division = selections[item]
            if division_count == 0:
                new_division_name = division
            else:
                new_division_name += " // " + division
            division_count += 1
            merged_list += self.bracket_data.divisions[division]
            del self.bracket_data.divisions[division]
        return new_division_name, merged_list
    

    #Merges divisions based on user input
    def merge_division(self, selections):
        selected_items = self.division_box.curselection()
        if len(selected_items) > 1:

            new_division_name, merged_list = self.create_new_division(selections, selected_items)
            self.bracket_data.divisions.update( {new_division_name : merged_list} )
            self.top_eight = self.bracket_data.top_eight()
            self.redraw()


    #Unpacks and then redraws all necesssary tk widgets to
    #display a change in the data by the user
    def redraw(self):
        self.score_label.pack_forget()
        self.division_label.pack_forget()
        self.edit_area.pack_forget()
        self.division_box.pack_forget()
        self.divisions_window_active = False
        self.merge_button.pack_forget()

        self.fill_brackets()
        self.divisions()


    #Clears and then refills the bracket data area
    def fill_brackets(self):
        self.score_label.pack()
        self.edit_area.delete('1.0', END)
        self.edit_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        for division in sorted(self.top_eight, key=len):
            self.edit_area.insert(tk.INSERT, "\n" + division + "\n", 'bold')
            for archer in self.top_eight[division]:
                self.edit_area.insert(tk.INSERT, archer.name + ": " + str(archer.score) + "\n")


    #Resets all data back to the original state before merges
    def reset(self):
        self.bracket_data = copy.deepcopy(self.bracket_data_original)
        self.top_eight = copy.deepcopy(self.top_eight_original)
        self.redraw()


    #Creates and fills frame to hold the bracket data, in addition to
    #the score and divisions label
    def create_frame(self):
        frame1 = tk.Frame(
            master = self.top,
            bg = '#808000'
        )
        self.score_label = Label(frame1, text='Score Summary:', font='Helvetica 18 bold')
        self.division_label = Label(text='Divisions:', font='Helvetica 18 bold')
        frame1.pack(fill='both',expand='yes')
        self.edit_area = tkst.ScrolledText(
            master = frame1,
            wrap = tk.WORD,
            width = 20,
            height = 10
        )
        #Configures the font for the headers in the bracket data section
        self.edit_area.tag_configure('bold', font=("Verdana", 12, 'bold'))

    #Renders button for csv uploads
    def create_upload_button(self):
        upload_button = tk.Button(self.top, text ="Upload File", command = lambda: self.file_dialog())
        upload_button.pack()

    #Creates tkinter instance and runs the mainloop
    def main(self):
        self.top = tk.Tk()
        self.create_frame()
        self.create_upload_button()
        self.top.mainloop()


gui = GUI()
gui.main()