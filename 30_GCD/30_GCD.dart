import 'dart:io';
import 'dart:math';

// GDC - greates common divisor - dart program to finf the gdc of two numbers

int gcd(int num1, int num2) {
  int minn = min(num1, num2);
  for (int i = 0; i <= minn; i++) {
    if (num1 % i == 0 && num2 % i == 0) {
      break;
    }
  }
  return minn;
}

int eucledianMethod(int num1, int num2) {
  while (num2 > 0) {
    int temp = num1;
    num1 = num2;
    num2 = temp % num2;
  }
  return num1;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);

      stdout.write("Enter a positive integer value : ");
      int num2 = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      if (num1 > maxLimit || num2 > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num1 == 0 || num2 == 0) {
        print("Enter a valid integer value : ");
      } else {
        int result = gcd(num1, num2);
        int euclideanResult = eucledianMethod(num1, num2);
        print("GCD = $result");
        print("GCD - $euclideanResult");
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
