a=100

def hello():
    global a
    a= 500
    print("inside", a)

hello()
print("outside", a)