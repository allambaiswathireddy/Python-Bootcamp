#sum of all the numbers in a list by using for loop
n=list(map(int,input().split("@")))
sum=0
for i in n:
    sum+=i
    print(sum)