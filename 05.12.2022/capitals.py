from tkinter import Tk, simpledialog, messagebox

def read_from_file(filePath):
    with open(filePath) as file:
        for line in file:
            line = line.rsplit('\n')
            country, city = line[0].split('/')
            the_world[country] = city

def write_to_file(country_name, city_name, filePath):
    with open(filePath, 'a') as file:
        file.write(f'\n{country_name}/{city_name}')

print("Ask the expert - capital cities of the world!")

root = Tk()
root.withdraw()

the_world = {}
read_from_file('05.12.2022/capitals_data.txt')


while True:
    query_country = simpledialog.askstring('Country','Type the name of a country')
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', f'The capital city of {query_country} is {result} !')
    else:
        new_city = simpledialog.askstring("Teach me", f"I don't know the capital of {query_country}. Tell me which is the capital")
        the_world[query_country] = new_city
        write_to_file(query_country, new_city, '05.12.2022/capitals_data.txt')
        
