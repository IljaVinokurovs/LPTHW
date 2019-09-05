numbers = []
def loop (number1, number2):
	i = 0
	while i < number1:
		print(f"At the top i is {i}")
		numbers.append(i)
		i = i + number2
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
		
	print("The numbers: ")

	for num in numbers:
		print(num)

loop(7, 3)

print("\n\n\n\n")

number1 = 5
number2 = 1
numbers = []
for x in range(number1):

	print(f"At the top x is {x}")
	numbers.append(x)
	x = x + number2
	print("Numbers now: ", numbers)
	print(f"At the bottom x is {x}")
		
print("The numbers: ")

for num in numbers:
	print(num)