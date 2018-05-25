##John Farrell
##DSS615
##Assignment 2

#pp 31-35 Exercises 1-60 odd, 61, 63, 64, 68, 69, 72, 73, 77, 78
print("pp 31-35 Exercises 1-60 odd, 61, 63, 64, 68, 69, 72, 73, 77, 78")
print("1.",3 * 4)
print("3.", 1/(2 ** 3))
print("5.", (5 - 3) * 4)
print("7.", 7//3)
print("9.", 7 %3)
print("11.", 5//5)
print("13. sales.2008 is not a valid variable name")
print("15. fOrM_1040 is a valid variable name")
print("17. expenses? is not a valid variable name")

#19 - 31
a = 2
b = 3
c = 4
print("19. (a * b) + c =", (a * b) + c)
print("21. (1 + b) * c =", (1 + b) * c)
print("23. b ** (c - a)", b ** (c - a))
print("25. 7 * 8 + 5 =", 7 * 8 + 5)
print("27. 5.5% of 20 =", 20 * .055)
print("29. 17(3+162) =", 17 * (3+162))
print("31.")
print("\t\tx\ty")
print("x=2\t\t2\tNA")
print("y=3*x\t\t2\t6")
print("x=y+5\t\t11\t6")
print("print(x+4)\t11\t6")
print("y=y+1\t\t11\t7")

#33
print("33.")
a = 4
b = 5 * a
print(a + b)

#35
print("35.")
num = 5
num *= 2
print(num)

#37
print("37.")
totalMinutes = 135
hours = totalMinutes // 60
minutes = totalMinutes % 60
print(hours, minutes)

print("39. Error is a + b = c, for this to be correct it will need to be c = a + b")
print("41. Error is 0.05 = interest, for this to be correct it will need to be interest = 0.05")
print("43. ", int(10.75))
print("45. ", abs(3-10))
print("47. ", round(3.1279,3))

#49 - 54
a = 5
b = 3
print("49. int(-a/2) =", int(-a/2))
print("51. abs(a - 5) =", abs(a - 5))
print("53. round(a + .5) =",round(a + .5))

#55-60
print("55. cost = cost + 5 is the same as cost += 5")
print("57. cost = cost / 6 is the same as cost /= 6")
print("59. sum = sum % 2 is the same as sum %= 2")

#61
revenue = 98456
costs = 45000
profit = revenue - costs
print("61. Profits =", profit)

#63
price = 19.95
discountPercent = 30
markdown =  (discountPercent / 100) * price
price -= markdown
print("63. Discounted Price =", round(price, 2))

#64
fixedCosts = 5000
pricePerUnit = 8
costPerUnit = 6
breakEvenPoint = fixedCosts / (pricePerUnit - costPerUnit)
print("64. The break-even point =", breakEvenPoint)

#68
purchasePrice = 10
sellingPrice = 15
percentProfit = ((sellingPrice - purchasePrice) / purchasePrice) * 100
print("68. The percent profit =", percentProfit,"%")

#69
perArceCorn = 18
farmSize = 30
cornProducedFarm = perArceCorn * farmSize
print("69. If farms on average produce", perArceCorn, "tons of corn per acre, a", farmSize, "acre farm will produce", cornProducedFarm, "tons of corn.")

#72
#Set variables
totalMiles = 233
dcDeparture = 2
nycArrival = 7
#calculate the time it took to travel between each point
timeTraveled = nycArrival - dcDeparture
#Calculate the average speed for the full trip
avgSpeed = totalMiles / timeTraveled
print("72. The average miles per hour of a trip leaving Washington D.C. at", dcDeparture,"O'Clock and arriving at NYC at",nycArrival,"O'Clock is", avgSpeed)

#73
#set variables
avgWaterPerPersonPerDay = 1600
usPopulation = 315000000
daysYear = 365
#calculate total water usage per year for all of US
totalUsWaterUsagePerYear = (avgWaterPerPersonPerDay * daysYear) * usPopulation
print("73. The total water Usage per year in the United States is", totalUsWaterUsagePerYear, "gallons")

#77
#Set variables
usDebt = 1.68e+13
usPop = 3.1588e+8
#calculate per capita
perCapDebt = round(usDebt/usPop)
print("77. The Per Capita Debt in the United States is $", perCapDebt)

#78
#set variables
calPerCubicFoot = 48600
feetPerMile = 5280
#Calculate the feet per cubic mile
feetCubicMile = feetPerMile ** 3
#Caliculate teh calories per cubic mile
calPerCubicMile = feetCubicMile * calPerCubicFoot
print("78. There are", calPerCubicMile, "calories in 1 cubic mile of ice cream.")


#pp 43-49 Exercises 1-92 odd, 97, 100, 102, 107, 110, 111
print("pp 43-49 Exercises 1-92 odd, 97, 100, 102, 107, 110, 111")

#pp 54-56 Exercises 1-53 odd, 55, 57, 58
print("54-56 Exercises 1-53 odd, 55, 57, 58")

#pp 66-71 Exercises 1-100 odd, 101, 102, 103
print("pp 66-71 Exercises 1-100 odd, 101, 102, 103")

#pp 74-76  Programming Projects 1-6
print("pp 74-76  Programming Projects 1-6")
