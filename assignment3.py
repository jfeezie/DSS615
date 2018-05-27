# #John Farrell
# #DSS615
# #Assignment 3
#
# #pp 86-89 Exercises 1-85 odd
# print("pp 86-89 Exercises 1-85 odd")
# print("1. ", chr(104) + chr(105))
# print("3. The letter before G is " + chr(ord('G') - 1) + ".")
# print("5.")
# list1 = [17, 3, 12, 9, 10]
# list1.sort()
# print("Minimum: ", list1[0])
# print("Maximum: ", list1[-1])
# print("7. ", end="")
# letter = 'D'
# print(letter + " is the " + str(ord(letter) - ord('A') + 1) + "th letter of the alphabet.")
# #Set variables for 9-19
# a = 2
# b = 3
# print("9.", 3 * a == 2 * b)
# print("11.", b <= 3)
# print("13.", a ** (5 -2) > 7)
# print("15.", (a < b) or (b < a))
# print("17.", not((a < b) and (a < (b + a))))
# print("19.", ((a ==b) and (a * a < b * b)) or ((b < a) and (2 * a < b)))
# print("21.", "9W" != "9w")
# print("23.", "Car" < "Train")
# print("25.", "99" > "ninety-nine")
# print("27.", ("Duck" < "pig") and ("pig" < "big"))
# print("29.", not(('B' == 'b') or ("Big" < "big")))
# print("31.", "ty" in "Python")
# print("33.", isinstance(32, float))
# print("35.", isinstance(32., float))
# print("37.", "colonel".startswith('k'))
# print("39.", "potato".endswith("oe"))
# print("41.", True or False)
# print("43.", not True)
# print("45. Equivalent")
# print("47. Not Equivalent")
# print("49. Equivalent")
# print("51. Equivalent")
# print("53. Equivalent")
# print("55. a <= b")
# print("57. (a >= b) and (c == d)")
# print("59. a > b")
# print("61. ans in ['Y', 'y', 'Yes', 'yes']")
# print("63.  2010 <= year <= 2013")
# print("65. 3 <= n < 9")
# print("67. -20 < n <= 10")
# print("69. ", end="")
# str1 = "target"
# print(str1.startswith('t') and str1.endswith('t'))
# print("71. ", end="")
# str1 = "ticket"
# print(str1.startswith('t') or str1.endswith('t'))
# print("73. ", end="")
# str1 = "Teapot"
# str2 = "Tea"
# print(str1.startswith(str2))
# print("75. ", end="")
# str1 = "Teapot"
# print(str1.endswith(str1[-4:]))
# print("77. ", end="")
# str1 = "spam and eggs"
# print(str1.startswith(str1[:len(str1) - 1]))
# print("79. ", end="")
# print(isinstance(25, float))
# print("81. ", end="")
# num = str(34)
# print(isinstance(num, int))
# print("83. ", end="")
# str1 = "5e-12"
# print(str1.isdigit())
# print("85. He said " + chr(34) + "How ya doin?" + chr(34) + " to me.")
# print()
#pp 98-104 Exercises 1-43 odd
# print("98-104 Exercises 1-43 odd")
# print("1. ", end="")
# num = 4
# if num <=9:
#     print("Less than ten.")
# elif num == 4:
#     print("Equal to four.")
# print("3. ", end="")
# print('a' < 'B' < 'c')
# print("5. ", end="")
# a = 5
# sentence = ""
# if ((3 * a) - 4) < 12:
#     sentence = "Remember, "
# print(sentence + "tomorrow is another day.")
# print("7. ", end="")
# a = 2
# b = 3
# c = 5
# if (a * b) < c:
#     b = 7
# else:
#     b = (c * a)
# print(b)
# print("9. ", end="")
# letter = input("Enter A, B, or C: ")
# letter = letter.upper()
# if letter == "A":
#     print("A, my name is Alice.")
# elif letter == "B":
#     print("To be, or not to be.")
# elif letter == "C":
#     print("Oh, say can you see.")
# else:
#     print("You did not enter a valid letter.")
# print("11. ", end="")
# a = 5
# if (a > 2) and ((a ==3) or (a < 7)):
#     print("Hi")
# print("13. ", end="")
# if "spam":
#     print("A nonempty string is true.")
# else:
#     print("A nonempty string is false.")
# print("15. There is a syntax and a logic error in this problem.  First the syntax error is the if statement should state n == 7.  Also, the logic error is in the calculation of the square.  It should be n**2.  Also, ideally the program should be determining if the input is a digit and providing feedback to the user in cases where the if statement is not met.")
# n = input("Enter a number: ")
# if n.isdigit():
#     n = eval(n)
#     if n == 7:
#         print("The square is", n ** 2)
#         print("The neagtive is", -n)
#     else:
#         print("The number we were hoping you entered was 7.")
# else:
#     print("You did not enter a valid nummber.")
# print("17. There is a syntax error in that or is captilized and the statement itself is written improperly.")
# major = "Computer Science"
# if (major == "Business") or (major == "Computer Science"):
#     print("Yes")
# print("19. a = 5")
# print("21.")
# print("if (j == 7):")
# print("\tb = 1")
# print("else:")
# print("\tb = 2")
# print("23. ", end="")
# answer = input("Is Alaska bigger than Texas and California Combined: ")
# answer = answer.upper()
# if (answer == "YES") or (answer == "Y"):
#     print("Correct")
# else:
#     print("Wrong")
# print("25.")
# #Determine bill amount and then compare the bill amount time .15 to 2.  If less then 2 the tip is $2.  If more then 2 the tip amount is the calculation.
# billAmount = eval(input("Enter Amount of bill: "))
# if ((billAmount * .15) < 2):
#     print("Tip is $2.00")
# else:
#     print("Tip is ${0:,.2f}".format(billAmount * .15))
# print("27.")
# #Determine the compare number of entered widgets to 100.  Then do the calculations as required less then 100 times by .25.  more then 100 times by .2.
# widgets = eval(input("Enter number of widgets: "))
# if (widgets < 100):
#     print("Cost is ${0:,.2f}".format(widgets * .25))
# else:
#     print("Cost is ${0:,.2f}".format(widgets * .20))
# print("29.")
# #Accept user input for the question.  Upper case the input.  Compare input to correct answer.  Output correct if matches and nice try if wrong.
# answer = input("Who was the first Ronald McDonald: ")
# if (answer.upper() == "WILLARD SCOTT"):
#     print("You are correct.")
# else:
#     print("Nice try.")
# print("31.")
# #Create a list of scores with user input.  Eiter sort list and remove lost score or remove lowest score from list with min.  Take the average of 2 remaining scores.
# scores = []
# scores.append(eval(input("Enter the first score: ")))
# scores.append(eval(input("Enter the second score: ")))
# scores.append(eval(input("Enter the third score: ")))
# scores.remove(min(scores))
# average = sum(scores) / 2
# print("The average of the two highest scores is {0:.2f}".format(average))
# print("33.")
# #Create inputs for pounds purchased and cash provided.  Times pounds by 2.5 and compare it to cash received.  If cash received is more then calculation then provide change.  If cash received is less then ask for more money.
# poundsApples = eval(input("Enter weight of apples in pounds: "))
# paymentReceived = eval(input("Enter payment in dollars: "))
# if ((poundsApples * 2.5) < paymentReceived):
#     print("Your change is ${0:,.2f}".format(paymentReceived - (poundsApples * 2.5)))
# else:
#     print("You owe ${0:,.2f} more".format((poundsApples * 2.5) - paymentReceived))
# print("35.")
# #Provide user with an input.
# #If length 1 and case is upper comply else does not comply
# #Determine if the input is a digit
# #If a digit then did not comply
# #If not a digit determine lenght of str
#
# letter = input("Enter a single uppercase letter: ")
# if (len(letter) == 1) and (letter == letter.upper()) and (not letter.isdigit()):
#     print("You complied with the request.")
# else:
#     print("You did not comply with the request.")

# print("37.")
# #Request time to be input as 0000 to 2359
# #Separate the input into hours and minutes
# #Determine AM or PM
# #calculate hours with %12
# #output combined hours, minutes AMPM in regular time
# militaryTime = input("Enter a military time (0000) to (2359): ")
# hours = int(militaryTime[0:2])
# minutes = militaryTime[2:4]
# if hours >= 12:
#     ampm = "pm"
#     hours %= 12
# else:
#     ampm = "am"
# if hours == 0:
#     hours = 12
# print("The regular time is {0}:{1}{2}".format(hours, minutes, ampm))
# print("39.")
# #Accept inputs from two banks with rates and periods
# #Perform calculation to APY for both
# #Compare which rate is best
# #output the rates for both banks with and the bank with the better rate
# rateOne = eval(input("Enter annual rate of interest for Bank One: "))
# periodsOne = int(input("Enter number of compounding periods for Bank One: "))
# rateTwo = eval(input("Enter annual rate of interest for Bank Two: "))
# periodsTwo = int(input("Enter number of compounding periods for Bank Two: "))
# rateOnePer = rateOne/100
# rateTwoPer = rateTwo/100
# apyOne = (((1 + ((rateOnePer/periodsOne))) ** periodsOne) - 1)
# apyTwo = (((1 + ((rateTwoPer/periodsTwo))) ** periodsTwo) - 1)
# print("APY for Bank One is {0:.3%}.".format(apyOne))
# print("APY for Bank Two is {0:.3%}.".format(apyTwo))
# if apyOne > apyTwo:
#     bestApy = "Bank One is the better bank."
# elif apyTwo > apyOne:
#     bestApy = "Bank Two is the better bank."
# else:
#     bestApy = "Bank One and Bank Two provide the same APY."
# print(bestApy)

# print("41.")
# #Accept a gpa input
# #determine if the grade is good enough to graduteself.
# #if not good enough to graudate display not good enough
# #if good enough to graduate check for honors
# #display graduate and relevant honor details
# gpa = eval(input("Enter your gpa (2 to 4): "))
# if not (2 <= gpa <= 4):
#     print("Invalid GPA average entered.  GPA must be between 2 and 4.")
# else:
#     if gpa >= 3.9:
#         honors = " summa cum laude."
#     elif gpa >= 3.6:
#         honors = " magna cum laude."
#     elif gpa >= 3.3:
#         honors = " cum laude."
#     else:
#         honors = "."
#     print("You graduated" + honors)


# print("43.")
# #Get taxable income
# #If income less then 20000 set tax rate to .2 * income
# #if greater then or equal to 20000 check to see if less then 50000 or greater the 50000
# #less then 5000 set rate to 400 + .25 * (income - 25000)
# #greater then set to 1150 + .35 * (income - 50000)
# #Print outcome
# taxableIncome = eval(input("Enter your taxable income: "))
# if taxableIncome < 20000:
#     taxAmount = .2 * taxableIncome
# else:
#     if taxableIncome < 50000:
#         taxAmount = 400 + .25 * (taxableIncome - 25000)
#     else:
#         taxAmount = 1150 + .35 * (taxableIncome - 50000)
# print("Your tax is ${0:,.2f}".format(taxAmount))
# print()


#pp 111-117 Exercises 1-31 odd
print("pp 111-117 Exercises 1-31 odd")
print("1. 24")
print("3. 10")
print("5. ", end ="")
list1 = [2, 4, 6, 8]
total = 0
while list1:
    total += list1[0]
    list1 = list1[1:]
print(total)
print("7.")
print("a")
print("b")
print("c")
print("d")
print("9. It is an infinite loop")
print("11. i would need to be -1 or remove the -1 from the while statement.")





#pp 127-136 Exercises 1-83 odd

#pp 139-142  Programming Projects 1-8
