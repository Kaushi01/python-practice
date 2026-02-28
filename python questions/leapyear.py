#leap year

n= int(input())

if n%100==0:
    if n%400==0:
      print("It is a leap year")
    else:
       print("Century year but not leap year")
    
elif n%4==0:
       print("It is a leap year")
    
else:
    print("It is not a leap year")