#7068 any num print extract 7 0 6 8 only

n= int(input()) #7068
temp=n

count=0
while n>0:

    count= count+1
    n=n//10
print(count)

n= temp
c= count-1

while True:
    first=n//(10**c)
    start= first%10
    print("count", c, "number", n, 10**c, first,start)


    c=c-1



    
    
