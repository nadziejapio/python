def main():
    i = input("Input: ")
    print(f"Output: {shorten(i)}")

def shorten(word):
    ans = ""
    for letter in word:
        if letter in ["a","A","e","E","i","I","o","O","u","U"]:
            continue
        else:
            ans += letter
    return ans

if __name__ == "__main__":
    main()