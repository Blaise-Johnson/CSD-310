# Group B
    #Justin Bradley
    #Natalia Carbajal
    #Blaise Johnson
    #Luis Rodriguez
# Professor Sue Sampson
# CSD 310 - Assignment 9.1 Milestone 2

import mysql.connector
from mysql.connector import errorcode
import dotenv
from dotenv import dotenv_values
# using our .env file
secrets = dotenv_values(".env")
""" database config object """

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "port": int(secrets["PORT"]),
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}
""" MySQL: mysql_test.py Connection test code """
""" try/catch block for handling potential MySQL database errors """
db = None
try:
# connect to the database using the config object
    db = mysql.connector.connect(**config)

    #EMPLOYEE TABLE - query and print every row from the Employee table
    #Must exist before Client table because of foreign key constraint
    cursor = db.cursor(dictionary=True)
    print(f"--EMPLOYEES--")
    cursor.execute("SELECT * FROM Employee")
    Employee = cursor.fetchall()

    for employee in Employee:
        print(f"Employee ID: {employee['EmployeeID']}")
        print(f"Name: {employee['FirstName']} {employee['LastName']}")
        print(f"Role: {employee['Role']}")
        print(f"Phone: {employee['Phone']}")
        print(f"Email: {employee['Email']}")
        print(f"Hire Date: {employee['HireDate']}")
        print( )

    print("------------------------------")

    #Client table - query and print every row from the client table
    cursor = db.cursor(dictionary=True)
    print(f"--CLIENTS--")
    cursor.execute("SELECT * FROM client")
    client = cursor.fetchall()

    for client in client:
        print(f"Client ID: {client['ClientID']}")
        print(f"Name: {client['FirstName']} {client['LastName']}")
        print(f"Phone: {client['Phone']}")
        print(f"Email: {client['Email']}")
        print(f"Address: {client['Address']}")
        print(f"Date: {client['DateAdded']}")
        print(f"Employee ID: {client['EmployeeID']}")
        print()
    print("------------------------------")

    #Asset table - query and print every row from the asset table
    cursor = db.cursor(dictionary=True)
    print(f"--ASSETS--")
    cursor.execute("SELECT * FROM asset")
    asset = cursor.fetchall()

    for asset in asset:
        print(f"Asset ID: {asset['AssetID']}")
        print(f"Asset Type: {asset['AssetType']}")
        print(f"Value: {asset['Value']}")
        print(f"Purchase Date: {asset['PurchaseDate']}")
        print(f"Client ID: {asset['ClientID']}")
        print()

    print("------------------------------")

    #transactions - query and print every row from the transactionrecord table
    cursor = db.cursor(dictionary=True)
    print(f"--TRANSACTION RECORDS--")
    cursor.execute("SELECT * FROM transactionrecord")
    transactionrecord = cursor.fetchall()

    for transactionrecord in transactionrecord:
        print(f"Transaction ID: {transactionrecord['TransactionID']}")
        print(f"Transaction Date: {transactionrecord['TransactionDate']}")
        print(f"Amount: {transactionrecord['Amount']}")
        print(f"Transaction Type: {transactionrecord['TransactionType']}")
        print(f"Client ID: {transactionrecord['ClientID']}")
        print(f"Asset ID: {transactionrecord['AssetID']}")
        print()
    print("------------------------------")

    #Appointments - query and print every row from the appointment table
    cursor = db.cursor(dictionary=True)
    print(f"--APPOINTMENTS--")
    cursor.execute("SELECT * FROM appointment")
    appointment = cursor.fetchall()

    for appointment in appointment:
        print(f"Appointment ID: {appointment['AppointmentID']}")
        print(f"Appointment Date: {appointment['AppointmentDate']}")
        print(f"Appointment Time: {appointment['AppointmentTime']}")
        print(f"Appointment Purpose: {appointment['Purpose']}")
        print(f"Client ID: {appointment['ClientID']}")
        print(f"Employee ID: {appointment['EmployeeID']}")
        print()
    print("------------------------------")

    #Billing - query and print every row from the billing table
    cursor = db.cursor(dictionary=True)
    print(f"--BILLING--")
    cursor.execute("SELECT * FROM billing")
    billing = cursor.fetchall()

    for billing in billing:
        print(f"Billing ID: {billing['BillingID']}")
        print(f"Billing Date: {billing['BillingDate']}")
        print(f"Amount: {billing['Amount']}")
        print(f"Status: {billing['Status']}")
        print(f"Client ID: {billing['ClientID']}")
        print()


# output the connection status
    print("\nDatabase user {} connected to MySQL on host {} with database {}"
    .format(config["user"], config["host"], config["database"]))
    input("\n\nPress any key to continue...")
except mysql.connector.Error as err:
    """ on error code """
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    """ close the connection to MySQL """
    if db is not None:
        db.close()

# Bradley changes:
# - Added db = None before the try block so it's always defined, even if the connection fails
# - Replaced pass in the finally block with a check that closes the connection if it was opened
# - Deleted the commented-out #db.close() at the bottom
# - Added Group B header to the top
# - Switched every cursor to db.cursor(dictionary=True) and replaced positional
#   indexing (e.g. client[6]) with column-name keys (e.g. client["DateAdded"])
# - Renamed the secrets file from dotenv_values2.env to .env (matches the other
#   module scripts and is already covered by the repo-wide .gitignore rule)
# - Moved the hardcoded port 3304 into the .env file as PORT, read via secrets["PORT"]