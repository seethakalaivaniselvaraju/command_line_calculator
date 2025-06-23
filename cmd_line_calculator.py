def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    try:
        a=int(input("Enter the first value:"))
        b=int(input("Enter the second value:"))
    except ValueError:
        print("Please Enter valid Integer Value")
        continue
    try:
        operation = int(input(
            "Enter your choice\n"
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "Your Choice: "
        ))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue
    if operation==1:
        print(f"{a}+{b}={add(a,b)}")
    elif operation==2:
        print(f"{a}-{b}={sub(a,b)}")
    elif operation==3:
        print(f"{a}*{b}={mul(a,b)}")
    else:
        try:
            if b == 0:
                raise ZeroDivisionError
            print(f"{a}/{b}={div(a,b)}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
    choice=input(("Do you want to exit(y/n)"))
    choice=choice.lower()
    if choice=='n':
        continue
    else:
        print("Thank you for using the Command line calculator")
        break


    