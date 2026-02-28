n= int(input())
temp=n


while temp>0:
    extract= (temp//10)%10
    
print(extract)
sq=0
cube=0
quad=0
temp=n
while temp>0:
    last= temp%10
    sq+= last**2
    cube= last**3
    quad= last**4
    print(f"{sq}+{cube}+{quad}={sq+cube+quad}")