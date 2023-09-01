import emoji
import sys

i = input("Input: ")

try:
    print(f"Output: {emoji.emojize(i)}")

except Exceptation:
    sys.exit()