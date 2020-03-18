# archery_elimination_brackets
# author: Sam Ruditsky

This application loads in a csv file of archery tournament data,
and returns a window to view the top eight in each division, and
or merge dvisions to facilitate cration of elimination brackets
at archery tournaments

To run this application first update the file headers.py
to match the headers in your csv file. Your csv file must
contain a header of some variant for each of the following:

name
bow_type
gender
age_group
score

Once you have configured the headers, you can run the application by
running python main.py in your console inside of the application directory
(You must have an updated version of python installed to run the program).