print("welcome to python calculator")

while True:
    print("\nSelect an operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice=input("Enter your choice: (1/2/3/4/5): ")

    if choice=="5":
        print("Thanks for using the python calculator! Goodbye.")
        break
    try:
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please try again.")
        continue


    if choice=="1":
        result = num1 + num2
        print(result)

    elif choice=="2":
        result = num1 - num2
        print(result)

    elif choice=="3":
        result = num1 * num2
        print(result)

    elif choice=="4":
        result = num1 / num2
        print(result)

    else:
        print("Invalid choice")


