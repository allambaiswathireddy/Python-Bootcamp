#find sum of all the elements in an array

list=list(map(int,input().split(",")))
sum=0
for i in list:
    sum+=i
print(sum)
    