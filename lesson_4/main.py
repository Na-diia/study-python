def say_hello(username, age):
    print(f'Hello, {username}, welcome to the club, buddy!')
    print(f'Your age is {age}, you are so beautiful!')

def print_numbers(start, stop):
    for num in range(start, stop): #range(10) =>  виведе цифри від 0 до 9
        print(f'Current number is {num}')
    print('------------------')
user_data = {
    "Dima": 25, "Sarah": 34, "Tom": 11
}
list_of_ranges = [(1, 10), (2, 9), (3, 8)]

for name, age in user_data.items():
    say_hello(name, age)

for start_pos, stop_pos in list_of_ranges:
    print_numbers(start_pos, stop_pos)

def check_connection(username, count_tries, priority):
    if priority > 10:
        finish = 5
        for attempt in range(1, count_tries + 1):
            if attempt == finish:
                print('Connect was successfully')
                break
            print(f'Attempt {attempt} to connect to {username} ')
    elif 5 <= priority < 10:
        finish = 3
        for attempt in range(1, 6):
            if attempt == finish:
                print('Connect was successfully')
            print(f'Attempt {attempt} to connect to {username} ')
    else:
        print('Your username has so low priority')

# check_connection(count_tries=10, username='Oleg', priority=100)
