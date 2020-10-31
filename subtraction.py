# Creates two numbers that subtract to more than or equal 0 
import random

operand1 = random.randint(1,100)
operand2 = random.randint(1,100)
theDifference = operand1 - operand2

while theDifference < 0:
	if operand1 >= 50:
		operand2 = random.randint(1,50)
	else:
		operand2 = random.randint(1,100)
	theDifference = operand1 - operand2

result = operand1 - operand2
print(str(operand1) + " - " + str(operand2))
print(result)
