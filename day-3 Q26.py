#find the min element in a given list

list=list(map(int,input().split(",")))
min=list[0]
for i in range(len(list)):
    if(list[i]<min):
        min=list[i]
print(min)