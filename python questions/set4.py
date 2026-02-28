#Take a number and check it is 1 digit number , or 2 digit number, or 3 digit number or something else
n=int(input())

if n<=9:
    print('Single Digit')
elif n>9 and n<=99:  #or only n<=99
    print("Double Digit")
elif n>99 and n<=999:  #or only n<=999
    print("Three Digit")
else:
    print("Something Else")
