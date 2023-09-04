from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
print (len(sys.argv))

if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        i = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output:", figlet.renderText(i))
    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    i = input("Input: ")
    figlet.setFont(font = random.choice(fonts))
    print("Output:{\n}", figlet.renderText(i))

else:
    sys.exit("Invalid usage")