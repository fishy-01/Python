# Creating a list of car brands
cars = ["toyota", "subaru", "mazda", "vw"]

# Creating a list of numbers
num = [6, 9, 78, 0, -8, 2, 79]

# Sorting the list of numbers
num.sort()

# Printing the list of car brands
print(cars)

# Replacing the second element of the 'cars' list with "nissan"
cars[1] = "nissan"

# Sorting the list of car brands
cars.sort()

# Printing a message that includes the second car brand
print(f"I love driving {cars[1]}")

#tuple, indexed,immutable(unchangable)
fruits=("mangoes" , "bananas", "apples")
print(fruits)
print(fruits[2])

#set
color={"yellow", "blue", "green"}
print(color)

#dictionaries

employees={"name":"Becky" , "age":20, "salary":1000000}
print(employees)
print(f"the age of {employees['name']} is {employees['age']}")