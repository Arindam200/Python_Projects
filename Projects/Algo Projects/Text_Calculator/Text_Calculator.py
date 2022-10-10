print("Welcome to Caalculator")
print('''
+ for addition
- for subtraction
* for multiplication
/ for division
''')
Num1= int(input("Choose the first number: "))
Num2= int(input("Choose the second number: "))
method= input("Choose the method you want to apply[+|-|*|/]: ")
if method=='+':
    print(Num1+Num2)
elif method=='-':
    print(Num1-Num2)
elif method=='*':
    print(Num1*Num2)
elif method=='/':
    print(Num1/Num2)
else:
    print("Please Choose a above mentioned method[+,-,*,/]")
