amount_of_numbers = int(input("How money numbers do want to add? \n"))
num = 0
sum = 0
for i in range(amount_of_numbers):
    num +=1
    sum = sum + num
print(sum)

# Or it can be like this
n = int(input("Enter number : \n"))
total =int( (n*(n+1))/2)
print(total)

