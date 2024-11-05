# create a program that checks whether a number is odd or even
# Get the input number from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd2
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


    # BMI CALCULATION
age = int(input("Enter your age: "))

if age >= 18 and age < 100:
    print("Valid to be a registered voter")
elif age <= 0:
    print("Not yet born")
elif age >= 100:
    print("Alien")
else:
    print("Too young to be a registered voter")

#BMI SYSTEM
weight = float(input("Enter the value of your weight in kilograms: "))
height = float(input("Enter the value of your height in meters: "))
BMI = weight / pow(height, 2)

print(f"The value of BMI is: {round(BMI, 2)}")

if BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI <= 24.9:
    print("You are of normal weight")
elif 25 <= BMI <= 29.9:
    print("You are overweight")
elif 30 <= BMI <= 39.9:
    print("You are obese")
elif BMI >= 40:
    print("You are severely obese")