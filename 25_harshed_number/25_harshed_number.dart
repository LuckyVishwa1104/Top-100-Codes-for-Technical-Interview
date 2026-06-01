import 'dart:io';

// Harshed number - a number which is completely divisible by the sum of its digits

bool isHarshed(int num) {
  int sum = 0;
  int numerator = num;
  while (num > 0) {
    sum = sum + (num % 10);
    num = num ~/ 10;
  }
  if (numerator % sum == 0) {
    return true;
  }
  return false;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      if (num > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num <= 0) {
        print("Enter a valid integer value : ");
      } else {
        bool result = isHarshed(num);
        if (result) {
          print("$num is a Harshed number");
        } else {
          print("$num is not a Harsehd number");
        }
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
