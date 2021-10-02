# If - Else Statement
age = int(input("Enter Your Age: "))

if age >= 18:
    print("You're allowed")
else:
     print("You're not allowed")
     
# Elif Statement
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Ladke ne Bohot padhai Kiya hai")
elif marks >= 80:
    print("Ladka Kidhar toh kum padh gaya")
elif marks >= 70:
    print("Ladke ne machaya")
elif marks < 60:
    print("Bewafa")
elif marks < 40:
    print("Ladke ne Hag diya")
else:
    print('Enter the value between 0 - 100.')
    
# List - (Array) & Operators & Functions
fruits =  ['Apple', 'Orange', 'Mango',]
print(fruits[0])

fruits[0] = "Guava"   # Accessing
print(fruits)

vege = ['Coriander', 'Cauliflower']
print(vege*2)

print(fruits + vege)  # Concatinate

# List Functions
fruits.append('Pineapple')
print(fruits)

fruits.insert(1,"Grapes")
print(fruits)

print(fruits.index("Guava"))

print(len(fruits))

# Range
numbers = list(range(1,500,2))
print(numbers)

# Functions
def func1():        # Declaring Function
    print('Hello')
    a = int(input('Enter the value for a: '))
    b = int(input("Enter the value for b: "))
    
    c = a+b
    
    print("The Sum is ",c)
    
func1()  # Calling Functions


# For loop
for x in range(1,20):
    print(x)
    
# Use for loop to print even numbers
for y in range(0,21,2):
    print(y)
    
# Boolean Logic
user = "Atharva"
Pass = "Old"

if user == "Atharva" and Pass == "Old":
    print("Exist")
else: 
    print("Dead")
