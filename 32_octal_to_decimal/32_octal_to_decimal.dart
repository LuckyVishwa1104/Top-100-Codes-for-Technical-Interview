import 'dart:io';
import 'dart:math';

// program to convert coctal number to equivalent decimal number

int octalToDecimal(int octal) {
  int power = 0;
  int decimalSum = 0;
  String octalString = octal.toString();
  for (int i = octalString.length - 1; i <= 0; i--) {
    decimalSum =
        decimalSum + (int.parse(octalString[i]) * pow(8, power).toInt());
    power = power + 1;
  }
  return decimalSum;
}

bool isValidOctal(int num) {
  String numStr = num.toString();
  for (int i = 0; i < numStr.length; i++) {
    int digit = int.parse(numStr[i]);

    if (digit < 0 || digit > 7) {
      return false;
    }
  }
  return true;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);

      if (num1 < 0) {
        print("Enter the value in decimal format");
      } else if (isValidOctal(num1)) {
        print("Invalid octal number");
      } else {
        int result = octalToDecimal(num1);
        print("Octal $num1 = $result Decimal");
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
