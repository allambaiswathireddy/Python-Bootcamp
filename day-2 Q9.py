my_list=list(map(int,input().split("@")))
for i in range(len(my_list)):
    print(my_list[i])
    print("\n-----")
for i in my_list:
    print(i,end=" ")
    