#
# Project 2: Chicago Lobbyist Database App
# Course: CS 341, Fall 2024, UIC
# System: Codio
# Author: Mohammad Yazdani
#

import sqlite3
import objecttier

##################################################################  
#
# retrieve_basicinfo
#
def retrieve_basicinfo(dbConn):
    print()
    name = input("Enter lobbyist name (first or last, wildcards _ and % supported):\n")

    # Get a list of lobbyists from the database
    lobbyists = objecttier.get_lobbyists(dbConn, name)
    print("\nNumber of lobbyists found:", len(lobbyists))

    if len(lobbyists) > 100:
        print("\nThere are too many lobbyists to display, please narrow your search and try again...")
        pass
    else:
        print()
        # Display the lobbyists' info
        for l in lobbyists:
            print(l.Lobbyist_ID, ":", l.First_Name, l.Last_Name, "Phone:", l.Phone)

##################################################################  
#
# retrieve_detailedinfo
#
def retrieve_detailedinfo(dbConn):
    print()
    lobId = input("Enter Lobbyist ID: ")

    # Get detailed information on the lobbyist
    lobbyist = objecttier.get_lobbyist_details(dbConn, lobId)

    if lobbyist is None:
        print("\nNo Lobbyist with that ID was found.")
    else:
        # Display the detailed information
        print()
        print(lobbyist.Lobbyist_ID, ":")
        print("  Full Name:", lobbyist.Salutation, lobbyist.First_Name, lobbyist.Middle_Initial, lobbyist.Last_Name, lobbyist.Suffix)
        print("  Address:", lobbyist.Address_1, lobbyist.Address_2, ",", lobbyist.City, ",", lobbyist.State_Initial, lobbyist.Zip_Code, lobbyist.Country)
        print("  Email:", lobbyist.Email)
        print("  Phone:", lobbyist.Phone)
        print("  Fax:", lobbyist.Fax)
        print("  Years Registered: ", end=" ")
        for year in lobbyist.Years_Registered:
            print(str(year), end=", ")
        print("\n  Employers: ", end=" ")
        for e in lobbyist.Employers:
            print(e, end=", ")
        print("\n  Total Compensation: $" + f"{lobbyist.Total_Compensation:,.2f}")

##################################################################  
#
# retrieve_toplobbyists
#
def retrieve_toplobbyists(dbConn):
    print()
    N = input("Enter the value of N: ")
    N = int(N) # Convert to int
    if (int(N) < 1):
        print("Please enter a positive value for N...")
    else:
        year = input("Enter the year: ")
        # Get the top N lobbyists for given year
        lobbyists = objecttier.get_top_N_lobbyists(dbConn, N, year)

        i = 1
        for l in lobbyists:
            print()
            # Print lobbyist info and clients
            print(i, ".", l.First_Name, l.Last_Name)
            print("  Phone:", l.Phone)
            print("  Total Compensation: $" + f"{l.Total_Compensation:,.2f}")
            print("  Clients: ", end=" ")
            for c in l.Clients:
                print(c, end=", ")
            print()
            i += 1

##################################################################  
#
# register_lobbyistyear
#
def register_lobbyistyear(dbConn):
    print()
    year = input("Enter year: ")
    lobId = input("Enter the lobbyist ID: ")

    # Call to add a year onto a lobbyist
    if objecttier.add_lobbyist_year(dbConn, lobId, year) != 1:
        print("\nNo lobbyist with that ID was found.")
    else:
        print("\nLobbyist successfully registered.")

##################################################################  
#
# register_salutation
#
def register_salutation(dbConn):
    print()
    lobId = input("Enter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")

    # Call to add salutation onto a lobbyist
    if objecttier.set_salutation(dbConn, lobId, salutation) != 1:
        print("\nNo lobbyist with that ID was found.")
    else:
        print("\nSalutation successfully set.")

##################################################################  
#
# main
#
dbConn = sqlite3.connect('Chicago_Lobbyists.db')

print("** Welcome to the Chicago Lobbyist Database Application **")
print("\nGeneral Statistics:")
print("  Number of Lobbyists:", f"{objecttier.num_lobbyists(dbConn):,}")
print("  Number of Employers:", f"{objecttier.num_employers(dbConn):,}")
print("  Number of Clients:", f"{objecttier.num_clients(dbConn):,}")

print()
cmd = input("Please enter a command (1-5, x to exit): ")

while cmd != "x":
    if cmd == "1":
        retrieve_basicinfo(dbConn)
    elif cmd == "2":
        retrieve_detailedinfo(dbConn)
    elif cmd == "3":
        retrieve_toplobbyists(dbConn)
    elif cmd == "4":
        register_lobbyistyear(dbConn)
    elif cmd == "5":
        register_salutation(dbConn)
    else:
        print("**Error, unknown command, try again...")

    print()
    cmd = input("Please enter a command (1-5, x to exit): ")

dbConn.close()

#
# done
#
