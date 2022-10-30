string=str(input("enter the word:"))
oddcharacters=""
n=len(string)
for x in range(0,n):
    if(x%2!=0):
        oddcharacters=oddcharacters+string[x]
print(oddcharacters)
        
