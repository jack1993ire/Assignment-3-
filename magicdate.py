# This program is used to tell you about a magic date
# Magic means the month times the day is equal to the year


# asking user to enter month, day and year
month = int(input("Enter month (in numerical form) : "))
day = int(input("Enter day (in numerical form) : "))
year = int(input("Enter year (last two digits) : "))

# if month times day is equal to year then the date is magic otherwise date is not magic
if month * day == year:
    print("Date is magic.")
else:
    print("Date is not magic.")

