#a=40, b=40, c=100

a= int(input())
b= int(input())
c= int(input())

if a==b and a!=c and b!=c:
    print("Iso")
elif b==c and b!=a and c!=a:
    print("Iso")
elif c==a and c!=b and a!=b:
    print("Iso")
else:
    print("Not Iso")
