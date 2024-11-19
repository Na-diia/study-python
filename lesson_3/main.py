# a = [1, 2, 3, 4, 5]
# b = ['apple', 'banana', 'cherry']

# print(a[0], a[1], a[-1], b[1])
#
# print(a[1:4], a[::2])
# print(b[::2])
# print(a[::-1])
# print(b[::-1])

#METHODS

# a.append(6)
# b.append('tomato')
# print(a, b)

# a.insert(3, 7.4)
# b.insert(1, 'bottle')
#
# a.remove(7.4)
# b.remove('bottle')
# print(a, b)

# last_elem_1 = a.pop()
# last_elem_2 = b.pop() #remove the last item of list, return element which pop removes
# last_elem_1 = a.pop(0)
# last_elem_2 = b.pop(0)
# print(last_elem_1, last_elem_2)

# print(a.index(3), b.index('banana'))
#
# a.extend([5, 5, 5])
# b.extend(['cherry', 'banana', 'banana'])
# print(a, b)
# print(a.count(5), b.count('banana'), b.count('cherry'))
#
# a.sort(reverse=True)
# b.sort(reverse=True)
# print(a, b)
#
# a.reverse()
# b.reverse()
# print(a, b)

# TUPLE

# a = (1, 2, 3, 4, 5, 5, 4)
# print(a[0],a[1], a[2])
# print(a[:2], a[-2:]) #(1, 2) (4, 5)
#
# print(a.count(4), a.count(5))
# print(a.index(3))

#DICT

test_dict = {
    "user": "Oleg",
    "age": 21,
    "country": "Poland"
}
# print(test_dict['user'], test_dict['age'], test_dict.get("country"))
# print(test_dict.get("animal", "key not found"))
# test_dict["age"] = 30
# print(test_dict["age"])
# test_dict["animal"] = "cat"
# print(test_dict["animal"])
# animal = test_dict.pop("animal")
# print(test_dict)
# print(animal) #cat

#METHODS

# copy_test = test_dict.copy()
# test_dict.clear()
# print(test_dict)
# print(copy_test)

for key, value in test_dict.items():
    print(f"key: {key}, value: {value}")

# wrong_key = test_dict.pop('currency', "key not found")
# print(wrong_key)

dict_update = {
    "new_role": "admin",
    "salary": 10000
}
test_dict.update(dict_update)
print(test_dict)