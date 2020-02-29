from random import randint
name_parts = ["me", "cha", "bra", "mo", "chi", "bra", "mi", "ha", "ra", "ma", "tha", "ka", "po"]

def select_name_part(name_list):
    x = randint(0, len(name_list) - 1)
    return name_list[x]

def create_name(length_of_name, name_list):
    name = ''
    for x in range(length_of_name):
        name += select_name_part(name_list)
    return name

def create_name_list(listpop):
    names_list = []
    for x in range(listpop):
        names_list.append((create_name(randint(2, 5), name_parts)).capitalize())
    return names_list

#for names in create_name_list(20):
#    print(names)


with open("saves/Names.txt","w+") as f:
    for names in create_name_list(20):
        f.write(names + '\n')

print("gen complete")