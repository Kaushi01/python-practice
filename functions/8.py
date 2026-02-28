#prime num
a= int(input())
b= int(input())

for i in range(a+1, b):

    n=i
    f=0
    for j in range(1, n+1):
        if (n%j==0):
            f+=1
    if f==2:
        print(i)