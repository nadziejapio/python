def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_with_two_letters(s) and min_max_characters(s) and numbers(s) and signs(s):
        return True
    else
        return False

def start_with_two_letters(plate):
    if 1 < len(plate) < 7:
        if plate[0].isalpha() and plate[1].isalpha():
            return True
    else:
        return False
def numbers(plate):

def signs(plate):


main()