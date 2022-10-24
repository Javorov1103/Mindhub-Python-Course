# my_list = ['ivan', 'parvan', 'pesho', 'gosho', 'kalin','ivan', 'parvan', 'pesho', 'gosho', 'kalin','ivan', 'parvan', 'pesho', 'gosho', 'kalin','ivan', 'parvan', 'pesho', 'gosho', 'kalin','ivan', 'parvan', 'pesho', 'gosho', 'kalin','ivan', 'parvan', 'pesho', 'gosho', 'kalin']
# my_list[2] = 'svetlio'
# print("Guest list", my_list)

# for name in my_list:
#     print(f"{name},  I want to invite you bla bla bla")

# for i in range(len(my_list)):
#     if(i % 2 == 0):
#         print(f"{i+1} {my_list[i]},  I want to invite you bla bla bla in 18:00")
#     else:
#         print(f"{i+1} {my_list[i]},  I want to invite you bla bla bla in 20:00")
    

# import random

# colors=['blue', 'orange', 'white', 'red', 'green']

# color = random.choice(colors)

# odd_numbers = []
# even_numbers = []
# numbers_3 =[]


# for i in range(1,21):
#     # if i != 0:
#         if i % 2 == 0 :
#             odd_numbers.append(i)
#         else:
#             even_numbers.append(i)
#         if i % 3 == 0:
#             numbers_3.append(i)

# print(f"{odd_numbers} Брой: {len(odd_numbers)} Сума: {sum(odd_numbers)}")
# print(f"{even_numbers} Брой: {len(even_numbers)} Сума: {sum(even_numbers)}")
# print(f"{numbers_3} Брой: {len(numbers_3)} Сума: {sum(numbers_3)}")

import random

multi =[]
for i in range(20):
    number = random.randint(1,100)
    if number % 5 ==0:
        multi.append(number)

result = 1
for number in multi:
    result = result*number

print(result)
