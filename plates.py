def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_with_two_letters(s) and numbers(s) and signs(s):
        return True
    else
        return False

def start_with_two_letters(plate):
    if 1 < len(plate) < 7:
        if plate[0].isalpha() and plate[1].isalpha():
            return True
        else:
            return False
    else:
        return False

def numbers(plate):
    if len(plate)>3:
        if plate[2] == "0":
            return False
        


def signs(plate):
    if plate.isalnum():
        return True
    else:
        return False

main()