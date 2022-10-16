# Program make a simple calculator

# This function adds two numbers
def add_num(x, y):
    return x + y

# This function subtracts two numbers
def subtract_num(x, y):
    return x - y

# This function multiplies two numbers
def multiply_num(x, y):
    return x * y

# This function divides two numbers
def divide_num(x, y):
    return x / y


print("Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter your choice: ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add_num(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract_num(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply_num(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide_num(num1, num2))
        
        next_cal = input("Want to do next calculation? (yes/no): ")
        if next_cal == "no":
          break
    
    else:
        print("Invalid Input")
