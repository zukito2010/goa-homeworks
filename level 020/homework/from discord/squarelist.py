def squared_list(list=[]):
    print(list)
    new_list = [x ** 2 for x in list]
    print(new_list)

squared_list([5, 1, 5, 1, 6, 2, 3, 6, 8])
