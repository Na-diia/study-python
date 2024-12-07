import jwt

headers = {
    "alg": "HS256",
    "typ": "JWT"
}

payload = {
    "username": "tester_user",
    "email": "tester@gmail.com",
    "is_active": False
}

secret = "secret_1234"
encoded_jwt = jwt.encode({"some": "payload"}, "secret", alg='HS256')
# token = jwt.jwt.JWT.encode(self="JWT", alg='HS256', optional_headers=headers, payload=payload, key=secret)
# token = jwt.JWT.encode(self=jwt.JWT(), payload=payload,alg='HS256', optional_headers=headers)
print(encoded_jwt)
