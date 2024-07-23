#how many even numbers are there in the above question
n=list(map(int,input().split(",")))
count=0
for i in range(1,len(n),2):
    count+=1
print(count)