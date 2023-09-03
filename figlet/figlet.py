from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
print (len(sys.argv))
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" or sys.argv[1] != "--font" or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        i = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output:", figlet.renderText(i))

else:
    i = input("Input: ")
    figlet.setFont(font = random.choice(fonts))
    print("Output:", figlet.renderText(i))
