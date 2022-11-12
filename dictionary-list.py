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
    os.system('cls')
    print("\033[0;33;1mYour Dictionary List\033[0m\n"); print("\033[31mSelection Menu\033[0m") 
    print("\033[36m1 ->\033[0m \033[3mAdd an item\033[0m")
    print("\033[36m2 ->\033[0m \033[3mSearch\033[0m")
    print("\033[36m3 ->\033[0m \033[3mExit (y/n)\033[0m")
    time.sleep(1)
    usr_Input = int(input("\nWhat program menu do you want to do? (\033[36m1 / 2 / 3\033[0m)\n\nYour answer here:\033[36m "))
    if usr_Input == 1:
        os.system('cls')
        print("\033[0mSelecting No.1 would automatically create a new database for you stored on the main personalData - Contact Tracing")
        key_ID = input("Enter the name to be used as data storage (dictionary)\n\nYour answer here: ")
        os.system('cls')

        # user input for the main info
        usr_valName = input("Full Name: ")
        usr_valSex = input("\nYour Sex (M / F): ")
        usr_valBD = input("\nYour Birthday (mm/dd/yyyy): ")
        usr_valAge = input("\nYour Age: ")
        usr_valAdd = input("\nYour Address: ")
        usr_valPN = input("\nYour Phone Number: ")
        usr_valEA = input("\nYour E-Mail Address: ")
        usr_valCS = input("\nYour Nationality: ")
        usr_valNN = input("\nYour Civil Status: ")
        usr_valVac1 = input("\nCOVID-19 Vaccination Status (Dose - Booster) for ex.(2 - 1) <- 2nd Dose, 1st Booster: ")
        usr_valVac2 = input("\nType of COVID-19 Vaccine ex. (Sinovac-Coronavac - Pfizer): ")
        usr_valRate = input("\nComorbidity: ")
        usr_valCT1 = input("\nHave you been tested for COVID-19 in the past working 14 days? (Yes / No): ")
        usr_valCT2 = input("\nHave you been diagnosed with COVID-19 on the past working 14 days? (Yes / No): ")
        usr_valCT3 = input("\nAny symptoms present back from 2 days (48 hours) such as coughing, fevers, fatigue, muscle or body ache, loss of taste and smell, sore throat, nausea or vomiting, and/or diarrhea?  (Yes / No): ")
        usr_valCT4 = input("\nClose contact with person diagnosed as positive or any presence of COVID-19 symptoms on the last 10 days? (Yes / No): ")
        usr_valCT5 = input("\nHave you been quarantined on the last working 14 days? (Yes / No): ")

        # this function increments a new database dictionary inside the personalData main dictionary
        personalData[key_ID] = {"Full Name" : usr_valName, "Sex" : usr_valSex, "Birthday" : usr_valBD, "Age" : usr_valAge, "Address" : usr_valAdd, "Phone Number" : usr_valPN, "E-Mail Address" : usr_valEA, "Nationality" : usr_valNN,"Civil Status" : usr_valCS, "COVID-19 Vaccination Status" : usr_valVac1, "Vaccine Type" : usr_valVac2, "Comorbidity" : usr_valRate, "Tested for COVID-19" : usr_valCT1, "Diagnosed with COVID-19" : usr_valCT2, "Symptoms Present" : usr_valCT3, "Close Contact" : usr_valCT4, "Quarantine" : usr_valCT5}
        # program nested dictionary is now updated, appended, and is working.
        os.system('cls')
        print(f"Your Contact-Tracing Information named " + key_ID + " has been saved.\n")
        time.sleep(2)

    if usr_Input == 2: # option 2 completed with print() function
        var_Access = input("\033[0mEnter the dictionary name you want to access the data from\n\nYour answer here: ")
        os.system('cls')
        print("The stored data for " + var_Access + " has now been assessed.")
        #---------PERSONAL INFORMATION---------
        print("\n\033[0mPERSONAL INFORMATION\033[1m")
        print("Full Name: " + personalData[var_Access]["Full Name"])
        print("Sex: " + personalData[var_Access]["Sex"])
        print("Birthday: " + personalData[var_Access]["Birthday"])
        print("Age: " + personalData[var_Access]["Age"])
        print("Address: " + personalData[var_Access]["Address"])

        #---------CONTACT INFORMATION---------
        print("\n\033[1mCONTACT INFORMATION\033[0m")
        print("Phone Number: " + personalData[var_Access]["Phone Number"])
        print("E-Mail Address: " + personalData[var_Access]["E-Mail Address"])
        print("Nationality: " + personalData[var_Access]["Nationality"])
        print("Civil Status: " + personalData[var_Access]["Civil Status"])

        #---------COVID-19 TRACING INFORMATION---------
        print("\n\033[1mCOVID-19 TRACING INFORMATION\033[0m")
        print("COVID-19 Vaccination Status (n - n): " + personalData[var_Access]["COVID-19 Vaccination Status"])
        print("Type of Vaccine Used (n - n): " + personalData[var_Access]["Vaccine Type"])
        print("Comorbidity: " + personalData[var_Access]["Comorbidity"])
        print("Have been tested for COVID-19: " + personalData[var_Access]["Tested for COVID-19"])
        print("Have been Diagnosed with COVID-19: " + personalData[var_Access]["Diagnosed with COVID-19"])
        print("Symptoms Present: " + personalData[var_Access]["Symptoms Present"])
        print("Close Contact with Positive Individual: " + personalData[var_Access]["Close Contact"])
        print("Have been quarantined on the last 14 days: " + personalData[var_Access]["Quarantine"])
        usr_Ask = input(f"\nType n to exit option 2): ")
        if usr_Ask == "n":
            continue;

    if usr_Input == 3: # option 3 completed and is working properly within the while loop scenario
        usr_Ask = input("\033[0mDo you wish to continue? \033[36m(y/n)\033[0m\n\nYour answer here:\033[36m ")
        if usr_Ask == "y":
            print("\033[0m ")
            os.system('cls')
            continue;
        elif usr_Ask == "n":
            print("\033[0m ")
            os.system('cls')
            break;

print(personalData)
print("\n\n")