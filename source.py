import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

w=input("Enter the word: ")
w = w.lower()
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % w)
results = cursor.fetchall()

if results:
    for result in results:
        if result.isupper():  #for acronyms like NATO
            print(result.upper())
        elif result.istitle():
            print(result.title())
        else:
            print(result)
else:
    print("No word found!")