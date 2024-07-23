n=int(input())
x="swimming"
y="badminton"
z="table tennis"
height=int(input())
weight=int(input())
body_fat=int(input())
x_medals=int(input())
if(height>=140 and weight>=n%2 and body_fat<12):
    print("y will travel")
    if(height>=118 and height<=140 and weight==x_medals and body_fat<12):
        print("z will travel")
        print("xyz will travel")
else:
    print("not travel")

        