# identifying variables 
first_name = "Jerrika"
last_name = "Barnett"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()} Would you like to learn some Python today?")

# Strings and changing case in a string
name = "Jerrika Barnett"
print(name.lower())
print(name.upper())
print(name.title())

# printing messages with quotations
message = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(message)

# Using variables in f-strings
famous_person = "Albert Einstein"
print(f'{famous_person} once said, "A person who never made a mistake never tried anything new."')

print("Languages")  

# add whitespace before output
print("\tLanguages") 

# list as new line
print("Languages:\nEnglish\nSpanish\nFrench") 

# list as new line and added whitespace
print("Languages:\n\tEnglish\n\tSpanish\n\tFrench") 

# how to take out whitespace
favorite_food = ' ice cream '
favorite_food.rstrip() # takes out whitespace on right end of string
' ice cream'
favorite_food.lstrip() # takes out whitespace on left end of string
'ice cream '
favorite_food.strip() # takes out whitespace on both sides of string
'ice cream'
