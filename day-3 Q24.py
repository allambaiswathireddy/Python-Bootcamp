#print the element in a particular index

#test case 1
#k=3
#3 6 8 4 61 2
#output=4

#test case=2
#k=8
#80 70 54 36 72
#output=36

k=int(input())
list=list(map(int,input().split(",")))
idx=k%len(list)
print(list[idx])