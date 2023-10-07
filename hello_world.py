# Ask for the user's name
name = input("What is your name? ")

# Ask for the user's year of birth and convert it to an integer
birth_year = int(input("What year were you born? "))

# Greet the user with their name
print(f"Hello, {name}!")

# Get the current year
from datetime import datetime
this_year = datetime.now().year
    
# Calculate the age by subtracting the year of birth from the current year
age = this_year - birth_year

# Print the user's age
print(f"You must be {age} years old.")

# Say goodbye
print("Goodbye!")