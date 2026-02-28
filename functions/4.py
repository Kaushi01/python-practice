def fact(x):
    f=1
    for i in range(1, x+1):
        f*=i
    return f


n=5
r=3

ans= fact(n)/ (fact(r)*fact(n-r))
print(ans)

