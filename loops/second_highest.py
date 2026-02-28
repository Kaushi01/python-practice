#second_highest

max=0 

for i in range(5):
    a= int(input())
    if a>max:
        s_max=max
        max=a
    elif a>s_max:
        s_max=a

print(max,s_max)