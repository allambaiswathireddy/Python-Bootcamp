#reverse of a number

#n=int(input())
#r = int(str(n)[::-1])
#print(r)

#or

n=int(input())
rev=""
while(n>0):
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))

