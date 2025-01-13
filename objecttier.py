#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Project 2: Chicago Lobbyist Database App
# Course: CS 341, Fall 2024, UIC
# System: Codio
# Author: Mohammad Yazdani
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   def __init__(self, ID, first, last, num):
      self._Lobbyist_ID = ID
      self._First_Name = first
      self._Last_Name = last
      self._Phone = num

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   def __init__(self, ID, sal, first, mid_init, last, sufx, addy1, addy2, city, state_init, zip, country, email, num, fax_num, num_years, employer, total_comp):
      self._Lobbyist_ID = ID
      self._Salutation = sal
      self._First_Name = first
      self._Middle_Initial = mid_init
      self._Last_Name = last
      self._Suffix = sufx
      self._Address_1 = addy1
      self._Address_2 = addy2
      self._City = city
      self._State_Initial = state_init
      self._Zip_Code = zip
      self._Country = country
      self._Email = email
      self._Phone = num
      self._Fax = fax_num
      self._Years_Registered = num_years
      self._Employers = employer
      self._Total_Compensation = total_comp

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def Salutation(self):
      return self._Salutation

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Middle_Initial(self):
      return self._Middle_Initial

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Suffix(self):
      return self._Suffix

   @property
   def Address_1(self):
      return self._Address_1

   @property
   def Address_2(self):
      return self._Address_2

   @property
   def City(self):
      return self._City

   @property
   def State_Initial(self):
      return self._State_Initial

   @property
   def Zip_Code(self):
      return self._Zip_Code

   @property
   def Country(self):
      return self._Country

   @property
   def Email(self):
      return self._Email

   @property
   def Phone(self):
      return self._Phone

   @property
   def Fax(self):
      return self._Fax

   @property
   def Years_Registered(self):
      return self._Years_Registered

   @property
   def Employers(self):
      return self._Employers

   @property
   def Total_Compensation(self):
      return self._Total_Compensation

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   def __init__(self, ID, first, last, num, comp, client):
      self._Lobbyist_ID = ID
      self._First_Name = first
      self._Last_Name = last
      self._Phone = num
      self._Total_Compensation = comp
      self._Clients = client

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone

   @property
   def Total_Compensation(self):
      return self._Total_Compensation

   @property
   def Clients(self):
      return self._Clients

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
    try:
        # Get number of lobbyists in the database
        row = datatier.select_one_row(dbConn, "SELECT COUNT(*) FROM LobbyistInfo;")
        return row[0]
    except Exception as err:
        # Return -1 if any error occurs
        return -1
    finally:
        pass

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
    try:
        # Get number of employers in the database
        row = datatier.select_one_row(dbConn, "SELECT COUNT(*) FROM EmployerInfo;")
        return row[0]
    except Exception as err:
        # Return -1 if any error occurs
        return -1
    finally:
        pass

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
    try:
        # Get number of clients in the database
        row = datatier.select_one_row(dbConn, "SELECT COUNT(*) FROM ClientInfo;")
        return row[0]
    except Exception as err:
        # Return -1 if any error occurs
        return -1
    finally:
        pass

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
    try:
        sql = """
            SELECT Lobbyist_ID, First_Name, Last_Name, Phone
            FROM LobbyistInfo
            WHERE First_Name LIKE ? OR Last_Name LIKE ?
            ORDER BY Lobbyist_ID ASC;
            """

        # Get the results
        rows = datatier.select_n_rows(dbConn, sql, [pattern, pattern])
        lobbyists = []

        # Create object for each lobbyists and append into list
        for row in rows:
            lobbyists.append(Lobbyist(row[0], row[1], row[2], row[3]))
        
        # Return list of lobbyists
        return lobbyists
    except Exception as err:
        # Return empty list if any error occurs or None found
        return []
    finally:
        pass


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    try:
        sql = """
            SELECT *
            FROM LobbyistInfo
            WHERE Lobbyist_ID = ?;
            """

        # Exec query for general info
        info = datatier.select_one_row(dbConn, sql, [lobbyist_id])

        sql = """
            SELECT Year FROM LobbyistYears
            WHERE Lobbyist_ID = ?
            ORDER BY Year ASC;
            """

        # Exec query for years and append the years into a list
        rows = datatier.select_n_rows(dbConn, sql, [lobbyist_id])
        years = []
        for row in rows:
            years.append(row[0])

        sql = """
            SELECT Employer_Name FROM EmployerInfo
            JOIN LobbyistAndEmployer ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
            WHERE Lobbyist_ID = ?
            GROUP BY Employer_Name
            ORDER BY Employer_Name ASC;
            """

        # Exec query for employers and append the employers into a list
        rows = datatier.select_n_rows(dbConn, sql, [lobbyist_id])
        employers = []
        for row in rows:
            employers.append(row[0])

        sql = """
            SELECT SUM(Compensation_Amount) FROM Compensation
            WHERE Lobbyist_ID = ?;
            """

        # Exec query for total comp
        row = datatier.select_one_row(dbConn, sql, [lobbyist_id])
        comp = 0.0
        if row and row[0] is not None:
            comp += row[0]

        return LobbyistDetails(info[0], info[1], info[2], info[3], info[4], info[5], info[6],
                            info[7], info[8], info[9], info[10], info[11], info[12], info[13],
                            info[14], years, employers, comp)    
    except Exception as err:
        # Return None if any error occurs or None found
        return None
    finally:
        pass

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
    try:
        sql = """
            SELECT LobbyistInfo.Lobbyist_ID, First_Name, Last_Name, Phone, SUM(Compensation_Amount) AS Comp
            FROM LobbyistInfo
            JOIN Compensation ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
            WHERE strftime('%Y', Period_Start) = ?
            AND strftime('%Y', Period_END) = ?
            GROUP BY LobbyistInfo.Lobbyist_ID
            ORDER BY Comp DESC
            LIMIT ?;
            """
        
        # Exec query and append into a list
        rows = datatier.select_n_rows(dbConn, sql, [year, year, N])
        lobbyists = []
        for row in rows:
            sql1 = """
                SELECT Client_Name FROM ClientInfo
                JOIN Compensation ON ClientInfo.Client_ID = Compensation.Client_ID
                JOIN LobbyistInfo ON Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
                WHERE LobbyistInfo.Lobbyist_ID = ?
                AND strftime('%Y', Period_Start) = ?
                AND strftime('%Y', Period_END) = ?
                GROUP BY ClientInfo.Client_ID
                ORDER BY Client_Name ASC;
                """

            # Exec query and append the client name for each lobbyist into a list
            cl_rows = datatier.select_n_rows(dbConn, sql1, [row[0], year, year])
            clients = []
            for cl_row in cl_rows:
                clients.append(cl_row[0])

            lobbyists.append(LobbyistClients(row[0],row[1],row[2],row[3],row[4],clients))

        # Return a list of lobbyists
        return lobbyists
    except Exception as err:
        # Return an empty list if any errors occur or None found
        return []
    finally:
        pass

##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    try:
        # Check if Lobbyist ID exists
        sql = "SELECT Lobbyist_ID FROM LobbyistInfo WHERE Lobbyist_ID = ?"
        if datatier.select_one_row(dbConn, sql, [lobbyist_id]) == ():
            return 0
        else:
            # Perform action query and rowcount for error
            sql = "INSERT INTO LobbyistYears(Lobbyist_ID, Year) VALUES (?,?);"
            result = datatier.perform_action(dbConn, sql, [lobbyist_id, year])
            if result == -1:
                return 0
        return 1
    except Exception as err:
        # Return 0 if any errors occur
        return 0
    finally:
        pass

##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
    try:
        # Perform action query and rowcount for error
        sql = "UPDATE LobbyistInfo SET Salutation = ? WHERE Lobbyist_ID = ?"
        result = datatier.perform_action(dbConn, sql, [salutation, lobbyist_id])
        if result == -1 or result == 0:
            return 0
        else:
            return 1
    except Exception as err:
        # Return 0 if any errors occur
        return 0
    finally:
        pass
