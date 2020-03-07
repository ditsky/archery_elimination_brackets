from TournamentResults import TournamentResults
import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as tkst
import ref

def fileDialog(editArea):
    filename = filedialog.askopenfilename(initialdir = "/Home/personal_projects/archery_elimination_brackets",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    bracket_data = TournamentResults()
    bracket_data.load_csv(filename)
    top_eight = bracket_data.top_eight()
    for division in top_eight:
        editArea.insert(tk.INSERT, "\ndivision: " + division + "\n")
        for archer in top_eight[division]:
            editArea.insert(tk.INSERT, archer.name + ": " + str(archer.score) + "\n")

def main():
    
    top = tk.Tk()
    
    frame1 = tk.Frame(
        master = top,
        bg = '#808000'
    )
    frame1.pack(fill='both',expand='yes')
    editArea = tkst.ScrolledText(
        master = frame1,
        wrap = tk.WORD,
        width = 20,
        height = 10
    )

    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.insert(tk.INSERT, "\nScores Summary:\n")


    upload_button = tk.Button(top, text ="Upload File", command = lambda: fileDialog(editArea))
    upload_button.pack()

    top.mainloop()


main()