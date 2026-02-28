#Take a three digit number and check if it is pallindrome or not

n= int(input())
unit_dig= n%10
last_two_dig= n//10

second_dig= last_two_dig%10
third_dig= last_two_dig//10

rev=unit_dig*100 + second_dig*10+ unit_dig
print(rev)

if  rev==n:
    print("pallindrome")
else:
    print("Not pallindrome")