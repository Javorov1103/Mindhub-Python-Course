number = int(input())  
def read_and_process_message():
    message_type = input()
    match message_type:
        case 'success':
            operation = input()
            message = input()
            show_success_message(operation,message)
        case 'warning':
            message = input()
            show_warning_message(message)
        case 'error':
            operation = input()
            message = input()
            error_code = input()
            show_error_message(operation,message,error_code)
            
def show_success_message(operation,message):
    print()
def show_warning_message(message):
    print()
def show_error_message(operation,message,error_code):
    print()
    
for i in range(number):
    read_and_process_message()