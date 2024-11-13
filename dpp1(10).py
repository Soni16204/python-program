#print a pattern of star using nested for loop
n=int(input("enter the no of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end=" ")
    print()