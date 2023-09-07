import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-lines arguments")
else:
    try:
        students = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        with open('after.csv', "a") as after_file:
            writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
            for student in students:
                writer.writerow({"first": student['name'].split(",")[1].strip(), "last":student['name'].split(",")[0].strip(), "house": student['house']})
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')