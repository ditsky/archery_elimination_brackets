import csv
import headers
import copy
from Archer import Archer

#Class to load a csv file and organize its contents into divisions
#and to create a bracket for the top 8 in each division
class TournamentResults:
    
    #Initalizes headers and divisions dictionaries
    def __init__(self):
        self.headers = {}
        self.divisions = {}

    #Loads and processes a given csv file
    def load_csv(self, csv_file_path):
        with open(csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self.process_headers(row)
                    if (not self.has_required_headers()):
                        print("CSV DOES NOT CONTAIN REQUIRED HEADERS!!")
                        return
                else:
                    self.process_archer_row(row)

                line_count += 1
            print("Processed " + str(line_count) + " lines.")

    #Processes and stores the headers of the csv file
    def process_headers(self, row):
        header_index = 0
        for header in row:
            key = header.strip().lower()
            self.headers.update({key : header_index})
            header_index += 1

    #Checks to make sure the all necessary headers are present
    def has_required_headers(self):
        return (headers.name in self.headers and headers.bow_type in self.headers 
               and headers.score in self.headers and headers.gender in self.headers 
               and headers.age_group in self.headers)

    #Processes and stores an archer data line of the csv
    def process_archer_row(self, row):
        name = self.get_field(row, headers.name).strip()
        bow_type = self.get_field(row, headers.bow_type).strip()
        gender = self.get_field(row, headers.gender).strip()
        age_group = self.get_field(row, headers.age_group).strip()
        score = self.get_field(row, headers.score).strip()
        if (score.isdigit()):

            newArcher = Archer(name, bow_type, gender, age_group, score)
            division_name = bow_type + " - " + gender + " - " + age_group

            if division_name not in self.divisions:
                self.divisions.update({division_name : []})
            if self.unique(newArcher, self.divisions[division_name]):
                self.divisions[division_name].append(newArcher)

    #Checks that the new archer is not already in this division
    def unique(self, newArcher, division):
        for archer in division:
            if (newArcher.name == archer.name and newArcher.gender == archer.gender and 
                newArcher.bow_type == archer.bow_type and newArcher.age_group == archer.age_group):
                return False
        return True
       

    #Returns the given field in he given row of the csv
    def get_field(self, row, field):
        return row[self.headers[field]]

    #Creates a list of the top eight archers for each division 
    def top_eight(self):
        top_eight = copy.deepcopy(self.divisions)
        for division in top_eight:
            top_eight[division].sort(reverse=True, key=self.sort_by_score)
        for division in top_eight:
            top_eight[division] = top_eight[division][0:8]
        return top_eight
        
    #Sorts a division by archer score
    def sort_by_score(self, archer):
        return archer.score






    
    



    

