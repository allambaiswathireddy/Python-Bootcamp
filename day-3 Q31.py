#find the sum of squares of a digit in a given number

n=int(input())
s=0
while(n>0):
    r=n%10
    s+=r*r
    n=n//10
print(s)