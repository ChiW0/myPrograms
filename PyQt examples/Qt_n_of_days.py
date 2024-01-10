# Import functions dealing with the Date from Core module
from PyQt6.QtCore import QDate

# Use daysInMonth and daysInYear to print the respective values for the current date or a given date
def nOfDays():
    now = QDate.currentDate() # Returns current date

    d = QDate(1949, 12, 1) # Returns info about certain date. Takes args YYYY, MM, DD

    print(f'Days in month: {now.daysInMonth()}') # Prints days in the current month
    print(f'Days in year: {d.daysInYear()}') # Prints days in certain year

nOfDays()