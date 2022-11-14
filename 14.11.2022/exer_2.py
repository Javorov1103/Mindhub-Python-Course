import random

numbers1 =[]
numbers2 = []
sum_numbers =[]

for i in range(20):
    numbers1.append(random.randint(1,100))
    numbers2.append(random.randint(1,100))
    sum_numbers.append(numbers1[i]+numbers2[i])

sum_numbers.sort()
print(sum_numbers)