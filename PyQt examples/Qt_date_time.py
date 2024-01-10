# Import functions handling date and time from Core module
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

# Use date/time functions to print date/time in multiple formats. Convert all toString!!
def dateAndTime():
    now = QDate.currentDate() # Return only the current date 
    print(now.toString(Qt.DateFormat.ISODate)) # Print date in YYYY-MM-DD format
    print(now.toString(Qt.DateFormat.RFC2822Date)) # Print date in DD Mon YYYY format

    dateTime = QDateTime.currentDateTime() # Return the current date AND time
    print(dateTime.toString()) # Print local date and time in WkD Mon DD HH:MM:SS YYYY

    time = QTime.currentTime() # Return only the current time
    print(time.toString(Qt.DateFormat.ISODate)) # Print time in HH:MM:SS format

dateAndTime()