#import
from cs50 import get_string, longest_match
import csv
import sys

def main():
    if len(sys.argv) != 3:
        print ("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    people = []
    with open(sys.argv[1], "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            person = row.copy()
            people.append(person)


    dna = str()
    with open(sys.argv[2], "r") as f:
        dna = f.read()
    n = len(person)
    letters = tuple(dna)
    klucze = tuple(person.keys())
    dlugosc = []
    klucz = 0
        #for i in klucze:
            #for j in len(dna):
                #if dna[j:(j+len(klucze[i])] = i:
                    #if dna[j-len(klucze[i]):j] = i:
                        #klucz =+
                    #else:
                        #klucz =+
                        #dlugosc.append(klucz)
                        #klucz = 0


    print(f"{dna}")


main()