import 'dart:io';
import 'dart:math';

// program to check whether a number is a perfect square

bool isPerfectSquare(int num) {
  int squareRoot = sqrt(num).toInt();
  if (squareRoot * squareRoot == num) {
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
        bool result = isPerfectSquare(num);
        if (result) {
          print("$num is a perfect square");
        } else {
          print("$num is not a perfect square");
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
