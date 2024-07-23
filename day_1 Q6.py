n=int(input())
s=0
term=n
while(n>0):
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    s=s+fact
    n=n//10
if(s==term):
    print("strong number")
else:
    print("not a strong number")
    
    