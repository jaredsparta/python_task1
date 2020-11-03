# input are strings already and the names should be string, so no need to cast them
# the age should be an integer so i cast using int()
first_name = input("What's your first name? ").capitalize()
middle_name = input("If you have a middle name please input, otherwise leave blank -> ").capitalize()
last_name = input("What's your last name? ").capitalize()
age = int(input("How old are you? "))

# postcodes are usually written as full capitals so we used .upper() to ensure consistency in convention
address = input("What's the first line of your address? ").capitalize()
postcode = input("What's your post code? ").upper()

# again, NI numbers are written capitalised so we use .upper() to achieve the same
ni_no = input("What's your National Insurance number? ").upper()
course = input("What course did you apply for at Sparta Global? ").capitalize()
educ = input("What university education do you do? ").capitalize()


# these print statements will print out the information
# they are grouped in what i thought were similar categories
print("\nNAME:", first_name, middle_name, last_name, f"\n You are {age} years old")
print("You live at:", address, postcode)
print("You NI number is:", ni_no)
print("You applied for", course, "at Sparta and you studied", educ)