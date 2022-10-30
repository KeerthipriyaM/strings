a=str(input("enter the string:"))
count=0
b="aeiou"
for x in a:
    if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U") :
        count=count+1
print(count)
