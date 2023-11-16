import datetime
import os

hourly_wage = 18
overtime_wage = 27

txt_file = "hoursTotal.txt"

def get_day():
    x = datetime.datetime.now()
    current_day = ((x.strftime("%A")) + ", " + (x.strftime("%B ")) + (x.strftime("%d")))
    print(current_day)

get_day()

today_hours = float(input("How many hours did you work today?: "))

def get_weekly_hours():
    with open(txt_file, "r") as file:
        week_hours_str = file.read().strip()
        week_hours_float = float(week_hours_str)
    return week_hours_float

week_hours = get_weekly_hours()
 
def earning_calc():
    total_hours = today_hours + week_hours
    if total_hours >= 40:
        normal_pay = 40 * hourly_wage
        overtime_hours = total_hours - 40
        overtime_pay = overtime_hours * overtime_wage
        gross_pay = normal_pay + overtime_pay
    if total_hours <= 40:
        gross_pay = total_hours * hourly_wage
        gp_str = str(gross_pay)
    print("The aproximate grossing eanred this week is:", gp_str)
    total_hours_str = str(total_hours)
    return total_hours_str

update_wk_hrs = earning_calc()


def write_to_dayshours():
    with open(txt_file, "w") as file:
        file.write(update_wk_hrs)
        file.close()

write_to_dayshours()

#print("Current working directory:", os.getcwd())