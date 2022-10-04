height = float(input("Enter the height in cm: "))
weight = float(input("Enter the weight in kg: "))

BMI = weight / (height/100)**2

print(f"Your Body Mass Index is {BMI:.2f}")
if BMI <= 18.5:
    print("You are Underweight.")
elif BMI <= 24.9:
    print("You are Healthy.")
elif BMI <= 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")
