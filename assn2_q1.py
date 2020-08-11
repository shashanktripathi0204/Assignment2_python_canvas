# pattern

for i in range(1,11):
    if i<6:
        for j in range(0,i):
            print("*",end="")
        print()
    else:
        for j in reversed(range(10-i)):
            print("*",end="")
        print()
