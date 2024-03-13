x = int(input("Enter number\n"))
for i in range(x+1):
    i = i-x
    print(i*"*", end="")
    
    for j in range(i):
        print(j*"*" , end="")