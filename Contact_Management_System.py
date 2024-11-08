import csv
import re

'''
checkExistence() is used to check whether the contact is already
exist or not. It take contact name as parameter because as we saw
in the mobile phones, we can't save one or more contact's with
same name but we can save same numbers by using different names.
'''
def checkExistence(name):
    try:
        data = []
        with open("contacts.csv","r") as file:
            reader = csv.reader(file)
            for i in reader:
                data.append(i)
        for i in data:
            if i[0] == name:
                return False
        return True
        
    except Exception as e:
        print(f"Error Occured : {e}")


# addContact() is used to add new contact.
def addContact():
    data = [None, None]
    data[0] = input("enter name : ")
    data[1] = input("enter contact number : ")
    while(not phoneNumberValidation(data[1])):
        print("You've entered invalid phone number.")
        data[1] = input("enter correct contact number : ")
    try:
        with open("contacts.csv","a",newline="") as file:
            if(checkExistence(data[0])):
                add = csv.writer(file)
                add.writerow(data)
            else:
                print("Contact already exists!!")
    except Exception as e:
        print(f"Error Occured : {e}")
        

# display() is used to print contact information in some design format.
def display(row):
    n = len(row[0])
    m = len(row[1])
    print(f"{(n+3)*'-'}{(m+2)*'-'}")
    print(f"|{'Name'.ljust((n+1),' ')}|{'Contact'.ljust((m+1),' ')}|")
    print(f"{(n+3)*'-'}{(m+2)*'-'}")
    print(f"|{row[0].ljust((n+1),' ')}|{row[1].ljust((m+1),' ')}|")
    print(f"{(n+3)*'-'}{(m+2)*'-'}")
    

# searchContact() is used to search the contact whether it exists or not.
def searchContact():
    name = input("enter name : ")
    contacts = []
    try:
        with open("contacts.csv","r") as file:
            reader = csv.reader(file)
            for i in reader:
                contacts.append(i)

        flag = True
        for i in contacts:
            if i[0] == name:
                display(i)
                flag = False
                break
        if flag:
            similarContacts =[]
            n = 0
            for i in contacts:
                if name in i[0]:
                    similarContacts.append(i)
                    x = len(i[0])
                    if x > n:
                        n = x 
                    
            if similarContacts == []:
                print(f"'{name}' contact is not exist.")
            else:
                m = 17
                print(f"\nContacts similar to '{name}' list below.")
                print(f"{(n+3)*'-'}{(m+2)*'-'}")
                print(f"|{'Name'.ljust((n+1),' ')}|{'Contact'.ljust((m+1),' ')}|")
                print(f"{(n+3)*'-'}{(m+2)*'-'}")
                for i in similarContacts:
                    print(f"|{i[0].ljust((n+1),' ')}|{i[1].ljust((m+1),' ')}|")
                    print(f"{(n+3)*'-'}{(m+2)*'-'}")
        
    except Exception as e:
        print(f"Error Occured : {e}")


# getDataIndex(name) is used to get the index of a particular contact name in contact dataset. This function is helpful in update operation.       
def getDataIndex(name):
    data = []
    try:
        with open("contacts.csv","r") as file:
            reader = csv.reader(file)
            for i in reader:
                data.append(i)
        for i in range(len(data)):
            if data[i][0] == name:
                return i
        return -1
    except Exception as e:
        print("Error Occured : {e}")
    


# updateContact() is used to update contact information.
def updateContact():
    data = []
    try:
        with open("contacts.csv","r") as file:
            reader = csv.reader(file)
            for i in reader:
                data.append(i)
                
        name = input("enter name : ")
        index = getDataIndex(name)
        if (index != -1):
            print("Which field you want to update?")
            print("1. Name")
            print("2. Contact Number")
            flag = True
            while(flag):
                choice = input("please enter your choice(1 or 2) : ")
                if choice == "1":
                    data[index][0] = input("enter new name : ")
                    flag = False
                elif choice == "2":
                    data[index][1] = input("enter new contact number : ")
                    flag = False
                else:
                    print("Wrong Choice!! Please make choice again.\n")
            with open("contacts.csv","w",newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print("Contact Updated Successfully!!")
        else:
            print(f"'{name}' contact is not exists.")
    except Exception as e:
        print("Error Occured : {e}")

# displayAll() is used to print all contacts in design format 
def displayAll():
    try:
        maxNameLength = 0
        with open("contacts.csv","r") as file:
            reader = csv.reader(file)
            for i in reader:
                length = len(i[0])
                if length > maxNameLength:
                    maxNameLength = length
        
        with open("contacts.csv","r") as file:
            reader = csv.reader(file)
            n = maxNameLength
            m = 17
            print(f"{(n+3)*'-'}{(m+2)*'-'}")
            print(f"|{'Name'.ljust((n+1),' ')}|{'Contact'.ljust((m+1),' ')}|")
            print(f"{(n+3)*'-'}{(m+2)*'-'}")
            for i in reader:
                print(f"|{i[0].ljust((n+1),' ')}|{i[1].ljust((m+1),' ')}|")
                print(f"{(n+3)*'-'}{(m+2)*'-'}")
                    
    except Exception as e:
        print(f"Error Occured : {e}")

# phoneNumberValidation(number) is used to check that the phone number is valid or not.
def phoneNumberValidation(number):
    pattern = r"^\+?\d{10,15}$"
    if re.fullmatch(pattern, number):
        return True
    return False

#Below 2 statement used to create an empty contacts.csv file to prevent file not exist error
with open("contacts.csv","a") as file:
    pass

ans = "y"
while(ans == "y" or ans == "yes"):
    print("1. Adding Contact.")
    print("2. Search Contact.")
    print("3. Update Contact.")
    print("4. List all contacts.")
    choice = input("\nPlease enter your choice(1,2,3 or 4) : ")
    if choice == "1":
        addContact()
    elif choice == "2":
        searchContact()
    elif choice == "3":
        updateContact()
    elif choice == "4":
        displayAll()
    else:
        print("Wrong Choice!! Please enter your choice again.")
    ans = input("\nYou want to continue?(y/n) : ")
