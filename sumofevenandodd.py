"""#Inputs
n = int(input("Enter a number :"))

#Logic

sumOfEvenNumbers = n*(n+1)
sumOfOddNumbers = n*n

#Output

print(f"Sum of even numbers upto {n} = {sumOfEvenNumbers}")
print(f"Sum of odd numbers upto {n} = {sumOfOddNumbers}") """
#Inputs
n = int(input("Enter a number :"))
yorn = input("Do you want to include the number too?: (yes or no)")
if yorn.lower() == "yes" or yorn.lower() == "y":
    if n%2 == 0:
        sumOfEvenNumbers = n
        sumOfOddNumbers = 0
    else:
        sumOfOddNumbers = n
        sumOfEvenNumbers = 0
else:
    sumOfOddNumbers = 0
    sumOfEvenNumbers = 0

#Logic 
for i in range (0, n ):
    if i%2 == 0:
        sumOfEvenNumbers += i
    else:
        sumOfOddNumbers += i
        

#Output
print(f"Sum of even numbers upto {n} = {sumOfEvenNumbers}")
print(f"Sum of odd numbers upto {n} = {sumOfOddNumbers}")
