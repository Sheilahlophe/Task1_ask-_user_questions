# Ask the name of the user (str)
name = input("enter your name" + ":")

# Ask the age of the user
age = int(input("enter youe age" + ":"))

# Ask the height in cm
height_cm = float(input("enter your height in cm" + ":"))

# Ask their favourite number
favourite_number = int(input("Enter your favourite number" ":"))

# Calculate their birth year
birth_year = 2026 - age

# Calculate their height in metre
height_m = height_cm / 100

# Calculate their number squared
number_squared = favourite_number **2

# Print neatly formatted profile card
#Can be printed in different ways, I have included the 2 ways 
print("\n===== PERSONAL PROFILE =====")
print(f"{name} {age} {height_cm} {height_m} {favourite_number} {number_squared} {birth_year}")

#This the second way of printing
print("\n===== PERSONAL PROFILE =====")
print("Name:", name)
print("Age:", age)
print("Height in cm:", height_cm)
print("Height in metres:", height_m)
print("Favourite number:", favourite_number)
print("Favourite number squared:", number_squared)
print("Year born:", birth_year)




