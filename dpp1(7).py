#Find the largest number in a list using a for loop
a=[1,2,3,4,5,6,7,8]
largest=a[0]
for i in a:
    if i>largest:
        largest =i
print(largest)