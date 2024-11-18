# string = 'Hello, World!'

# if 'Hello'  not  in string:
#     print('Hello in string')
# elif 'World' in string :
#     print('world in string')
# else:
#     print('Word not in string')

# a= 10 
# b = 20

# if a == 11 and b == 20 or b < 30 :
#     print(a + b)
# else:
#     print('Wrong conditions')

# test_list = ['hello', 'test', 1, 2, 3]

# if 'hello' in test_list and 1 in test_list:
#     print('hello 1')
# elif 'test' in test_list and 4 not in test_list:
#     print('test not 4')
# else:
#     print('Your conditions were wrong')

# a = 10 
# b = 20 
# c = 'chat is active'
# d = 'count of users'

# if len(c) >= b:
#     print(c)
# elif len(d) <= a:
#     print(d)
# else:
#     print('Wrong conditions')

# user_1 = {
#     "name": "Tom",
#     "age": 21,
#     "balance": 20000,
#     "currency": "USD",
#     "status": True
# }

# user_2 = {
#     "name": "John",
#     "age": 17,
#     "balance": 5000,
#     "currency": "EUR",
#     "status": False
# }

# user_3 = {
    
#     "age": 30,
#     "balance": 100000,
#     "currency": "UAH",
#     "status": True
# }

# list_currency = ["USD", "EUR", "UAH"]

# if user_3.get("name", None) and user_3["age"] >= 18 and user_3["status"]:
#     if user_3["balance"] >= 10000 and user_3["currency"] in list_currency:
#         print(f"Hello! You can create your binance account, welcome {user_3['name']}")
#     elif user_3["balance"] >= 1000 and user_3["currency"] in list_currency:
#         print("You need more money!")
#     else:
#       print("Money ctitical not enough")
# elif not user_3.get("name", None) :
#     print('Please, type your name!')     
# elif user_3["age"] < 18:
#     print("For registry binance account you have to be 18 years old")
# else: 
#     print("something went wrong")

# test_list = [1, 2, 3, 4, 5, 6]

# for num in test_list:
#     print(f"You got a {num}")

# a = 0

# while a < 10:
#     a += 1
#     print(a)

# test_list = [1, 2, 3, 4, 5]

# while len(test_list) < 10:
#     test_list.append(3)
#     print(test_list)

# test_list = ['test', 'python', 'code']

# for s in test_list:
#     print(s, '----->')
#     if s == 'test':
#         print(s)
#     elif s == 'python':
#         print(s)
#     else :
#         print(s)

# a = 0
# add_list = []

# while len(add_list) < 100:
#     print('Len of the list:', len(add_list))
#     add_list.append(a)
#     a +=1
#     if len(add_list) == 50:
#         print('You are at the middle of the list')

user_1 = {
    "user_name": "tester",
    "role": "admin",
    "account_connection": True
}

user_2 = {
    "user_name": "junior",
    "role": "user",
    "account_connection": False
}

user_3 = {
    "user_name": "middle",
    "role": "pro-user",
    "account_connection": True
}

list_of_users = [user_1, user_2, user_3]

for user in list_of_users:
    print(f"Work with {user['user_name']} account", "-----<<<<")
    if not user['account_connection']:
        count_of_tries = 10
        while count_of_tries != 0:
            print('Try to connect to user account')
            count_of_tries -= 1
            if count_of_tries == 5:
                print('Middle of tries')
                continue
            print('Count of tries left', count_of_tries)
    elif user["role"] == 'admin':
        print(f"Hello in system {user['user_name']}")
    else:
        print("Welcome on the board!")
