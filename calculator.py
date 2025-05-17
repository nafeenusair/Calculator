print("Calculator")

while True:
    num1 = int(input())
    op = input()
    num2 = int(input())

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "%":
        print(num1 % num2)
    else:
        print("Wrong Input!")

    yesNo = input("Do you want to continue?y/n: ")
    if yesNo.lower() == "n":
        break