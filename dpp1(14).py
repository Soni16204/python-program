# find the prime number between 1 to 50 using nested for and if
for i in range(1,51):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
                print(i)
