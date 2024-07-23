#take a space seperated input from the user and print alternate elements in a list
n=list(map(int,input().split("@")))
for i in range(1,len(n),2):
    print(n[i],end=" ")