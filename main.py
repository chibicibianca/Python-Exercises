#Write a Python program to match a string that contains only upper and lowercase letters,
# numbers, and underscores.

import re

def progr(txt):
    if re.search('\w_', txt):
        print("True")
    else:
        print("False")

progr("A_naban4343ana_")
progr("123ddd!_!")
progr("")