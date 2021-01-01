print("My Calculator\n=================")
num1 = input("Enter the First Number: ")
num2 = input("Enter the Second Number: ")

operation = input("Please Choose operation: \n1.Add \n2.Sub \n3.Mul \n4.Div  \n(+,-,x,/)")

num1 = int(num1)
num2 = int(num2)

if operation == "+":
    print (num1 + num2)

elif operation == "/":
    print (num1 / num2)

elif operation == "x":
    print (num1 * num2)

elif operation == "-":
    print (num1 - num2)

else:
    print("use x,-,/ or + next time!")