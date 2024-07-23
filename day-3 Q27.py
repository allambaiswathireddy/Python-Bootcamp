#replace the elements in an array with avg of max and min element

#test case 1
#13 2 67 20 68
#output=35 35 35 35 35
list=list(map(int,input().split(",")))
max=list[0]
min=list[0]
avg=0
for i in range(len(list)):
    if(list[i]>max):
        max=list[i]
    elif(list[i]<min):
        min=list[i]
    avg=(max+min)//2
for i in range(len(list)):
    list[i]=avg
print(list)
