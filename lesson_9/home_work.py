import requests
# Завдання 1: Виконання GET-запиту

site = "https://jsonplaceholder.typicode.com/comments?"
response_get = requests.get(url=site)
# print(response_get.json())
# Завдання 2: Параметри запиту

response_get_2 = requests.get(url=site, params={"postId": 1})
print(response_get_2.json())
# Завдання 3: POST-запит
body = {
    "name": "Nadiia",
    "email": "nadiia@gmail.com",
    "body": "Hello, buddy"
}
req_post = requests.post(url=site, json=body)
print(req_post.status_code)
print(req_post.reason)
print(req_post.text)

# Завдання 4: Обробка відповіді

for header, value in response_get.headers.items():
    print(f"Headers: {header}, ==> Value: {value}")

# Завдання 5: Обробка помилок

url = "https://jsonplaceholder.typicode.com/comments"

try:
    result = requests.get(url)
    result.raise_for_status()
except requests.exceptions.RequestException as err:
    print("HTTP Error")
    print(err.args[0])

print(result)

# Завдання 6: Збереження вмісту в файл

response= requests.get(url)
file_object = open("my_file.txt", "r+")
file_object.write(str(response.content))