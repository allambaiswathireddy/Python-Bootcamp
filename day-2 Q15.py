#you are given with a comma seperated natural numbers 1 to 10 print only the even numbers
n=list(map(int,input().split(",")))
for i in range(1,len(n),2): #it works only if we have natural numbers
    print(n[i],end=" ")
    