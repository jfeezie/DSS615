#John Farrell
#DSS615
#Assignment 1

##Python Shell Walkthrough
###Output for 1
print(2 + 3)

###Output for 2
print("Hello World")


##Python Code Editor Walkthrough

print(2+3)
for i in range(4):
    print("Hello World!")

##An Open a Program Walkthrough
###Display Presidents with a specific first name
firstName = input("Enter a first name: ")
foundFlag = False
infile = open("USPres.txt", 'r')
for line in infile:
    if line.startswith(firstName + ' '):
        print(line.rstrip())
        foundFlag = True
if not foundFlag:
    print("No president had the first name", firstName + '.')
