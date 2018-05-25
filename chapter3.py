#Section 3.1

#Example 1
# print("Example 1")
# print(1 <= 1)
# print(1 < 1)
# print("car" < "cat")
# print("Dog" < "dog")
# print("fun" in "refunded")
# print()
# #Example 2
# print("Example 2")
# a = 4
# b = 3
# c = "hello"
# d = "bye"
# print((a+b) < (2 * a))
# print((len(c)-b) == (a/2))
# print(c < ("good" + d))
# print()
# #Example 3
# print("Example 3")
# list1 = [6, 4, -5, 3.5]
# list1.sort()
# print(list1)
# list2 = ["ha", "hi", 'B', '7']
# list2.sort()
# print(list2)
# print()
# #Example 4
# print("Example 4")
# list1 = [chr(177), "cat", "car", "Dog", "dog", "8-ball", "5" + chr(162)]
# list1.sort()
# print(list1)
# print()
# #Example 5
# print("Example 5")
# monarchs = [("George", 5), ("Elizabeth", 2), ("George", 6), ("Elizabeth", 1)]
# monarchs.sort()
# print(monarchs)
# print()
# #Example 6
# print("Example 6")
# n=4
# answ = "Y"
# print((2 < n) and (n < 6))
# print((2 < n) or (n == 6))
# print(not(n < 6))
# print((answ == "Y") or (answ == "y"))
# print((answ == "Y") and (answ == "y"))
# print(not(answ == "y"))
# print((2 < n) and (n == 5 + 1) or (answ == "No"))
# print((n == 2) and (n == 7) or (answ == "Y"))
# print((n == 2) and ((n == 7) or (answ == "Y")))
# print()
# print()
#
# #Section 3.2
# #Example 1
# print("Example 1")
# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# if num1 > num2:
#     largerValue = num1
# else:
#     largerValue = num2
# print("The larger value is", str(largerValue) + ".")
# print()
# #Example 2
# print("Example 2")
# answer = eval(input("How many gallons does a ten-gallon hat hold? "))
# if (0.5 <= answer <= 1):
#     print("Good, ", end="")
# else:
#     print("No, ", end="")
# print("it holds about 3/4 of a gallon.")
# #Example 3
# print("Example 3")
# firstNumber = eval(input("Enter first number: "))
# secondNumber = eval(input("Enter second number: "))
# thirdNumber = eval(input("Enter third number: "))
# max = firstNumber
# if secondNumber > max:
#     max = secondNumber
# if thirdNumber > max:
#     max = thirdNumber
# print("The largest number is", str(max) + ".")

# #Example 4
# print("Example 4")
# color = input("Enter a color (BLUE or RED): ")
# mode = input("Enter a mode (STEADY or FLASHING): ")
# color = color.upper()
# mode = mode.upper()
# result = ""
# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear View."
#     else:
#         result = "Clouds Due."
# else:
#     if mode == "STEADY":
#         result = "Rain Ahead."
#     else:
#         result = "Snow Ahead."
# print("The weather forecast is", result)

# #Example 5
# print("Example 5")
# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))
# if costs == revenue:
#     result = "Break Even."
# else:
#     if costs < revenue:
#         profit = revenue - costs
#         result = "Profit is ${0:,.2f}.".format(profit)
#     else:
#         loss = costs - revenue
#         result = "Loss is ${0:,.2f}.".format(loss)
# print(result)

# #Example 6
# print("Example 6")
# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# if num1 > num2:
#     print("The larger value is", str(num1) + ".")
# elif num2 > num1:
#     print("The larger value is", str(num2) + ".")
# else:
#     print("The two values are equal.")

# #Example 7
# print("Example 7")
# str1 = "Enter total earnings this year prior to current pay period: "
# ytdEarnings = eval(input(str1))
# curEarnings = eval(input("Enter earnings for the current pay period: "))
# totalEarnings = ytdEarnings + curEarnings
# socialSecurityBenTax = 0
# if totalEarnings <= 117000:
#     socialSecurityBenTax = 0.062 * curEarnings
# elif ytdEarnings < 117000:
#     socialSecurityBenTax = 0.062 * (117000 - curEarnings)
#
# medicareTax = 0.0145 * curEarnings
# if ytdEarnings >= 200000:
#     medicareTax += 0.009 * curEarnings
# elif totalEarnings > 200000:
#     medicareTax += 0.009 * (totalEarnings - 200000)
# ficaTax = socialSecurityBenTax + medicareTax
# print("FICA tax for the current pay period: ${0:0,.2f}".format(ficaTax))


# #Example 8
# print("Example 8")
# gpa = eval(input("Enter your gpa: "))
# if gpa >= 3.9:
#     honors = " summa cum laude."
# elif gpa >= 3.6:
#     honors = " magna cum laude."
# elif gpa >= 3.3:
#     honors = " cum laude."
# else:
#     honors = "."
# print("You graduated" + honors)

#Example 9
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
if num1.isdigit() and num2.isdigit():
    print("The sum is", str(eval(num1) + eval(num2)))
elif not num1.isdigit():
    if not num2.isdigit():
        print("Neither entry was a proper number.")
    else:
        print("The first entry was not a proper number.")
else:
    print("The second entry was not a proper number.")












#
