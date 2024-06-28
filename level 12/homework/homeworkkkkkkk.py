grade = int(input("enter your score 1-100: "))

if 90 <= grade <= 100:
    print("your grade is A")
elif 80 <= grade < 90:
    print("your grade is b")
elif 70 <= grade < 80:
    print("your grade is c")
elif 60 <= grade < 70:
    print("your grade is d")
elif 0 <= grade < 60:
    print("your grade is f")
else:
    print("thats not real score lol")
