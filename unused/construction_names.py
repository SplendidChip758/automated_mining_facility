import random
import string

name_list = []

prefix = "Utility Unit"
letters = string.ascii_uppercase


for i in range(10):
    number = str(random.randint(0,9))
    letter = random.choice(letters)
    name = '"' + prefix + " " + number + letter + "-" + number + '"'
    name_list.append(name)

with open('construction_name.txt', 'w') as f:

    for item in name_list:
        
        f.write("%s " % item)
