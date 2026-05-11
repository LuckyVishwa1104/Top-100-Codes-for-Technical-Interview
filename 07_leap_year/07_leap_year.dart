import "dart:io";

bool isLeapYear(int year) {
  if ((year % 4 == 0) || ((year % 400 == 0) && (year % 100 != 0))) {
    return true;
  } else {
    return false;
  }
}

void main() {
  try {
    stdout.write("Enter year : ");
    int year = int.parse(stdin.readLineSync()!);

    if (year <= 0) {
      print("Kindly enter proper year.");
    } else if (isLeapYear(year)) {
      print("$year is a Leap Year");
    } else {
      print("$year is not a Leap Year");
    }
  } on FormatException catch (e) {
    print("Invalid Input : $e");
  } catch (e) {
    print("Exception caught : $e");
  }
}
