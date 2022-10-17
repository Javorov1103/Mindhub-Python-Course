import random

num = random.randint(1,100)
user_num = int(input())
points =0
while num != user_num:
    if num > user_num:
        print('Higher')
    
    if num < user_num:
        print("Lower")
    
    points += 1
    user_num = int(input())

print(f"You win with {points} steps")