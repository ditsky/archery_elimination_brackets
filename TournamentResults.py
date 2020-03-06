import csv
import ref
import copy
from Archer import Archer

class TournamentResults:
    
    def __init__(self):
        self.headers = {}
        self.divisions = {}

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

    def process_headers(self, row):
        header_index = 0
        for header in row:
            key = header.strip().lower()
            self.headers.update({key : header_index})
            header_index += 1

    def has_required_headers(self):
        return (ref.name in self.headers and ref.bow_type in self.headers 
               and ref.score in self.headers and ref.gender in self.headers 
               and ref.age_group in self.headers)

    def process_archer_row(self, row):
        name = self.get_field(row, ref.name)
        bow_type = self.get_field(row, ref.bow_type)
        gender = self.get_field(row, ref.gender)
        age_group = self.get_field(row, ref.age_group)
        score = self.get_field(row, ref.score)
        newArcher = Archer(name, bow_type, gender, age_group, score)

        division_name = bow_type + " - " + gender + " - " + age_group

        if division_name not in self.divisions:
            self.divisions.update({division_name : []})
        self.divisions[division_name].append(newArcher)
       

    def get_field(self, row, field):
        return row[self.headers[field]]

    def top_eight(self):
        top_eight = copy.deepcopy(self.divisions)
        for division in top_eight:
            top_eight[division].sort(reverse=True, key=self.sort_by_score)
        for division in top_eight:
            top_eight[division] = top_eight[division][0:10]
        return top_eight
        
    
    def sort_by_score(self, archer):
        return archer.score






    
    



    

