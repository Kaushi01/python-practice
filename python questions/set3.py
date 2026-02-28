#Take three number and print the biggest number 

a=int(input())
b=int(input())
c=int(input())


if a>=b and a>=c:
    print("a is greatest")
elif b>=a and b>=c:
    print("b is greatest")
elif c>=a and c>=b:
    print("c is greatest")