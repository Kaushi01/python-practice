x=1
for lines in range(3):
    print("lines",lines, "x",x)
    for i in range(x):
        print("*", end=" ")
    print()
    x= x+2