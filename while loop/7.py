#n= 1783 print all digits

n= 6099

for i in  range(n):
    last=n%10
    print(last)

    n=n//10

    if n==0:
        break

       