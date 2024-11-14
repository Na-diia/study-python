# lst = [1, 2, 3, 4, 5]
# dct = {'name': 'Tom', 'age': 5}
# name = 'Tom'
# tpl = ('n', 'a', 'g')

# result = dct['age'] in lst or dct['name'] in tpl #dct.age
# print(dct['name'] == name and dct['age'] in lst) 

#INTEGRATED FUNCTIONS

# num_1 = '1'
# print(type(num_1))
# num_1 = int(num_1)
# print(type(num_1))
# num_1 = float(num_1)
# print(type(num_1))

string = 'hello world!'
print(len(string))    # кількість символів
print(string.upper()) # у верхній регістр
print(string.lower()) # у нижній регістр
print(string.capitalize()) # збільшує першук букву
string = string.replace('!', '.')
print(string) # 'hello, world.' - replace letters or symbols
string = string.split()
print(string)
string = " ".join(string)
print(string)
print(string.count("o"))
string = 1
string = str(string)
print(type(string))