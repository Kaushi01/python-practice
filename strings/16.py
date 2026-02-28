str= "mukesh kumar ambani"

str= str+" "

word=""
for t in str:
    if t!=" ":
        word= word+t
    elif t==" " and word!= "":
        
        print(word[0].upper())
        word= ""


