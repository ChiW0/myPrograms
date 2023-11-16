#include <iostream>
#include <fstream>
#include <ctime>
#include <string>
using namespace std;

void getDay() {
    time_t curr_time = time(nullptr);
    tm* dateTime = localtime(&curr_time);

    const char* dayNames[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

    const char* monthNames[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

    int weekday = dateTime->tm_wday;
    int month = dateTime->tm_mon;
    int monthDay = dateTime->tm_mday;

    cout << dayNames[weekday] << ", " << monthNames[month] << " " << monthDay << "\n";
}

float hoursInput() {
    float hours;
    cout << "How many hours did you work today?\n";
    cin >> hours;
    return hours;
}

float getWeeklyHours() {
    string weeklyHours_Str;
    ifstream fileReader("hours.txt");
    
    if (fileReader.is_open()) {
        getline(fileReader, weeklyHours_Str);
        fileReader.close();

        float weeklyHours_Flt = stof(weeklyHours_Str);
        return weeklyHours_Flt;
    } else {
        cout << "File not found, unable to read\n";
        return -1.0;
    }
}

string earningCalc() {
    const int hourlyWage = 18;
    const int overtimeWage = 27;
    float dayHours = hoursInput();
    float weekHours = getWeeklyHours();
    float hoursToDate = dayHours + weekHours;
    float grossPay;

    if (hoursToDate >= 40) {
        float normalMoney = 40 * hourlyWage;
        float overtimeHours = hoursToDate - 40;
        float overtimeMoney = overtimeHours * overtimeWage;
        grossPay = normalMoney + overtimeMoney;
    } else {
        grossPay = hoursToDate * hourlyWage;
    }

    cout << "Aproximate hours worked this week: " << hoursToDate << "\n";
    cout << "Aproximate grossing money earned this week: " << grossPay <<"\n";
    string hoursToDate_Str = to_string(hoursToDate);
    return hoursToDate_Str;
}

int main() {
    getDay();
    string totalHours_Str = earningCalc();

    ofstream fileWriter("hours.txt");
    
    if (fileWriter.is_open()) {
        fileWriter << totalHours_Str;
        fileWriter.close();
    } else {
        cout << "File not found, unable to write to file\n";
    }

}