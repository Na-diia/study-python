base_list = [1, 2, 3]
print(len(base_list))
base_list.append(4) # add item  in the end of the list
print(base_list)
base_list.extend([5, 6, 7])
print(base_list) # [1, 2, 3, 4, 5, 6, 7]
print(base_list.index(4))

#DICTIONARY
base_dict = {'name': 'Tom', 'age': 40, 'high': 180}
print(base_dict.keys())
print(base_dict.values())
print(base_dict.items()) #([('name', 'Tom'), ('age', 40), ('high', 180)])
print(base_dict['name'], base_dict.get('name'))