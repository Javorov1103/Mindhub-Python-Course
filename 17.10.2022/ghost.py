import random

ghost_door = random.randint(1,3)

print("Three rooms")
print('1, 2 or 3')
guess = int(input())

while guess < 1 or guess > 3:
    print("Wrong number")
    guess = int(input())

if ghost_door != guess:
    print("No ghost")
else:
    print("Ghost")

