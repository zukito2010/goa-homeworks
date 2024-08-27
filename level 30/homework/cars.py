car1 = {
    "Brand": "Toyota",
    "Model": "Corolla",
    "Year": 2020,
    "Price": "$20,000"
}
car2 = {
    "Brand": "Honda",
    "Model": "Civic",
    "Year": 2021,
    "Price": "$22,000"
}
car3 = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 2022,
    "Price": "$30,000"
}

print("car1: ")
for key,value in car1.items():
    print(f"Key: {key}, Value: {value}")

print("car2: ")
for key,value in car2.items():
    print(f"Key: {key}, Value: {value}")

print("car3: ")
for key,value in car3.items():
    print(f"Key: {key}, Value: {value}")