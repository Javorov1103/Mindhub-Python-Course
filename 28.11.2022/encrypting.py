from tkinter import messagebox, simpledialog, Tk

def get_task():
    task = simpledialog.askstring('Tasks','Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message','Enter the secret message')
    return message

def is_even(number):
    return number % 2 == 0

# Get the letters of the message, which are on the even indexes
def get_even_letters(message):
    even_letters = []
    for i in range(0, len(message)):
        if is_even(i):
            even_letters.append(message[i])
    return even_letters

# Get the letters of the message, which are on the odd indexes
def get_odd_letters(message):
    odd_letters = []
    for i in range(0,len(message)):
        if not is_even(i):
            odd_letters.append(message[i])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message +'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    for i in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[i])
        letter_list.append(even_letters[i])
    new_message = ''.join(letter_list)
    return new_message
    
root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        messagebox.showinfo('Message',f'Ciphertext of the secret message is {message}')
    elif task == 'decrypt':
        message = get_message()
        messagebox.showinfo('Message',f'Plaintext of the secret message is {message}')
    else:
        break

root.mainloop()