import emoji
import sys

i = input("Input: ")

try:
    print("Output:" + emoji.emojize(i))

except Exceptation:
    sys.exit()