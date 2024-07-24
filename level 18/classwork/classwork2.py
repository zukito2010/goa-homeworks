def num_summary(num1 = 0, num2 = 0, num3 = 0):
    if type(num1) is not int:
        print("please input first number with  integer value")
    elif type(num2) is not int:
        print("please input second number with integer value")
    elif type(num3) is not int:
        print("please input second third with integer value")
    else:    
        print(num1 + num2 + num3)
        

num_summary(5,8,1)

