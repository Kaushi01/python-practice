def fact(x):
    f=1
    i=1
    while i<=x:
        f*=i
        i=i+1
    return f


n=5
r=3

ans= fact(n)/ (fact(r)*fact(n-r))
print(ans)

