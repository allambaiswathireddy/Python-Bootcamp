#find the elements present in k+n  index

#test case 1
#k=3 ,n=2
#3 6 8 4 61 2
#output=2

#test case 2
#k=3,n=4
#80 70 54 36 72
#output=error

#n=int(input())
#k=int(input())
#len=0
#ans=0
#if(len<k+n):
#    print("error")
#else:
#   for i in range(1,k):
#        for j in range(1,n):
#            ans=k[i]+n[i]
#    print(ans)


n=int(input())
k=int(input())
len=0
list=list(map(int,input().split(",")))
if(len<k+n):
    print("error")
else:
    for i in range(len(list)):
        print(list[k+n],end=" ")
        break