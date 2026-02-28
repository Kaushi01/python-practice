#456-> 654
#reverse three digit number
#Hint: % will give unit digit. then reverse the two digits remaining 


a=int(input("Enter the three digit number: "))

num1=a%10 #say 765 , we get 5
last_two_digit= a//10 #we get 76

num2= last_two_digit%10
num3= last_two_digit//10

print(f"{num1}{num2}{num3}")

