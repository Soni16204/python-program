#Find the average of numbers in a list using a for loop
num=int(input("enter the number of elements to be inserted:"))
sum=0
for i in range(0,num):
    elem=int(input("enter element:"))
sum=sum+elem
average=sum/num
print("average element in the list:")

a=[3,5,7,8,9]
for i in a:
    avg=sum(a)/len(a)
    print(avg)
