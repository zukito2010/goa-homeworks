def divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        print("it is divided by both")
    elif num % 3 == 0:
        print("its divided by only 3")
    elif num % 5 == 0:
        print("its divided by only 5")
    else:
        print("its divided by neither")

divisibility(15)
divisibility(5)
divisibility(3)
divisibility(8)
