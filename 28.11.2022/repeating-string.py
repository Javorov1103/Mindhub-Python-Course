def repeat_string(text, count):
    reapeated_string = ''
    for i in range(count):
        reapeated_string = reapeated_string + text
    return reapeated_string

text = input()
count = int(input())

rep_str = repeat_string(text, count)

print(rep_str)