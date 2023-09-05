def main():
    i = input("Input: ")
    print("Output: ", end="")
for letter in i:
    if letter in ["a","A","e","E","i","I","o","O","u","U"]:
        continue
    else:
        print(letter, end="")
print()