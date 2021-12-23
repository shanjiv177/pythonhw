"""
#Ask for how many marks the exam was conducted for
maxMarks = int(input("What is the maximum marks in each subject? : "))
# take in the marks of each subject
first = int(input("What is the marks in first subject? :"))
second = int(input("What is the marks in second subject? :"))
third = int(input("What is the marks in third subject? :"))
fourth = int(input("What is the marks in fourth subject? :"))

average = ((first + second +third + fourth)/(4*maxMarks))*100

if average>90:
    print("Your grade is A+")
elif average<90 and average>= 80:
    print("Your grade is A")
elif average<80 and average>= 70:
    print("Your grade is B")
elif average<70 and average>=60:
    print("Your grade is C")
else:
    print("Your Grade is D")
"""
#Ask for how many marks the exam was conducted for
maxMarks = int(input("What is the maximum marks in each subject? : "))
# take in the marks of each subject
first = int(input("What is the marks in first subject? :"))
second = int(input("What is the marks in second subject? :"))
third = int(input("What is the marks in third subject? :"))
fourth = int(input("What is the marks in fourth subject? :"))
#Check if entered marks are valid
boolean = True
while boolean == True:
    if first<= maxMarks and second<=maxMarks and third<=maxMarks and fourth <= maxMarks:
        average = ((first + second +third + fourth)/(4*maxMarks))*100

        if average>90:
            print("Your grade is A+")
            break
        elif average<90 and average>= 80:
            print("Your grade is A")
            break
        elif average<80 and average>= 70:
            print("Your grade is B")
            break
        elif average<70 and average>=60:
            print("Your grade is C")
            break
        else:
            print("Your Grade is D")
            break

    else:
        while first>maxMarks or second>maxMarks or third>maxMarks or fourth>maxMarks:
            yorn = input("Do you want to restart? : (Yes or NO) ")
            if yorn.lower() == "yes" or yorn.lower() == "y":
                maxMarks = int(input("What is the maximum marks in each subject? : "))
                first = int(input("What is the marks in first subject? :"))
                second = int(input("What is the marks in second subject? :"))
                third = int(input("What is the marks in third subject? :"))
                fourth = int(input("What is the marks in fourth subject? :"))
            else:
                boolean = False
                break
