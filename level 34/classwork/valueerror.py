listi = [1,2,3]

a = int(input("choose a number from a listi: "))

try:
    print(listi[a])
except IndexError:
    print("type error")
except ValueError:
    print("value error")
    