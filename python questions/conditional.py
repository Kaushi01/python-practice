n=2023 #2024, 2000, 2100

ans=(n%4==0 and n%100!=0) or (n%100==0 and n%400 == 0)

print (ans)

