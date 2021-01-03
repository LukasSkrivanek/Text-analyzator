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
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Link name
SEPARATOR = "-" * 50
USERS = {"Bob": "123", "Ann": "pass123", "Mike": "password", "Liz": "pass123"}
print(SEPARATOR)
welcome = print("Welcome to the app. Please log in:")
username = input("USERNAME: ").title()
if not username in USERS.keys():
    print("Name is not in database")
    exit()
password = input("PASSWORD: ")
if not password in USERS[username]:
    print("password is incorrect")
    exit()
print(SEPARATOR)
# Text selection
print(f"We have {len(TEXTS)} texts to be analyzed.")
text_insertion = int(input(f"Enter a number of text 1 to {len(TEXTS)} ,you have selected: "))
print(SEPARATOR)
# Volba textu testing
if text_insertion == 1:
    text = str(TEXTS[0])
elif text_insertion == 2:
    text = str(TEXTS[1])
else:
    text = str(TEXTS[2])
# Text analysis
words = 0
lowercase = 0
uppercase = 0
titlecase = 0
number = 0
number_count = 0

text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.replace("-", "")

for word in text.split():
    if word.isalpha() or word.isdigit() or word.isupper():
        words += 1
    if word.isupper() and word.isalpha():
        uppercase += 1
    if word.istitle() and word.isalpha():
        titlecase += 1
    if word.islower() and word.isalpha():
        lowercase += 1
    if word.isdigit():
        number += 1
        # Sum of numbers
        word = float(word)
        number_count += word

print(f"There are {words} words in the selected text.")
print(f"There are {titlecase} titlecase words")
print(f"There are {uppercase} uppercase words")
print(f"There are {lowercase} lowercase words")
print(f"There are {number} numeric strings")
print(SEPARATOR)
# Graph
pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) ==1:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)

pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 2:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)


pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 3:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)

pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 4:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)


pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 5:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)


pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 6:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)


pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 7:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)

pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 8:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)

pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 9:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)


pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 10:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)

pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 11:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)


pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 12:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)


pocet_slov = 0
znak = '*'
for word in text.split():
  if len(word) == 13:
    pocet_slov += 1
    new_word = word
if pocet_slov > 0:
  znak = len(new_word) * znak
  print(len(new_word), znak, pocet_slov)
print(SEPARATOR)
# print(Sum of numbers)
print(f"If we summed all the numbers in this text we would get: {number_count}")
print(SEPARATOR)