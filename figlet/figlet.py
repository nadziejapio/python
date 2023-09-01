from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if sys.argv == 0:
    print(fonts)
elif sys.argv == 2:
    sys.exit()
else:
    sys.exit()
