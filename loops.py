# while loop

num=2
while num<=15:
    print(f"loop: {num}")
    num+=3

#create a decremental while loop that initial 100 to zero with a difference of 5 each

num = 100
while num >= 0:
    print(f"loop: {num}")
    num -= 5  # Decrement num by 5

#for loop
name=["salmon", "eric", "David", "Moses", "Bravin"]

for i in name:
    print(i)

#sum of the elements

num=[10, 20,30,40,50,60,70,80,90,100]

total = 0
for n in num:
    total += n

print("The sum is:", total)

myschool="Dedan"
for m in myschool:
    print(m)

#even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []  # Initialize an empty list for even numbers

for num in numbers:
    if num % 2 == 0:
        even.append(num)
        print(even)  # Print the list each time an even number is added


