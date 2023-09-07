import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-lines arguments")
else:
    try:
        students = []
        with open('before.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        with open('after.csv') as after_file:
            writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
            writer.writerow()
            for student in students
            print(students)
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')