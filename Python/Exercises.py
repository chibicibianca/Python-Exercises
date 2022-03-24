#14 Write a Python program to match a string that contains only upper and lowercase letters,
# numbers, and underscores.
import re

def progr14(txt):
    if re.search('\w_', txt):
        print("True")
    else:
        print("False")

progr14("A_naban4343ana_")
progr14("123ddd!_!")
progr14("")


#15 Write a Python program where a string will start with a specific number
def progr15(txt):
    if re.match('^\d', txt):
        print("True")
    else:
        print("False")

progr15("111 mar")
progr15("A1na")

#16Write a Python program to remove leading zeros from an IP address
ip = "235.05.000.567"
str = re.sub('\.[0]*','.',ip)
print(str)

#17Write a Python program to check for a number at the end of a string
def progr17(txt):
    if re.search('.*\d$', txt):
        print("True")
    else:
        print("False")

progr17("sdsadsd1111")


#18 Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
#"Exercises number 1, 12, 13, and 345 are important"

char = re.finditer(r"([0-9]{1,3})", "numerele 1, 12, 123")
for n in char:
    print(n.group(0))

#19Write a Python program to search some literals strings in a string.
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'
def progr19(txt):
    x = ['fox', 'dog', 'horse']
    for i in x:
        if re.search(i, txt):
            print(i)
        else:
            print("Nope")

progr19("This cat dog 1 is awesome")

#20 Write a Python program to search a literals string in a string
# and also find the location within the original string where the pattern occurs.
def progr20(txt):
    x = "fox"
    if re.search(x, txt):
        n = txt.find(x)
        s = re.search(x,txt).start()
        e = re.search(x,txt).end()
        print(n, s, e)
    else:
        print("Nope")

progr20('The quick brown fox jumps over the lazy dog.')


#21 Write a Python program to find the substrings within a string.
# Sample text :
# 'Python exercises, PHP exercises, C# exercises'
# Pattern :
# 'exercises'
txt = "Python exercises, PHP exercises, C# exercises"
pattern = "exercises"

for nr in re.findall(pattern, txt):
    print(nr)

#22 Write a Python program to find the occurrence and position of the substrings within a string.

txt = "Python exercises, PHP exercises, C# exercises"
pattern = "exercises"

def progr22(pattern, txt):
    nr = 0
    for i in re.finditer(pattern, txt):
        nr = nr+1
        s = i.start()
        e = i.end()
        print(pattern, nr, s, e)

progr22(pattern, txt)

#23Write a Python program to replace whitespaces with an underscore and vice versa
def progr23(txt):
    text = txt.replace(' ','_')
    print(text)
    text = txt.replace('_', ' ')
    print(text)

progr23("Ana are __ mere")

#24Write a Python program to extract year, month and date from an url
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

date = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
print(date)

#25Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format
date = "2022-02-03"

date_rev = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)

print(date_rev)

#26 Write a Python program to match if two words from a list of words starting with letter 'P'
def progr26(txt):
    n = 0
    if re.match("^P+", txt):
        n = n+1
    for i in re.findall("(P\w+)", txt):
        n = n+1
        if n>2:
            print("Yes")
            break


def progr1(txt):
    for i in txt:
        m = re.match("(P\w+)\W(P\w+)", i)
        if m:
            print(m.groups())


words = ["Python PHP", "Java JavaScript", "c c++"]

for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        # Check for success
        if m:
            print(m.groups())

progr1("PAna are Prune si ortocale")
progr26("PAna are Prune si Portocale")

#27 Write a Python program to separate and print the numbers of a given string
def progr27(txt):
    nr = []
    for word in txt.split():
        if word.isdigit():
            nr.append(int(word))
    print(nr)

progr27("123 11 1111")

#28Write a Python program to find all words starting with 'a' or 'e' in a given string
# def progr28(txt):
#     words = []
#     for w in txt.split():
#         word = re.findall(r'\b[ae]\w+', w)
#         if word:
#             words.append(word)
#
#     print(words)

txt = "Ana are mere albe dar si elemente de culoare eeee"
list = re.findall(r"\b[ae]\w+", txt)
print(list)

#progr28("Ana are mere albe dar si elemente de culoare eeee")

#29Write a Python program to separate and print the numbers and their position of a given string
def progr29(txt):
    nr = []
    for word in txt.split():
        if word.isdigit():
            s = re.search(word,txt).start()
            e = re.search(word,txt).end()
            print("Numarul este %d si incepe la pozitia %d si termina la %d"%(int(word),s,e))

progr29("123 este nr meu noroco dar si 4 cat si 11")


#30 Write a Python program to abbreviate 'Road' as 'Rd.' in a given string
def progr30(txt):
    print(re.sub("Road","Rd", txt))


progr30("Road is")

#31 Write a Python program to replace all occurrences of space, comma, or dot with a colon
def progr31(txt):
    txt = txt.replace(",", ";")
    txt = txt.replace(".", ";")
    txt = txt.replace(" ", ";")
    print(txt)


progr31("Acest text are , si .")


#32 Write a Python program to find all three, four, five characters long word in a string
txt = 'All my jumps words do not have 5 chars in the txt'
print(re.findall(r"\b\w{3,5}\b", txt))
print(re.findall(r"\b\w{4,}\b", txt))  #at least 4

#36 Write a python program to convert camel case string to snake case string.
def camel_to_snake(text):
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(camel_to_snake('PythonExercises'))
print(snake_to_camel('Python_exercises'))

#39 Write a Python program to remove multiple spaces in a string.
txt = "ana   are mere"
txt1 = re.sub(' +', ' ', txt)
print(txt1)

