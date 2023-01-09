def intersect(a,b):
    c = []
    for item in a:
        if item in b:
            c.append(item)
    return c

a = [1,2,7,12]
b = [1,2,8,9]

print(intersect(a,b))