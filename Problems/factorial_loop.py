# Find factorial of a number

number = 5
factorial = 1

while number > 1:
    factorial *= number
    number -= 1

print(f'Factorial of {number}: ', factorial)
