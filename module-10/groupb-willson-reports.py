# Group B
    #Justin Bradley
    #Natalia Carbajal
    #Blaise Johnson
    #Luis Rodriguez
# Professor Sue Sampson
# CSD 310 - Assignment 10.1 Milestone 3

import mysql.connector
from mysql.connector import errorcode
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
# ---------------- Report 1 ----------------
    cursor = db.cursor(dictionary=True)

    print("\n========== CLIENT & FINANCIAL ADVISOR REPORT ==========\n")

    cursor.execute("""
    SELECT
        c.ClientID,
        CONCAT(c.FirstName,' ',c.LastName) AS Client,
        CONCAT(e.FirstName,' ',e.LastName) AS Advisor,
        e.Role
    FROM Client c
    JOIN Employee e
        ON c.EmployeeID = e.EmployeeID
    ORDER BY c.ClientID;
    """)

    report = cursor.fetchall()

    for row in report:
        print(f"Client ID: {row['ClientID']}")
        print(f"Client: {row['Client']}")
        print(f"Advisor: {row['Advisor']}")
        print(f"Role: {row['Role']}")
        print()
# ---------------- Report 2 ----------------
    cursor = db.cursor(dictionary=True)

    print("\n========== CLIENT INVESTMENT REPORT ==========\n")

    cursor.execute("""
    SELECT
        c.ClientID,
        CONCAT(c.FirstName,' ',c.LastName) AS Client,
        a.AssetType,
        a.Value,
        a.PurchaseDate
    FROM Client c
    JOIN Asset a
        ON c.ClientID = a.ClientID
    ORDER BY a.Value DESC;
    """)

    report = cursor.fetchall()

    for row in report:
        print(f"Client ID: {row['ClientID']}")
        print(f"Client: {row['Client']}")
        print(f"Asset: {row['AssetType']}")
        print(f"Value: ${row['Value']}")
        print(f"Purchase Date: {row['PurchaseDate']}")
        print()
    # ---------------- Report 3 ----------------
    cursor = db.cursor(dictionary=True)

    print("\n========== BILLING STATUS REPORT ==========\n")

    cursor.execute("""
    SELECT
        b.BillingID,
        CONCAT(c.FirstName,' ',c.LastName) AS Client,
        b.BillingDate,
        b.Amount,
        b.Status
    FROM Billing b
    JOIN Client c
        ON b.ClientID = c.ClientID
    ORDER BY b.Status, b.BillingDate;
    """)

    report = cursor.fetchall()

    for row in report:
        print(f"Billing ID: {row['BillingID']}")
        print(f"Client: {row['Client']}")
        print(f"Billing Date: {row['BillingDate']}")
        print(f"Amount: ${row['Amount']}")
        print(f"Status: {row['Status']}")
        print()

    # Connection status
    print("\nDatabase user {} connected to MySQL on host {} with database {}"
          .format(config["user"], config["host"], config["database"]))

    input("\n\nPress Enter to continue.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    if db is not None:
        db.close()