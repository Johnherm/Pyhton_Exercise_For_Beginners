# How to find average of N numbers?

input_number = int(input("How money numbers do you want to find their average?\n"))
amount_of_numbers = 0
print(" Please write different integers and enter it each number you write:\n")
for i in range (input_number):
    numbers = int(input())
    amount_of_numbers +=1
    average = numbers/amount_of_numbers
print(f"The average of you entered number is \n{average}")