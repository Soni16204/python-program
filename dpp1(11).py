#Calculate factorial of a number using a while loop
n=int(input("enter any number:"))
f=1
while(n>=1):
    f*=n
    n-=1
print("factorial is",f)