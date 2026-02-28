#Question 5: 
# Take a 2 digit number and reverse it. (method II)

num=int(input("Enter two digit number: "))

num1=num%10
num2=num//10

print(f"{num1}{num2}")