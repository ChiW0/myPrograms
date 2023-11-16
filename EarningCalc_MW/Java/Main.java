// Import the goods
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.io.FileWriter;

public class Main {
// prints the current date in Weekday, Month Day format
    public static void getDay() {
        LocalDate currrentDate = LocalDate.now();
        DateTimeFormatter dateFormat = DateTimeFormatter.ofPattern("E, MMMM dd");
        String formattedDate = currrentDate.format(dateFormat);
        System.out.println(formattedDate);
}

// Creates a scanner to get input of how many hours worked, then converts input to float and returns the value.
public static float hoursInput() {
    Scanner inputMachine = new Scanner(System.in);
    System.out.println("How many hours did you work today?: ");
    String hours = inputMachine.nextLine();
    float floatHours = Float.parseFloat(hours);
    inputMachine.close();
    return floatHours;
}

// Creates a scanner to get string from file representing total weekly hours worked. Converts string to float and returns it.
public static float getWeeklyHours() { 
    float weeklyHours = -1.0f;
    String hoursStr = null;

    try {
    File weeklyHoursFile = new File("hoursTotal.txt");
    Scanner readFile = new Scanner(weeklyHoursFile);
    while (readFile.hasNextLine()) {
        hoursStr = readFile.nextLine();

    }

    if (hoursStr != null){
    weeklyHours = Float.parseFloat(hoursStr.trim());
    }
    readFile.close();
   // weeklyHours = Float.parseFloat(hoursStr.trim());

    } catch(Exception e) {

    }
    
    return weeklyHours;
}

/* Calls last 2 methods floats and sums them. 
then is passed to an if...else statement that calculates total earned depending on if it's over 40hours or not to account for overtime.
finally prints total hours worked and the grossing pay for those hours.
returns the total hours as a string. */
public static String earningCalc() {
    byte hourlyWage = 18;
    byte overtimeWage = 27;
    float dayHours = hoursInput();
    float weekHours = getWeeklyHours();
    float updatedHours = dayHours + weekHours;
    float grossPay;
    if (updatedHours >= 40) {
        float normalMoney = 40 * hourlyWage;
        float overtimeHours = updatedHours - 40;
        float overtimeMoney = overtimeHours * overtimeWage;
        grossPay = normalMoney + overtimeMoney;
    } else {
        grossPay = updatedHours * hourlyWage;
    }
    System.out.println("Aproximate hours worked this week: " + updatedHours);
    System.out.println("The aproximate grossing earned this week is: " + grossPay);
    String updatedHoursStr = Float.toString(updatedHours);
    return updatedHoursStr;
}

// runs method that prints date. runs calculator method and catches the returned variable. Creates a file writer that writes string to file references earlier.
public static void main(String[] args) {
    getDay();
    String totalHoursStr = earningCalc();

    try {
        FileWriter writeToFile = new FileWriter("hoursTotal.txt");
        writeToFile.write(totalHoursStr);
        writeToFile.close();
    } catch (IOException e) {
        System.out.println("An error occurred while writing to file.");
        e.printStackTrace();
    }

    }
}