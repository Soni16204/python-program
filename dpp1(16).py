#Print numbers in a list until a negative number is encountered using a while loop:
num=[1,2,3,-1,4,5]
index=0
while(index<len(num)):
    if num[index] < 0:
        break
    print(num[index])
    index+=1
       