
'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. 
''',

'''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.
''',

'''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.
''']

# Link name
SEPARATOR = "-" * 50
users = {"Bob": "123", "Ann": "pass123", "Mike": "password", "Liz": "pass123"}
print(SEPARATOR)
welcome = print("Welcome to the app. Please log in:")
username = input("USERNAME: ")
if username not in users.keys():
    print("Name is incorrect")
    exit()
password = input("PASSWORD: ")
if password != users[username]:
    print("password is incorrect")
    exit()
print(SEPARATOR)
# Text selection
print(f"We have {len(TEXTS)} texts to be analyzed.")
text_insertion = input(f"Enter a number of text 1 to {len(TEXTS)} ,you have selected: ")
print(SEPARATOR)

if not text_insertion.isnumeric():
    print("Number of text must be a number")
    exit()
elif int(text_insertion) == 1:
    text_choice = str(TEXTS[0])
elif int(text_insertion) == 2:
    text_choice = str(TEXTS[1])
elif int(text_insertion) == 3:
    text_choice = str(TEXTS[2])
elif int(text_insertion) >= 4 or text_insertion == 0:
    print("You have selected wrong number of text")
    exit()
# Text analysis
title_case = 0
upper_case = 0
lower_case = 0
words = 0
digits = list()
frequencies = dict()

for word in text_choice.split():
    word = word.strip(",.")
    words += 1
    if len(word) not in frequencies:
        frequencies[len(word)] = 1
    else:
        frequencies[len(word)] += 1
    if word.istitle():
        title_case = title_case + 1
    elif word.isupper():
        upper_case = upper_case + 1
    elif word.islower():
        lower_case = lower_case + 1
    elif word.isdigit():
        digits.append(int(word))

print(
    f"There are {words} words in the selected text.",
    f"There are {title_case} titlecase words",
    f"There are {lower_case} lowercase words",
    f"There are {upper_case} uppercase words",
    f"There are {len(digits)} numeric words",
    SEPARATOR,
    f"If we summed all the numbers in this text we would get: {sum(digits)}",
    sep="\n"
)
# Graph
print(frequencies)
for k, v in frequencies.items():
    print(k, int(v) * '*', v)
print(SEPARATOR)
