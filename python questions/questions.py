
p=int(input("Enter principal"))
r=int(input("Enter Rate"))
t=int(input("Enter time"))

si=(p*r*t)/100
print(si)

amt=p*(1+r/100)**t
print(amt)

ci= amt - p
print(ci)


