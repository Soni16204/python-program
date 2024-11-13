#Find the first occurrence of a number in a list using a while loop
num=[1,2,3,4,3,5]
target=3
index=0
found=-1
while index< len(num):
    if num[index]==target:
        found=index
        break
    index+=1
print("first occurence of",target, "is at index:",found)


       
