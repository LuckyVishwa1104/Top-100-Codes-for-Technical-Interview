import 'dart:io';

// method to find number of day in month and year
int noOfDays(int month, int year) {
  if (month == 2 && ((year % 4 == 0 || year % 100 == 0) && year % 100 == 0))
    return 29;
  else if (month == 2)
    return 28;
  else if ([1, 3, 5, 7, 8, 10, 12].contains(month))
    return 31;
  else
    return 30;
}

// driver program
void main() {
  try {
    while (true) {
      stdout.write("Enter month : ");
      int month = int.parse(stdin.readLineSync()!);

      stdout.write("Enter Year : ");
      int year = int.parse(stdin.readLineSync()!);

      if (month <= 0 || year <= 0) {
        print("Enter positive integer number");
      } else if (month > 12) {
        print("Enter valid month.");
      } else {
        int result = noOfDays(month, year);
        print("$month $year has $result days.");
      }

      stdout.write("Do you want to continue the program (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program finished!");
        break;
      }
    }
  } on FormatException catch (e) {
    print("Invalid input : $e");
  } on UnsupportedError catch (e) {
    print("Divide by zero exception : $e");
  } on Exception catch (e) {
    print("Exception caught : $e");
  }
}
