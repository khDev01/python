print(result)# Creates two numbers that sum up to less than or equal 100
import random

operand1 = random.randint(1,100)
operand2 = random.randint(1,100)
theSum = operand1 + operand2

while theSum > 100:
	if operand1 >= 50:
		operand2 = random.randint(1,50)
	else:
		operand2 = random.randint(1,100)
	theSum = operand1 + operand2

result = operand1 + operand2
print(str(operand1) + " + " + str(operand2))
print(result)
print("-------------------------")
