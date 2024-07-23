#check whether given number is palindrome or not using while loop

n=int(input())
ori=n
rev=0
while(n>0):
    a=n%10
    rev=rev*10+a 
    n=n//10
if( ori == rev):
    print("yes")
else:
    print("no")