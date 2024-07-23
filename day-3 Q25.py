#find the max element in a given list

#test case 1
#12 23 36 44 45 57
#output=57

#test case 2
#56 78 -8 12 34 -99
#output=78


list=list(map(int,input().split(",")))
max=list[0]
for i in range(len(list)):
    if(list[i]>max):
        max=list[i]
print(max)