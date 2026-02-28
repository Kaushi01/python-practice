#456-> 654
#reverse three digit number
#Hint: % will give unit digit. then reverse the two digits remaining  (METHOD-2)


a=int(input("Enter the three digit number: "))

last_digit=a%10 #say 765 , we get 5

last_two_digit= a//10 #we get 76

second_last= last_two_digit%10 #6
first_digit=last_two_digit//10 #5

print(last_digit*100 + second_last*10 + first_digit)