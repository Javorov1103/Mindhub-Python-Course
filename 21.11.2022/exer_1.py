
#Дефиниране на функция
#дефинирана ф-я не изпълнява кода в тялото си, без да е извикана

# Функция, която връща резултат
def calculate_area_of_square(side: int):
    # Тяло на функцията
    # Изчислявам лицето на квадрата
    area = side*side
    # Връщам резултата от изчислението
    return area

# Функция, която просто извършва действие (void)
def print_long_hello():
    print("Hello")
    print("Hello from the other side")
    print("How are you")

#Извикваме функциите
print_long_hello()
print(calculate_area_of_square(4))
print(calculate_area_of_square(6))
print(calculate_area_of_square(10))
