#take a string and print all characters in the string which are vowels.
str= "Ramesh"
# a=0
# e=0
# i=0
# o=0
# u=0
for ch in str:
    if ch.lower() in ["a","e","i","o","u"]:
        print(ch)