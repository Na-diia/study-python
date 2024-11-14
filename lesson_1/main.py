
user_email = 'example@gmail.com'
# userEmail = 'example@gmail.com'
# print(user_email, userEmail)

# name='John'
# print(name)

# name = 'John'
# print(name)

# num_1 = 100
# num_2 = 10 
# num_3 = num_1 + num_2

# print(num_3)

# num_1 = 7
# num_2 = 2
# num_3 = num_1 / num_2
# num_4 = num_1 // num_2 #скільки разів поміщується num_2 в num_1

# print(num_3, num_4)

# num_1 = 5
# num_2 = 2
# num_3 = num_1 ** num_2 #скільки буде num_1 в ступені num_2

# print(num_3)

# num_1 = 7
# num_2 = 2
# num_3 = num_1 % num_2 #рахує скільки 2 поміститься в 7 і повертає залишок, тобто 1

# print(num_3)

#Оператори порівняння

# num_1 = 7
# num_2 = 2
# num_3 = num_1 == num_2 # false
# num_4 = num_1 != num_2 # true
# num_5 = num_1 < num_2 #false
# num_6 = num_1 > num_2 #true

# print(num_5, num_6)

#Логічні оператори

# num = 10
# name = 'Tom'

# result = num  > 5 and name == 'Tom'
# result = num < 5 or name == 'Tom'
# message = 'Tom got some money' 
# print(name in message) # the same like include in JS
# print(name not in message) # not include 

# name = 'John'
# message = 'You won!'

# print (name in message)

# age = 50 
# name = 'Ira'
# animal = 'Cat'

# print(age == 50 and 'I' in name and animal != 'Dog')
# print(age == 50 and 'I' in name or animal == 'Dog')

#Data type

num_1 = 5
print(type(num_1))# int

num_2 = 3.14
print(type(num_2))# float

string = 'hello'
print(type(string))# str

check = True
print(type(check)) # bool

lst = ['hello', 'my', 'name', 'is', 'Tom']
print(type(lst)) # list

tpl = (1, 2, 3)
print(type(tpl)) #tuple - кортеж

dct = {'name': 'John', 'age': 23}
print(type(dct))# dict

set_ex = {1, 2, 3} # не можна вводити однакові значення, інтерпретатор їх не побачить
print(type(set_ex)) #set

print(type(None)) #NoneType

class Person: 
    pass #not to do anything

a = Person()
print(type(a))

