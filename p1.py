#T1

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:",num1 + num2)
print("Subtraction:",num1 - num2)
print("Multiplication:",num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Error: Division by zero is not allowed.")



#T2

fn = input("Enter your first name:")
ln = input("Enter your last name:")

print("Hello," + fn + " " + ln + " " +'Welcome to the world of Python.')