name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")
# print(f'Your name is {name}, you are {age} years old and you live in {city}. Nice to meet you.')

print(name.capitalize()) #возвращает строку name с первым символом в верхнем регистре, а остальные в нижнем
print(name.upper()) #возвращает строку name в верхнем регистре
print(name.casefold()) #возвращает строку name в нижнем регистре
print(name.center(12)) #возвращает строку name c отступом в 4 пробела (1 пробел кратный значению 3?)
print(name.count("i")) #возвращает число равное количеству символов в скобках
print(name.endswith("r")) #возвращает true если name оканчивается на заданный символ
print(name.find("o")) #возвращает число равное порядку на котором находится искомый символ, начало с 0
print(name.isalnum()) #возвращает true если name содержит только цифры и буквы (без символов)
print(name.isalpha()) #возвращает true если name содержит только буквы
print(name.isascii()) #возвращает true если name содержит буквы ASCII 
print(name.isdigit()) #возвращает true если name - цифровая строка
print(name.isdecimal()) #возвращает true если name - дробное число
print(name.isnumeric()) #возвращает true если name - число
print(name.isprintable()) #возвращает true если name выводимая строка
