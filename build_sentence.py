import random

names = ['Gosho', 'Pesho', 'Mitko']
verbs = ['kicks', 'rides', 'eats']
nouns = ['burger', 'car', 'bike']

# index = random.randint(0,len(names))
# name = names[index]
name = random.choice(names)

# index = random.randint(0,len(verbs))
# verb = verbs[index]
verb = random.choice(verbs)

# index = random.randint(0,len(nouns))
# noun = nouns[index]
noun = random.choice(nouns)

print(f'{name} {verb} {noun}')
print(name + " " + verb + " " + noun)

