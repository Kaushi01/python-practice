
def sumOfPower(n, p):
    sum=0
    while n>0:
        last= n%10
        sum= sum + last**p
        n= n//10
    return sum

ans= sumOfPower(123, 2)+ sumOfPower(123, 3)+ sumOfPower(123, 4)
print(ans)