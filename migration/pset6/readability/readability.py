from cs50 import get_string

# main


def main():
    s = get_text()
    let = 0
    wor = 0
    sen = 0
    space = [" "]
    dots = [".", "!", "?"]

# loop

    for c in s:
        if c.isalpha():
            let += 1
        if c in space:
            wor += 1
        if c in dots:
            sen += 1
    x = 0
    L = float(let / float(wor + 1) * 100)
    S = float(sen / float(wor + 1) * 100)

# maths

    x = 0.0588 * L - 0.296 * S - 15.8
    g = str(round(x))

# printing

    if x > 16:
        print("Grade 16+")
    elif x < 1:
        print("Before Grade 1")
    else:
        print("Grade " + g)

# get input


def get_text():
    s = get_string("Text: ")
    return s


# execute
main()