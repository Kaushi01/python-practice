#take a num and find sum of its digits using string concepts

num= 123
s= str(num)

sum=0
for i in range(0, len(s)):
    sum+=int(s[i])
print(sum)