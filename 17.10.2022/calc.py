while True:
    number1 = int(input())
    number2 = int(input())

    operation = input()

    match operation:
        case '+':
            print(number1 + number2)
        case '-':
            print(number1 - number2)
        case '*':
            print(number1*number2)
        case '/':   
            print(number1 / number2)
        case 'exit':
            break
        case _:
            print("Invalid operation")
 