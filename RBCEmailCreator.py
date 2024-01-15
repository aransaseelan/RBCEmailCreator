numberofPeople = int(input("How many people's emails do you need."))

firstnames = []
lastnames = []


for i in range(numberofPeople):
    firstnames.append(input("Please enter the firstname. \n"))
    lastnames.append(input("Please enter the lastname. \n"))


print("Here are your emails!!")
for i in range(numberofPeople):
    print(firstnames[i] + "." + lastnames[i] + "@rbc.com" + "\n")

#Email is formated first.last@rbc.com
