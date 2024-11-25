# 1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
# 2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
# 3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
# 4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`. Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.

def add (a, b):
    print(a + b)
add(a=10, b=20)

def subtract (a, b):
    print(a - b)
subtract(a=20, b=10)

def multiply (a, b):
    print(a * b)
multiply(a=10, b=10)

def divide(a, b):
    if b == 0:
     print('Type another number')
    else:
     print(a / b)

divide(a=9, b=0)