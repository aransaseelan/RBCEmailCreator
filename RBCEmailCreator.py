with open('RBC CUSEC Name List.txt', 'r') as file:
    data = file.readlines() #readlines reads the file line by line and returns a list of strings
    print(data)
    firstnames = []
    lastnames = []
    for line in data: 
        parts = line.strip().split() #strip takes out the white spaces in the front and back, split takes out the white spaces in the middle
        if len(parts) >= 2:
            firstnames.append(parts[0])
            lastnames.append(parts[1])

with open('RBCEmail.txt', 'w') as output_file:
    for i in range(len(firstnames)):
        output_file.write(firstnames[i] + "." + lastnames[i] + "@rbc.com" + "\n")

# Move the print statement outside the loop
with open('RBCEmail.txt', 'r') as output_file:
    output = output_file.read()
    print(output)


#Email is formated first.last@rbc.com