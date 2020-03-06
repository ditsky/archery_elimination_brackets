from TournamentResults import TournamentResults
import Tkinter

def main():
    

    bracket_data = TournamentResults()
    bracket_data.load_csv("2019 Shamrock Registration  - Shamrock Scoring.csv")

    top = Tkinter.Tk()
    # Code to add widgets will go here...
    top.mainloop()


main()