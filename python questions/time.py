#hr= 15
#min= 56
#sec= 45

hr=int(input())
min=int(input())
sec=int(input())

if hr==0:
    print(f"{12}:{min}:{sec} AM")
elif hr<12:
    print(f"{hr}:{min}:{sec} AM")
elif hr>12:
    print(f"{hr-12}:{min}:{sec} PM")
elif hr==12:
    print(f"{hr}:{min}:{sec} PM")


