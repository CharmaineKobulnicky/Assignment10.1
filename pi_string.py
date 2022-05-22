import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

address = input("What is your address? ")

filename = 'address.json'
with open(filename, 'w') as f:
    json.dump(address, f)
    print(f"We'll remember you when you come back, {address}!")

phoneNumber = input("What is your phone number? ")

filename = 'phoneNumber.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {phoneNumber}!")

