import random
import string

name_list = []

prefix = ['Node','Hub', 'Conduit', 'Grid', 'Installation', 'Junction']
letter = string.ascii_uppercase

length = 10

for i in range(100):
    number = str(random.randint(0,999))
    n = random.randint(1, 3)
    letters = ''.join(random.choice(letter) for i in range(n))
    pre = random.choice(prefix)
    name = '"' + pre + " " + letters + "-" + number + '"'
    name_list.append(name)

chunks = (name_list[i:i+length] for i in range(0, len(name_list), length))

with open('planet_name.txt', 'w') as f:

    for item in chunks:
        for name in item:
            f.write("%s " % name)
        f.write("\n")    
