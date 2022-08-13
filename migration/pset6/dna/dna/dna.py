import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print ("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)
    # TODO: Read database file into a variable
    people = []
    with open(sys.argv[1], 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            people.append(row)
    #print(list(people))
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as f:
        dna = f.read()
    # TODO: Find longest match of each STR in DNA sequence
    sekwencje = []
    for i in range(len(list(people[0]))):
        if i == 0:
            continue
        else:
            sekwencje.append(longest_match(dna, list(people[0])[i]))
    #longest_match(dna, people[i].values[j)
    # TODO: Check database for matching profiles
    check = 0
    for i in range(len(people)):
        for j in range(len(list(people[0]))):
            if j == 0:
                continue
            elif int(sekwencje[j-1]) == int((list(people[i].values())[j])):
                check =+ 1
        if check == len(sekwencje):
            print(list(people[i].values())[0])
            return
        else:
            check = 0
    print('No match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
