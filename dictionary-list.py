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
import os, time
personalData = {
}

while True: #re-arranged the program with the while loop scenario (implementing option [3])
    os.system("cls")
    print("Your Dictionary List"); print("Selection Menu") 
    print("1 -> Add an item")
    print("2 -> Search")
    print("3 -> Exit (y/n)")
    time.sleep(1)
    usr_Input = int(input("What program menu do you want to do? (1 / 2 / 3)\n\nYour answer here: "))
    if usr_Input == 1:
        print("Selecting No.1 would automatically create a new database for you stored on the main personalData - Contact Tracing")
        key_ID = str(input("Enter the name to be used as data storage (dictionary)\n\nYour answer here: "))
        # user input for the main info
        usr_valName = str(input("\n\nFull Name: ")) 
        usr_valSex = str(input("\nYour Sex (M / F): ")) 
        usr_valBD = str(input("\nYour Birthday (mm/dd/yyyy): "))
        usr_valAge = int(input("\nYour Age: "))
        usr_valAdd = str(input("\nYour Address: "))
        usr_valPN = int(input("\nYour Phone Number: "))
        usr_valEA = str(input("\nYour E-Mail Address: "))
        usr_valCS = str(input("\nYour Nationality: "))
        usr_valNN = str(input("\nYour Civil Status: "))
        usr_valVac = str(input("\nCOVID-19 Vaccination Status: "))
        usr_valRate = str(input("\nComorbidity: "))
        # this function increments a new database dictionary inside the personalData main dictionary
        personalData[key_ID] = {f"Full Name" : usr_valName, "Sex" : usr_valSex, "Birthday" : usr_valBD, "Age" : usr_valAge, "Sex" : usr_valSex, "Address" : usr_valAdd, "Phone Number" : usr_valPN, "E-Mail Address" : usr_valEA, "Civil Status" : usr_valCS, "Nationality" : usr_valNN, "COVID-19 Vaccination Status" : usr_valVac, "Comorbidity" : usr_valRate}
        # program nested dictionary is now updated, appended, and is working.
        print("Your Contact-Tracing Information has been saved.")

    if usr_Input == 2:
        var_Access = input("Enter the dictionary name you want to access the data from\n\nYour answer here: ")
        print(personalData[key_ID]["Full Name"])
        print(personalData[key_ID]["Sex"])
        print(personalData[key_ID]["Address"])
        print(personalData[key_ID]["Phone Number"])
        print(personalData[key_ID]["E-Mail Address"])
        print(personalData[key_ID]["Civil Status"])
        print(personalData[key_ID]["Nationality"])
        print(personalData[key_ID]["COVID-19 Vaccination Status"])
        print(personalData[key_ID]["Comorbidity"])

    if usr_Input == 3:
        usr_Ask = input("Do you wish to continue? (y/n)\n\nYour answer here: ")
        if usr_Ask == "y" or "yes":
            continue;
        elif usr_Ask == "n" or "no":
            break;