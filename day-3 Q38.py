#find the sum os squares of given number

n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)
