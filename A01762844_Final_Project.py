##### Manager  #######

def identification():
    identity = "admin"
    password = "password"

    while True:
        id = input("What is your identity: ")
        if id == identity:
            print("Identity correct!")
            break  # Break out of the loop if the identity is correct
        else:
            print("Wrong identity")

    while True:
        passw = input("What is your password: ")
        if passw == password:
            print("You have access to the platform.")
            break  # Same with the password
        else:
            print("Incorrect password")


#identification()

def add_country_and_price():
    list_country = []
    country_price = []

    while True:
        print(" Please enter new destination")
        print("--------------------------------")
        country = input("Enter a country (or 'q' to quit): ")

        if country.lower() == 'q':
            break   # if tap 'q' ==> the break quit the loop

        price = float(input(f"Enter price for {country}: "))
        country_price.append([country, price])

    matrix = []

    for entry in country_price:
        matrix.append([entry[0], f"${entry[1]:.2f}"])
    print("_________________________________")
    print("Matrix of Countries and Prices:")
    print("_________________________________")
    for entry in matrix:
        print(entry[0] + ": " + entry[1])  # entry[0] for the country and entry[1] for the price
    print("New file created with these new informations")

    with open("Country&Price.txt", "w") as file:
        file.write("Country and Price:\n")
        for entry in matrix:
            file.write(f"{entry[0]}: {entry[1]}\n")

#add_country_and_price()


###### Customer ######

import re
# Library for using RegeX
def is_valid_email():
    # regex for valid email
    while True:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        email = input("enter a valid email : example :XXX.YYYY@ZZZZ.com\n ")
    # match() to verify if motif match with the pattern
        if  re.match(pattern, email):
        #return True
            print("email valid")
            break
        else:
        #return False
            print("email not valid")

#is_valid_email()


def See_Destination_and_price():
    destination = {"Paris":1500, "Mexico":4500, "Los Angeles":3700}
    #Dictionnary with keys : Name of the destination and volors : prices
    print("Where you want to go ? ")
    print("1: Paris - $1500\n2: Mexico - $4500\n3: Los Angeles - $3700")

    choice = int(input("Make your choice : "))

    for index, (city, price) in enumerate(destination.items(), start=1):
        # enumerates function to iterate the keys and valors of the dictionary with start=1 because it is easier to find our way
        if index == choice:
            print(f"You choose the following  destination {city} with the price of  ${price}")
            break
    else:
        print("invalid choice ")

    print("Do you want the price in € ? ")
    convert = input("1:Yes\n2:No\n")
    if convert == "1":
        euros = price/18
        print(price,"from pesos to euros : ",euros,"€")
        print("Thank you for your Trust ")
    else :
        print("Thank you for your Trust ")
        pass

#See_Destination_and_price()


def menu():
    print("\nWELCOME\n")
    print("----------------------------")
    print("What is your situation ? ")
    print("----------------------------")
    print("1: I'm an Employee")
    print("2 : I'm an Client")
    print("----------------------------")

#menu()


def main():
    menu()
    situation = int(input("Your situation ? "))
    if situation == 1 :
        identification()
        add_country_and_price()
        main()
    if situation==2:
        is_valid_email()
        See_Destination_and_price()
    else:
        exit()

main()
