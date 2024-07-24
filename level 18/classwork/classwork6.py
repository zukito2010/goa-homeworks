def discount(age=0):
    if age >= 18:
        return "You didn't get a discount"
    else:
        return "You get a discount"

aage = int(input("Enter your age: "))
print(discount(aage))
