#find the missing number in an array

#**very impo question
#this logic will work only for natural numbers and whole numbers
list=list(map(int,input().split(",")))
missing_number=0
sum=0
sum1=0
for i in range(1,11):
    sum+=i
for i in range(0,len(list)):
    sum1+=list[i]
missing_number=sum-sum1
print(missing_number)
