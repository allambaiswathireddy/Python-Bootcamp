#*find peak element in an array
list=list(map(int,input().split()))
for i in range(0,len(list)):
   if(list[i-1]<list[i]>list[i+1]):
##if (arr[i]>= arr[i - 1] and arr[i]>=arr[i + 1])
     print(list[i])

