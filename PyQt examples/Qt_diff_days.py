# Import functions dealing with date from core module
from PyQt6.QtCore import QDate, Qt

def XmasCntdwn():
    now = QDate.currentDate()
    y = now.year()

    print (f'today is {now.toString(Qt.DateFormat.RFC2822Date)}')

    xmas1 = QDate(y-1, 12, 25)
    xmas2 = QDate(y, 12, 25)

    daysPassed = xmas1.daysTo(now)
    print(f'{daysPassed} days have passed since last Christmas')

    daysUntil = now.daysTo(xmas2)
    print(f'There are {daysUntil} days until next Christmas')

XmasCntdwn()