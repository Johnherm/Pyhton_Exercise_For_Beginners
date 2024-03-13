x = int(input("Enter number\n"))
for i in range(x+1):
    print(i*"*", end="")
    for j in range(i):
        print(j*"*")