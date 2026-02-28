n= int(input())
#temp=n
#count=0

def countDigit(temp):
 count=0
 while temp>0:
    last= temp%10
    count+=1
    temp=temp//10
 return count
  
def armstrong():
  temp=n
  armstrong=0
  temp=n
  while temp>0:
   dig= temp%10
   armstrong+= dig**count
   temp=temp//10
  return armstrong
  
if armstrong==n:
  print("YES")
else:
  print("NO")
  