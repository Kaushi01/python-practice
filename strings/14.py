str= "  Ram    is    dancing on the floor"

str= str + " "

word= ""
for t in str:
    if t!=" ":
        word+=t
    elif t==" " and word!= "":
        print(word)
        word= ""

# print(word)


