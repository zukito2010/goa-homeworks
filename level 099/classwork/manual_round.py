def manual_round(num):
    if int(str(num).split(".")[1][0]) < 5:
        return int(num)
    else:
        return int(num+1)
print(manual_round(2.5))