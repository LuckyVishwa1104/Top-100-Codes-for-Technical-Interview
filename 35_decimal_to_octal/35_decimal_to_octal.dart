import 'dart:io';

// program to convert decimal to octal number

String reverseString(String num) {
  String revString = "";
  for (int i = num.length - 1; i >= 0; i--) {
    revString = revString + num[i];
  }
  return revString;
}

String decimalToOctal(int decimal) {
  String octalNum = "";
  while (decimal > 0) {
    int remainder = decimal % 8;
    decimal = decimal ~/ 8;
    octalNum = octalNum + remainder.toString();
  }
  return reverseString(octalNum);
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0) {
        print("Enter the value in decimal");
      } else {
        String result = decimalToOctal(num);
        print("Decimal $num = $result Octal");
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
