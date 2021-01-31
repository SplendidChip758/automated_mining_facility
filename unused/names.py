import random
import string

name_list = []

n = 20

for i in range(1000):
    letter = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    number = str(random.randint(10000,99999))
    name = letter + "-" + number
    name_list.append(name)

chunks = (name_list[i:i+n] for i in range(0, len(name_list), n))

with open('name_list.txt', 'w') as f:

    for item in chunks:
        for name in item:
            f.write("%s " % name)
        f.write("\n")    
