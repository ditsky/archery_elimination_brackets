from TournamentResults import TournamentResults
import tkinter as tk
import ref

def fileDialog():
    filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    bracket_data = TournamentResults()
    bracket_data.load_csv(filename)
    top_eight = bracket_data.top_eight()
    for division in top_eight:
        print("division: " + division + "\n")
        for archer in top_eight[division]:
            print(archer.name + ": " + archer.score + "\n")

def main():
    
    top = Tkinter.Tk()

    hello_button = Tkinter.Button(top, text ="Upload File", command = fileDialog)
    hello_button.pack()

    

    top.mainloop()




main()