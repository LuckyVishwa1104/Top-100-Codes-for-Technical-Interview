import 'dart:io';

// Program to check whether a number is a perfect number or not
// perfect number - it is a number for which the sum of its factor is equal to number itself

bool isPerfect(int num) {
  int sum = 0;
  for (int i = 1; i < num; i++) {
    if (num % i == 0) {
      sum = sum + i;
    }
  }
  if (num == sum) {
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
        bool result = isPerfect(num);
        if (result) {
          print("$num is a perfect number");
        } else {
          print("$num is not a perfect number");
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
