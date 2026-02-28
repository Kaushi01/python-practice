#pallindrome

n= int(input())
p=n
rev=0
while n>0:
    last=n%10
   
    rev= rev*10+last 
    n=n//10

print(n, rev)
if(p==rev):
    print("Pallindrome")
else:
    print("Not")

print(rev)





