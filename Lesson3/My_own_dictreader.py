import csv
# I'm going to use this class as a dict reader with my own twist
#You can use this with any csv file

class CaselessDictReader(csv.DictReader):
 
#Here I am overriding the already existing csv.fieldnames property converting all fieldnames without leading and trailing spaces to upper case.
    @property
    def fieldnames(self):
        return [field.strip().upper()
		for field in csv.DictReader.fieldnames.fget(self)]
    def next(self):
        return InsensitiveDict(csv.DictReader.next(self))

class IgnoreCaseDict(dict):
    # In this class I am overriding the __getitem__ method to automatically ignore the spaces and Uppercase the input key
    def __getitem__(self, key):
        return dict.__getitem__(self, key.strip().upper())

from My_own_dictreader import CaselessDictReader
#Now I am going to read the csv using the custom dictreader I created, the CaselessDictReader class

with open('football_players.csv', newline='') as my_csv:
     reader = CaselessDictReader(my_csv)
#Printout every thing nicely
     for row in reader:
         print(dict(row))


