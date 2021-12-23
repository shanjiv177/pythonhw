#Inputs

num = int(input("Enter the number: "))
rev_num = 0
#Logic

while num != 0:
    rem = num%10
    rev_num = rev_num*10 + rem
    num = num//10

#Outputs

print(rev_num)