#Take a three digit number and check if it is pallindrome or not

n= int(input())

last= n%10
first= n//100

if last== first:
    print("Pallindrome")
else:
    print("Not pallindrome")