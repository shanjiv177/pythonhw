"""num = (input("Enter the number: "))

if num == num[::-1]:
    print("It is a palindrome")
else:
    print("Not a palindrome")"""

#Inputs

num = int(input("Enter the number: "))
rev_num = 0
original_num = str(num)
#Logic

while num != 0:
    rem = num%10
    rev_num = rev_num*10 + rem
    num = num//10

#Outputs

if original_num == str(rev_num):
    print("It is a palindrome")
else:
    print("Not a palindrome")


