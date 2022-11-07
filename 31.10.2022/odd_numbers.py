n=6

# while n > 0:
#     n = n-1
#     if n % 2 !=0:
#         continue
#     print(n)

name = 'Antonia'

for letter in name:
    if letter == 'a' or letter == 't':
        continue
    print(letter, end=", ")

for i in range(len(name)):
    if name[i] == 'a' or name[i] == 't':
        continue
    print(name[i], end=", ")
