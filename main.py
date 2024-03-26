import datetime  # импорт модуля datetime


def hello(name):
    print("Hello there,", name)
    print("Hi there,", name)


hello('Igor')


def sum_nums(a, b):
    sum = a + b
    return sum


first_sum = sum_nums(10, 5)

print(first_sum)

print(sum_nums(50.5, 20))

print(sum_nums(sum_nums(50.5, 20), 30))

print(datetime.MAXYEAR)
