# Import functions dealing with date and time from Core module
from PyQt6.QtCore import QDateTime, Qt


def UtcLocal():
    dateTime = QDateTime.currentDateTime() # Returns current date and time
    print('Local datetime: ', dateTime.toString()) # Print local date and time in WkD Mon DD HH:MM:SS YYYY
    print('Universal datetime(UTC): ', dateTime.toUTC().toString()) # Print UTC date and time in WkD Mon DD HH:MM:SS YYYY
    print(f'The offset from UTC is: {dateTime.offsetFromUtc()} seconds.') # Print the offset between local time and UTC in seconds

UtcLocal()