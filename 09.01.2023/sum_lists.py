def calculate_sum(num1,num2):
    return num1+num2

def set_elements_sum(a,b):
    c = []
    for i in range(len(a)):
        result = calculate_sum(a[i],b[i])
        c.append(result)
    return c

x = [1,5,7,6]
y = [2,4,9,3]

print(set_elements_sum(x,y))