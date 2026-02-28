#even number check div by 8 , or if num is odd check div by 5
n= int(input())

if n%2==0:
    print('even')
    if n%8==0:
      print("even and div by 8")
    else:
      print("condition1 satisfied")


if n%2!=0:
    print('odd')
    if n%5==0:
      print("odd and div by 5")
    else:
     print("condition 2 satisfied")

