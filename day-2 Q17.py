#you are given with a space seperated interger list find number of even and odd elements in a given list
n=list(map(int,input().split(",")))
count=0
even_var=0
odd_var=0
for i in range(0,len(n)):
    if(n[i]%2==0):
        even_var+=1
    else:
        odd_var+=1
print(even_var)
print(odd_var)