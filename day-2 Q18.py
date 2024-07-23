#given an space seperated integer list find the avg of elements present in the even index
list=list(map(int,input().split(",")))
sum=0
count=0
n=len(list)
for i in range(len(list)):
    if(i%2==0):
        sum+=list[i]
        count+=1
print(sum/count)
        