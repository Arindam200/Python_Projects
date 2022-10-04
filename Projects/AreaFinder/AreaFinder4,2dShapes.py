#purpose: to find the area of the desired 2d shape selected by the user
#updates: 
    #1. 2022-10-04 09:12:41 : created this project
    #2. 2022-10-04 09:51:11 : completed the project



#my details

print("----------------")
print("created by: ")
print("https://github.com/ChefYeshpal")
print("for: hacktober")
print("----------------")

#for adding, subtracting, multiplying, and dividing
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("---------------------")

print("Select the shape whose area you want to find.")
print("1.Square")
print("2.Rectangle")
print("3.Triangle")
print("4.Circle")

print("---------------------")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    print("---------------------")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter Height/Radius : "))
        num2 = float(input("Enter Length/Base : "))

        print("---------------------")

        if choice == '1':
            print("The area of your square is", ((num1)**2))

        elif choice == '2':
            print("The area of your rectangle is", num1*num2)

        elif choice == '3':
            print("The area of the triangle is", 1/2*num1*num2)         #1/2*h*b

        elif choice == '4':
            print("The area of your circle is", 22/7*((num1)**2))        #pi*r(sq)
        print("---------------------")
        break

        
    else:
        print("Invalid Input")
