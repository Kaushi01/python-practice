#Take a number and check if it is integer number or decimal number 
n=int(input())

integer_n= int(n)
decimal_n= n - integer_n

if decimal_n==0:
    print("Integer")
else:
    print("Decimal")