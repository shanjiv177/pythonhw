nameList = []
ageList = []
MainList = []

boolean = True

while boolean == True:
    name = input("What is the person's name? :")
    age = int(input("What is the person's age (in numbers)?: "))

    nameList.append(name)
    ageList.append(age)

    yorn = input("Do you want to add an another person?: (yes or no)")
    if yorn.lower() == "yes" or yorn.lower() == "y":
        boolean = True
    elif yorn.lower() == "no" or yorn.lower() == "n":
        boolean = False

number = 0

for i in range(0, len(nameList)):
    if ageList[i]>18:
        MainList.append(nameList[i])
    
for i in range(len(MainList)):
    print(MainList[i])