num = 0
#user pick a number
pickNum = "Pick a number from 1 to 9:\n"
num = input(pickNum)
#how to ensure that user can only input the number 1-9
if num != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    print("fuck")
#explain first step
threenum= str(num) + str(num) + str(num)
three = "Ok, we're going to turn that into three digit which is: " + str(threenum) + "."
print(three)
#expain second
addNum = "\nOk, now we're going to add three of "+ str(num) + " together to find the second number!"
print(addNum)
#add them together
numtime3 = int(num) + int(num) + int(num)
nums = str(num) + "+" + str(num) + "+" + str(num) + " equal " + str(numtime3)
print(nums)
#Now divide three digits number by the second number
divideText = "Now next step is divide the three digit number by the number we got from adding each of the digits together.\n"
divideNum = int(threenum) / int(numtime3)
divide = str(threenum) + " divided by " + str(numtime3) + " is " + str(divideNum) + "!\n"
print(divide)
