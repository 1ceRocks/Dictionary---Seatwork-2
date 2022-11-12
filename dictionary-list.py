# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# importing library for implementing additional features to the program
import os

# first and foremost, let's make a dictionary list for creating a stored value data within user input for back-end programming.
personalData = {
    "dataBase" : {
        "Full Name" : "IceRocks", 
        "Age" : 20, "Gender" : "M", 
        "Address" : "Manila, Philippines"
    } # random stored data for search (2 - option) labeled as reference
}

# next, of course, we want to make a display menu of options using print()
os.system("cls")
print("Your Dictionary List")
print("Selection Menu")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")

# let's now create the user-input program interface
os.system("cls")
usr_Input = int(input("What program menu do you want to do? (1 / 2 / 3)\n\nYour answer here: ")) # this would be the user-input for selecting between 1 , 2 , or 3.
if usr_Input == 1:
    print("Selecting No.1 would automatically create a new database for you stored on the main personalData - Contact Tracing")
    key_ID = str(input("Enter your name to be used as data storage (dictionary)\n\nYour answer here: "))
    # user input for the main info
    usr_valName = str(input("\n\nFull Name: ")); 
    usr_valAge = int(input("\nYour Age: ")); 
    usr_valSex = str(input("\nYour Sex (M / F): ")); 
    usr_valVac = str(input("\nCOVID-19 Vaccination Status: ")); 
    usr_valRate = str(input("\nComorbidity: "))
    # this function increments a new database dictionary inside the personalData main dictionary
    personalData[key_ID] = {f"Full Name" : {usr_valName}, "Age" : {usr_valAge}, "Sex" : {usr_valSex}, "COVID-19 Vaccination Status" : {usr_valVac}, "Comorbidity" : {usr_valRate}}
    print("Your Contact-Tracing Information has been saved.") # program nested dictionary is now updated, appended, and is working.
    print("\nHere's a brief summary of your input")