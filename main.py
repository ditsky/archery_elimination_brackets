from TournamentResults import TournamentResults
import Tkinter

def main():
    

    bracket_data = TournamentResults()
    bracket_data.load_csv("2019 Shamrock Registration  - Shamrock Scoring.csv")
    top_eight = bracket_data.top_eight()
    for division in top_eight:
        print("division: " + division + "\n")
        for archer in top_eight[division]:
            print(archer.name + ": " + archer.score + "\n")

    top = Tkinter.Tk()
    # Code to add widgets will go here...
    top.mainloop()


main()