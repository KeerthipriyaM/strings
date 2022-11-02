a=str(input("enter the string:"))
alphabets="abcdefghijklmnopqrstuvwxyz"
countlower=0
countupper=0
for x in alphabets:
    for y in a:
        if(x==y):
            countlower=countlower+1
        if(x.upper()==y):
            countupper=countupper+1
print(countlower)
print(countupper)
